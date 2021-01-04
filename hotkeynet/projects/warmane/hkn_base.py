# -*- coding: utf-8 -*-

import typing

from .config import Config
from ... import keyname
from ...script import (
    Script, Command, Hotkey,
    CallCommand,
)
from ...utils import render_template

TAB = " " * 4

_cmd_LaunchAndRename_tpl = f"""
    <SendPC %1%>
        <Run "{Config.WOW_EXE_PATH}">
            <RenameWin "World of Warcraft" %2%>
"""

cmd_LaunchAndRename = Command(
    name="LaunchAndRename",
    content=_cmd_LaunchAndRename_tpl,
)
"""
运行游戏客户端, 并重命名游戏窗口

参数定义:

- %1%: Local or IP address; example: Local 表示本地, 192.168.0.1 表示局域网中的其他机器的 IP
- %2%: 窗口的新名称; example WoW1

这里的窗口的新名称是用来指定给哪个窗口发送键盘鼠标命令的关键.
"""


# --- use one of following Command to overwrite cmd_LaunchAndRenameGameClientWindow
_cmd_LaunchAndRenameWoW1ToWoW5_tpl = """
    {%- for i in range(1, 5+1) %}
    {{ cmd.call("Local", "WoW" + i|string) }}
    {%- endfor %}
""".strip()

cmd_LaunchAndRenameWoW1ToWoW5 = Command(
    name="LaunchAndRenameWoW1ToWoW5",
    content=render_template(_cmd_LaunchAndRenameWoW1ToWoW5_tpl, cmd=cmd_LaunchAndRename),
)

_cmd_LaunchAndRenameWoW1ToWoW10_tpl = """
    {%- for i in range(1, 10+1) %}
    {{ cmd.call("Local", "WoW" + i|string) }}
    {%- endfor %}
""".strip()

cmd_LaunchAndRenameWoW1ToWoW10 = Command(
    name="LaunchAndRenameWoW1ToWoW10",
    content=render_template(_cmd_LaunchAndRenameWoW1ToWoW10_tpl, cmd=cmd_LaunchAndRename),
)
"""
注意!!! 在 HotketNet 界面菜单上的 Options -> Settings 中有一项
Window name match 一定要勾选 Exact Match. 如果勾选的是 Partial Match,
则你在调用 WoW1 窗口的时候, 由于是用的部分匹配, WoW10 也会被匹配到,
导致你的 WoW1 和 WoW10 无法被区分开来.
"""

_cmd_LaunchAndRenameWoW1ToWoW18_tpl = """
    {%- for i in range(1, 18+1) %}
    {{ cmd.call("Local", "WoW" + i|string) }}
    {%- endfor %}
""".strip()

cmd_LaunchAndRenameWoW1ToWoW18 = Command(
    name="LaunchAndRenameWoW1ToWoW18",
    content=render_template(_cmd_LaunchAndRenameWoW1ToWoW18_tpl, cmd=cmd_LaunchAndRename),
)

cmd_LaunchAndRenameGameClientWindow = None  # type: Command

_cmd_BringToForeground_tpl = """
    <SendPC Local>
        <TargetWin %1%>
            <Wait 50>
            // This command may cause: Operating system SetForegroundWindow function failed; Windows reports system error 0. 
            // You CANNOT operate this too fast
            <SetForegroundWin> // This command response fast
            // <SetActiveWin> // This command cause big delay
"""

cmd_BringToForeground = Command(
    name="BringToForeground",
    content=_cmd_BringToForeground_tpl,
)
"""
将某个窗口作为当前焦点窗口, 带到最前端.

参数:

- %1%: 窗口名, 例如: WoW1
"""

_cmd_ResizeAndRelocateWindowToCenter_tpl = """
    <SendPC Local>
        <Wait 50>
        <SendWinM %1%>
            <SetWinRect {left_top_x} {left_top_y} {width} {height}>
"""

cmd_ResizeAndRelocateWindowToCenter1600x900 = Command(
    name="ResizeAndRelocateWindowToCenter",
    content=_cmd_ResizeAndRelocateWindowToCenter_tpl.format(
        left_top_x=120, left_top_y=0, width=1600, height=900,
    ),
)

cmd_ResizeAndRelocateWindowToCenter1800x1012 = Command(
    name="ResizeAndRelocateWindowToCenter",
    content=_cmd_ResizeAndRelocateWindowToCenter_tpl.format(
        left_top_x=120, left_top_y=0, width=1800, height=1012
    ),
)


cmd_ResizeAndRelocateWindowToCenter = None  # type: Command
"""
Resize and Relocate the Specified Window to the center;
将某个窗口尺寸调整, 给左边留出一竖条用于 Control Panel, 并移动到屏幕中心区域
"""

