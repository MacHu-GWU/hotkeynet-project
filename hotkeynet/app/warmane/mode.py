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

    def __attrs_post_init__(self):
        self.hkn_script = HknScript(mode=self)

    def dump(self, verbose: bool = False):
        path_warmane_hkn.write_text(
            self.hkn_script.script.render(verbose=verbose),
        )

    @property
    def launched_windows(self) -> T.List[Window]:
        launched_labels = set()
        launched_windows = list()
        for char in self.active_chars:
            if char.window.label not in launched_labels:
                launched_windows.append(char.window)
                launched_labels.add(char.window.label)
        for char in self.login_chars:
            if char.window.label not in launched_labels:
                launched_windows.append(char.window)
                launched_labels.add(char.window.label)
        launched_windows = list(sorted(
            launched_windows,
            key=lambda w: w.label
        ))
        return launched_windows

    @property
    def labels(self) -> T.List[hk.Label]:
        return [
            hk.Label.make(name=window.label, window=window.title)
            for window in self.launched_windows
        ]

    # @property
    # def logins(self):
    #     pass

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