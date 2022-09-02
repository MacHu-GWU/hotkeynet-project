# -*- coding: utf-8 -*-

"""
该模块定义了在 Warmane 服务器上所拥有的角色. 并且提供了一系列函数方便于我们对角色进行排列组合.

这个模块里的所有类都是一个 namespace, 仅仅是为了方便引用而提供的类. 这些类下面的方法其实
都可以是 ``staticmethod``. 但是为了免去为每个方法写 ``@staticmethod`` 的麻烦, 我们就
把类名起一个以下划线开头的名字, 然后创建一个名称像类名的实例.
"""

import typing as T

from hotkeynet.game.wow.wlk import (
    Talent as TL,
    TalentCategory as TC,
    Window,
    Character,
)

from .account import AccountEnum


class _CharacterFactory:
    """
    枚举出所有账号下的所有角色的所有天赋.

    例如 fatmulti1 中有这些角色.

    1. batlefury, 防骑, 惩戒, 需要创建 2 个函数
    2. litgoatdka, DK, 坦克 和 冰AOE, 需要创建 2 个函数
    3. litgoatssa, 术士, PvP, 需要创建 1 个函数

    这样我们可以通过调用这些 可以被搜索定位, 名字人类可理解 的函数方便的创建游戏角色的实例.
    """

    def make_char_qsa_pve_protect_pala(self) -> Character:
        return Character(
            account=AccountEnum.account_fat01.value,
            name="qsa",
            talent=TL.paladin_pve_protect,
            window=Window.make(1),
        )

    def make_char_qsb_pve_retri_pala(self) -> Character:
        return Character(
            account=AccountEnum.account_fat02.value,
            name="qsb",
            talent=TL.paladin_pve_retri,
            window=Window.make(2),
        )

    def make_char_qsc_pve_retri_pala(self) -> Character:
        return Character(
            account=AccountEnum.account_fat03.value,
            name="qsc",
            talent=TL.paladin_pve_retri,
            window=Window.make(3),
        )

    def make_char_qsd_pve_retri_pala(self) -> Character:
        return Character(
            account=AccountEnum.account_fat04.value,
            name="qsd",
            talent=TL.paladin_pve_retri,
            window=Window.make(4),
        )

    def make_char_qse_pve_retri_pala(self) -> Character:
        return Character(
            account=AccountEnum.account_fat05.value,
            name="qse",
            talent=TL.paladin_pve_holy,
            window=Window.make(5),
        )


CharacterFactory = _CharacterFactory()


class _LoginCharactersFactory:
    def _make_chars_1_to_5(self) -> T.List[Character]:
        return [
            CharacterFactory.make_char_qsa_pve_protect_pala().set_inactive(),
            CharacterFactory.make_char_qsb_pve_retri_pala().set_inactive(),
            CharacterFactory.make_char_qsc_pve_retri_pala().set_inactive(),
            CharacterFactory.make_char_qsd_pve_retri_pala().set_inactive(),
            CharacterFactory.make_char_qse_pve_retri_pala().set_inactive(),
        ]


LoginCharactersFactory = _LoginCharactersFactory()


