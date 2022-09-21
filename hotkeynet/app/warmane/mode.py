# -*- coding: utf-8 -*-

"""
第一步先定义游戏用什么窗口, 什么分辨率, 上哪些角色.
"""

import typing as T

import attr
from attrs_mate import AttrsClass

import hotkeynet as hk
from hotkeynet.game.wow.model import Account
from hotkeynet.game.wow.wlk import (
    Window,
    Talent as TL,
    TalentCategory as TC,
)

from .character import (
    Character,
    LoginCharactersFactory,
    ActiveCharactersFactory,
    CharacterHelper,
)
from .game_client import GameClient
from .hkn import HknScript
from .paths import path_warmane_hkn


@attr.s
class Mode(AttrsClass):
    """
    代表你使用多开脚本进行游戏的设置, 设置包含了以下内容:

    1. 游戏窗口的位置, 分辨率
    2. 上哪些角色的哪个天赋
    3. 每个角色在哪个窗口中
    4. 各个角色分别扮演团队中的什么角色

    :param game_client: 与客户端有关的设置
    :param active_chars: 指定要使用哪些角色进行游戏
    :param login_chars: 指定要登录哪些角色. 要进行游戏的角色自动会被视为需要登录.
        如果 login_chars 和 active_chars 的设置有冲突, 则以 active_chars 为准.
    :param hkn_script: HotkeyNet 脚本的按键定义.

    **注**

    1. 这个类有很多 @classmethod 的 工厂函数, 可以用来创建 Mode 的实例.
    2. 所有的工厂函数都必须要以 use_ 开头! 内部实现依赖于这个来做一些工作.

    **设计思想**
    """
    game_client: GameClient = attr.ib(factory=GameClient)
    active_chars: T.List[Character] = attr.ib(factory=list)
    login_chars: T.List[Character] = attr.ib(factory=list)
    hkn_script: HknScript = attr.ib(default=None)

    def _ensure_no_duplicate_window(self, chars: T.List[Character]):
        if len({char.window.label for char in chars}) != len(chars):
            for char in chars:
                print(char.window.label, char.account.username)
            raise ValueError(f"Character list {chars} cannot has duplicate window label!")

    @active_chars.validator
    def check_active_chars(self, attribute, value):
        self._ensure_no_duplicate_window(value)

    @login_chars.validator
    def check_login_chars(self, attribute, value):
        self._ensure_no_duplicate_window(value)

    def __attrs_post_init__(self):
        # 所有关于 characters 列表的定义
        self.active_chars = CharacterHelper.sort_chars_by_window_label(self.active_chars)
        self.login_chars = CharacterHelper.sort_chars_by_window_label(self.login_chars)
        self.hkn_script = HknScript(mode=self)

    def dump(self, verbose: bool = False):
        path_warmane_hkn.write_text(
            self.hkn_script.script.render(verbose=verbose),
        )

    @property
    def login_window_and_account_pairs(self) -> T.List[T.Tuple[Window, Account]]:
        """

        """
        label_set: T.Set[str] = set()
        window_and_account_pairs: T.List[T.Tuple[Window, Account]] = list()
        for char in self.active_chars:
            if char.window.label not in label_set:
                window_and_account_pairs.append((char.window, char.account))
                label_set.add(char.window.label)
        for char in self.login_chars:
            if char.window.label not in label_set:
                window_and_account_pairs.append((char.window, char.account))
                label_set.add(char.window.label)
        window_and_account_pairs = list(sorted(
            window_and_account_pairs,
            key=lambda x: x[0]
        ))
        return window_and_account_pairs

    @property
    def lbs_all(self) -> T.List[str]:
        """
        返回所有要进行游戏的人物角色所对应的游戏窗口的 label.

        在多开热键定义中, 常用于那些对所有角色生效的按键. 比如 1234, 前进后退等.
        """
        return [char.window.label for char in self.active_chars]

    def lbs_by_tl(self, tl: TL) -> T.List[str]:
        """
        返回所有要进行游戏的人物角色中, 匹配某个具体天赋的角色所对应的游戏窗口的 label.

        在多开热键定义中, 常用于根据天赋筛选部分角色.
        """
        return [
            char.window.label
            for char in CharacterHelper.filter_by_talent(self.active_chars, tl)
        ]

    def lbs_by_tc(self, tc: TC) -> T.List[str]:
        """
        返回所有要进行游戏的人物角色中, 匹配某个天赋分组的角色所对应的游戏窗口的 label.

        在多开热键定义中, 常用于根据天赋筛选部分角色.
        """
        return [
            char.window.label
            for char in CharacterHelper.filter_by_talent_category(
                self.active_chars, tc,
            )
        ]

    @property
    def lbs_tank1(self) -> T.List[str]:
        return [
            char.window.label
            for char in self.active_chars
            if char.is_tank_1
        ]

    @property
    def lbs_tank2(self) -> T.List[str]:
        return [
            char.window.label
            for char in self.active_chars
            if char.is_tank_2
        ]

    @property
    def lbs_dr_pala1(self) -> T.List[str]:
        return [
            char.window.label
            for char in self.active_chars
            if char.is_dr_pala_1
        ]

    @property
    def lbs_dr_pala2(self) -> T.List[str]:
        return [
            char.window.label
            for char in self.active_chars
            if char.is_dr_pala_2
        ]

    def remove_inactive_labels(self, label_list: T.List[str]):
        """
        给定一个 label 的列表, 从中删除那些不存在相对应的 active character 的 label.

        在多开热键定义中, 你可能在 Hotkey 按键中定义了一大批 label, 但是不同的游戏模式下
        你启用的队伍里不见得有这些 label, 所以我们希望将这些 label 移除. 该技巧适合定义
        一个较为通用的键位逻辑, 然后用该函数删除那些不可能有意义的 SendLabel 事件.
        """
        all_labels = set(self.lbs_all)
        for label in list(label_list):
            if label not in all_labels:
                label_list.remove(label)

    def remove_tank_labels(self, label_list: T.List[str]):
        """
        有时候我们希望全团进行一些动作, 但唯独坦克职业不动.
        """
        all_tank_labels = [
            char.window.label
            for char in self.active_chars
            if char.is_tank_1 or char.is_tank_2
        ]
        for label in list(label_list):
            if label in all_tank_labels:
                label_list.remove(label)

    # --------------------------------------------------------------------------
    # Mode definition
    # --------------------------------------------------------------------------
    __anchore_mode_definition = None

    @classmethod
    def use_solo_dungeon_batlefury_quentin_opiitou_swagsonic_kangliu(cls):
        return cls(
            game_client=GameClient().use_1920_1080_resolution(),
            # game_client=GameClient().use_1600_900_resolution(),
            # game_client=GameClient().use_1176_664_resolution(),
            login_chars=LoginCharactersFactory.make_chars_10p(),
            active_chars=ActiveCharactersFactory.make_team_solo_dungeon_batlefury_quentin_opiitou_swagsonic_kangliu(),
        )

    @classmethod
    def use_solo_raid_10p_batlefury_luxiaofeng_core_team(cls):
        return cls(
            game_client=GameClient().use_1920_1080_resolution(),
            # game_client=GameClient().use_1600_900_resolution(),
            # game_client=GameClient().use_1176_664_resolution(),
            login_chars=LoginCharactersFactory.make_chars_10p(),
            active_chars=ActiveCharactersFactory.make_team_solo_raid_10p_batlefury_luxiaofeng_core_team(),
        )

    @classmethod
    def use_solo_dungeon_5p_lgqs_abcde(cls):
        return cls(
            game_client=GameClient().use_1920_1080_resolution(),
            # game_client=GameClient().use_1600_900_resolution(),
            # game_client=GameClient().use_1176_664_resolution(),
            login_chars=[],
            active_chars=ActiveCharactersFactory.make_team_solo_dungeon_lgqs_abcde(),
        )

    # @classmethod
    # def use_solo_dungeon_batlefury_quentin_opiitou_swagsonic_kangliu(cls):
    #     return cls(
    #         game_client=GameClient().use_1920_1080_resolution(),
    #         # game_client=GameClient().use_1600_900_resolution(),
    #         # game_client=GameClient().use_1176_664_resolution(),
    #         login_chars=LoginCharactersFactory.make_chars_10p(),
    #         active_chars=ActiveCharactersFactory.make_team_solo_dungeon_batlefury_quentin_opiitou_swagsonic_kangliu(),
    #     )

    @classmethod
    def use_22p_monthly_login_1(cls):
        return cls(
            game_client=GameClient().use_1600_900_resolution(),
            active_chars=ActiveCharactersFactory.make_team_22p_monthly_login_1(),
        )

    @classmethod
    def use_22p_monthly_login_2(cls):
        return cls(
            game_client=GameClient().use_1600_900_resolution(),
            active_chars=ActiveCharactersFactory.make_team_22p_monthly_login_2(),
        )

    @classmethod
    def use_5p_team_solo_dungeon_festival_team_1_dk(cls):
        return cls(
            game_client=GameClient().use_1600_900_resolution(),
            active_chars=ActiveCharactersFactory.make_team_solo_dungeon_festival_team_1_dk(),
        )

    @classmethod
    def use_5p_team_solo_dungeon_festival_team_2_ss(cls):
        return cls(
            game_client=GameClient().use_1600_900_resolution(),
            active_chars=ActiveCharactersFactory.make_team_solo_dungeon_festival_team_2_ss(),
        )

    @classmethod
    def use_5p_team_solo_dungeon_festival_team_3_mix(cls):
        return cls(
            game_client=GameClient().use_1600_900_resolution(),
            active_chars=ActiveCharactersFactory.make_team_solo_dungeon_festival_team_3_mix(),
        )

    @classmethod
    def use_5p_team_solo_festival_team_4_ms_sm(cls):
        return cls(
            game_client=GameClient().use_1600_900_resolution(),
            active_chars=ActiveCharactersFactory.make_team_solo_dungeon_festival_team_4_ms_sm(),
            login_chars=LoginCharactersFactory.make_chars_5p_ganjj_laoshou_lgms_and_lssm(),
        )

    @classmethod
    def use_5p_team_solo_festival_team_5_ms_sm(cls):
        return cls(
            game_client=GameClient().use_1600_900_resolution(),
            active_chars=ActiveCharactersFactory.make_team_solo_dungeon_festival_team_5_ms_sm(),
            login_chars=LoginCharactersFactory.make_chars_5p_ganjj_laoshou_lgms_and_lssm(),
        )

    @classmethod
    def use_5p_team_solo_festival_team_6_litgugu_efgh(cls):
        return cls(
            game_client=GameClient().use_1600_900_resolution(),
            active_chars=ActiveCharactersFactory.make_team_solo_dungeon_festival_team_6_litgugu_efgh()
        )