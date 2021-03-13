# -*- coding: utf-8 -*-

"""
实现在多开模式下 小键盘 Numpad 1-12 的功能.
"""

from .. import act
from ._config_and_script import config, script
from ..constant.talent_category_association import TalentCategory
from .... import keyname
from ....script import (
    Hotkey,
    Mouse, SendLabel,
)

def build_hk_numpad_4():
    """
    **功能**

    所有萨满放置图腾.
    """
    return Hotkey(
        name="Reset Camera",
        key=keyname.SCROLOCK_ON(keyname.NUMPAD_4),
        actions=[
            SendLabel(
                name="all",
                to=config.lbs_all(),
                actions=[
                    act.Camera.SET_FIRST_CAMERA_VIEW_2,
                ]
            )
        ],
        script=script,
    )

hk_numpad_4_reset_camera = build_hk_numpad_4()


def build_hk_numpad_5():
    """
    **功能**

    所有萨满放置图腾.
    """
    return Hotkey(
        name="ShamanPutTotem",
        key=keyname.SCROLOCK_ON(keyname.NUMPAD_5),
        actions=[
            SendLabel(
                name=TalentCategory.shaman.name,
                to=config.lbs_by_tc(TalentCategory.shaman),
                actions=[
                    act.Shaman.ALL_SPEC_CALL_OF_THE_ELEMENTS,
                ]
            )
        ],
        script=script,
    )

hk_numpad_5_shaman_put_totem = build_hk_numpad_5()


def build_hk_numpad_6():
    """
    **功能**

    所有萨满回收所有图腾.
    """
    return Hotkey(
        name="ShamanRecallTotem",
        key=keyname.SCROLOCK_ON(keyname.NUMPAD_6),
        actions=[
            SendLabel(
                name=TalentCategory.shaman.name,
                to=config.lbs_by_tc(TalentCategory.shaman),
                actions=[
                    act.Shaman.ALL_SPEC_TOTEMIC_RECALL,
                ]
            )
        ],
        script=script,
    )

hk_numpad_6_shaman_recall_totem = build_hk_numpad_6()


def build_hk_numpad_7():
    """
    **功能**

    所有人后退一步, 解除跟随状态.
    """
    return Hotkey(
        name="StopFollowing",
        key=keyname.SCROLOCK_ON(keyname.NUMPAD_7),
        actions=[
            SendLabel(
                name="all",
                to=config.lbs_all(),
                actions=[
                    act.Movement.MOVE_BACKWARD,
                ]
            )
        ],
        script=script,
    )

hk_numpad_7_all_move_backward = build_hk_numpad_7()


def build_hk_numpad_8():
    """
    **功能**

    在所有窗口内的相对位置一样的地方点击左键, 用于接受任务, 点击界面上的菜单, 打开关闭包裹等.

    设置于 Numpad8 是因为左键用的频率较高, 使用 MMO 鼠标时大拇指自然的就在这个位置.
    建议为非司机角色设置摄像头永久跟随, 使得所有人的视野方向一致.
    """
    return Hotkey(
        name="SyncLeftClick",
        key=keyname.SCROLOCK_ON(keyname.NUMPAD_8),
        actions=[
            SendLabel(
                name="all",
                to=config.lbs_all(),
                actions=[
                    Mouse(button=keyname.MOUSE_LButton),
                ]
            )
        ],
        script=script,
    )


hk_numpad_8_sync_left_click = build_hk_numpad_8()


def build_hk_numpad_9():
    """
    **功能**

    在所有窗口内的相对位置一样的地方点击右键, 用于与物品互动, 捡东西等.

    设置于 Numpad9 是因为想要放在 左键点击 Hotkey 的按键 Numpad8 旁边.
    建议为非司机角色设置摄像头永久跟随, 使得所有人的视野方向一致.
    """
    return Hotkey(
        name="SyncRightClick",
        key=keyname.SCROLOCK_ON(keyname.NUMPAD_9),
        actions=[
            SendLabel(
                name="all",
                to=config.lbs_all(),
                actions=[
                    Mouse(button=keyname.MOUSE_RButton),
                ]
            )
        ],
        script=script,
    )


hk_numpad_9_sync_right_click = build_hk_numpad_9()


def build_hk_numpad_0():
    """
    **功能**

    所有人跟随焦点人物.
    """
    return Hotkey(
        name="AllFollowFocus",
        key=keyname.SCROLOCK_ON(keyname.NUMPAD_0),
        actions=[
            SendLabel(
                name="all",
                to=config.lbs_all(),
                actions=[
                    act.Movement.FOLLOW_FOCUS,
                ]
            )
        ],
        script=script,
    )


hk_numpad_0_all_follow_focus = build_hk_numpad_0()


def build_hk_numpad_11():
    """
    **功能**

    所有人上坐骑或是飞行形态.

    需要将上马宏放在 Numpad11 键位上. 具体的宏请参考 ``act.General.MOUNT_UP``.
    """
    return Hotkey(
        name="AllMountUp",
        key=keyname.SCROLOCK_ON(keyname.NUMPAD_11_DIVIDE),
        actions=[
            SendLabel(
                name="all",
                to=config.lbs_all(),
                actions=[
                    act.General.MOUNT_UP_MACRO_KEY_NUMPAD_11_DIVIDE,
                ]
            )
        ],
        script=script,
    )


hk_numpad_11_mount_up = build_hk_numpad_11()


def build_hk_numpad_12():
    """
    **功能鞥**

    跟焦点的目标右键点击互动, 常用于接任务, 剥皮, 对话.

    该键位于 MMO 鼠标的右下角 12 号(Multiply) 位置, 比较好按.
    """
    return Hotkey(
        name="InteractFocusTarget",
        key=keyname.SCROLOCK_ON(keyname.NUMPAD_12_MULTIPLY),
        actions=[
            SendLabel(
                name="all",
                to=config.lbs_all(),
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    act.Target.INTERACT_WITH_TARGET,
                ]
            )
        ],
        script=script,
    )


hk_numpad_12_interact_with_focus_target = build_hk_numpad_12()