class _ActiveCharactersFactory:
    def _set_5p_team_leader(self, chars: T.List[Character]):  # pragma: no cover
        if len(chars) != 5:
            raise ValueError("solo dungeon team has to be 5 member!")

        # find leader char window
        leader_char_window: T.Optional[Window] = None

        # try to find the leader if explicitly defined
        if leader_char_window is None:
            for char in chars:
                if char.is_tank_1:
                    leader_char_window = char.window

        # try to find the leader if it is tank talent
        if leader_char_window is None:
            for char in chars:
                if TC.tank in char.talent.categories:
                    leader_char_window = char.window

        # try to find a plate char
        if leader_char_window is None:
            for char in chars:
                categories = char.talent.categories
                if (
                    TC.warrior in categories
                    or TC.dk in categories
                    or TC.paladin in categories
                ):
                    leader_char_window = char.window

        if leader_char_window is None:
            raise ValueError("you have to define at least one TANK or one Plate char")

        # set other char leader1 as the tank
        for char in chars:
            if char.window.label != leader_char_window.label:
                char.set_leader_1_window(leader_char_window)

        return chars

    def _find_key_char_window(
        self,
        chars: T.List[Character],
        attr: str,
    ) -> T.Optional[Window]:
        """
        从一堆 Character 当中找到那个扮演某个特定队伍角色的人所在的窗口.

        例如找到 1 号司机, 1 号坦克.

        如果一个队伍里有多个人被设为 1 号司机, 那么就设为自然顺序遇到的第一个 1 号司机.
        """
        window: T.Optional[Window] = None
        for char in chars:
            if getattr(char, attr):
                return char.window
        return window

    def _set_key_char_window(
        self,
        chars: T.List[Character],
        attr: str,
        window: Window,
    ):
        """
        例如将指定的窗口设为所有人的 1 号司机.

        这里要注意的是 1 号司机本人不会将自己设为一号司机. 因为司机通常会要绑定焦点. 司机
        本人不需要吧自己设为焦点.
        """
        for char in chars:
            if char.window.label != window.label:
                setattr(char, attr, window)

    def _set_team_leader_and_tank(self, chars: T.List[Character]):  # pragma: no cover
        """
        在定义队伍时, 我们希望能简化操作. 只要在一堆角色中指定谁是 1 号司机, 谁是 2 号司机,
        那么其他人就自动将他们的 Character.leader_1_window, Character.leader_2_window
        设置好.
        """
        # find leader char window
        leader_1_window: T.Optional[Window] = self._find_key_char_window(chars, "is_leader_1")
        leader_2_window: T.Optional[Window] = self._find_key_char_window(chars, "is_leader_2")
        tank_1_window: T.Optional[Window] = self._find_key_char_window(chars, "is_tank_1")
        tank_2_window: T.Optional[Window] = self._find_key_char_window(chars, "is_tank_2")

        if leader_1_window is not None:
            self._set_key_char_window(chars, "leader_1_window", leader_1_window)
        else:
            raise ValueError("At least one char has to be the leader 1")

        if leader_2_window is not None:
            self._set_key_char_window(chars, "leader_2_window", leader_2_window)

        if tank_1_window is not None:
            self._set_key_char_window(chars, "tank_1_window", tank_1_window)

        if tank_2_window is not None:
            self._set_key_char_window(chars, "leader_1_window", tank_2_window)

        return chars

    __anchor_make_team_warmane_solo_dungeon = None

    def make_team_solo_dungeon_qs_abcde(self) -> T.List[Character]:
        """
        主力 5 人组
        """
        return self._set_team_leader_and_tank(chars=[
            (
                CharacterFactory.make_char_qsa_pve_protect_pala()
                    .set_is_leader_1().set_tank_1().set_dr_pala_1()
                    .set_is_leader_2().set_tank_2().set_dr_pala_2()
            ),
            CharacterFactory.make_char_qsb_pve_retri_pala(),
            CharacterFactory.make_char_qsc_pve_retri_pala(),
            CharacterFactory.make_char_qsd_pve_retri_pala(),
            CharacterFactory.make_char_qse_pve_retri_pala(),
        ])


ActiveCharactersFactory = _ActiveCharactersFactory()


class _CharacterHelper:
    def sort_chars_by_window_label(
        self,
        chars: T.Iterable[Character],
    ) -> T.List[Character]:
        """
        将许多角色按照所在的窗口编号排序.
        """
        return list(sorted(chars, key=lambda char: char.window.label))

    def sort_chars_by_window_title(
        self,
        chars: T.Iterable[Character],
    ) -> T.List[Character]:
        """
        将许多角色按照所在的窗口名称排序.
        """
        return list(sorted(chars, key=lambda char: char.window.title))

    def filter_by_talent(
        self,
        chars: T.Iterable[Character],
        tl: TL,
    ) -> T.List[Character]:
        """
        筛选出属于某个天赋的所有角色.

        例如你可以选出所有 PvE DK 血坦克 ``Talent.dk_pve_blood_tank`` 的角色.
        """
        return [
            char
            for char in chars
            if char.talent is tl
        ]

    def filter_by_talent_category(
        self,
        chars: T.Iterable[Character],
        tc: TC,
    ) -> T.List[Character]:
        """
        筛选出天赋属于某个天赋类别的所有角色.

        例如你可以选出所有 PvE Tank 类别的角色. 实际上是先根据类别找出所有对应的天赋的集合,
        然后一一判断这个角色的天赋在不在集合中.
        """
        talent_set = tc.talents
        return [
            char
            for char in chars
            if char.talent in talent_set
        ]


CharacterHelper = _CharacterHelper()
