# -*- coding: utf-8 -*-

"""
实现在多开模式下 小键盘 Numpad 1-12 的功能. 这些按键可以用专用 MMORPG 鼠标的侧面轻松按到.
"""

import typing as T

import hotkeynet as hk
from hotkeynet import KN
from hotkeynet.game.wow.wlk import (
    Character,
    Window,
    Talent as TL,
    TalentCategory as TC,
    char_oset_helper,
)
from hotkeynet.app.wow.wlk.servers.acore import act

if T.TYPE_CHECKING:
    from .script import HknScript


class HotkeyGroup05Numpad1To12Mixin:
    def build_hk_numpad_4(self: "HknScript"):
        """
        重置摄像头
        """
        with hk.Hotkey(
            id="Reset Camera",
            key=KN.SCROLOCK_ON(KN.NUMPAD_4),
        ) as self.hk_numpad_4_reset_camera:
            with hk.SendLabel(
                id="all",
                to=self.mode.lbs_all,
            ):
                act.camera.SET_FIRST_CAMERA_VIEW_2()

    def build_hk_numpad_5(self: "HknScript"):
        """
        所有萨满放置图腾.
        """
        with hk.Hotkey(
            id="ShamanPutTotem",
            key=KN.SCROLOCK_ON(KN.NUMPAD_5),
        ) as self.hk_numpad_5_shaman_put_totem:
            with hk.SendLabel(
                id=TC.shaman.name,
                to=self.mode.lbs_by_tc(TC.shaman),
            ):
                act.shaman.Call_of_the_Ancestors()

    def build_hk_numpad_6(self: "HknScript"):
        """
        **功能**

        所有萨满回收所有图腾.
        """
        with hk.Hotkey(
            id="ShamanRecallTotem",
            key=KN.SCROLOCK_ON(KN.NUMPAD_6),
        ) as self.hk_numpad_6_shaman_recall_totem:
            with hk.SendLabel(
                name=TC.shaman.name,
                to=self.mode.lbs_by_tc(TC.shaman),
            ):
                act.shaman.Totemic_Recall()

    def build_hk_numpad_7(self: "HknScript"):
        """
        所有人后退一步, 解除跟随状态.
        """
        with hk.Hotkey(
            id="StopFollowing",
            key=KN.SCROLOCK_ON(KN.NUMPAD_7),
        ) as self.hk_numpad_7_all_move_backward:
            with hk.SendLabel(
                id="all",
                to=self.mode.lbs_all,
            ):
                act.movement.MOVE_BACKWARD()

    def build_hk_numpad_8(self: "HknScript"):
        """
        在所有窗口内的相对位置一样的地方点击左键, 用于接受任务, 点击界面上的菜单, 打开关闭包裹等.

        设置于 Numpad8 是因为左键用的频率较高, 使用 MMO 鼠标时大拇指自然的就在这个位置.
        建议为非司机角色设置摄像头永久跟随, 使得所有人的视野方向一致.
        """
        with hk.Hotkey(
            id="SyncLeftClick",
            key=KN.SCROLOCK_ON(KN.NUMPAD_8),
        ) as self.hk_numpad_8_sync_left_click:
            with hk.SendLabel(
                id="all",
                to=self.mode.lbs_all,
            ):
                hk.ClickMouse(button=KN.MOUSE_LButton)

    def build_hk_numpad_9(self: "HknScript"):
        """
        在所有窗口内的相对位置一样的地方点击右键, 用于与物品互动, 捡东西等.

        设置于 Numpad9 是因为想要放在 左键点击 Hotkey 的按键 Numpad8 旁边.
        建议为非司机角色设置摄像头永久跟随, 使得所有人的视野方向一致.
        """
        with hk.Hotkey(
            id="SyncRightClick",
            key=KN.SCROLOCK_ON(KN.NUMPAD_9),
        ) as self.hk_numpad_9_sync_right_click:
            with hk.SendLabel(
                id="all",
                to=self.mode.lbs_all,
            ):
                hk.ClickMouse(button=KN.MOUSE_RButton),

    def build_hk_numpad_10(self: "HknScript"):
        """
        所有人跟随焦点人物.
        """
        with hk.Hotkey(
            id="AllFollowFocus",
            key=KN.SCROLOCK_ON(KN.NUMPAD_0),
        ) as self.hk_numpad_0_all_follow_focus:
            with hk.SendLabel(
                id="all",
                to=self.mode.lbs_all,
            ):
                act.movement.FOLLOW_FOCUS()

    def build_hk_numpad_11(self: "HknScript"):
        """
        **功能**

        所有人上坐骑或是飞行形态.

        需要将上马宏放在 Numpad11 键位上. 具体的宏请参考 ``act.General.MOUNT_UP``.
        """
        with hk.Hotkey(
            id="AllMountUp",
            key=KN.SCROLOCK_ON(KN.NUMPAD_11_DIVIDE),
        ) as self.hk_numpad_11_mount_up:
            with hk.SendLabel(
                id="all",
                to=self.mode.lbs_all,
            ):
                act.general.MOUNT_UP_MACRO_KEY_NUMPAD_11_DIVIDE()

    def build_hk_numpad_12(self: "HknScript"):
        """
        跟焦点的目标右键点击互动, 常用于接任务, 剥皮, 对话.

        该键位于 MMO 鼠标的右下角 12 号(Multiply) 位置, 比较好按.
        """
        with hk.Hotkey(
            id="InteractFocusTarget",
            key=KN.SCROLOCK_ON(KN.NUMPAD_12_MULTIPLY),
        ) as self.hk_numpad_12_interact_with_focus_target:
            with hk.SendLabel(
                id="all",
                to=self.mode.lbs_all,
            ):
                act.target.TARGET_FOCUS_TARGET()
                act.target.INTERACT_WITH_TARGET()

    def build_hk_group_05_numpad_1_to_12_mixin(self: "HknScript"):
        self.build_hk_numpad_4()
        self.build_hk_numpad_5()
        self.build_hk_numpad_6()
        self.build_hk_numpad_7()
        self.build_hk_numpad_8()
        self.build_hk_numpad_9()
        self.build_hk_numpad_10()
        self.build_hk_numpad_11()
        self.build_hk_numpad_12()
