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
    from .mode import Mode


@attr.s
class HknScript(AttrsClass):
    mode: 'Mode' = attr.ib(default=None)
    script: hk.Script = attr.ib(factory=hk.Script)

    def __attrs_post_init__(self):
        # 此时 Script 已经不再 context 中, 我们也不希望没定义一个 Hotkey 就一直用
        # with script 的语法. 所以我们手动将 script 对象设置为 Context 的顶层
        hk.context.push(self.script)
        self.build_labels()
        self.build_cmd()
        self.build_hk_group_01_window_and_login()
        self.build_hk_group_02_movement()
        self.build_hk_group_03_act_1_to_12()
        self.build_hk_group_04_pet_control()
        self.build_hk_group_05_numpad_1_to_12()
        self.build_hk_group_06_party_and_system()
        self.build_hk_group_07()
        self.build_hk_group_08_alt_numpad_1_to_12()
        self.build_hk_group_09_ctrl_numpad_1_to_12()
        self.build_hk_group_10()
        self.build_hk_group_11_healbot()
        self.build_control_panel()

    def build_labels(self):
        self.labels = [
            hk.Label.make(name=window.label, window=window.title)
            for window, _ in self.mode.login_window_and_account_pairs
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
                hk.RenameWin(old="魔", new=hk.CommandArgEnum.Arg1)

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
            for window, _ in self.mode.login_window_and_account_pairs:
                self.cmd_launch_and_rename_game_client.call(args=[window.title, ])

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
            for window, _ in self.mode.login_window_and_account_pairs:
                self.cmd_resize_and_relocate_window.call(args=[window.title, ])

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
            id="RoundRobinToggleWindow",
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
        HOTKEY_LIST_TOGGLE_SPECIFIC_WINDOW_1_TO_25 = ctrl_f1_to_10 + shift_f5_to_f12 + shift_insert_to_pgdn
        assert len(HOTKEY_LIST_TOGGLE_SPECIFIC_WINDOW_1_TO_25) == 24

        self.hk_list_toggle_specific_window: T.List[hk.Hotkey] = list()
        for index, key in enumerate(HOTKEY_LIST_TOGGLE_SPECIFIC_WINDOW_1_TO_25, start=1):
            with hk.Hotkey(
                id=f"ToggleToSpecificWindow {key}",
                key=key,
            ) as hotkey:
                self.cmd_bring_window_to_foreground.call(args=[Window.make(index).title, ])
                self.hk_list_toggle_specific_window.append(hotkey)

    def build_hk_center_overlap_layout(self):
        with hk.Hotkey(
            id="CenterOverlapLayout",
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
        HOTKEY_LIST_LOGIN_SPECIFIC_ACCOUNT_1_TO_25 = ctrl_alt_f1_to_10 + shift_alt_f5_to_f12 + shift_alt_insert_to_pgdn
        assert len(HOTKEY_LIST_LOGIN_SPECIFIC_ACCOUNT_1_TO_25) == 24

        self.hk_list_toggle_specific_window: T.List[hk.Hotkey] = list()

        for window, account in self.mode.login_window_and_account_pairs:
            with hk.Hotkey(
                id=f"SingleLogin{account.username.title()}",
                key=KN.SCROLOCK_ON(
                    HOTKEY_LIST_LOGIN_SPECIFIC_ACCOUNT_1_TO_25[int(window.label.replace("w", "")) - 1]
                ),
            ) as hotkey:
                self.cmd_enter_username_and_password.call(args=[
                    window.title,
                    account.username,
                    account.password,
                ])
                self.hk_list_toggle_specific_window.append(hotkey)

    def build_hk_batch_logout(self):
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

    def build_hk_logout_on_current_window(self):
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

    def build_hk_group_01_window_and_login(self):
        self.build_hk_round_robin_toggle_window()
        self.build_hk_toggle_specific_window()
        self.build_hk_center_overlap_layout()
        self.build_hk_login_specific_account()
        self.build_hk_batch_logout()
        self.build_hk_logout_on_current_window()

    # -------------------------------------------------------------------------
    # 实现与人物移动有关的快捷键.
    # -------------------------------------------------------------------------
    __anchor_hk_02_movement = None

    def _convert_int_lbs_to_str_lbs(self, lbs: T.List[int]) -> T.List[str]:
        return [f"w{str(ind).zfill(2)}" for ind in lbs]

    def _go_up(self, lbs: T.List[int]):
        with hk.SendLabel(
            id="up",
            to=self._convert_int_lbs_to_str_lbs(lbs),
        ) as send_label:
            act.Movement.MOVE_FORWARD()
            return send_label

    def _go_down(self, lbs: T.List[int]):
        with hk.SendLabel(
            id="down",
            to=self._convert_int_lbs_to_str_lbs(lbs),
        ) as send_label:
            act.Movement.MOVE_BACKWARD()
            return send_label

    def _go_left(self, lbs: T.List[int]):
        with hk.SendLabel(
            id="left",
            to=self._convert_int_lbs_to_str_lbs(lbs),
        ) as send_label:
            act.Movement.MOVE_LEFT()
            return send_label

    def _go_right(self, lbs: T.List[int]):
        with hk.SendLabel(
            id="right",
            to=self._convert_int_lbs_to_str_lbs(lbs),
        ) as send_label:
            act.Movement.MOVE_RIGHT()
            return send_label

    def _go_left_up(self, lbs: T.List[int]):
        with hk.SendLabel(
            id="left_up",
            to=self._convert_int_lbs_to_str_lbs(lbs),
        ) as send_label:
            act.Movement.MOVE_LEFT_TOP()
            return send_label

    def _go_left_down(self, lbs: T.List[int]):
        with hk.SendLabel(
            id="left_down",
            to=self._convert_int_lbs_to_str_lbs(lbs),
        ) as send_label:
            act.Movement.MOVE_LEFT_BOTTOM()
            return send_label

    def _go_right_up(self, lbs: T.List[int]):
        with hk.SendLabel(
            id="right_up",
            to=self._convert_int_lbs_to_str_lbs(lbs),
        ) as send_label:
            act.Movement.MOVE_RIGHT_TOP()
            return send_label

    def _go_right_down(self, lbs: T.List[int]):
        with hk.SendLabel(
            id="right_down",
            to=self._convert_int_lbs_to_str_lbs(lbs),
        ) as send_label:
            act.Movement.MOVE_RIGHT_BOTTOM()
            return send_label

    def build_hk_all_move_up_down_turn_left_right(self):
        """
        按下键盘上的上下左右方向键, 分别使得所有窗口 前进, 后退, 左转, 右转.
        """
        with hk.MovementHotkey(
            id="All Move Up Down, Turn Left Right",
            key=KN.SCROLOCK_ON(f"{KN.UP}, {KN.DOWN}, {KN.LEFT}, {KN.RIGHT}"),
        ) as self.hk_all_move_up_down_turn_left_right:
            with hk.SendLabel(
                to=self.mode.lbs_all,
            ):
                act.General.TRIGGER()

    def build_hk_non_tank_move_up_down_turn_left_right(self):
        """
        按下 Ctrl + 上下左右方向键, 非坦克职业按下同样的键. 用于实现非坦克职业进行走位躲避技能.
        """
        with hk.MovementHotkey(
            id="Non Tank Move Up Down, Turn Left Right",
            key=KN.SCROLOCK_ON(KN.CTRL_(f"{KN.UP}, {KN.DOWN}, {KN.LEFT}, {KN.RIGHT}")),
        ) as self.hk_non_tank_move_up_down_turn_left_right:
            with hk.SendLabel(
                to=self.mode.lbs_by_tc(TC.non_tank),
            ):
                act.General.TRIGGER()

    def build_hk_non_tank_move_left_right(self):
        """
        按下 Ctrl + A / D, 非坦克职业进行 Q / E 平移, 走位躲避技能.
        """
        with hk.MovementHotkey(
            id="Non Tank Move Left",
            key=KN.SCROLOCK_ON(KN.CTRL_(KN.A)),
        ) as self.hk_non_tank_move_left:
            with hk.SendLabel(
                to=self.mode.lbs_by_tc(TC.non_tank),
            ):
                act.Movement.MOVE_LEFT()

        with hk.MovementHotkey(
            id="Non Tank Move Right",
            key=KN.SCROLOCK_ON(KN.CTRL_(KN.D)),
        ) as self.hk_non_tank_move_right:
            with hk.SendLabel(
                to=self.mode.lbs_by_tc(TC.non_tank),
            ):
                act.Movement.MOVE_RIGHT()

    def build_hk_all_jump(self):
        with hk.MovementHotkey(
            id="All Jump",
            key=KN.SCROLOCK_ON(KN.SHIFT_(KN.SPACE)),
        ) as self.hk_all_jump:
            with hk.SendLabel(
                to=self.mode.lbs_all,
            ):
                act.Movement.JUMP()

    def build_hk_spread_matrix(self):
        """
        **矩阵分散站位***

        角色分队

        G1: 防骑, 奶德, 法师, 猎人, 术士
        G2: DK坦, 奶骑, 萨满, 暗牧, 鸟德: 奶骑组群刷不厉害, 所以需要萨满, 暗牧辅助

        以下矩阵分散站位适用于所有人在Boss的一侧进行分散的情形. 典型的Boss战有:

        Naxx 蜘蛛1, 2; ICC 亡语女士
        ICC 亡语女士, 萨鲁法尔, 血腥女王

        先按下 "[" 键进行矩阵分散, 然后按下 "]" 将 法师和暗牧移动到边缘.

                   防骑   DK坦

              术士     猎人     元素萨

        法师    奶德     鸟德    奶骑     暗牧
        """
        with hk.MovementHotkey(
            id="Spread Matrix 1",
            key=KN.SCROLOCK_ON(KN.OEM4_SQUARE_BRACKET_LEFT),
        ) as self.hk_spread_matrix_1:
            send_label_list: T.List[hk.SendLabel] = [
                self._go_left([6, 15, 14]),
                self._go_right([3, 11, 18]),
                self._go_left_down([4, 8, 16, 13]),
                self._go_right_down([5, 9, 12, 17]),
                self._go_down([2, ]),
            ]
            for send_label in send_label_list:
                self.mode.remove_inactive_labels(send_label.to)

        with hk.MovementHotkey(
            id="Spread Matrix 2",
            key=KN.SCROLOCK_ON(KN.OEM6_SQUARE_BRACKET_RIGHT),
        ) as self.hk_spread_matrix_2:
            send_label_list: T.List[hk.SendLabel] = [
                self._go_left([4, 11, 12]),
                self._go_right([5, 15, 16]),
            ]
            for send_label in send_label_list:
                self.mode.remove_inactive_labels(send_label.to)

    def build_hk_spread_circle(self):
        """
        **环形分散站位**

        以下环形分散站位适用于所有人相互距离8码, 而又需要小范围的移动而躲避技能的情况. 典型的Boss战有:

        - Naxx 克尔苏加德
        - ICC 烂肠, 腐面, 血亲王议会

        按下该快捷键后, 大家会分别向, 上下左右, 斜线方向移动, 并且面朝一致的方向, 也就是可以
        保持圆形队形不变向前后移动. 此适用于无法预先安排好阵型, 而需要在战斗中走到指定位置的情形.
        按下快捷键分散后, 大家离中心的距离其实是不一样的, 有的远有的近. 此时再按下跟随焦点键,
        所有人即可向中心靠拢, 然后再按后退键即可实现一个环形站位, 且环形大小可以通过前进后退进行调整.

                    鸟德/奶德2
            猎人                暗牧
                      DK坦
        奶德          boss          奶骑
                      防骑
            法师                元素萨
                    术士/奶德3
        """
        with hk.MovementHotkey(
            id="Spread Circle",
            key=KN.SCROLOCK_ON(KN.OEM5_PIPE_OR_BACK_SLASH),
        ) as self.hk_spread_circle1:
            send_label_list: T.List[hk.SendLabel] = [
                self._go_up([3, 14, 15]),
                self._go_down([6, 11, 18]),
                self._go_left([8, 12, 16]),
                self._go_right([9, 13, 17]),
                self._go_left_up([7, 19]),
                self._go_left_down([4, 20]),
                self._go_right_up([5, 21]),
                self._go_right_down([2, 22]),
            ]
            for send_label in send_label_list:
                self.mode.remove_tank_labels(send_label.to)
                self.mode.remove_inactive_labels(send_label.to)

    def build_hk_group_02_movement(self):
        self.build_hk_all_move_up_down_turn_left_right()
        self.build_hk_non_tank_move_up_down_turn_left_right()
        self.build_hk_non_tank_move_left_right()
        self.build_hk_all_jump()
        self.build_hk_spread_matrix()
        self.build_hk_spread_circle()

    # -------------------------------------------------------------------------
    # 实现按键 1-12 的功能.
    # -------------------------------------------------------------------------
    __anchor_hk_03_key_1_to_12 = None

    def _get_send_label_by_id(
        self,
        id_: str,
        blocks: T.Iterable[hk.SendLabel],
    ) -> T.Optional[hk.SendLabel]:
        for block in blocks:
            if isinstance(block, hk.SendLabel):
                if block.id == id_:
                    return block
        return None

    def build_actions_default(
        self,
        key: str,
        healer_target_focus: bool = False,
        healer_target_focus_target: bool = False,
        healer_target_self: bool = False,
        healer_target_party: bool = False,
        healer_target_raid: bool = False,
    ) -> T.List[hk.SendLabel]:
        """
        通常情况下, 我们打怪的逻辑是: 坦克拉怪, DPS 输出, 治疗奶. 而我们有那么多键位. 为了
        避免为那么多键位写一大堆重复代码, 我们定义了一个工厂函数, 用于生成默认的设置.
        简单来说默认设置就是:

        1. 坦克对当前选择的怪施放技能
        2. DPS 对焦点的目标释放技能
        3. 治疗 对某个目标释放技能, 这里的 "某个" 取决于哪个模式. 请参考下面的参数定义:

        :param healer_target_focus: 治疗前 (下同), 先选定焦点, 通常是坦克司机
        :param healer_target_focus_target: 先选择焦点的目标, 通常是坦克选择队友然后治疗该队友
        :param healer_target_self: 先选择自己
        :param healer_target_party: 先用宏随机选定小队成员
        :param healer_target_raid: 先用宏随机选择团队成员

        以上 5 个模式中必须选择其中的一个.

        **注**

        这里我们需要为所有的 Active Characters 的每一个特定的天赋创建一个 SendLabel 对象.
        这和我们之前为一类 TalentCategory 创建一个 SendLabel, 然后在 SendLabel.to
        里面指定多个 label 的模式不同. 虽然后者从代码的角度讲更加紧凑, 但是却丧失了之后为
        每个特定的天赋在特殊场景下指定不同的行为的能力. 所以我们才用的这种不符合直觉的写法.
        """
        if sum([
            healer_target_focus,
            healer_target_focus_target,
            healer_target_self,
            healer_target_party,
            healer_target_raid,
        ]) != 1:
            raise ValueError()

        send_label_list = list()

        # Tank
        for talent in TC.tank.talents:
            with hk.SendLabel(
                id=talent.name,
                to=self.mode.lbs_by_tl(talent),
            ) as send_label:
                hk.Key.make(key)
                send_label_list.append(send_label)

        # DPS
        for talent in TC.dps.talents:
            with hk.SendLabel(
                id=talent.name,
                to=self.mode.lbs_by_tl(talent),
            ) as send_label:
                act.Target.TARGET_FOCUS_TARGET()
                hk.Key.make(key)
                send_label_list.append(send_label)

        # Healer
        for talent in TC.healer.talents:
            with hk.SendLabel(
                id=talent.name,
                to=self.mode.lbs_by_tl(talent),
            ) as send_label:
                if healer_target_focus:
                    act.Target.TARGET_FOCUS()
                    hk.Key.make(key)
                elif healer_target_focus_target:
                    act.Target.TARGET_FOCUS_TARGET()
                    hk.Key.make(key)
                elif healer_target_self:
                    act.Target.TARGET_SELF()
                    hk.Key.make(key)
                elif healer_target_party:
                    act.Target.TARGET_PARTY()
                    hk.Key.make(key)
                elif healer_target_raid:
                    act.Target.TARGET_RAID()
                    hk.Key.make(key)
                else:  # pragma: no cover
                    raise NotImplementedError

                send_label_list.append(send_label)

        return send_label_list

    def build_hk_1_heal_tank(self):
        with hk.Hotkey(
            id="Key1",
            key=KN.SCROLOCK_ON(KN.KEY_1),
        ) as self.hk_1:
            send_label_list = self.build_actions_default(
                key=KN.KEY_1,
                healer_target_focus=True,  # 治疗选择 焦点
            )
            # 特殊职业的特殊设定
            send_label = self._get_send_label_by_id(
                id_=TL.paladin_pve_holy.name,
                blocks=send_label_list,
            )
            with send_label():
                send_label.blocks = [
                    act.Target.TARGET_RAID(),
                    act.General.TRIGGER(),
                ]

    def build_hk_2_heal_nothing(self):
        with hk.Hotkey(
            id="Key2",
            key=KN.SCROLOCK_ON(KN.KEY_2),
        ) as self.hk_2:
            send_label_list = self.build_actions_default(
                key=KN.KEY_2,
                healer_target_focus_target=True,  # 治疗选择 焦点的目标
            )
            # 特殊职业的特殊设定
            send_label = self._get_send_label_by_id(
                id_=TL.paladin_pve_holy.name,
                blocks=send_label_list,
            )
            with send_label():
                send_label.blocks = [
                    act.Target.TARGET_RAID(),
                    act.General.TRIGGER(),
                ]

    def build_hk_3_heal_tank(self):
        with hk.Hotkey(
            id="Key3",
            key=KN.SCROLOCK_ON(KN.KEY_3),
        ) as self.hk_3:
            send_label_list = self.build_actions_default(
                key=KN.KEY_3,
                healer_target_focus=True,  # 治疗选择 焦点
            )
            # 特殊职业的特殊设定
            send_label = self._get_send_label_by_id(
                id_=TL.paladin_pve_holy.name,
                blocks=send_label_list,
            )
            with send_label():
                send_label.blocks = [
                    act.General.TRIGGER(),
                ]

    def build_hk_4_heal_nothing(self):
        with hk.Hotkey(
            id="Key4",
            key=KN.SCROLOCK_ON(KN.KEY_4),
        ) as self.hk_4:
            send_label_list = self.build_actions_default(
                key=KN.KEY_4,
                healer_target_focus_target=True,  # 选择 焦点的目标
            )

    def build_hk_5_aoe_heal_self(self):
        with hk.Hotkey(
            id="Key5",
            key=KN.SCROLOCK_ON(KN.KEY_5),
        ) as self.hk_5:
            send_label_list = self.build_actions_default(
                key=KN.KEY_5,
                healer_target_focus_target=True,  # 选择 焦点的目标
            )

            # 奶骑对自己放圣光术
            send_label = self._get_send_label_by_id(
                id_=TL.paladin_pve_holy.name,
                blocks=send_label_list,
            )
            with send_label():
                send_label.blocks = [
                    act.Target.TARGET_SELF(),
                    act.Paladin.HOLY_SPEC_KEY_5_HOLY_LIGHT(),
                ]

            # 奶萨对自己放治疗链
            send_label = self._get_send_label_by_id(
                id_=TL.shaman_pve_resto.name,
                blocks=send_label_list,
            )
            with send_label():
                send_label.blocks = [
                    act.Target.TARGET_SELF(),
                    act.Shaman.ALL_SPEC_CHAIN_HEAL(),
                ]

            # 奶德对自己放野性生长
            send_label = self._get_send_label_by_id(
                id_=TL.druid_pve_resto.name,
                blocks=send_label_list,
            )
            with send_label():
                send_label.blocks = [
                    act.Target.TARGET_SELF(),
                    act.Druid.RESTO_SPEC_WILD_GROWTH_KEY_5(),
                ]

            # 戒律牧放治疗祷言
            send_label = self._get_send_label_by_id(
                id_=TL.priest_pve_disco.name,
                blocks=send_label_list,
            )
            with send_label():
                send_label.blocks = [
                    act.Priest.ALL_SPEC_PRAYER_OF_HEALING(),
                ]

            # 神圣牧放治疗祷言
            send_label = self._get_send_label_by_id(
                id_=TL.priest_pve_holy.name,
                blocks=send_label_list,
            )
            with send_label():
                send_label.blocks = [
                    act.Priest.ALL_SPEC_PRAYER_OF_HEALING(),
                ]

    def build_hk_6_one_time_debuff(self):
        with hk.Hotkey(
            id="Key6",
            key=KN.SCROLOCK_ON(KN.KEY_6),
        ) as self.hk_6:
            send_label_list = self.build_actions_default(
                key=KN.KEY_6,
                healer_target_focus_target=True,  # 选择 焦点
            )

    def build_hk_7(self):
        with hk.Hotkey(
            id="Key7",
            key=KN.SCROLOCK_ON(KN.KEY_7),
        ) as self.hk_7:
            send_label_list = self.build_actions_default(
                key=KN.KEY_7,
                healer_target_focus_target=True,  # 选择 焦点
            )

    def build_hk_8_buff_self(self):
        with hk.Hotkey(
            id="Key8",
            key=KN.SCROLOCK_ON(KN.KEY_8),
        ) as self.hk_8:
            with hk.SendLabel(
                id="all",
                to=self.mode.lbs_all,
            ):
                hk.Key(key=KN.KEY_8)

    def build_hk_9_buff_raid(self):

        with hk.Hotkey(
            id="Key9",
            key=KN.SCROLOCK_ON(KN.KEY_9),
        ) as self.hk_9:
            with hk.SendLabel(
                id="all",
                to=self.mode.lbs_all,
            ):
                hk.Key(key=KN.KEY_9)

    def build_hk_0_short_term_buff(self):
        """
        补刷持续时间短的 Buff.
        """
        with hk.Hotkey(
            id="Key0",
            key=KN.SCROLOCK_ON(KN.KEY_0),
        ) as self.hk_0_short_term_buff:
            with hk.SendLabel(
                id=TC.dk.name,
                to=self.mode.lbs_by_tc(TC.dk),
            ):
                act.DK.ALL_SPEC_HORN_OF_WINTER_KEY_SHIFT_TAB()
            with hk.SendLabel(
                id=TC.paladin_healer.name,
                to=self.mode.lbs_by_tc(TC.paladin_healer),
            ):
                act.Target.TARGET_FOCUS()
                act.Paladin.HOLY_SPEC_KEY_0_BEACON_OF_LIGHT()
            with hk.SendLabel(
                id=TC.shaman.name,
                to=self.mode.lbs_by_tc(TC.shaman),
            ):
                act.Shaman.ALL_SPEC_KEY_0_WATER_OR_LIGHTNING_SHIELD()
            with hk.SendLabel(
                id=TC.warlock.name,
                to=self.mode.lbs_by_tc(TC.warlock),
            ):
                act.Warlock.ALL_SPEC_FEL_ARMOR()
            with hk.SendLabel(
                id=TC.priest.name,
                to=self.mode.lbs_by_tc(TC.priest),
            ):
                act.Priest.ALL_SPEC_INNER_FIRE()

    def build_hk_11_focus_mode_1(self):
        """
        所有人的焦点设置为它们的 1 号司机 (除了司机本人)
        """
        with hk.Hotkey(
            id="SetFocusMode1",
            key=KN.SCROLOCK_ON(KN.KEY_11_MINUS),
        ) as self.hk_11_focus_mode_1:
            for char in self.mode.active_chars:
                if char.is_leader_1:  # 司机本人清除焦点
                    with hk.SendLabel(
                        id=char.account.username,
                        to=[char.window.label, ],
                    ):
                        act.General.CLEAR_FOCUS_NUMPAD_7()
                else:  # 其他人设置焦点
                    with hk.SendLabel(
                        id=char.account.username,
                        to=[char.window.label, ],
                    ):
                        act.target_leader_key_mapper[char.leader_1_window.label]()
                        act.General.SET_FOCUS_KEY_NUMPAD_6()

    def build_hk_12_focus_mode_2(self):
        """
        所有人的焦点设置为它们的 2 号司机 (除了司机本人)
        """
        with hk.Hotkey(
            id="SetFocusMode2",
            key=KN.SCROLOCK_ON(KN.KEY_12_PLUS),
        ) as self.hk_12_focus_mode_2:
            for char in self.mode.active_chars:
                if char.is_leader_2:  # 司机本人清除焦点
                    with hk.SendLabel(
                        id=char.account.username,
                        to=[char.window.label, ],
                    ):
                        act.General.CLEAR_FOCUS_NUMPAD_7()
                else:  # 其他人设置焦点
                    with hk.SendLabel(
                        name=char.account.username,
                        to=[char.window.label, ],
                    ):
                        act.target_leader_key_mapper[char.leader_2_window.label]()
                        act.General.SET_FOCUS_KEY_NUMPAD_6()

    # # --- alt 1,2,3,4,5
    def build_hk_alt_5(self):
        """
        对自己放大型群刷技能.
        """
        with hk.Hotkey(
            id="Alt 5",
            key=KN.SCROLOCK_ON(KN.ALT_(KN.KEY_5)),
        ) as self.hk_alt_5:
            with hk.SendLabel(
                id=TC.priest_holy.name,
                to=self.mode.lbs_by_tc(tc=TC.priest_holy),
            ):
                act.Target.TARGET_SELF()
                act.Priest.HOLY_SPEC_CIRCLE_OF_HEALING()

            with hk.SendLabel(
                id=TC.shaman.name,
                to=self.mode.lbs_by_tc(tc=TC.shaman),
            ):
                act.Target.TARGET_FOCUS_TARGET()
                act.Shaman.ALL_SPEC_CHAIN_HEAL()

    def build_hk_group_03_act_1_to_12(self):
        self.build_hk_1_heal_tank()
        self.build_hk_2_heal_nothing()
        self.build_hk_3_heal_tank()
        self.build_hk_4_heal_nothing()
        self.build_hk_5_aoe_heal_self()
        self.build_hk_6_one_time_debuff()
        self.build_hk_7()
        self.build_hk_8_buff_self()
        self.build_hk_9_buff_raid()
        self.build_hk_0_short_term_buff()
        self.build_hk_11_focus_mode_1()
        self.build_hk_12_focus_mode_2()

        self.build_hk_alt_5()

    # -------------------------------------------------------------------------
    # 实现 Ctrl 1 ~ 6 的功能. 主要是宠物的动作条按键. 1 进攻主人目标, 2 撤回, 3 原地待命.
    # -------------------------------------------------------------------------
    __anchor_hk_04_ctrl_1_to_6_pet_action = None

    def build_hk_ctrl_1_to_6(self):
        for i in range(1, 1 + 6):
            with hk.Hotkey(
                id="Ctrl {}".format(i),
                key=KN.SCROLOCK_ON(KN.CTRL_(getattr(KN, "KEY_{}".format(i)))),
            ):
                with hk.SendLabel(
                    name="all",
                    to=self.mode.lbs_all,
                ):
                    act.Target.TARGET_FOCUS_TARGET()
                    act.General.TRIGGER()

    def build_hk_group_04_pet_control(self):
        self.build_hk_ctrl_1_to_6()

    # -------------------------------------------------------------------------
    # 实现在多开模式下 小键盘 Numpad 1-12 的功能. 这些按键可以用专用 MMORPG 鼠标的侧面
    # 轻松按到.
    # -------------------------------------------------------------------------
    __anchor_hk_05_numpad_1_to_12 = None

    def build_hk_numpad_4(self):
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
                act.Camera.SET_FIRST_CAMERA_VIEW_2()

    def build_hk_numpad_5(self):
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
                act.Shaman.ALL_SPEC_CALL_OF_THE_ELEMENTS()

    def build_hk_numpad_6(self):
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
                act.Shaman.ALL_SPEC_TOTEMIC_RECALL()

    def build_hk_numpad_7(self):
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
                act.Movement.MOVE_BACKWARD()

    def build_hk_numpad_8(self):
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

    def build_hk_numpad_9(self):
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

    def build_hk_numpad_0(self):
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
                act.Movement.FOLLOW_FOCUS()

    def build_hk_numpad_11(self):
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
                act.General.MOUNT_UP_MACRO_KEY_NUMPAD_11_DIVIDE()

    def build_hk_numpad_12(self):
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
                act.Target.TARGET_FOCUS_TARGET()
                act.Target.INTERACT_WITH_TARGET()

    def build_hk_group_05_numpad_1_to_12(self):
        self.build_hk_numpad_4()
        self.build_hk_numpad_5()
        self.build_hk_numpad_6()
        self.build_hk_numpad_7()
        self.build_hk_numpad_8()
        self.build_hk_numpad_9()
        self.build_hk_numpad_0()
        self.build_hk_numpad_11()
        self.build_hk_numpad_12()

    # -------------------------------------------------------------------------
    # 实现功能性的按键
    # -------------------------------------------------------------------------
    __anchor_hk_06_utility_action = None

    def build_hk_confirm(self):
        with hk.Hotkey(
            id="Confirm",
            key=KN.SCROLOCK_ON(KN.CTRL_(KN.Y)),
        ) as self.hk_confirm:
            with hk.SendLabel(
                id="all",
                to=self.mode.lbs_all,
            ):
                act.General.CONFIRM_MACRO_KEY_NUMPAD_5()

    def build_hk_leave_party(self):
        with hk.Hotkey(
            id="LeaveParty",
            key=KN.SCROLOCK_ON(KN.CTRL_(KN.L)),
        ) as self.hk_leave_party:
            with hk.SendLabel(
                name="all",
                to=self.mode.lbs_all,
            ):
                act.General.LEAVE_PARTY_MACRO_KEY_ALT_END()

    def build_hk_all_pass_item(self):
        """
        所有的角色放弃拾取物品.
        """
        with hk.Hotkey(
            id="All Pass Item",
            key=KN.SCROLOCK_ON(KN.CTRL_ALT_(KN.Q)),
        ) as self.hk_all_pass_item:
            with hk.SendLabel(
                id="pass_item_button",
                to=self.mode.lbs_all,
            ):
                hk.ClickMouse(button=KN.MOUSE_LButton).set_mode_as_x_y(
                    x=self.mode.game_client.pass_item_button_x,
                    y=self.mode.game_client.pass_item_button_1_y,
                )
                hk.ClickMouse(button=KN.MOUSE_LButton).set_mode_as_x_y(
                    x=self.mode.game_client.pass_item_button_x,
                    y=self.mode.game_client.pass_item_button_2_y,
                )
                hk.ClickMouse(button=KN.MOUSE_LButton).set_mode_as_x_y(
                    x=self.mode.game_client.pass_item_button_x,
                    y=self.mode.game_client.pass_item_button_3_y,
                )
                hk.ClickMouse(button=KN.MOUSE_LButton).set_mode_as_x_y(
                    x=self.mode.game_client.pass_item_button_x,
                    y=self.mode.game_client.pass_item_button_4_y,
                )

    def build_hk_volumn_down(self):
        with hk.Hotkey(
            id="Volume Down",
            key=KN.SCROLOCK_ON(KN.CTRL_SHIFT_ALT(KN.M)),
        ) as self.hk_volumn_down:
            with hk.SendLabel(
                id="all",
                to=self.mode.lbs_all,
            ):
                act.System.MASTER_VOLUME_DOWN()

    def build_hk_group_06_party_and_system(self):
        self.build_hk_confirm()
        self.build_hk_leave_party()
        self.build_hk_all_pass_item()
        self.build_hk_volumn_down()

    # -------------------------------------------------------------------------
    # 实现每个游戏内所绑定的动作条快捷键, 会触发哪些职业的哪些功能.
    # -------------------------------------------------------------------------
    def build_hk_skills(self):
        __anchor_action_bar_1 = "Domino Action Bar 1"

        # with hk.Hotkey(
        #     id="Alt F1",
        #     key=KN.SCROLOCK_ON(KN.ALT_(KN.F1)),
        # ) as self.hk_alt_f1:
        #     with hk.SendLabel(
        #         to=self.mode.lbs_all,
        #     ):
        #         hk.Key.trigger()
        # 
        # with hk.Hotkey(
        #     id="Alt F2",
        #     key=KN.SCROLOCK_ON(KN.ALT_(KN.F2)),
        # ) as self.hk_alt_f2:
        #     with hk.SendLabel(
        #         to=self.mode.lbs_all,
        #     ):
        #         hk.Key.trigger()
        # 
        # with hk.Hotkey(
        #     id="Shift F1",
        #     key=KN.SCROLOCK_ON(KN.SHIFT_(KN.F1)),
        # ) as self.hk_shift_f1:
        #     with hk.SendLabel(
        #         to=self.mode.lbs_all,
        #     ):
        #         hk.Key.trigger()
        # 
        # with hk.Hotkey(
        #     id="Shift F1",
        #     key=KN.SCROLOCK_ON(KN.SHIFT_(KN.F1)),
        # ) as self.hk_shift_f1:
        #     with hk.SendLabel(
        #         to=self.mode.lbs_all,
        #     ):
        #         hk.Key.trigger()
        # 
        # with hk.Hotkey(
        #     id="Shift F2",
        #     key=KN.SCROLOCK_ON(KN.SHIFT_(KN.F2)),
        # ) as self.hk_shift_f2:
        #     with hk.SendLabel(
        #         to=self.mode.lbs_all,
        #     ):
        #         hk.Key.trigger()
        # 
        # with hk.Hotkey(
        #     id="Shift C",
        #     key=KN.SCROLOCK_ON(KN.SHIFT_(KN.C)),
        # ) as self.hk_shift_c:
        #     with hk.SendLabel(
        #         to=self.mode.lbs_all,
        #     ):
        #         hk.Key.trigger()
        # 
        # with hk.Hotkey(
        #     id="Shift R",
        #     key=KN.SCROLOCK_ON(KN.SHIFT_(KN.R)),
        # ) as self.hk_shift_r:
        #     with hk.SendLabel(
        #         to=self.mode.lbs_all,
        #     ):
        #         hk.Key.trigger()
        # 
        # with hk.Hotkey(
        #     id="Shift F",
        #     key=KN.SCROLOCK_ON(KN.SHIFT_(KN.F)),
        # ) as self.hk_shift_f:
        #     with hk.SendLabel(
        #         to=self.mode.lbs_all,
        #     ):
        #         hk.Key.trigger()
        # 
        # with hk.Hotkey(
        #     id="Shift G",
        #     key=KN.SCROLOCK_ON(KN.SHIFT_(KN.G)),
        # ) as self.hk_shift_g:
        #     with hk.SendLabel(
        #         to=self.mode.lbs_all,
        #     ):
        #         hk.Key.trigger()

        with hk.Hotkey(
            id="Shift Tab",
            key=KN.SCROLOCK_ON(KN.SHIFT_(KN.TAB)),
        ) as self.hk_shift_tab:
            with hk.SendLabel(
                to=self.mode.lbs_by_tc(TC.shaman),
            ):
                hk.Key.trigger()

        # with hk.Hotkey(
        #     id="Ctrl E",
        #     key=KN.SCROLOCK_ON(KN.CTRL_(KN.E)),
        # ) as self.hk_ctrl_e:
        #     with hk.SendLabel(
        #         to=self.mode.lbs_all,
        #     ):
        #         hk.Key.trigger()
        #
        # with hk.Hotkey(
        #     id="Ctrl R",
        #     key=KN.SCROLOCK_ON(KN.CTRL_(KN.R)),
        # ) as self.hk_ctrl_r:
        #     with hk.SendLabel(
        #         to=self.mode.lbs_all,
        #     ):
        #         hk.Key.trigger()
        #
        # with hk.Hotkey(
        #     id="Ctrl F",
        #     key=KN.SCROLOCK_ON(KN.CTRL_(KN.F)),
        # ) as self.hk_ctrl_f:
        #     with hk.SendLabel(
        #         to=self.mode.lbs_all,
        #     ):
        #         hk.Key.trigger()

        __anchor_action_bar_2 = "Domino Action Bar 2"
        # with hk.Hotkey(
        #     id="MButton",
        #     key=KN.SCROLOCK_ON(KN.MOUSE_MButton),
        # ) as self.hk_middle_click:
        #     with hk.SendLabel(
        #         to=self.mode.lbs_all,
        #     ):
        #         hk.Key.trigger()
        #
        # with hk.Hotkey(
        #     id="Shift MButton",
        #     key=KN.SCROLOCK_ON(KN.SHIFT_(KN.MOUSE_MButton)),
        # ) as self.hk_shift_middle_click:
        #     with hk.SendLabel(
        #         to=self.mode.lbs_all,
        #     ):
        #         hk.Key.trigger()
        #
        # with hk.Hotkey(
        #     id="Alt MButton",
        #     key=KN.SCROLOCK_ON(KN.ALT_(KN.MOUSE_MButton)),
        # ) as self.hk_alt_middle_click:
        #     with hk.SendLabel(
        #         to=self.mode.lbs_all,
        #     ):
        #         hk.Key.trigger()

        with hk.Hotkey(
            id="Ctrl + `",
            key=KN.SCROLOCK_ON(KN.CTRL_(KN.OEM3_WAVE_OR_BACK_QUOTE)),
        ) as self.hk_ctrl_oem3_wave:
            with hk.SendLabel(
                to=self.mode.lbs_all,
            ):
                act.General.MOUNT_DOWN_MACRO_CTRL_OEM3_WAVE()

        # with hk.Hotkey(
        #     id="Shift + `",
        #     key=KN.SCROLOCK_ON(KN.SHIFT_(KN.OEM3_WAVE_OR_BACK_QUOTE)),
        # ) as self.hk_shift_oem3_wave:
        #     with hk.SendLabel(
        #         to=self.mode.lbs_all,
        #     ):
        #         hk.Key.trigger()
        #
        # with hk.Hotkey(
        #     id="Alt + `",
        #     key=KN.SCROLOCK_ON(KN.ALT_(KN.OEM3_WAVE_OR_BACK_QUOTE)),
        # ) as self.hk_alt_oem3_wave:
        #     with hk.SendLabel(
        #         to=self.mode.lbs_all,
        #     ):
        #         hk.Key.trigger()
        #
        # with hk.Hotkey(
        #     id="Alt + A",
        #     key=KN.SCROLOCK_ON(KN.ALT_(KN.A)),
        # ) as self.hk_alt_a:
        #     with hk.SendLabel(
        #         to=self.mode.lbs_all,
        #     ):
        #         hk.Key.trigger()
        #
        # with hk.Hotkey(
        #     id="Alt + S",
        #     key=KN.SCROLOCK_ON(KN.ALT_(KN.S)),
        # ) as self.hk_alt_s:
        #     with hk.SendLabel(
        #         to=self.mode.lbs_all,
        #     ):
        #         hk.Key.trigger()
        #
        # with hk.Hotkey(
        #     id="Alt + D",
        #     key=KN.SCROLOCK_ON(KN.ALT_(KN.D)),
        # ) as self.hk_alt_d:
        #     with hk.SendLabel(
        #         to=self.mode.lbs_all,
        #     ):
        #         hk.Key.trigger()
        #
        # with hk.Hotkey(
        #     id="Alt + E",
        #     key=KN.SCROLOCK_ON(KN.ALT_(KN.E)),
        # ) as self.hk_alt_e:
        #     with hk.SendLabel(
        #         to=self.mode.lbs_all,
        #     ):
        #         hk.Key.trigger()
        #
        # with hk.Hotkey(
        #     id="Alt + R",
        #     key=KN.SCROLOCK_ON(KN.ALT_(KN.R)),
        # ) as self.hk_alt_r:
        #     with hk.SendLabel(
        #         to=self.mode.lbs_all,
        #     ):
        #         hk.Key.trigger()
        #
        # with hk.Hotkey(
        #     id="Alt + F",
        #     key=KN.SCROLOCK_ON(KN.ALT_(KN.F)),
        # ) as self.hk_alt_f:
        #     with hk.SendLabel(
        #         to=self.mode.lbs_all,
        #     ):
        #         hk.Key.trigger()

        __anchor_action_bar_3 = "Domino Action Bar 3"

        # with hk.Hotkey(
        #     id="Shift + Z",
        #     key=KN.SCROLOCK_ON(KN.SHIFT_(KN.Z)),
        # ) as self.hk_shift_z:
        #     with hk.SendLabel(
        #         to=self.mode.lbs_all,
        #     ):
        #         hk.Key.trigger()
        #
        # with hk.Hotkey(
        #     id="Shift + T",
        #     key=KN.SCROLOCK_ON(KN.SHIFT_(KN.T)),
        # ) as self.hk_shift_t:
        #     with hk.SendLabel(
        #         to=self.mode.lbs_all,
        #     ):
        #         hk.Key.trigger()
        #
        # with hk.Hotkey(
        #     id="Shift + X",
        #     key=KN.SCROLOCK_ON(KN.SHIFT_(KN.X)),
        # ) as self.hk_shift_x:
        #     with hk.SendLabel(
        #         to=self.mode.lbs_all,
        #     ):
        #         hk.Key.trigger()

        # 所有人取消坐骑下地
        with hk.Hotkey(
            id="Ctrl + Z",
            key=KN.SCROLOCK_ON(KN.CTRL_(KN.Z)),
        ) as self.hk_ctrl_z:
            with hk.SendLabel(
                to=self.mode.lbs_all,
            ):
                act.General.LAND_MOUNT_SPELL_KEY_CTRL_Z()

        # 吃食物
        with hk.Hotkey(
            id="Ctrl + T",
            key=KN.SCROLOCK_ON(KN.CTRL_(KN.T)),
        ) as self.hk_ctrl_t:
            with hk.SendLabel(
                to=self.mode.lbs_all,
            ):
                act.General.EAT_FOOD_KEY_CTRL_T()

        with hk.Hotkey(
            id="Ctrl + G",
            key=KN.SCROLOCK_ON(KN.CTRL_(KN.G)),
        ) as self.hk_ctrl_g:
            with hk.SendLabel(
                to=self.mode.lbs_all,
            ):
                hk.Key.trigger()

        # with hk.Hotkey(
        #     id="Ctrl + X",
        #     key=KN.SCROLOCK_ON(KN.CTRL_(KN.X)),
        # ) as self.hk_ctrl_x:
        #     with hk.SendLabel(
        #         to=self.mode.lbs_all,
        #     ):
        #         hk.Key.trigger()
        #
        # with hk.Hotkey(
        #     id="Alt + Z",
        #     key=KN.SCROLOCK_ON(KN.ALT_(KN.Z)),
        # ) as self.hk_alt_z:
        #     with hk.SendLabel(
        #         to=self.mode.lbs_all,
        #     ):
        #         hk.Key.trigger()
        #
        # with hk.Hotkey(
        #     id="Alt + T",
        #     key=KN.SCROLOCK_ON(KN.ALT_(KN.T)),
        # ) as self.hk_alt_t:
        #     with hk.SendLabel(
        #         to=self.mode.lbs_all,
        #     ):
        #         hk.Key.trigger()

        with hk.Hotkey(
            id="Alt + G - 所有鸟德放台风, 推波击退",
            key=KN.SCROLOCK_ON(KN.ALT_(KN.G)),
        ) as self.hk_alt_g_druid_typhoon:
            with hk.SendLabel(
                to=self.mode.lbs_by_tc(TC.druid_balance),
            ):
                act.Druid.BALANCE_SPEC_TYPHOON_KEY_G()

        with hk.Hotkey(
            id="Alt + X - 所有 AOE 职业放区域选定 AOE 技能, 例如法师暴风雪, DK死亡凋零",
            key=KN.SCROLOCK_ON(KN.ALT_(KN.X)),
        ) as self.hk_alt_x_aoe:
            with hk.SendLabel(
                id=TC.dk.name,
                to=self.mode.lbs_by_tc(TC.dk),
            ):
                # act.General.ESC()
                act.DK.ALL_SPEC_DEATH_AND_DECAY_KEY_ALT_X()

            with hk.SendLabel(
                id=TC.hunter.name,
                to=self.mode.lbs_by_tc(TC.hunter),
            ):
                # act.General.ESC()
                act.Hunter.ALL_SPEC_VOLLEY_ALT_X()

            with hk.SendLabel(
                id=TC.druid_balance.name,
                to=self.mode.lbs_by_tc(TC.druid_balance),
            ):
                # act.General.ESC()
                act.Druid.ALL_SPEC_HURRICANE()

            with hk.SendLabel(
                id=TC.warlock.name,
                to=self.mode.lbs_by_tc(TC.warlock),
            ):
                # act.General.ESC()
                act.Warlock.ALL_SPEC_RAIN_OF_FIRE()

            with hk.SendLabel(
                id=TC.mage.name,
                to=self.mode.lbs_by_tc(TC.mage),
            ):
                # act.General.ESC()
                act.Mage.ALL_SPEC_BLIZZARD()

        # _ACTION_BAR_2_________________________________ = ""
        # with hk.Hotkey(
        #     id="R - 能打断的职业打断",
        #     key=KN.SCROLOCK_ON(KN.ALT_(KN.G)),
        # ) as self.hk_alt_g_druid_typhoon:
        #     with hk.SendLabel(
        #         id=TC.paladin_protect.name,
        #         to=self.mode.lbs_by_tc(TC.paladin_protect),
        #     ):
        #         hk.Key(key=KN.R)
        #
        #
        # _hk_r_actions = [
        #     # paladin
        #     SendLabel(
        #         name=TC.paladin_protect.name,
        #         to=self.mode.lbs_by_tc(TC.paladin_protect),
        #         actions=[
        #             Key(name=KN.R),
        #         ]
        #     ),
        #     SendLabel(
        #         name=TC.paladin_holy.name,
        #         to=self.mode.lbs_by_tc(TC.paladin_holy),
        #         actions=[
        #             act.Paladin.HOLY_SPEC_KEY_R_FOCUS_JUDGEMENT,
        #         ]
        #     ),
        #     # death knight
        #     SendLabel(
        #         name=TC.dk_tank.name,
        #         to=self.mode.lbs_by_tc(TC.dk_tank),
        #         actions=[
        #             act.DK.ALL_SPEC_MIND_FREEZE_KEY_R,
        #         ]
        #     ),
        #     SendLabel(
        #         name=TC.dk_dps.name,
        #         to=self.mode.lbs_by_tc(TC.dk_dps),
        #         actions=[
        #             act.Target.TARGET_FOCUS_TARGET,
        #             act.DK.ALL_SPEC_MIND_FREEZE_KEY_R,
        #         ]
        #     ),
        #     # hunter
        #     SendLabel(
        #         name=TC.hunter_marksman.name,
        #         to=self.mode.lbs_by_tc(TC.hunter_marksman),
        #         actions=[
        #             act.Target.TARGET_FOCUS_TARGET,
        #             act.Hunter.MARKSMAN_SPEC_DPS_ROTATE_MACRO,
        #         ]
        #     ),
        #     # shaman
        #     SendLabel(
        #         name=TC.shaman.name,
        #         to=self.mode.lbs_by_tc(TC.shaman),
        #         actions=[
        #             act.Target.TARGET_FOCUS_TARGET,
        #             act.Shaman.ALL_SPEC_WIND_SHEAR_MACRO,
        #         ]
        #     ),
        #
        #     # mage
        #     SendLabel(
        #         name=TC.mage.name,
        #         to=self.mode.lbs_by_tc(TC.mage),
        #         actions=[
        #             act.Target.TARGET_FOCUS_TARGET,
        #             act.Mage.ALL_SPEC_COUNTER_SPELL_MACRO,
        #         ]
        #     ),
        # ]
        #
        # special_labels = union_list(*[
        #     sl.to
        #     for sl in _hk_r_actions
        # ])
        #
        # regular_tank_labels = difference_list(
        #     self.mode.lbs_by_tc(TC.tank),
        #     special_labels,
        # )
        #
        # regular_dps_labels = difference_list(
        #     self.mode.lbs_by_tc(TC.dps),
        #     special_labels,
        # )
        #
        # regular_healer_labels = difference_list(
        #     self.mode.lbs_by_tc(TC.healer),
        #     special_labels,
        # )
        #
        # _hk_r_actions.extend([
        #     SendLabel(
        #         name="other_tank",
        #         to=regular_tank_labels,
        #         actions=[
        #             Key(name=KN.KEY_2),
        #         ]
        #     ),
        #     SendLabel(
        #         name="other_dps",
        #         to=regular_dps_labels,
        #         actions=[
        #             act.Target.TARGET_FOCUS_TARGET,
        #             Key(name=KN.KEY_3),
        #         ]
        #     ),
        #     SendLabel(
        #         name="other_healer",
        #         to=regular_healer_labels,
        #         actions=[
        #             act.Target.TARGET_FOCUS,
        #             Key(name=KN.KEY_3),
        #         ]
        #     ),
        # ])
        #
        # hk_r = Hotkey(
        #     name="R Interrupt Spell",
        #     key=KN.SCROLOCK_ON(KN.R),
        #     actions=_hk_r_actions,
        #     script=script,
        # )

        # ABOVE IS TODO

        # with hk.Hotkey(
        #     id="Z",
        #     key=KN.SCROLOCK_ON(KN.Z),
        # ) as self.hk_z:
        #     with hk.SendLabel(
        #         to=self.mode.lbs_all,
        #     ):
        #         hk.Key.trigger()

        # pala put cleansing skill on Action Bar Key T
        # shaman put curse toxin skill on Action Bar Key on T
        # druid put remove curse skill on Action Bar Key on T
        # mage put remove curse skill on Action Bar Key on T
        # priest put dispel magic skill on Action Bar Key on T
        with hk.Hotkey(
            id="T - 所有驱散职业随机选择团队成员驱散",
            key=KN.SCROLOCK_ON(KN.T),
        ) as self.hk_t_dispel_raid:
            with hk.SendLabel(
                id=TC.dispeler.name,
                to=self.mode.lbs_by_tc(TC.dispeler),
            ):
                act.Target.TARGET_RAID()
                hk.Key.trigger()

        # with hk.Hotkey(
        #     id="G",
        #     key=KN.SCROLOCK_ON(KN.G),
        # ) as self.hk_g:
        #     with hk.SendLabel(
        #         to=self.mode.lbs_all,
        #     ):
        #         hk.Key.trigger()

        # with hk.Hotkey(
        #     id="X",
        #     key=KN.SCROLOCK_ON(KN.X),
        # ) as self.hk_x:
        #     with hk.SendLabel(
        #         to=self.mode.lbs_all,
        #     ):
        #         hk.Key.trigger()

        __anchor_action_bar_7_8_9_10 = "Domino Action Bar 7 8 9 10"

        _anchor_action_bar_7_8_9_10 = ""
        _anchor_action_bar_undefined = ""

        with hk.Hotkey(
            id="Alt Shift + F - 鸟德星落",
            key=KN.SCROLOCK_ON(KN.ALT_SHIFT_(KN.F)),
        ) as self.hk_alt_shift_f_all_boomkin_star_fall:
            with hk.SendLabel(
                id=TC.druid_balance.name,
                to=self.mode.lbs_by_tc(TC.druid_balance),
            ):
                act.Druid.BALANCE_SPEC_STAR_FALL_ALT_F()

            with hk.SendLabel(
                id=TC.dk.name,
                to=self.mode.lbs_by_tc(TC.dk),
            ):
                act.DK.UNHOLY_SPEC_CORPSE_EXPLOSION_ALF_F()

    def build_hk_group_07(self):
        self.build_hk_skills()

    # -------------------------------------------------------------------------
    # 实现 Alt + 小键盘 1-12 的快捷键功能. 通常是一些不常用, 但是关键时刻必备的技能.
    # -------------------------------------------------------------------------
    __anchor_hk_08_alt_numpad_1_to_12 = None

    def build_hk_alt_numpad_1_misdirect_and_tot_focus(self):
        with hk.Hotkey(
            id="Alt Numpad1 - 猎人误导坦克",
            key=KN.SCROLOCK_ON(KN.ALT_(KN.NUMPAD_1)),
        ) as self.hk_alt_numpad_1:
            with hk.SendLabel(
                id=TC.hunter.name,
                to=self.mode.lbs_by_tc(TC.hunter),
            ):
                act.Hunter.ALL_SPEC_MISDIRECTION_FOCUS_MACRO()

    def build_hk_alt_numpad_2_aspect_of_pact_or_hawk(self):
        with hk.Hotkey(
            id="Alt Numpad2 - 猎人在雄鹰和豹群守护之间切换",
            key=KN.SCROLOCK_ON(KN.ALT_(KN.NUMPAD_2)),
        ) as self.hk_alt_numpad_2:
            with hk.SendLabel(
                id=TC.hunter.name,
                to=self.mode.lbs_by_tc(TC.hunter),
            ):
                act.Hunter.ALL_SPEC_ASPECT_OF_PACT_OR_DRAGON_HAWK()

    def build_hk_alt_numpad_3_aspect_of_viper_or_hawk(self):
        with hk.Hotkey(
            id="Alt Numpad3 - 猎人在雄鹰和蝮蛇守护之间切换",
            key=KN.SCROLOCK_ON(KN.ALT_(KN.NUMPAD_3)),
        ) as self.hk_alt_numpad_3:
            with hk.SendLabel(
                name=TC.hunter.name,
                to=self.mode.lbs_by_tc(TC.hunter),
            ):
                act.Hunter.ALL_SPEC_ASPECT_OF_VIPER_OR_DRAGON_HAWK()

    def build_hk_alt_numpad_4_all_boomy_star_fall(self):
        with hk.Hotkey(
            id="Alt Numpad4 - 鸟德集体放星落",
            key=KN.SCROLOCK_ON(KN.ALT_(KN.NUMPAD_4)),
        ) as self.hk_alt_numpad_4:
            with hk.SendLabel(
                id=TC.druid_balance.name,
                to=self.mode.lbs_by_tc(TC.druid_balance),
            ):
                act.General.STOP_CASTING_KEY_OEM1_SEMICOLUMN()
                act.Druid.BALANCE_SPEC_STAR_FALL_ALT_F()

    def build_hk_alt_numpad_5_all_dps_burst(self):
        with hk.Hotkey(
            id="Alt Numpad5 - DPS 开爆发技能",
            key=KN.SCROLOCK_ON(KN.ALT_(KN.NUMPAD_5)),
        ) as self.hk_alt_numpad_5:
            with hk.SendLabel(
                id=TC.dps.name,
                to=self.mode.lbs_by_tc(TC.dps),
            ):
                act.General.DPS_BURST_MACRO_KEY_ALT_D()

    def build_hk_alt_numpad_6_all_dps_burst_and_hero(self):
        with hk.Hotkey(
            id="Alt Numpad6 - 开嗜血, 同时所有 DPS 开爆发技能",
            key=KN.SCROLOCK_ON(KN.ALT_(KN.NUMPAD_6)),
        ) as self.hk_alt_numpad_6:
            with hk.SendLabel(
                id="all_non_shaman_dps",
                to=utils.difference_list(
                    self.mode.lbs_by_tc(TC.dps),
                    self.mode.lbs_by_tc(TC.shaman),
                ),
            ):
                act.General.DPS_BURST_MACRO_KEY_ALT_D()

            with hk.SendLabel(
                id=TC.shaman_elemental.name,
                to=self.mode.lbs_by_tc(TC.shaman_elemental),
            ):
                act.Shaman.ALL_SPEC_BLOOD_THIRST_HEROISM()
                act.General.DPS_BURST_MACRO_KEY_ALT_D()

            with hk.SendLabel(
                id=TC.shaman_resto.name,
                to=self.mode.lbs_by_tc(TC.shaman_resto),
            ):
                act.Shaman.ALL_SPEC_BLOOD_THIRST_HEROISM()

    def build_hk_alt_numpad_7_8_9_first_raid_damage_reduction(self):
        with hk.Hotkey(
            id="Alt Numpad7",
            key=KN.SCROLOCK_ON(KN.ALT_(KN.NUMPAD_7)),
        ) as self.hk_alt_numpad_7:
            with hk.SendLabel(
                id=TC.paladin_protect.name,
                to=self.mode.lbs_by_tc(TC.paladin_protect),
            ):
                # 要点两下, 启动神圣牺牲后自己取消
                act.Paladin.ALL_SPEC_DIVINE_SACRIFICE()
                act.Paladin.ALL_SPEC_DIVINE_SACRIFICE()

        with hk.Hotkey(
            id="Alt Numpad8",
            key=KN.SCROLOCK_ON(KN.ALT_(KN.NUMPAD_8)),
        ) as self.hk_alt_numpad_8:
            with hk.SendLabel(
                id=TC.paladin_holy.name,
                to=self.mode.lbs_by_tc(TC.paladin_holy),
            ):
                # 要点两下, 启动神圣牺牲后自己取消
                act.Paladin.ALL_SPEC_DIVINE_SACRIFICE()
                act.Paladin.ALL_SPEC_DIVINE_SACRIFICE()

        with hk.Hotkey(
            id="Alt Numpad9",
            key=KN.SCROLOCK_ON(KN.ALT_(KN.NUMPAD_9)),
        ) as self.hk_alt_numpad_9:
            with hk.SendLabel(
                id=TC.paladin_holy.name,
                to=self.mode.lbs_by_tc(TC.paladin_holy),
            ):
                act.Paladin.ALL_SPEC_AURA_MASTERY()

    def build_hk_alt_numpad_10_cleansing_totem(self):
        with hk.Hotkey(
            id="Alt Numpad10 - 萨满放清毒图腾",
            key=KN.SCROLOCK_ON(KN.ALT_(KN.NUMPAD_0)),
        ) as self.hk_alt_numpad_10:
            with hk.SendLabel(
                id=TC.shaman.name,
                to=self.mode.lbs_by_tc(TC.shaman),
            ):
                act.General.STOP_CASTING_KEY_OEM1_SEMICOLUMN()
                act.Shaman.ALL_SPEC_CLEANSING_TOTEM()

    def build_hk_alt_numpad_11_tremor_totem(self):
        with hk.Hotkey(
            id="Alt Numpad11 - 萨满放战栗图腾",
            key=KN.SCROLOCK_ON(KN.ALT_(KN.NUMPAD_11_DIVIDE)),
        ) as self.hk_alt_numpad_11:
            with hk.SendLabel(
                id=TC.shaman.name,
                to=self.mode.lbs_by_tc(TC.shaman),
            ):
                act.General.STOP_CASTING_KEY_OEM1_SEMICOLUMN()
                act.Shaman.ALL_SPEC_TREMOR_TOTEM()

    def build_hk_alt_numpad_12_earth_binding_totem(self):
        with hk.Hotkey(
            id="Alt Numpad12 - 萨满放地缚图腾",
            key=KN.SCROLOCK_ON(KN.ALT_(KN.NUMPAD_12_MULTIPLY)),
        ) as self.hk_alt_numpad_12:
            with hk.SendLabel(
                id=TC.shaman.name,
                to=self.mode.lbs_by_tc(TC.shaman),
            ):
                act.General.STOP_CASTING_KEY_OEM1_SEMICOLUMN()
                act.Shaman.ALL_SPEC_EARTHBIND_TOTEM()

    def build_hk_group_08_alt_numpad_1_to_12(self):
        self.build_hk_alt_numpad_1_misdirect_and_tot_focus()
        self.build_hk_alt_numpad_2_aspect_of_pact_or_hawk()
        self.build_hk_alt_numpad_3_aspect_of_viper_or_hawk()
        self.build_hk_alt_numpad_4_all_boomy_star_fall()
        self.build_hk_alt_numpad_5_all_dps_burst()
        self.build_hk_alt_numpad_6_all_dps_burst_and_hero()
        self.build_hk_alt_numpad_7_8_9_first_raid_damage_reduction()
        self.build_hk_alt_numpad_10_cleansing_totem()
        self.build_hk_alt_numpad_11_tremor_totem()
        self.build_hk_alt_numpad_12_earth_binding_totem()

    # -------------------------------------------------------------------------
    # 实现 Ctrl + 小键盘 1-12 的快捷键功能. 通常是一些不常用, 但是关键时刻必备的技能.
    # -------------------------------------------------------------------------
    __anchor_hk_09_ctrl_1_to_12 = None

    def build_hk_ctrl_numpad_1_silence_shot_focus_target(self):
        with hk.Hotkey(
            id="Ctrl Numpad1 - 射击猎人对焦点的目标释放沉默射击",
            key=KN.SCROLOCK_ON(KN.CTRL_(KN.NUMPAD_1)),
        ) as self.hk_ctrl_numpad_1:
            with hk.SendLabel(
                id=TC.hunter.name,
                to=self.mode.lbs_by_tc(TC.hunter),
            ):
                act.Target.TARGET_FOCUS_TARGET()
                act.Hunter.MARKSMAN_SPEC_SILENCING_SHOT()

    def build_hk_ctrl_numpad_2_counter_spell_focus_target(self):
        with hk.Hotkey(
            id="Ctrl Numpad2 - 法师对焦点的目标释放法术反制",
            key=KN.SCROLOCK_ON(KN.CTRL_(KN.NUMPAD_2)),
        ) as self.hk_ctrl_numpad_2:
            with hk.SendLabel(
                id=TC.mage.name,
                to=self.mode.lbs_by_tc(TC.mage),
            ):
                act.Target.TARGET_FOCUS_TARGET()
                act.Mage.ALL_SPEC_COUNTER_SPELL_MACRO()

    def build_hk_ctrl_numpad_3_aggressive_dispel(self):
        with hk.Hotkey(
            id="Ctrl Numpad3 - 进攻驱散",
            key=KN.SCROLOCK_ON(KN.CTRL_(KN.NUMPAD_3)),
        ) as self.hk_ctrl_numpad_3:
            with hk.SendLabel(
                id=TC.shaman.name,
                to=self.mode.lbs_by_tc(TC.shaman),
            ):
                act.Target.TARGET_FOCUS_TARGET()
                act.General.STOP_CASTING_KEY_OEM1_SEMICOLUMN()
                act.Shaman.ALL_SPEC_PURGE()

            with hk.SendLabel(
                id=TC.priest.name,
                to=self.mode.lbs_by_tc(TC.priest),
            ):
                act.Target.TARGET_FOCUS_TARGET()
                act.General.STOP_CASTING_KEY_OEM1_SEMICOLUMN()
                act.Priest.ALL_SPEC_DISPEL_MAGIC()

    def build_hk_ctrl_numpad_4_aoe_fear(self):
        with hk.Hotkey(
            id="Ctrl Numpad4",
            key=KN.SCROLOCK_ON(KN.CTRL_(KN.NUMPAD_4)),
        ) as self.hk_ctrl_numpad_4:
            with hk.SendLabel(
                id=TC.priest_shadow.name,
                to=self.mode.lbs_by_tc(TC.priest_shadow),
            ):
                act.General.STOP_CASTING_KEY_OEM1_SEMICOLUMN()
                act.Priest.SHADOW_SPEC_PSYCHIC_HORROR()

    def build_hk_ctrl_numpad_5_typhoon(self):
        with hk.Hotkey(
            id="Ctrl Numpad5",
            key=KN.SCROLOCK_ON(KN.CTRL_(KN.NUMPAD_5)),
        ) as self.hk_ctrl_numpad_5:
            with hk.SendLabel(
                id=TC.druid_balance.name,
                to=self.mode.lbs_by_tc(TC.druid_balance),
            ):
                act.General.STOP_CASTING_KEY_OEM1_SEMICOLUMN()
                act.Druid.BALANCE_SPEC_TYPHOON_KEY_G()

    def build_hk_ctrl_numpad_6_thunder_storm(self):
        with hk.Hotkey(
            id="Ctrl Numpad6",
            key=KN.SCROLOCK_ON(KN.CTRL_(KN.NUMPAD_6)),
        ) as self.hk_ctrl_numpad_6:
            with hk.SendLabel(
                id="all_elemental_shaman",
                to=self.mode.lbs_by_tc(TC.shaman_elemental),
            ):
                act.General.STOP_CASTING_KEY_OEM1_SEMICOLUMN()
                act.Shaman.ELEMENTAL_SPEC_THUNDER_STORM()

    def build_hk_ctrl_numpad_7_hymn_of_life(self):
        with hk.Hotkey(
            id="Ctrl Numpad7",
            key=KN.SCROLOCK_ON(KN.CTRL_(KN.NUMPAD_7)),
        ) as self.hk_ctrl_numpad_7:
            with hk.SendLabel(
                id=TC.priest.name,
                to=self.mode.lbs_by_tc(TC.priest),
            ):
                act.General.STOP_CASTING_KEY_OEM1_SEMICOLUMN()
                act.Priest.ALL_SPEC_DIVINE_HYMN()

    def build_hk_ctrl_numpad_10_hymn_of_mana(self):
        with hk.Hotkey(
            id="Ctrl Numpad10",
            key=KN.SCROLOCK_ON(KN.CTRL_(KN.NUMPAD_0)),
        ) as self.hk_ctrl_numpad_10:
            with hk.SendLabel(
                id=TC.priest.name,
                to=self.mode.lbs_by_tc(TC.priest),
            ):
                act.General.STOP_CASTING_KEY_OEM1_SEMICOLUMN()
                act.Priest.ALL_SPEC_HYMN_OF_HOPE()

    def build_hk_ctrl_numpad_11_tank_1_taunt(self):
        with hk.Hotkey(
            id="Ctrl Numpad11 - 主坦克嘲讽",
            key=KN.SCROLOCK_ON(KN.CTRL_(KN.NUMPAD_11_DIVIDE)),
        ) as self.hk_ctrl_numpad_11:
            with hk.SendLabel(
                id="tank1",
                to=self.mode.lbs_tank1,
            ):
                act.General.STOP_CASTING_KEY_OEM1_SEMICOLUMN()
                act.Paladin.PROTECT_SPEC_KEY_Z_HAND_OF_RECKONING()

    def build_hk_ctrl_numpad_12_tank_2_taunt(self):
        with hk.Hotkey(
            id="Ctrl Numpad12 - 副坦克嘲讽",
            key=KN.SCROLOCK_ON(KN.CTRL_(KN.NUMPAD_12_MULTIPLY)),
        ) as self.hk_ctrl_numpad_12:
            with hk.SendLabel(
                id="tank2",
                to=self.mode.lbs_tank2,
            ):
                act.General.STOP_CASTING_KEY_OEM1_SEMICOLUMN()
                act.DK.ALL_SPEC_DARK_COMMAND_KEY_Z()

    def build_hk_group_09_ctrl_numpad_1_to_12(self):
        self.build_hk_ctrl_numpad_1_silence_shot_focus_target()
        self.build_hk_ctrl_numpad_2_counter_spell_focus_target()
        self.build_hk_ctrl_numpad_3_aggressive_dispel()
        self.build_hk_ctrl_numpad_4_aoe_fear()
        self.build_hk_ctrl_numpad_5_typhoon()
        self.build_hk_ctrl_numpad_6_thunder_storm()
        self.build_hk_ctrl_numpad_7_hymn_of_life()
        self.build_hk_ctrl_numpad_10_hymn_of_mana()
        self.build_hk_ctrl_numpad_11_tank_1_taunt()
        self.build_hk_ctrl_numpad_12_tank_2_taunt()

    # -------------------------------------------------------------------------
    # 实现 Shift + 小键盘 1-12 的快捷键功能. 通常是一些不常用, 但是关键时刻必备的技能.
    # -------------------------------------------------------------------------
    __anchor_hk_10_shift_numpad_1_to_12 = None

    def build_hk_shift_numpad_1(self):
        with hk.Hotkey(
            id="Shift Numpad1",
            key=KN.SCROLOCK_ON(KN.NUMPAD_SHIFT_1_END),
        ) as self.hk_shift_numpad_1:
            with hk.SendLabel(
                name=TC.shaman.name,
                to=self.mode.lbs_by_tc(TC.shaman),
            ):
                act.General.STOP_CASTING_KEY_OEM1_SEMICOLUMN()
                act.Shaman.ALL_SPEC_CALL_OF_THE_ELEMENTS()

    def build_hk_shift_numpad_2(self):
        with hk.Hotkey(
            id="Shift Numpad2",
            key=KN.SCROLOCK_ON(KN.NUMPAD_SHIFT_2_DOWN),
        ) as self.hk_shift_numpad_2:
            with hk.SendLabel(
                id=TC.shaman.name,
                to=self.mode.lbs_by_tc(TC.shaman),
            ):
                act.General.STOP_CASTING_KEY_OEM1_SEMICOLUMN()
                act.Shaman.ALL_SPEC_TOTEMIC_RECALL()

    def build_hk_group_10(self):
        self.build_hk_shift_numpad_1()
        self.build_hk_shift_numpad_2()

    # -------------------------------------------------------------------------
    # 实现由在主控角色界面下, 用鼠标在团队框架上进行单机来实现治疗的快捷键.
    # 需要配合团队框架 Healbot 插件使用.
    # -------------------------------------------------------------------------
    __anchor_hk_11_heal_bot = None

    """
    下面的这批名字为 ``_build_send_label_...`` 的函数是用于生成 ... 的工厂函数. 
    
    我们为 5 大治疗职业: 奶骑, 奶萨, 奶德, 神/戒牧, 准备了工厂函数, 这些工厂函数定义了
    SendLabel.to 的部分, 留给用户自行定义具体的动作
    """

    def _build_send_label_holy_paladin(self, funcs: T.List[callable]):
        with hk.SendLabel(
            id=TC.paladin_holy.name,
            to=self.mode.lbs_by_tc(TC.paladin_holy),
        ) as send_label:
            for func in funcs:
                func()
            return send_label

    def _build_send_label_resto_shaman(self, funcs: T.List[callable]):
        with hk.SendLabel(
            id=TC.shaman_resto.name,
            to=self.mode.lbs_by_tc(TC.shaman_resto),
        ) as send_label:
            for func in funcs:
                func()
            return send_label

    def _build_send_label_resto_druid(self, funcs: T.List[callable]):
        with hk.SendLabel(
            id=TC.druid_resto.name,
            to=self.mode.lbs_by_tc(TC.druid_resto),
        ) as send_label:
            for func in funcs:
                func()
            return send_label

    def _build_send_label_disco_priest(self, funcs: T.List[callable]):
        with hk.SendLabel(
            id=TC.priest_disco.name,
            to=self.mode.lbs_by_tc(TC.priest_disco),
        ) as send_label:
            for func in funcs:
                func()
            return send_label

    def _build_send_label_holy_priest(self, funcs: T.List[callable]):
        with hk.SendLabel(
            id=TC.priest_holy.name,
            to=self.mode.lbs_by_tc(TC.priest_holy),
        ) as send_label:
            for func in funcs:
                func()
            return send_label

    def _build_send_label_tank(self):
        with hk.SendLabel(
            id=TC.tank.name,
            to=self.mode.lbs_by_tc(TC.tank),
        ) as send_label:
            hk.Key(id=KN.KEY_2)
            return send_label

    def _build_send_label_shaman(self, funcs: T.List[callable]):
        with hk.SendLabel(
            id=TC.shaman.name,
            to=self.mode.lbs_by_tc(TC.shaman),
        ) as send_label:
            for func in funcs:
                func()
            return send_label

    def _build_send_label_dps(self):
        with hk.SendLabel(
            id=TC.dps.name,
            to=self.mode.lbs_by_tc(TC.dps),
        ) as send_label:
            act.Target.TARGET_FOCUS_TARGET()
            hk.Key(key=KN.KEY_2)
            return send_label

    def _build_send_label_non_shaman_dps(self):
        """
        点击 Healbot 的时候, 所有 DPS 继续攻击焦点的目标. 唯独 增强萨满 和 元素萨满 例外.
        虽然它们是 DPS 职业, 但是依然要跟其他治疗一样, 对团队框架目标使用治疗链.
        """
        lbs_dps = self.mode.lbs_by_tc(TC.dps)
        lbs_shaman_non_resto = self.mode.lbs_by_tc(TC.shaman_non_resto)
        to = list(set(lbs_dps).difference(lbs_shaman_non_resto))
        to.sort()
        with hk.SendLabel(
            id="non_shaman_dps",
            to=to,
        ) as send_label:
            act.Target.TARGET_FOCUS_TARGET()
            hk.Key(key=KN.KEY_2)
            return send_label

    def build_hk_healbot_small_heal(self):
        with hk.Hotkey(
            id="Healbot Small Heal",
            key=KN.SCROLOCK_ON(KN.CTRL_(KN.MOUSE_LButton)),
        ) as self.hk_healbot_small_heal:
            self._build_send_label_holy_paladin([
                act.Paladin.HEAL_BOT_RIGHT_CLICK_FLASH_OF_LIGHT,
            ])
            self._build_send_label_resto_shaman([
                act.Shaman.HEAL_BOT_RIPTIDE_RIGHT_CLICK,
            ])
            self._build_send_label_resto_druid([
                act.Druid.HEAL_BOT_LEFT_CLICK_REJUVENATION,
            ])
            self._build_send_label_disco_priest([
                act.Priest.HEAL_BOT_ALL_SPEC_POWER_WORD_SHIELD,
            ])
            self._build_send_label_holy_priest([
                act.Priest.HEAL_BOT_DISCO_AND_HOLY_SPEC_FLASH_HEAL,
            ])
            self._build_send_label_tank()
            self._build_send_label_dps()

    def build_hk_healbot_big_heal(self):
        with hk.Hotkey(
            id="Healbot Big Heal",
            key=KN.SCROLOCK_ON(KN.CTRL_(KN.MOUSE_RButton)),
        ) as self.hk_healbot_big_heal:
            self._build_send_label_holy_paladin([
                act.Paladin.HEAL_BOT_LEFT_CLICK_HOLY_LIGHT,
            ]),
            self._build_send_label_resto_shaman([
                act.Shaman.HEAL_BOT_HEALING_WAVE_LEFT_CLICK,
            ]),
            self._build_send_label_resto_druid([
                act.Druid.HEAL_BOT_RIGHT_CLICK_NOURISH,
            ]),
            self._build_send_label_disco_priest([
                act.Priest.HEAL_BOT_ALL_SPEC_POWER_WORD_SHIELD,
            ]),
            self._build_send_label_holy_priest([
                act.Priest.HEAL_BOT_DISCO_AND_HOLY_SPEC_FLASH_HEAL,
            ]),
            self._build_send_label_tank(),
            self._build_send_label_dps(),

    def build_hk_healbot_aoe_heal(self):
        with hk.Hotkey(
            id="Healbot Aoe Heal",
            key=KN.SCROLOCK_ON(KN.SHIFT_(KN.MOUSE_LButton)),
        ) as self.hk_healbot_aoe_heal:
            self._build_send_label_holy_paladin([
                act.Paladin.HEAL_BOT_LEFT_CLICK_HOLY_LIGHT,
            ]),
            self._build_send_label_shaman([
                act.Shaman.HEAL_BOT_CHAIN_HEAL_MIDDLE_CLICK,
            ]),
            self._build_send_label_resto_druid([
                act.Druid.HEAL_BOT_SHIFT_LEFT_WILD_GROWTH,
            ]),
            self._build_send_label_disco_priest([
                act.Priest.HEAL_BOT_ALL_SPEC_POWER_WORD_SHIELD,
            ]),
            self._build_send_label_holy_priest([
                act.Priest.HEAL_BOT_HOLY_SPEC_CIRCLE_OF_HEAL,
            ]),
            self._build_send_label_tank(),
            self._build_send_label_non_shaman_dps(),

    def build_hk_healbot_dispel(self):
        with hk.Hotkey(
            id="Healbot Dispel",
            key=KN.SCROLOCK_ON(KN.MOUSE_MButton),
        ) as self.hk_healbot_dispel:
            self._build_send_label_holy_paladin([
                act.Paladin.HEAL_BOT_CLEANSE,
            ]),
            self._build_send_label_resto_shaman([
                act.Shaman.HEAL_BOT_CLEANSE_CTRL_LEFT_CLICK,
            ]),
            self._build_send_label_resto_druid([
                act.Druid.HEAL_BOT_CTRL_LEFT_REMOVE_CURSE,
            ]),
            self._build_send_label_disco_priest([
                act.Priest.HEAL_BOT_ALL_SPEC_DISPEL_MAGIC,
            ]),
            self._build_send_label_holy_priest([
                act.Priest.HEAL_BOT_ALL_SPEC_DISPEL_MAGIC,
            ]),
            self._build_send_label_tank(),
            self._build_send_label_non_shaman_dps(),

    def build_hk_group_11_healbot(self):
        self.build_hk_healbot_small_heal()
        self.build_hk_healbot_big_heal()
        self.build_hk_healbot_aoe_heal()
        self.build_hk_healbot_dispel()

    # -------------------------------------------------------------------------
    # 实现使用图形界面上的按钮, 替代一些不常用, 或是紧急情况需要用到的快捷键,
    # 避免了记忆复杂快捷键的麻烦
    # -------------------------------------------------------------------------
    __anchor_control_panel = None

    # def build_control_panel(self):
    #     WIDTH = 36
    #     HEIGHT = 36
    #
    #     with hk.Command(name="AutoExec") as self.cmd_auto_exec:
    #         with hk.CreatePanel(name="MBControlPanel", x=0, y=60, width=120, height=960) as main_panel:
    #             def set_hotkey_or_command(
    #                 button,
    #                 hotkey: T.Optional[hk.Hotkey] = None,
    #                 command: T.Optional[hk.Command] = None,
    #                 command_args: T.Optional[tuple] = None,
    #             ):
    #                 if hotkey is not None:
    #                     hk.SetButtonHotkey(
    #                         button=button.name,
    #                         hotkey=hotkey,
    #                     )
    #                 if command is not None:
    #                     hk.SetButtonCommand(
    #                         button=button.name,
    #                         command=command,
    #                         args=command_args,
    #                     )
    #
    #             def create_button(
    #                 name: str,
    #                 text: str,
    #                 hotkey: T.Optional[hk.Hotkey] = None,
    #                 command: T.Optional[hk.Command] = None,
    #                 command_args: T.Optional[tuple] = None,
    #             ):
    #                 button = hk.CreateButton(
    #                     name=name,
    #                     x=0,
    #                     y=0,
    #                     width=WIDTH,
    #                     height=HEIGHT,
    #                     text=text,
    #                 )
    #                 hk.AddButtonToPanel(
    #                     button=button.name,
    #                     panel=main_panel.name,
    #                 )
    #                 set_hotkey_or_command(button, hotkey, command, command_args)
    #
    #             def create_picture_button(
    #                 name: str,
    #                 file: str,
    #                 hotkey: T.Optional[hk.Hotkey] = None,
    #                 command: T.Optional[hk.Command] = None,
    #                 command_args: T.Optional[tuple] = None,
    #             ):
    #                 button = hk.CreatePictureButton(
    #                     name=name,
    #                     x=0,
    #                     y=0,
    #                     file=file,
    #                 )
    #                 hk.AddButtonToPanel(
    #                     button=button.name,
    #                     panel=main_panel.name,
    #                 )
    #                 set_hotkey_or_command(button, hotkey, command, command_args)
    #
    #             def create_colored_button(
    #                 name: str,
    #                 bkcolor: str,
    #                 textcolor: str = "000000",
    #                 text: T.Optional[str] = None,
    #                 hotkey: T.Optional[hk.Hotkey] = None,
    #                 command: T.Optional[hk.Command] = None,
    #                 command_args: T.Optional[tuple] = None,
    #             ):
    #                 button = hk.CreateColoredButton(
    #                     name=name,
    #                     x=0,
    #                     y=0,
    #                     width=WIDTH,
    #                     height=HEIGHT,
    #                     bkcolor=f"0x{bkcolor}",
    #                     textcolor=f"0x{textcolor}",
    #                     text=text,
    #                 )
    #                 hk.AddButtonToPanel(
    #                     button=button.name,
    #                     panel=main_panel.name,
    #                 )
    #                 set_hotkey_or_command(button, hotkey, command, command_args)
    #
    #             create_picture_button(
    #                 name="ButtonA01",
    #                 file=Icons.wow,
    #                 command=self.cmd_launch_and_rename_all_game_client,
    #             )
    #
    #             create_picture_button(
    #                 name="ButtonA02",
    #                 file=Icons.log_in,
    #                 command=self.cmd_batch_login,
    #             )
    #
    #             create_picture_button(
    #                 name="ButtonA03",
    #                 file=Icons.resize_window,
    #                 command=self.cmd_center_overlap_layout,
    #             )
    #
    #             # -------------------------------------------------------------
    #             # Alt + Numpad 1 - 12
    #             # -------------------------------------------------------------
    #             create_colored_button(
    #                 name="ButtonBarAlt1To12a",
    #                 bkcolor="E75638",
    #                 text="Alt"
    #             )
    #             create_colored_button(
    #                 name="ButtonBarAlt1To12b",
    #                 bkcolor="E75638",
    #                 text="+Num"
    #             )
    #             create_colored_button(
    #                 name="ButtonBarAlt1To12c",
    #                 bkcolor="E75638",
    #                 text="1-12"
    #             )
    #
    #             create_picture_button(
    #                 name="Alt1",
    #                 file=Icons.ability_hunter_misdirection,
    #                 hotkey=self.hk_alt_numpad_1,
    #             )
    #             create_picture_button(
    #                 name="Alt2",
    #                 file=Icons.ability_mount_whitetiger,
    #                 hotkey=self.hk_alt_numpad_2,
    #             )
    #             create_picture_button(
    #                 name="Alt3",
    #                 file=Icons.ability_hunter_aspectoftheviper,
    #                 hotkey=self.hk_alt_numpad_3,
    #             )
    #             create_picture_button(
    #                 name="Alt4",
    #                 file=Icons.ability_druid_starfall,
    #                 hotkey=self.hk_alt_numpad_4,
    #             )
    #             create_picture_button(
    #                 name="Alt5",
    #                 file=Icons.spell_nature_wispheal,
    #                 hotkey=self.hk_alt_numpad_5,
    #             )
    #             create_picture_button(
    #                 name="Alt6",
    #                 file=Icons.spell_nature_bloodlust,
    #                 hotkey=self.hk_alt_numpad_6,
    #             )
    #             create_picture_button(
    #                 name="Alt7",
    #                 file=Icons.spell_holy_powerwordbarrier,
    #                 hotkey=self.hk_alt_numpad_7,
    #             )
    #             create_picture_button(
    #                 name="Alt8",
    #                 file=Icons.spell_holy_powerwordbarrier,
    #                 hotkey=self.hk_alt_numpad_8,
    #             )
    #             create_picture_button(
    #                 name="Alt9",
    #                 file=Icons.spell_holy_auramastery,
    #                 hotkey=self.hk_alt_numpad_9,
    #             )
    #             create_picture_button(
    #                 name="Alt10",
    #                 file=Icons.spell_nature_diseasecleansingtotem,
    #                 hotkey=self.hk_alt_numpad_10,
    #             )
    #             create_picture_button(
    #                 name="Alt11",
    #                 file=Icons.spell_nature_tremortotem,
    #                 hotkey=self.hk_alt_numpad_11,
    #             )
    #             create_picture_button(
    #                 name="Alt12",
    #                 file=Icons.spell_nature_strengthofearthtotem02,
    #                 hotkey=self.hk_alt_numpad_12,
    #             )
    #
    #             # -------------------------------------------------------------
    #             # Ctrl + Numpad 1 - 12
    #             # -------------------------------------------------------------
    #             create_colored_button(
    #                 name="ButtonBarCtrl1To12a",
    #                 bkcolor="E75638",
    #                 text="Ctrl"
    #             )
    #             create_colored_button(
    #                 name="ButtonBarCtrl1To12b",
    #                 bkcolor="E75638",
    #                 text="+Num"
    #             )
    #             create_colored_button(
    #                 name="ButtonBarCtrl1To12c",
    #                 bkcolor="E75638",
    #                 text="1-12"
    #             )
    #
    #             create_picture_button(
    #                 name="CtrlNumpad1",
    #                 file=Icons.ability_theblackarrow,
    #                 hotkey=self.hk_ctrl_numpad_1,
    #             )
    #             create_picture_button(
    #                 name="CtrlNumpad2",
    #                 file=Icons.spell_frost_iceshock,
    #                 hotkey=self.hk_ctrl_numpad_2,
    #             )
    #             create_picture_button(
    #                 name="CtrlNumpad3",
    #                 file=Icons.spell_holy_dispelmagic,
    #                 hotkey=self.hk_ctrl_numpad_3,
    #             )
    #             create_picture_button(
    #                 name="CtrlNumpad4",
    #                 file=Icons.spell_shadow_psychicscream,
    #                 hotkey=self.hk_ctrl_numpad_4,
    #             )
    #             create_picture_button(
    #                 name="CtrlNumpad5",
    #                 file=Icons.ability_druid_typhoon,
    #                 hotkey=self.hk_ctrl_numpad_5,
    #             )
    #             create_picture_button(
    #                 name="CtrlNumpad6",
    #                 file=Icons.spell_shaman_thunderstorm,
    #                 hotkey=self.hk_ctrl_numpad_6,
    #             )
    #             create_picture_button(
    #                 name="CtrlNumpad7",
    #                 file=Icons.spell_holy_divinehymn,
    #                 hotkey=self.hk_ctrl_numpad_7,
    #             )
    #             create_picture_button(
    #                 name="CtrlNumpad8",
    #                 file=Icons.spell_nature_tranquility,
    #                 hotkey=self.hk_ctrl_numpad_7,
    #             )
    #             create_picture_button(
    #                 name="CtrlNumpad9",
    #                 file=Icons.spell_nature_tranquility,
    #                 hotkey=self.hk_ctrl_numpad_7,
    #             )
    #             create_picture_button(
    #                 name="CtrlNumpad10",
    #                 file=Icons.spell_holy_symbolofhope,
    #                 hotkey=self.hk_ctrl_numpad_10,
    #             )
    #             create_picture_button(
    #                 name="CtrlNumpad11",
    #                 file=Icons.spell_holy_unyieldingfaith,
    #                 hotkey=self.hk_ctrl_numpad_11,
    #             )
    #             create_picture_button(
    #                 name="CtrlNumpad12",
    #                 file=Icons.spell_nature_shamanrage,
    #                 hotkey=self.hk_ctrl_numpad_12,
    #             )
    #
    #             # -------------------------------------------------------------
    #             # Shift + Numpad 1 - 9
    #             # -------------------------------------------------------------
    #             create_colored_button(
    #                 name="ButtonBarShift1To9a",
    #                 bkcolor="E75638",
    #                 text="Shift"
    #             )
    #             create_colored_button(
    #                 name="ButtonBarShift1To9b",
    #                 bkcolor="E75638",
    #                 text="+Num"
    #             )
    #             create_colored_button(
    #                 name="ButtonBarShift1To9c",
    #                 bkcolor="E75638",
    #                 text="1-9"
    #             )
    #
    #             hk.SetPanelLayout(
    #                 panel=main_panel.name,
    #                 row_length=3,
    #                 margin=1,
    #                 button_width=36,
    #                 button_height=36,
    #             )
    #
    #             hk.TargetWin(window=main_panel.name)
    #             hk.AlwaysOnTop()

    def build_control_panel(self):
        WIDTH = 24
        HEIGHT = 24

        with hk.Command(name="AutoExec") as self.cmd_auto_exec:
            with hk.CreatePanel(name="MBControlPanel", x=0, y=60, width=120, height=960) as main_panel:
                # Define three temp utility function
                def set_hotkey_or_command(
                    button,
                    hotkey: T.Optional[hk.Hotkey] = None,
                    command: T.Optional[hk.Command] = None,
                    command_args: T.Optional[tuple] = None,
                ):
                    if hotkey is not None:
                        hk.SetButtonHotkey(
                            button=button.name,
                            hotkey=hotkey,
                        )
                    if command is not None:
                        hk.SetButtonCommand(
                            button=button.name,
                            command=command,
                            args=command_args,
                        )

                def create_button(
                    name: str,
                    text: str,
                    hotkey: T.Optional[hk.Hotkey] = None,
                    command: T.Optional[hk.Command] = None,
                    command_args: T.Optional[tuple] = None,
                ):
                    button = hk.CreateButton(
                        name=name,
                        x=0,
                        y=0,
                        width=WIDTH,
                        height=HEIGHT,
                        text=text,
                    )
                    hk.AddButtonToPanel(
                        button=button.name,
                        panel=main_panel.name,
                    )
                    set_hotkey_or_command(button, hotkey, command, command_args)

                def create_picture_button(
                    name: str,
                    file: str,
                    hotkey: T.Optional[hk.Hotkey] = None,
                    command: T.Optional[hk.Command] = None,
                    command_args: T.Optional[tuple] = None,
                ):
                    button = hk.CreatePictureButton(
                        name=name,
                        x=0,
                        y=0,
                        file=file,
                    )
                    hk.AddButtonToPanel(
                        button=button.name,
                        panel=main_panel.name,
                    )
                    set_hotkey_or_command(button, hotkey, command, command_args)

                def create_colored_button(
                    name: str,
                    bkcolor: str,
                    textcolor: str = "000000",
                    text: T.Optional[str] = None,
                    hotkey: T.Optional[hk.Hotkey] = None,
                    command: T.Optional[hk.Command] = None,
                    command_args: T.Optional[tuple] = None,
                ):
                    button = hk.CreateColoredButton(
                        name=name,
                        x=0,
                        y=0,
                        width=WIDTH,
                        height=HEIGHT,
                        bkcolor=f"0x{bkcolor}",
                        textcolor=f"0x{textcolor}",
                        text=text,
                    )
                    hk.AddButtonToPanel(
                        button=button.name,
                        panel=main_panel.name,
                    )
                    set_hotkey_or_command(button, hotkey, command, command_args)

                create_picture_button(
                    name="ButtonA01",
                    file=Icons.wow,
                    command=self.cmd_launch_and_rename_all_game_client,
                )

                create_picture_button(
                    name="ButtonA02",
                    file=Icons.log_in,
                    command=self.cmd_batch_login,
                )

                create_picture_button(
                    name="ButtonA03",
                    file=Icons.resize_window,
                    command=self.cmd_center_overlap_layout,
                )

                create_picture_button(
                    name="ButtonA04",
                    file=Icons.resize_window,
                    command=self.cmd_center_overlap_layout,
                )

                create_picture_button(
                    name="ButtonA05",
                    file=Icons.resize_window,
                    command=self.cmd_center_overlap_layout,
                )

                counter = 0
                index_mapper = dict()
                for window, account in self.mode.login_window_and_account_pairs:
                    index_mapper[window.index] = (window, account)
                for i in range(1, 1 + 25):
                    if i in index_mapper:
                        window, account = index_mapper[i]
                        create_button(
                            name=f"ButtonLogin{str(i).zfill(2)}",
                            text=window.label,
                            command=self.cmd_enter_username_and_password,
                            command_args=(
                                window.title,
                                account.username,
                                account.password,
                            )
                        )
                    else:
                        create_button(
                            name=f"ButtonLogin{str(i).zfill(2)}",
                            text="NA",
                        )

                # -------------------------------------------------------------
                # Login
                # -------------------------------------------------------------
                # for self.mode.

                # -------------------------------------------------------------
                # Alt + Numpad 1 - 12
                # -------------------------------------------------------------
                for id, text in enumerate([
                    "Alt",
                    "+",
                    "Num",
                    "Pad",
                    "1-12",
                ], start=1):
                    create_colored_button(
                        name=f"ButtonBarAlt1To12B{id}",
                        bkcolor="E75638",
                        text=text
                    )

                create_picture_button(
                    name="Alt1",
                    file=Icons.ability_hunter_misdirection,
                    hotkey=self.hk_alt_numpad_1,
                )
                create_picture_button(
                    name="Alt2",
                    file=Icons.ability_mount_whitetiger,
                    hotkey=self.hk_alt_numpad_2,
                )
                create_picture_button(
                    name="Alt3",
                    file=Icons.ability_hunter_aspectoftheviper,
                    hotkey=self.hk_alt_numpad_3,
                )
                create_button(
                    name=f"Alt3B1",
                    text="NA",
                )
                create_button(
                    name=f"Alt3B2",
                    text="NA",
                )

                create_picture_button(
                    name="Alt4",
                    file=Icons.ability_druid_starfall,
                    hotkey=self.hk_alt_numpad_4,
                )
                create_picture_button(
                    name="Alt5",
                    file=Icons.spell_nature_wispheal,
                    hotkey=self.hk_alt_numpad_5,
                )
                create_picture_button(
                    name="Alt6",
                    file=Icons.spell_nature_bloodlust,
                    hotkey=self.hk_alt_numpad_6,
                )
                create_button(
                    name=f"Alt6B1",
                    text="NA",
                )
                create_button(
                    name=f"Alt6B2",
                    text="NA",
                )

                create_picture_button(
                    name="Alt7",
                    file=Icons.spell_holy_powerwordbarrier,
                    hotkey=self.hk_alt_numpad_7,
                )
                create_picture_button(
                    name="Alt8",
                    file=Icons.spell_holy_powerwordbarrier,
                    hotkey=self.hk_alt_numpad_8,
                )
                create_picture_button(
                    name="Alt9",
                    file=Icons.spell_holy_auramastery,
                    hotkey=self.hk_alt_numpad_9,
                )
                create_button(
                    name=f"Alt9B1",
                    text="NA",
                )
                create_button(
                    name=f"Alt9B2",
                    text="NA",
                )

                create_picture_button(
                    name="Alt10",
                    file=Icons.spell_nature_diseasecleansingtotem,
                    hotkey=self.hk_alt_numpad_10,
                )
                create_picture_button(
                    name="Alt11",
                    file=Icons.spell_nature_tremortotem,
                    hotkey=self.hk_alt_numpad_11,
                )
                create_picture_button(
                    name="Alt12",
                    file=Icons.spell_nature_strengthofearthtotem02,
                    hotkey=self.hk_alt_numpad_12,
                )
                create_button(
                    name=f"Alt12B1",
                    text="NA",
                )
                create_button(
                    name=f"Alt12B2",
                    text="NA",
                )

                # -------------------------------------------------------------
                # Ctrl + Numpad 1 - 12
                # -------------------------------------------------------------
                for id, text in enumerate([
                    "Ctrl",
                    "+",
                    "Num",
                    "Pad",
                    "1-12",
                ], start=1):
                    create_colored_button(
                        name=f"ButtonBarCtrl1To12B{id}",
                        bkcolor="E75638",
                        text=text
                    )

                create_picture_button(
                    name="CtrlNumpad1",
                    file=Icons.ability_theblackarrow,
                    hotkey=self.hk_ctrl_numpad_1,
                )
                create_picture_button(
                    name="CtrlNumpad2",
                    file=Icons.spell_frost_iceshock,
                    hotkey=self.hk_ctrl_numpad_2,
                )
                create_picture_button(
                    name="CtrlNumpad3",
                    file=Icons.spell_holy_dispelmagic,
                    hotkey=self.hk_ctrl_numpad_3,
                )
                create_button(
                    name=f"Ctrl3B1",
                    text="NA",
                )
                create_button(
                    name=f"Ctrl3B2",
                    text="NA",
                )

                create_picture_button(
                    name="CtrlNumpad4",
                    file=Icons.spell_shadow_psychicscream,
                    hotkey=self.hk_ctrl_numpad_4,
                )
                create_picture_button(
                    name="CtrlNumpad5",
                    file=Icons.ability_druid_typhoon,
                    hotkey=self.hk_ctrl_numpad_5,
                )
                create_picture_button(
                    name="CtrlNumpad6",
                    file=Icons.spell_shaman_thunderstorm,
                    hotkey=self.hk_ctrl_numpad_6,
                )
                create_button(
                    name=f"Ctrl6B1",
                    text="NA",
                )
                create_button(
                    name=f"Ctrl6B2",
                    text="NA",
                )

                create_picture_button(
                    name="CtrlNumpad7",
                    file=Icons.spell_holy_divinehymn,
                    hotkey=self.hk_ctrl_numpad_7,
                )
                create_picture_button(
                    name="CtrlNumpad8",
                    file=Icons.spell_nature_tranquility,
                    hotkey=self.hk_ctrl_numpad_7,
                )
                create_picture_button(
                    name="CtrlNumpad9",
                    file=Icons.spell_nature_tranquility,
                    hotkey=self.hk_ctrl_numpad_7,
                )
                create_button(
                    name=f"Ctrl9B1",
                    text="NA",
                )
                create_button(
                    name=f"Ctrl9B2",
                    text="NA",
                )

                create_picture_button(
                    name="CtrlNumpad10",
                    file=Icons.spell_holy_symbolofhope,
                    hotkey=self.hk_ctrl_numpad_10,
                )
                create_picture_button(
                    name="CtrlNumpad11",
                    file=Icons.spell_holy_unyieldingfaith,
                    hotkey=self.hk_ctrl_numpad_11,
                )
                create_picture_button(
                    name="CtrlNumpad12",
                    file=Icons.spell_nature_shamanrage,
                    hotkey=self.hk_ctrl_numpad_12,
                )
                create_button(
                    name=f"Ctrl12B1",
                    text="NA",
                )
                create_button(
                    name=f"Ctrl12B2",
                    text="NA",
                )

                # # -------------------------------------------------------------
                # # Shift + Numpad 1 - 9
                # # -------------------------------------------------------------
                # create_colored_button(
                #     name="ButtonBarShift1To9a",
                #     bkcolor="E75638",
                #     text="Shift"
                # )
                # create_colored_button(
                #     name="ButtonBarShift1To9b",
                #     bkcolor="E75638",
                #     text="+Num"
                # )
                # create_colored_button(
                #     name="ButtonBarShift1To9c",
                #     bkcolor="E75638",
                #     text="1-9"
                # )

                hk.SetPanelLayout(
                    panel=main_panel.name,
                    row_length=5,
                    margin=1,
                    button_width=24,
                    button_height=24,
                )

                hk.TargetWin(window=main_panel.name)
                hk.AlwaysOnTop()
