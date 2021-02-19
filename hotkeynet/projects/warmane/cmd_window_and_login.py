# -*- coding: utf-8 -*-

from .config import Config
from .script import script
from ...script import Command
from ...utils import render_template, remove_indent

cmd_LaunchAndRename = Command(
    name="LaunchAndRename",
    actions=[
        remove_indent(f"""
        <SendPC %1%>
            <Run "{Config.wow_exe_path}">
            <RenameWin "World of Warcraft" %2%>
        """)
    ],
    script=script,
)
"""
运行游戏客户端, 并重命名游戏窗口

参数定义:

- %1%: Local or IP address; example: Local 表示本地, 192.168.0.1 表示局域网中的其他机器的 IP
- %2%: 窗口的新名称; example: WoW1

这里的窗口的新名称是用来指定给哪个窗口发送键盘鼠标命令的关键.
"""

cmd_LaunchAndRenameGameClientWindow = Command(
    name="LaunchAndRenameGameClientWindow",
    actions=[
        cmd_LaunchAndRename.call("Local", "WoW{}".format(window))
        for window in Config.Windows.launch_and_rename_windows
    ],
    script=script,
)
"""
批量启动多个游戏窗口并全部重命名

注意!!! 在 HotketNet 界面菜单上的 Options -> Settings 中有一项
Window name match 一定要勾选 Exact Match. 如果勾选的是 Partial Match,
则你在调用 WoW1 窗口的时候, 由于是用的部分匹配, WoW10 也会被匹配到,
导致你的 WoW1 和 WoW10 无法被区分开来.
"""

cmd_BringToForeground = Command(
    name="BringToForeground",
    actions=[
        remove_indent("""
        <SendPC Local>
            <TargetWin %1%>
                <Wait 50>
                <SetForegroundWin> // This command response fast
                // <SetActiveWin> // This command cause big delay
        """)
    ],
    script=script,
)
"""
将某个窗口作为当前焦点窗口, 带到最前端.

参数:

- %1%: 窗口名, 例如: WoW1

说明: 

This command may cause: Operating system SetForegroundWindow function failed; Windows reports system error 0.
You CANNOT operate this too fast
"""

cmd_ResizeAndRelocateWindowToCenter = Command(
    name="ResizeAndRelocateWindowToCenter",
    actions=[
        remove_indent("""
        <SendPC Local>
            <Wait 50>
            <SendWinM %1%>
                <SetWinRect {left_top_x} {left_top_y} {width} {height}>
        """.format(
            left_top_x=120,
            left_top_y=0,
            width=Config.Coordinate.window_width,
            height=Config.Coordinate.window_height,
        )),
    ],
    script=script,
)
"""
Resize and Relocate the Specified Window to the center
将某个窗口尺寸调整, 给左边留出一竖条用于 Control Panel, 并移动到屏幕中心区域.
"""


cmd_CenterOverlapLayout = Command(
    name="CenterOverlapLayout",
    actions=[
        cmd_ResizeAndRelocateWindowToCenter.call("WoW{}".format(window))
        for window in Config.Windows.launch_and_rename_windows
    ],
    script=script,
)
"""
Apply ResizeAndRelocateWindowToCenter to all window
让所有窗口都符合 ResizeAndRelocateWindowToCenter 中的尺寸和位置设置
"""


cmd_EnterUsernamePasssword = Command(
    name="EnterUsernamePasssword",
    actions=[
        remove_indent("""
        <SendPC Local>
            <SendWin %1%>
                // Wait to bring window foreground; 等待将窗口带到最前端
                <Wait 500>
                // Click OK on Wrong Pass Word Pop Out; 清除可能的密码错误窗口, 移除遮挡
                <ClickMouse LButton Both Window {wrong_password_pop_up_x} {wrong_password_pop_up_y} NoRestore>
                <Wait 300>
                // Click on username Input Box; 在用户名输入框点击左键
                <ClickMouse LButton Both Window {username_input_box_x} {username_input_box_y} NoRestore>
                <Wait 300>
                // Clear off password Input Box; 用 tab 切换到密码输入框然后清空
                <Key Tab>
                <Key Backspace>
                <Wait 100>
                // Clear off username Input Box; 用 tab 千幻回用户名输入框然后清空
                <Key Tab>
                <Key Backspace>
                <Wait 100>
                // Enter Username; 输入用户名
                <Text %2%>
                <Wait 100>
                // Switch To Password; 切换到密码输入框
                <Key Tab>
                <Wait 100>
                // Enter Password; 输入密码
                <Text %3%>
                <Wait 100>
                // Press Enter; 按下回车登录
                <Key Enter>
                // Wait for authentication and load character selection interface; 等待进入角色选择画面
                <Wait 500>
        """.format(
            wrong_password_pop_up_x=Config.Coordinate.wrong_password_pop_up_x,
            wrong_password_pop_up_y=Config.Coordinate.wrong_password_pop_up_y,
            username_input_box_x=Config.Coordinate.username_input_box_x,
            username_input_box_y=Config.Coordinate.username_input_box_y,
        ))
    ],
    script=script,
)
"""
在指定游戏客户端窗口内填入账号密码.

参数定义:

- %1%: 窗口名称
- %2%: 账号
- %3%: 密码
"""

cmd_BatchLogin = Command(
    name="BatchLogin",
    actions=[
        render_template(
            remove_indent("""
            <Wait 3000> // 等待一段时间, 让你有时间将错误的输入法切换对
            {%- for window, username, password in data %}
            {{ cmd.call(window, username, password) }}
            {%- endfor %}
            <Restore>
            """),
            data=[
                (
                    "WoW{}".format(window),
                    Config.Credential.account_sequence()[account - 1]["username"],
                    Config.Credential.account_sequence()[account - 1]["password"],
                )
                for window, account in zip(
                    Config.Windows.batch_login_windows,
                    Config.Windows.batch_login_accounts
                )
            ],
            cmd=cmd_EnterUsernamePasssword
        ),
    ],
    script=script,
)
"""
批量登录游戏账号
"""
