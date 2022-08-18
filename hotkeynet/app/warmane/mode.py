# -*- coding: utf-8 -*-

"""
第一步先定义游戏用什么窗口, 什么分辨率, 上哪些角色
"""

import typing as T

import attr
from attrs_mate import AttrsClass

# from .character import CharacterFactory
from .character import Character
from .game_client import GameClient


@attr.s
class Mode(AttrsClass):
    """
    代表你使用多开脚本进行游戏的设置, 包含了以下内容:

    1. 游戏窗口的位置, 分辨率
    2. 上哪些角色的哪个天赋
    3. 每个角色在哪个窗口中
    4. 各个角色分别扮演团队中的什么位置
    5. 等等
    """
    game_client_setup: GameClient = attr.ib(default=None)
    active_chars: T.List[Character] = attr.ib(factory=list)
    login_chars: T.List[Character] = attr.ib(factory=list)

    def mode_solo_dungeon_batlefury_quentin_opiitou_swagsonic_kangliu(self):
        pass

# Setup(
#     active_characters=[
#         CharacterFactory.make_char_fatmulti1_batlefury_pve_protect_pala().
#     ]
# )
