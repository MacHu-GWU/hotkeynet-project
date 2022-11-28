# -*- coding: utf-8 -*-

import typing as T

import attr
from attrs_mate import AttrsClass
import hotkeynet as hk

from .label import LabelMixin
from .cmd import CommandMixin

if T.TYPE_CHECKING:
    from ..mode.base import Mode


@attr.s
class HknScript(
    AttrsClass,
    LabelMixin,
    CommandMixin,
):
    mode: "Mode" = attr.ib(default=None)
    script: hk.Script = attr.ib(factory=hk.Script)

    def __attrs_post_init__(self):
        # 此时 Script 已经不再 context 中, 我们也不希望没定义一个 Hotkey 就一直用
        # with script 的语法. 所以我们手动将 script 对象设置为 Context 的顶层
        hk.context.push(self.script)
        self.build_label_mixin()
        self.build_command_mixin()
