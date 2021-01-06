# -*- coding: utf-8 -*-

from . import act
from .script import script
from .config import Config
from ... import keyname
from ...script import (
    Script, Command, Hotkey,
    Key, Mouse, SendLabel,
    CallCommand,
)

hk_numpad8_SyncLeftClick = Hotkey(
    name="SyncLeftClick",
    key=keyname.SCROLOCK_ON(keyname.NUMPAD_8),
    actions=[
        SendLabel(
            to=Config.SendLabelTo.all,
            actions=[
                Mouse(button=keyname.MOUSE_LButton),
            ]
        )
    ],
    script=script,
)
"""
在所有窗口内的相对位置一样的地方点击左键, 用于接受任务, 点击界面上的菜单, 打开关闭包裹等.
设置于 Numpad8 是因为左键用的频率较高, 使用 MMO 鼠标时大拇指自然的就在这个位置.
建议为非司机角色设置摄像头永久跟随, 使得所有人的视野方向一致.
"""

hk_numpad9_SyncRightClick = Hotkey(
    name="SyncRightClick",
    key=keyname.SCROLOCK_ON(keyname.NUMPAD_9),
    actions=[
        SendLabel(
            to=Config.SendLabelTo.all,
            actions=[
                Mouse(button=keyname.MOUSE_RButton),
            ]
        )
    ],
    script=script,
)
"""
在所有窗口内的相对位置一样的地方点击右键, 用于与物品互动, 捡东西等.
设置于 Numpad9 是因为想要放在 左键点击 Hotkey 的按键 Numpad8 旁边.
建议为非司机角色设置摄像头永久跟随, 使得所有人的视野方向一致.
"""

hk_numpad0_AllFollowFocus= Hotkey(
    name="AllFollowFocus",
    key=keyname.SCROLOCK_ON(keyname.NUMPAD_0),
    actions=[
        SendLabel(
            to=Config.SendLabelTo.all,
            actions=[
                act.General.FOLLOW_FOCUS,
            ]
        )
    ],
    script=script,
)
"""
将跟随焦点目标的宏 ``/follow focus`` 放在 Numpad0 键位上.
"""

hk_numpad11_mount_up= Hotkey(
    name="AllMountUp",
    key=keyname.SCROLOCK_ON(keyname.NUMPAD_11_DIVIDE),
    actions=[
        SendLabel(
            to=Config.SendLabelTo.all,
            actions=[
                act.General.MOUNT_UP,
            ]
        )
    ],
    script=script,
)
"""
所有人上马, 需要将上马宏放在 Numpad11 键位上. 具体的宏请参考 ``act.General.MOUNT_UP``.
"""

hk_numpad12_interact= Hotkey(
    name="AllInteractFocusTarget",
    key=keyname.SCROLOCK_ON(keyname.NUMPAD_12_MULTIPLY),
    actions=[
        SendLabel(
            to=Config.SendLabelTo.all,
            actions=[
                act.General.TARGET_FOCUS_TARGET,
                act.General.INTERACT_WITH_TARGET,
            ]
        )
    ],
    script=script,
)
"""
跟焦点的目标右键点击互动, 常用于接任务, 剥皮. 该键位于 MMO 鼠标的右下角 12 号(Multiply) 位置, 比较好按.
"""