_cmd_EnterUsernamePasssword_tpl = """
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
    wrong_password_pop_up_x=Config.WRONG_PASSWORD_POP_UP_X,
    wrong_password_pop_up_y=Config.WRONG_PASSWORD_POP_UP_Y,
    username_input_box_x=Config.USERNAME_INPUT_BOX_X,
    username_input_box_y=Config.USERNAME_INPUT_BOX_Y,
)

cmd_EnterUsernamePasssword = Command(
    name="EnterUsernamePasssword",
    content=_cmd_EnterUsernamePasssword_tpl,
)
"""
在指定游戏客户端窗口内填入账号密码.

参数定义:

- %1%: 窗口名称
- %2%: 账号
- %3%: 密码
"""

# --- use one of following Command to overwrite cmd_BatchLogin
def build_cmd_content_BatchLogin(windows: typing.Iterable[int], accounts: typing.Iterable[int]) -> str:
    """
    Sample output::

        <Wait 3000> // 等待一段时间
        <EnterUsernamePasssword WoW1 myaccount1 mypassword1>
        <EnterUsernamePasssword WoW2 myaccount2 mypassword2>
        ...
        <Restore>
    """
    lines = [
        f"{TAB}<Wait 3000> // 等待一段时间",
    ]
    for window, account in zip(windows, accounts):
        username = Config.credentials[account - 1]["username"]
        password = Config.credentials[account - 1]["password"]
        line = "{tab}<{command} {window} {username} {password}>".format(
            tab=TAB,
            command=cmd_EnterUsernamePasssword.name,
            window=f"WoW{window}",
            username=username,
            password=password,
        )
        lines.append(line)
    lines.append(f"{TAB}<Restore>")
    return "\n".join(lines)


cmd_BatchLoginFatmulti1To18 = Command(
    name="BatchLoginFatmulti1To18",
    content=build_cmd_content_BatchLogin(
        windows=range(1, 18+1),
        accounts=range(1, 18+1),
    ),
)

cmd_BatchLoginFatmulti1To5 = Command(
    name="BatchLoginFatmulti1To5",
    content=build_cmd_content_BatchLogin(
        windows=range(1, 5+1),
        accounts=range(1, 5+1),
    ),
)

cmd_BatchLoginFatmulti6To10 = Command(
    name="BatchLoginFatmulti6To10",
    content=build_cmd_content_BatchLogin(
        windows=range(6, 10+1),
        accounts=range(6, 10+1),
    ),
)

cmd_BatchLoginFatmulti1To10 = Command(
    name="BatchLoginFatmulti1To10",
    content=build_cmd_content_BatchLogin(
        windows=range(1, 10+1),
        accounts=range(1, 10+1),
    ),
)

cmd_BatchLogin10DruidPvP_tpl = Command(
    name="BatchLogin10DruidPvP",
    content=build_cmd_content_BatchLogin(
        windows=(3, 8, 11, 12, 13, 14, 15, 16, 17, 18),
        accounts=(3, 8, 11, 12, 13, 14, 15, 16, 17, 18),
    ),
)

cmd_BatchLogin = None  # type: Command
"""
批量登录游戏账号
"""

# --- using one of following function to overwrite hk_SingleLogin_list ---
def build_hk_list_SingleLogin(windows: typing.Iterable[int]) -> typing.List[Hotkey]:
    hk_list = list()
    for key, window in zip(keyname.Multibox.f1_to_f18, windows):
        username = Config.credentials[window - 1]["username"]
        password = Config.credentials[window - 1]["password"]
        window_name = f"WoW{window}"
        hk = Hotkey(
            name=f"SingleLogin{username.title()}",
            key=keyname.SCROLOCK_ON(keyname.CTRL_SHIFT_ALT(key)),
            actions=[
                cmd_EnterUsernamePasssword.call(window_name, username, password)
            ],
        )
        hk_list.append(hk)
    return hk_list


hk_SingleLogin_list_fatmulti1_to_18 = build_hk_list_SingleLogin(range(1, 18 + 1))

hk_SingleLogin_list = None  # type: typing.List[Hotkey]


# --- using one of following hotkey to overwrite hk_RoundRobinToggleWindow
def build_hk_bring_to_foreground(windows: typing.Iterable[int]):
    actions = list()
    for window in windows:
        actions.append("<Toggle>")
        actions.append("    {}".format(cmd_BringToForeground.call(f"WoW{window}")))

    return Hotkey(
        name="RoundRobinToggleWindow",
        key=keyname.SCROLOCK_ON(keyname.CTRL_(keyname.TAB)),
        actions=actions,
    )


hk_RoundRobinToggleWindow_5W_5P_WoW1ToWoW5 = build_hk_bring_to_foreground(range(1, 5 + 1))
hk_RoundRobinToggleWindow_10W_10P_WoW1ToWoW10 = build_hk_bring_to_foreground(range(1, 10 + 1))
hk_RoundRobinToggleWindow_18W_18P_WoW1ToWoW18 = build_hk_bring_to_foreground(range(1, 18 + 1))

hk_RoundRobinToggleWindow = None  # type: Hotkey


# --- using one of following hotkey to overwrite hk_ToggleToSpecificWindow_list
def build_hk_list_toggle_to_sepcific_window(windows: typing.Iterable[int]):
    hk_ToggleToSpecificWindow_list = list()
    for key, window in zip(keyname.Multibox.f1_to_f18, windows):
        hk = Hotkey(
            name=f"ToggleToSpecificWindowWoW{window}",
            key=keyname.SCROLOCK_ON(keyname.CTRL_(key)),
            actions=[
                cmd_BringToForeground.call(f"WoW{window}")
            ]
        )
        hk_ToggleToSpecificWindow_list.append(hk)
    return hk_ToggleToSpecificWindow_list


hk_ToggleToSpecificWindow_list_WoW1ToWoW5 = build_hk_list_toggle_to_sepcific_window(range(1, 5 + 1))
hk_ToggleToSpecificWindow_list_WoW1ToWoW10 = build_hk_list_toggle_to_sepcific_window(range(1, 10 + 1))
hk_ToggleToSpecificWindow_list_WoW1ToWoW18 = build_hk_list_toggle_to_sepcific_window(range(1, 18 + 1))

# 5 lvl 60 twink
hk_ToggleToSpecificWindow_list_WoW6ToWoW10 = build_hk_list_toggle_to_sepcific_window([6, 7, 8, 9, 10])

hk_ToggleToSpecificWindow_list_WoW1_WoW8_WoW11_WoW12_WoW13 = build_hk_list_toggle_to_sepcific_window([1, 8, 11, 12, 13])
hk_ToggleToSpecificWindow_list_WoW1_WoW18_WoW15_WoW16_WoW17 = build_hk_list_toggle_to_sepcific_window(
    [1, 18, 15, 16, 17])

hk_ToggleToSpecificWindow_list = None  # type: typing.List[Hotkey]


# ---
def create_script() -> Script:
    script = Script()

    script.add_command(cmd_LaunchAndRename)
    script.add_command(cmd_LaunchAndRenameGameClientWindow)
    script.add_command(cmd_BringToForeground)

    script.add_command(cmd_ResizeAndRelocateWindowToCenter)

    _cmd_CenterOverlapLayout_tpl = "\n".join([
        "    {}".format(cmd_ResizeAndRelocateWindowToCenter.call(f"WoW{window}"))
        for window in range(1, 18 + 1)
    ])

    cmd_CenterOverlapLayout = Command(
        name="CenterOverlapLayout",
        content=_cmd_CenterOverlapLayout_tpl,
    )
    script.add_command(cmd_CenterOverlapLayout)

    script.add_command(cmd_EnterUsernamePasssword)
    script.add_command(cmd_BatchLogin)

    # --- HOTKEY ---
    hk_LaunchAndRenameGameClientWindow = Hotkey(
        name="LaunchAndRenameGameClientWindow",
        key=keyname.SCROLOCK_ON(keyname.CTRL_ALT_(keyname.L)),
        actions=[
            CallCommand(
                cmd=cmd_LaunchAndRenameGameClientWindow,
            )
        ]
    )
    script.add_hotkey(hk_LaunchAndRenameGameClientWindow)

    script.add_hotkey(hk_RoundRobinToggleWindow)

    for hk in hk_ToggleToSpecificWindow_list:
        script.add_hotkey(hk)

    # Apply Command ResizeAndRelocateWindowToCenter to all window
    # 让所有窗口都符合 cmd_ResizeAndRelocateWindowToCenter 中的尺寸和位置设置
    hk_CenterOverlapLayout = Hotkey(
        name="CenterOverlapLayout",
        key=keyname.SCROLOCK_ON(keyname.CTRL_SHIFT_ALT(keyname.NUMPAD_11_DIVIDE)),
        actions=[
            CallCommand(cmd=cmd_CenterOverlapLayout)
        ]
    )
    script.add_hotkey(hk_CenterOverlapLayout)

    hk_BatchLogin = Hotkey(
        name="BatchLogin",
        key=keyname.SCROLOCK_ON(keyname.CTRL_ALT_(keyname.S)),
        actions=[
            CallCommand(
                cmd=cmd_BatchLogin,
            )
        ]
    )
    script.add_hotkey(hk_BatchLogin)

    for hk in hk_SingleLogin_list:
        script.add_hotkey(hk)

    return script
