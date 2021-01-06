# -*- coding: utf-8 -*-

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
    name="SyncRightClick",
    key=keyname.SCROLOCK_ON(keyname.NUMPAD_0),
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

