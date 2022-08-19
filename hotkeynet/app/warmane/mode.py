# -*- coding: utf-8 -*-

"""
第一步先定义游戏用什么窗口, 什么分辨率, 上哪些角色
"""

import typing as T

import attr
from attrs_mate import AttrsClass

import hotkeynet as hk
from hotkeynet.game.wow.wlk import Window

from .character import (
    sort_chars_by_window_label,
    Character,
    LoginCharactersFactory,
    ActiveCharactersFactory,
)
from .game_client import GameClient
from .hkn import HknScript
from .paths import path_warmane_hkn


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
        self.active_chars = sort_chars_by_window_label(self.active_chars)
        self.login_chars = sort_chars_by_window_label(self.login_chars)
        self._resolve_login()
        self.hkn_script = HknScript(mode=self)

    def dump(self, verbose: bool = False):
        path_warmane_hkn.write_text(
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
        self.managed_chars = sort_chars_by_window_label(self.managed_chars)

    # --------------------------------------------------------------------------
    @classmethod
    def use_solo_dungeon_batlefury_quentin_opiitou_swagsonic_kangliu(cls):
        return cls(
            game_client=GameClient().use_1920_1080_resolution(),
            # game_client=GameClient().use_1600_900_resolution(),
            # game_client=GameClient().use_1176_664_resolution(),
            login_chars=LoginCharactersFactory.make_chars_10p(),
            active_chars=ActiveCharactersFactory.make_team_solo_dungeon_batlefury_quentin_opiitou_swagsonic_kangliu(),
        )
