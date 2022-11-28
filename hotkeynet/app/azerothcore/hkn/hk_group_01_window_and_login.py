# -*- coding: utf-8 -*-

"""
实现与 "切换游戏客户端" 以及 "账号登录" 有关的快捷键.
"""

import typing as T

import hotkeynet as hk
from hotkeynet import KN


if T.TYPE_CHECKING:
    from .script import HknScript


class HotkeyGroup01WindowAndLoginMixin:
    def build_hk_round_robin_toggle_window(self: "HknScript"):
        with hk.Hotkey(
            id="RoundRobinToggleWindow",
            key=KN.SCROLOCK_ON(KN.CTRL_(KN.TAB)),
        ) as self.hk_round_robin_toggle_window:
            for char in self.mode.active_chars:
                with hk.Toggle():
                    self.cmd_bring_window_to_foreground.call(args=[char.window.title, ])

    def build_hk_toggle_specific_window(self: "HknScript"):
        """
        定义切换到指定窗口的快捷键.

        我们一共最多有 25 个窗口, 但不止 25 个可玩的角色. 这些角色可能今天在 1 号窗口玩,
         可能明天就在 2 号窗口玩. 为了降低人类的记忆成本, 所以我们有如下设计:

        切换到 1 ~ 25 号窗口的快捷键分别是:

        - Ctrl + F1 ~ F10, WoW1 - WoW10 窗口 (Ctrl F11, F12 留给了快捷键)
        - Shift + F5 ~ F12: WoW11 - WoW18 窗口 (Shift, F1, F2, F3, F4 留给了快捷键)
        - Shift + 小键盘的 Insert Home PgUp Delete, End, PgDn: WoW19 - WoW24 窗口

        具体这个窗口里的人物是谁我们不管.
        """
        # 10 + 8 + 6 = 24
        ctrl_f1_to_10 = [
            KN.SCROLOCK_ON(KN.CTRL_(key))
            for key in KN.F1_to_F12[:10]
        ]
        shift_f5_to_f12 = [
            KN.SCROLOCK_ON(KN.SHIFT_(key))
            for key in KN.F1_to_F12[4:]
        ]
        shift_insert_to_pgdn = [
            KN.SCROLOCK_ON(KN.SHIFT_(key))
            for key in KN.INSERT_TO_PGDN
        ]
        ctrl_f12 = [
            KN.SCROLOCK_ON(KN.CTRL_(KN.F12))
        ]
        HOTKEY_LIST_TOGGLE_SPECIFIC_WINDOW_1_TO_25 = (
            ctrl_f1_to_10
            + shift_f5_to_f12
            + shift_insert_to_pgdn
            + ctrl_f12
        )
        assert len(HOTKEY_LIST_TOGGLE_SPECIFIC_WINDOW_1_TO_25) == 25

        self.hk_list_toggle_specific_window: T.List[hk.Hotkey] = list()
        for index, key in enumerate(HOTKEY_LIST_TOGGLE_SPECIFIC_WINDOW_1_TO_25, start=1):
            with hk.Hotkey(
                id=f"ToggleToSpecificWindow {key}",
                key=key,
            ) as hotkey:
                self.cmd_bring_window_to_foreground.call(args=[Window.make(index).title, ])
                self.hk_list_toggle_specific_window.append(hotkey)

    def build_hk_center_overlap_layout(self: "HknScript"):
        with hk.Hotkey(
            id="CenterOverlapLayout",
            key=KN.SCROLOCK_ON(KN.CTRL_SHIFT_ALT(KN.NUMPAD_11_DIVIDE)),
        ) as self.hk_center_overlap_layout:
            self.cmd_center_overlap_layout.call()

    def build_hk_login_specific_account(self: "HknScript"):
        """
        定义在指定窗口登录指定账号的快捷键.

        我们一共最多有 25 个窗口, 但不止 25 个可玩的角色. 这些角色可能今天在 1 号窗口玩,
         可能明天就在 2 号窗口玩. 为了降低人类的记忆成本, 所以我们有如下设计:

        切换到 1 ~ 25 号窗口并登录的快捷键分别是:

        - Ctrl Alt + F1 ~ F10, WoW1 - WoW10 窗口 (Ctrl Alt F11, F12 留给了快捷键)
        - Shift Alt + F5 ~ F12: WoW11 - WoW18 窗口 (Shift Alt, F1, F2, F3, F4 留给了快捷键)
        - Shift Alt + 小键盘的 Insert Home PgUp Delete, End, PgDn: WoW19 - WoW24 窗口

        具体这个窗口里的人物是谁, 这个由 Mode.login_chars 和 Mode.active_chars 共同决定.
        """
        # 10 + 8 + 6 = 24
        ctrl_alt_f1_to_10 = [
            KN.SCROLOCK_ON(KN.CTRL_ALT_(key))
            for key in KN.F1_to_F12[:10]
        ]
        shift_alt_f5_to_f12 = [
            KN.SCROLOCK_ON(KN.ALT_SHIFT_(key))
            for key in KN.F1_to_F12[4:]
        ]
        shift_alt_insert_to_pgdn = [
            KN.SCROLOCK_ON(KN.ALT_SHIFT_(key))
            for key in KN.INSERT_TO_PGDN
        ]
        ctrl_alt_f12 = [
            KN.SCROLOCK_ON(KN.CTRL_ALT_(KN.F12)),
        ]

        HOTKEY_LIST_LOGIN_SPECIFIC_ACCOUNT_1_TO_25 = (
            ctrl_alt_f1_to_10
            + shift_alt_f5_to_f12
            + shift_alt_insert_to_pgdn
            + ctrl_alt_f12
        )

        assert len(HOTKEY_LIST_LOGIN_SPECIFIC_ACCOUNT_1_TO_25) == 25

        self.hk_list_toggle_specific_window: T.List[hk.Hotkey] = list()

        for window, account in self.mode.login_window_and_account_pairs:
            with hk.Hotkey(
                id=f"SingleLogin{account.username.title()}",
                key=HOTKEY_LIST_LOGIN_SPECIFIC_ACCOUNT_1_TO_25[int(window.label.replace("w", "")) - 1],
            ) as hotkey:
                self.cmd_enter_username_and_password.call(args=[
                    window.title,
                    account.username,
                    account.password,
                ])
                self.hk_list_toggle_specific_window.append(hotkey)

    def build_hk_batch_logout(self: "HknScript"):
        with hk.Hotkey(
            id="BatchLogout",
            key=KN.SCROLOCK_ON(KN.CTRL_ALT_(KN.O)),
        ) as self.hk_batch_logout:
            with hk.SendLabel(
                to=self.mode.lbs_all,
            ):
                # 确保菜单界面是关闭的状态
                hk.Wait.make(100),
                act.General.TOGGLE_MAIN_GAME_MENU(),
                hk.Wait.make(50),
                act.General.TOGGLE_MAIN_GAME_MENU(),
                hk.Wait.make(50),
                # 点击关闭菜单按钮
                hk.MoveMouse(
                    x=self.mode.game_client.return_to_game_button_x,
                    y=self.mode.game_client.return_to_game_button_y,
                )
                hk.Wait.make(50)
                hk.ClickMouse.make_left_click_on_window()
                hk.Wait.make(50)
                # 现在菜单按钮确保已经关上了, 然后可以打开菜单
                act.General.TOGGLE_MAIN_GAME_MENU()
                hk.Wait.make(50)
                # 点击登出按钮
                hk.MoveMouse(
                    x=self.mode.game_client.log_out_button_x,
                    y=self.mode.game_client.log_out_button_y,
                )
                hk.Wait.make(50)
                hk.ClickMouse.make_left_click_on_window()

    def build_hk_logout_on_current_window(self: "HknScript"):
        with hk.Hotkey(
            id="LogoutOnCurrentWindow",
            key=KN.SCROLOCK_ON(KN.CTRL_(KN.O)),
        ) as self.hk_logout_on_current_window:
            with hk.SendFocusWin():
                # 确保菜单界面是关闭的状态
                hk.Wait.make(100),
                act.General.TOGGLE_MAIN_GAME_MENU(),
                hk.Wait.make(50),
                act.General.TOGGLE_MAIN_GAME_MENU(),
                hk.Wait.make(50),
                # 点击关闭菜单按钮
                hk.MoveMouse(
                    x=self.mode.game_client.return_to_game_button_x,
                    y=self.mode.game_client.return_to_game_button_y,
                )
                # 点击关闭菜单按钮
                hk.MoveMouse(
                    x=self.mode.game_client.return_to_game_button_x,
                    y=self.mode.game_client.return_to_game_button_y,
                )
                hk.Wait.make(50)
                hk.ClickMouse.make_left_click_on_window()
                hk.Wait.make(50)
                # 现在菜单按钮确保已经关上了, 然后可以打开菜单
                act.General.TOGGLE_MAIN_GAME_MENU()
                hk.Wait.make(50)
                # 点击登出按钮
                hk.MoveMouse(
                    x=self.mode.game_client.log_out_button_x,
                    y=self.mode.game_client.log_out_button_y,
                )
                hk.Wait.make(50)
                hk.ClickMouse.make_left_click_on_window()

    def build_hk_group_01_window_and_login_mixin(self: "HknScript"):
        self.build_hk_round_robin_toggle_window()
        self.build_hk_toggle_specific_window()
        self.build_hk_center_overlap_layout()
        self.build_hk_login_specific_account()
        self.build_hk_batch_logout()
        self.build_hk_logout_on_current_window()