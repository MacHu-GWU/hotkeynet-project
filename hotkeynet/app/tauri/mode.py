# -*- coding: utf-8 -*-

"""
第一步先定义游戏用什么窗口, 什么分辨率, 上哪些角色
"""

import typing as T

import attr
from attrs_mate import AttrsClass

import hotkeynet as hk
from hotkeynet.game.wow.mop import (
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
from .paths import path_tauri_hkn


@attr.s
class Mode(AttrsClass):
    """
    代表你使用多开脚本进行游戏的设置, 包含了以下内容:

    1. 游戏窗口的位置, 分辨率
    2. 上哪些角色的哪个天赋
    3. 每个角色在哪个窗口中
    4. 各个角色分别扮演团队中的什么位置
    5. 等等

    **注**

    1. 所有的设置游戏模式的方法都必须要以 use_ 开头! 内部实现依赖于这个来做一些工作.
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
        self.active_chars = CharacterHelper.sort_chars_by_window_label(self.active_chars)
        self.login_chars = CharacterHelper.sort_chars_by_window_label(self.login_chars)
        self._resolve_login()
        self.hkn_script = HknScript(mode=self)

    def dump(self, verbose: bool = False):
        path_tauri_hkn.write_text(
            self.hkn_script.script.render(verbose=verbose),
        )

    def _resolve_login(self):
        self.occupied_labels: T.Set[str] = set()
        self.managed_chars: T.List[Character] = list()
        for char in self.active_chars:
            if char.window.label not in self.occupied_labels:
                self.managed_chars.append(char)
                self.occupied_labels.add(char.window.label)
        for char in self.login_chars:
            if char.window.label not in self.occupied_labels:
                self.managed_chars.append(char)
                self.occupied_labels.add(char.window.label)
        self.managed_chars = CharacterHelper.sort_chars_by_window_label(self.managed_chars)

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
    def use_solo_dungeon_carrot_flower_team(cls):
        return cls(
            game_client=GameClient().use_1920_1080_resolution(),
            # game_client=GameClient().use_1600_900_resolution(),
            # game_client=GameClient().use_1176_664_resolution(),
            # login_chars=LoginCharactersFactory.make_chars_10p(),
            active_chars=ActiveCharactersFactory.make_team_solo_dungeon_carrot_flower_team(),
        )
