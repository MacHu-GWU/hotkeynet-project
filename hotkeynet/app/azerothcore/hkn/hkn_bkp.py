# -*- coding: utf-8 -*-

import typing as T

import attr
from attrs_mate import AttrsClass

import hotkeynet as hk
from hotkeynet import KN
from hotkeynet import utils
from hotkeynet.game.wow.wlk import (
    Character,
    Window,
    Talent as TL,
    TalentCategory as TC,
    char_oset_helper,
)

from . import act
from .icons import Icons

if T.TYPE_CHECKING:
    from .mode.base import Mode


@attr.s
class HknScript(AttrsClass):
    mode: 'Mode' = attr.ib(default=None)
    script: hk.Script = attr.ib(factory=hk.Script)

    def __attrs_post_init__(self):
        # 此时 Script 已经不再 context 中, 我们也不希望没定义一个 Hotkey 就一直用
        # with script 的语法. 所以我们手动将 script 对象设置为 Context 的顶层

        self.build_hk_group_10()
        self.build_hk_group_11_healbot()
        self.build_control_panel()

