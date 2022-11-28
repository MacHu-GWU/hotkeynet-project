# -*- coding: utf-8 -*-

import typing as T

import attr
from attrs_mate import AttrsClass
import hotkeynet as hk

from .label import LabelMixin
from .cmd import CommandMixin
from .hk_group_01_window_and_login import HotkeyGroup01WindowAndLoginMixin
from .hk_group_02_movement import HotkeyGroup02MovementMixin
from .hk_group_03_act_1_to_12 import HotkeyGroup03Act1To12Mixin

if T.TYPE_CHECKING:
    from ..mode.base import Mode


@attr.s
class HknScript(
    AttrsClass,
    LabelMixin,
    CommandMixin,
    HotkeyGroup01WindowAndLoginMixin,
    HotkeyGroup02MovementMixin,
    HotkeyGroup03Act1To12Mixin,
):
    mode: "Mode" = attr.ib(default=None)
    script: hk.Script = attr.ib(factory=hk.Script)

    def __attrs_post_init__(self):
        # 此时 Script 已经不再 context 中, 我们也不希望没定义一个 Hotkey 就一直用
        # with script 的语法. 所以我们手动将 script 对象设置为 Context 的顶层
        hk.context.push(self.script)
        self.build_label_mixin()
        self.build_command_mixin()
        self.build_hk_group_01_window_and_login_mixin()
        self.build_hk_group_02_movement_mixin()
        self.build_hk_group_03_act_1_to_12_mixin()