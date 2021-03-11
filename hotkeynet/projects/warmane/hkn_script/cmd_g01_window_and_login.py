# -*- coding: utf-8 -*-

from ._config_and_script import config, script
from ..config import Config
from ..constant.windows import window_list, window_index
from ....script import Script, Command
from ....utils import render_template, remove_indent


def build_cmd_launch_and_rename_game_client():
    """
    运行一个游戏客户端, 并重命名游戏窗口.

    参数定义:

    - %1%: Local or IP address; example: Local 表示本地, 192.168.0.1 表示局域网中的其他机器的 IP
    - %2%: 窗口的新名称; example: WoW1

    这里的窗口的新名称是用来指定给哪个窗口发送键盘鼠标命令的关键.
    """
    return Command(
        name="LaunchAndRenameGameClient",
        actions=[
            remove_indent(f"""
            <SendPC %1%>
                <Run "{config.game_client_config.wow_exe_path}">
                <RenameWin "World of Warcraft" %2%>
            """)
        ],
        script=script,
    )


cmd_launch_and_rename_game_client = build_cmd_launch_and_rename_game_client()


def build_cmd_launch_and_rename_all_game_client():
    """
    批量启动多个游戏窗口并全部重命名.

    注意!!! 在 HotketNet 界面菜单上的 Options -> Settings 中有一项
    Window name match 一定要勾选 Exact Match. 如果勾选的是 Partial Match,
    则你在调用 WoW1 窗口的时候, 由于是用的部分匹配, WoW10 也会被匹配到,
    导致你的 WoW1 和 WoW10 无法被区分开来.

    参数定义:

    无
    """
    return Command(
        name="LaunchAndRenameAllGameClient",
        actions=[
            cmd_launch_and_rename_game_client.call("Local", window.title)
            for window in window_list[:config.game_client_config.n_windows]
        ],
        script=script,
    )


cmd_launch_and_rename_all_game_client = build_cmd_launch_and_rename_all_game_client()


def build_cmd_bring_window_to_foreground(script: Script, config: Config):
    """
    将某个窗口作为当前焦点窗口, 带到最前端.

    参数:

    - %1%: 窗口名, 例如: WoW1

    说明:

    This command may cause: Operating system SetForegroundWindow function failed;
    Windows reports system error 0. **You CANNOT operate this too fast**.
    """
    return Command(
        name="BringWindowToForeground",
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


cmd_bring_window_to_foreground = build_cmd_bring_window_to_foreground(script, config)


def build_cmd_resize_and_relocate_window():
    """
    将某个窗口尺寸调整, 给左边留出一竖条用于 Control Panel, 并移动到屏幕中心区域.
    Resize and Relocate the Specified Window to the center.
    """
    return Command(
        name="ResizeAndRelocateWindow",
        actions=[
            remove_indent("""
            <SendPC Local>
                <Wait 50>
                <SendWinM %1%>
                    <SetWinRect {left_top_x} {left_top_y} {width} {height}>
            """.format(
                left_top_x=config.game_client_config.window_left_top_x,
                left_top_y=config.game_client_config.window_left_top_y,
                width=config.game_client_config.window_width,
                height=config.game_client_config.window_height,
            )),
        ],
        script=script,
    )


cmd_resize_and_relocate_window = build_cmd_resize_and_relocate_window()


def build_cmd_center_overlap_layout():
    """
    让所有窗口都符合 ResizeAndRelocateWindow 中的尺寸和位置设置
    Apply ResizeAndRelocateWindow to all window
    """
    return Command(
        name="CenterOverlapLayout",
        actions=[
            cmd_resize_and_relocate_window.call(window.title)
            for window in window_list[:config.game_client_config.n_windows]
        ],
        script=script,
    )


cmd_center_overlap_layout = build_cmd_center_overlap_layout()


def build_cmd_enter_username_and_password():
    """
    在指定游戏客户端窗口内填入账号密码.

    参数定义:

    - %1%: 窗口名称
    - %2%: 账号
    - %3%: 密码
    """
    return Command(
        name="EnterUsernameAndPasssword",
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
                wrong_password_pop_up_x=config.game_client_config.wrong_password_pop_up_x,
                wrong_password_pop_up_y=config.game_client_config.wrong_password_pop_up_y,
                username_input_box_x=config.game_client_config.username_input_box_x,
                username_input_box_y=config.game_client_config.username_input_box_y,
            ))
        ],
        script=script,
    )


cmd_enter_username_and_password = build_cmd_enter_username_and_password()


def build_cmd_batch_login():
    """
    根据 Active Character 批量登录游戏账号.
    """
    return Command(
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
                        window_index[ac.window_index].title,
                        ac.credential.username,
                        ac.credential.password,
                    )
                    for ac in config.active_character_config.iter_by_window_index()
                ],
                cmd=cmd_enter_username_and_password
            ),
        ],
        script=script,
    )


cmd_batch_login = build_cmd_batch_login()
