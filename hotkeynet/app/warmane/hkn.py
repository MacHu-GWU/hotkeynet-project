# -*- coding: utf-8 -*-

import typing as T

import attr
from attrs_mate import AttrsClass

import hotkeynet as hk
from hotkeynet import KN
from hotkeynet.game.wow.wlk import (
    Character,
    Window,
    Talent,
    TalentCategory,
)

from . import act

if T.TYPE_CHECKING:
    from .mode import Mode


@attr.s
class HknScript(AttrsClass):
    mode: 'Mode' = attr.ib(default=None)
    script: hk.Script = attr.ib(factory=hk.Script)

    def __attrs_post_init__(self):
        hk.context.push(self.script)
        self.build_labels()
        self.build_cmd()
        self.build_hk_01()
        self.build_control_panel()

    def build_labels(self):
        self.labels = [
            hk.Label.make(name=char.window.label, window=char.window.title)
            for char in self.mode.managed_chars
        ]
        self.n_labels = len(self.labels)

    # -------------------------------------------------------------------------
    # 实现各种 "命令".
    # -------------------------------------------------------------------------
    def build_cmd_launch_and_rename_game_client(self):
        """
        运行一个游戏客户端, 并重命名游戏窗口.

        参数定义:

        - %1%: Local or IP address; example: Local 表示本地, 192.168.0.1 表示局域网中的其他机器的 IP
        - %2%: 窗口的新名称; example: WoW1

        这里的窗口的新名称是用来指定给哪个窗口发送键盘鼠标命令的关键.
        """
        with hk.Command(
            name="LaunchAndRenameGameClient",
        ) as self.cmd_launch_and_rename_game_client:
            with hk.SendPC():
                hk.Run.make(self.mode.game_client.wow_exe_path)
                hk.RenameWin(old="World of Warcraft", new=hk.CommandArgEnum.Arg1)

    def build_cmd_launch_and_rename_all_game_client(self):
        """
        批量启动多个游戏窗口并全部重命名.

        注意!!! 在 HotketNet 界面菜单上的 Options -> Settings 中有一项
        Window name match 一定要勾选 Exact Match. 如果勾选的是 Partial Match,
        则你在调用 WoW1 窗口的时候, 由于是用的部分匹配, WoW10 也会被匹配到,
        导致你的 WoW1 和 WoW10 无法被区分开来.
        """
        with hk.Command(
            name="LaunchAndRenameAllGameClient",
        ) as self.cmd_launch_and_rename_all_game_client:
            for char in self.mode.managed_chars:
                self.cmd_launch_and_rename_game_client.call(args=[char.window.title, ])

    def build_cmd_bring_window_to_foreground(self):
        """
        将某个窗口作为当前焦点窗口, 带到最前端.

        参数:

        - %1%: 窗口名, 例如: WoW01

        说明:

        This command may cause: Operating system SetForegroundWindow function failed;
        Windows reports system error 0. **You CANNOT operate this too fast**.
        """
        with hk.Command(
            name="BringWindowToForeground",
        ) as self.cmd_bring_window_to_foreground:
            with hk.SendPC():
                with hk.TargetWin(window=hk.CommandArgEnum.Arg1):
                    hk.Wait.make(50)
                    hk.SetForegroundWin()  # This command response fast
                    # hk.SetActiveWin()  # This command cause big delay

    def build_cmd_resize_and_relocate_window(self):
        """
        将某个窗口尺寸调整, 给左边留出一竖条用于 Control Panel, 并移动到屏幕中心区域.
        Resize and Relocate the Specified Window to the center.
        """
        with hk.Command(
            name="ResizeAndRelocateWindow",
        ) as self.cmd_resize_and_relocate_window:
            with hk.SendPC():
                with hk.Wait.make(50):
                    with hk.SendWinM(window=hk.CommandArgEnum.Arg1):
                        hk.SetWinRect.make(
                            x=self.mode.game_client.window_left_top_x,
                            y=self.mode.game_client.window_left_top_y,
                            width=self.mode.game_client.window_width,
                            height=self.mode.game_client.window_height,
                        )

    def build_cmd_center_overlap_layout(self):
        """
        让所有窗口都符合 ResizeAndRelocateWindow 中的尺寸和位置设置
        Apply ResizeAndRelocateWindow to all window
        """
        with hk.Command(
            name="CenterOverlapLayout",
        ) as self.cmd_center_overlap_layout:
            for char in self.mode.managed_chars:
                self.cmd_resize_and_relocate_window.call(args=[char.window.title, ])

    def build_cmd_enter_username_and_password(self):
        """
        在指定游戏客户端窗口内填入账号密码.

        参数定义:

        - %1%: 窗口名称
        - %2%: 账号
        - %3%: 密码
        """
        with hk.Command(
            name="EnterUsernameAndPasssword",
        ) as self.cmd_enter_username_and_password:
            with hk.SendPC():
                with hk.SendWin(window=hk.CommandArgEnum.Arg1):
                    # Wait to bring window foreground; 等待将窗口带到最前端
                    hk.Wait.make(500)
                    # Click OK on Wrong Pass Word Pop Out; 清除可能的密码错误窗口, 移除遮挡
                    (
                        hk.ClickMouse(button=hk.MouseButtonEnum.LButton.value)
                        .set_stroke_as_both()
                        .set_target_as_window()
                        .set_mode_as_x_y(
                            x=self.mode.game_client.wrong_password_pop_up_x,
                            y=self.mode.game_client.wrong_password_pop_up_y,
                        )
                        .set_restore_as_no()
                    )
                    hk.Wait.make(300)
                    # Click on username Input Box; 在用户名输入框点击左键
                    (
                        hk.ClickMouse(button=hk.MouseButtonEnum.LButton.value)
                        .set_stroke_as_both()
                        .set_target_as_window()
                        .set_mode_as_x_y(
                            x=self.mode.game_client.username_input_box_x,
                            y=self.mode.game_client.username_input_box_y,
                        )
                        .set_restore_as_no()
                    )
                    hk.Wait.make(300)
                    # Clear off password Input Box; 用 tab 切换到密码输入框然后清空
                    hk.Key.make(KN.TAB)
                    hk.Key.make(KN.BACKSPACE)
                    hk.Wait.make(100)
                    # Clear off username Input Box; 用 tab 切换回用户名输入框然后清空
                    hk.Key.make(KN.TAB)
                    hk.Key.make(KN.BACKSPACE)
                    hk.Wait.make(100)
                    # Enter Username; 输入用户名
                    hk.Text.make(hk.CommandArgEnum.Arg2)
                    hk.Wait.make(100)
                    # Switch To Password; 切换到密码输入框
                    hk.Key.make(KN.TAB)
                    hk.Wait.make(100)
                    # Enter Password; 输入密码
                    hk.Text.make(hk.CommandArgEnum.Arg3)
                    hk.Wait.make(100)
                    # Press Enter; 按下回车登录
                    hk.Key.make(KN.ENTER)
                    # Wait for authentication and load character selection interface; 等待进入角色选择画面
                    hk.Wait.make(500)

    def build_cmd_batch_login(self):
        """
        根据 Active Character 中定义的角色, 批量登录游戏账号.
        """
        with hk.Command(
            name="BatchLogin",
        ) as self.cmd_batch_login:
            hk.Wait.make(3000)
            for char in self.mode.active_chars:
                self.cmd_enter_username_and_password.call(args=[
                    char.window.title,
                    char.account.username,
                    char.account.password,
                ])

    def build_cmd(self):
        self.build_cmd_launch_and_rename_game_client()
        self.build_cmd_launch_and_rename_all_game_client()
        self.build_cmd_bring_window_to_foreground()
        self.build_cmd_resize_and_relocate_window()
        self.build_cmd_center_overlap_layout()
        self.build_cmd_enter_username_and_password()
        self.build_cmd_batch_login()

    # -------------------------------------------------------------------------
    # 实现与 "切换游戏客户端" 以及 "账号登录" 有关的快捷键.
    # -------------------------------------------------------------------------
    __anchor_hk_01_window_and_login = None

    def build_hk_round_robin_toggle_window(self):
        with hk.Hotkey(
            name="RoundRobinToggleWindow",
            key=KN.SCROLOCK_ON(KN.CTRL_(KN.TAB)),
        ) as self.hk_round_robin_toggle_window:
            for char in self.mode.active_chars:
                with hk.Toggle():
                    self.cmd_bring_window_to_foreground.call(args=[char.window.title, ])

    def build_hk_toggle_specific_window(self):
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
            KN.CTRL_(key)
            for key in KN.F1_to_F12[:10]
        ]
        shift_f5_to_f12 = [
            KN.SHIFT_(key)
            for key in KN.F1_to_F12[4:]
        ]
        shift_insert_to_pgdn = [
            KN.SHIFT_(key)
            for key in KN.INSERT_TO_PGDN
        ]
        HOTKEY_LIST_TOGGLE_SPECIFIC_WINDOW_1_TO_25 = ctrl_f1_to_10 + shift_f5_to_f12 + shift_insert_to_pgdn
        assert len(HOTKEY_LIST_TOGGLE_SPECIFIC_WINDOW_1_TO_25) == 24

        self.hk_list_toggle_specific_window: T.List[hk.Hotkey] = list()
        for index, key in enumerate(HOTKEY_LIST_TOGGLE_SPECIFIC_WINDOW_1_TO_25, start=1):
            with hk.Hotkey(
                name=f"ToggleToSpecificWindow {key}",
                key=key,
            ) as hotkey:
                self.cmd_bring_window_to_foreground.call(args=[Window.make(index).title, ])
                self.hk_list_toggle_specific_window.append(hotkey)

    def build_hk_center_overlap_layout(self):
        with hk.Hotkey(
            name="CenterOverlapLayout",
            key=KN.SCROLOCK_ON(KN.CTRL_SHIFT_ALT(KN.NUMPAD_11_DIVIDE)),
        ) as self.hk_center_overlap_layout:
            self.cmd_center_overlap_layout.call()

    def build_hk_login_specific_account(self):
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
            KN.CTRL_ALT_(key)
            for key in KN.F1_to_F12[:10]
        ]
        shift_alt_f5_to_f12 = [
            KN.ALT_SHIFT_(key)
            for key in KN.F1_to_F12[4:]
        ]
        shift_alt_insert_to_pgdn = [
            KN.ALT_SHIFT_(key)
            for key in KN.INSERT_TO_PGDN
        ]
        HOTKEY_LIST_LOGIN_SPECIFIC_ACCOUNT_1_TO_25 = ctrl_alt_f1_to_10 + shift_alt_f5_to_f12 + shift_alt_insert_to_pgdn
        assert len(HOTKEY_LIST_LOGIN_SPECIFIC_ACCOUNT_1_TO_25) == 24

        self.hk_list_toggle_specific_window: T.List[hk.Hotkey] = list()

        for char in self.mode.managed_chars:
            with hk.Hotkey(
                name=f"SingleLogin{char.account.username.title()}",
                key=KN.SCROLOCK_ON(
                    HOTKEY_LIST_LOGIN_SPECIFIC_ACCOUNT_1_TO_25[int(char.window.label.replace("w", "")) - 1]
                ),
            ) as hotkey:
                self.cmd_enter_username_and_password.call(args=[
                    char.window.title,
                    char.account.username,
                    char.account.password,
                ])
                self.hk_list_toggle_specific_window.append(hotkey)

    def build_hk_batch_logout(self):
        with hk.Hotkey(
            name="BatchLogout",
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
                (
                    hk.ClickMouse()
                    .set_left_click()
                    .set_stroke_as_both()
                    .set_target_as_window()
                    .set_mode_as_no_move()
                )
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
                (
                    hk.ClickMouse()
                    .set_left_click()
                    .set_stroke_as_both()
                    .set_target_as_window()
                    .set_mode_as_no_move()
                )

    def build_hk_logout_on_current_window(self):
        with hk.Hotkey(
            name="LogoutOnCurrentWindow",
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
                (
                    hk.ClickMouse()
                    .set_left_click()
                    .set_stroke_as_both()
                    .set_target_as_window()
                    .set_mode_as_no_move()
                )
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
                (
                    hk.ClickMouse()
                    .set_left_click()
                    .set_stroke_as_both()
                    .set_target_as_window()
                    .set_mode_as_no_move()
                )

    def build_hk_01(self):
        self.build_hk_round_robin_toggle_window()
        self.build_hk_toggle_specific_window()
        self.build_hk_center_overlap_layout()
        self.build_hk_login_specific_account()
        self.build_hk_batch_logout()
        self.build_hk_logout_on_current_window()

    def build_control_panel(self):
        with hk.Command(name="AutoExec") as self.cmd_auto_exec:
            with hk.CreatePanel(name="MBControlPanel", x=0, y=120, width=120, height=1000) as main_panel:
                hk.CreateButton(name="ButtonBar11", x=0, y=0, width=36, height=36, text="Alt")
                hk.AddButtonToPanel(button="ButtonBar11", panel=main_panel.name)
                hk.CreateButton(name="ButtonBar12", x=0, y=0, width=36, height=36, text="+")
                hk.AddButtonToPanel(button="ButtonBar12", panel=main_panel.name)
                hk.CreateButton(name="ButtonBar13", x=0, y=0, width=36, height=36, text="N1-12")
                hk.AddButtonToPanel(button="ButtonBar13", panel=main_panel.name)

                hk.CreateButton(name="ButtonA01", x=0, y=0, width=36, height=36, text="启动")
                hk.AddButtonToPanel(button="ButtonA01", panel=main_panel.name)
                hk.SetButtonCommand(button="ButtonA01", command=self.cmd_launch_and_rename_all_game_client)

                hk.CreateButton(name="ButtonA02", x=0, y=0, width=36, height=36, text="登录")
                hk.AddButtonToPanel(button="ButtonA02", panel=main_panel.name)
                hk.SetButtonCommand(button="ButtonA02", command=self.cmd_batch_login)

                hk.SetPanelLayout(
                    panel=main_panel.name,
                    row_length=3,
                    margin=1,
                    button_width=36,
                    button_height=36,
                )
                hk.TargetWin(window=main_panel.name)
                hk.AlwaysOnTop()
