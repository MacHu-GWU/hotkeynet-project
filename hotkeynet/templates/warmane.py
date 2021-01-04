# -*- coding: utf-8 -*-

import typing

from .warmane_config import Config
from .. import keyname
from ..script import (
    Script, Command, Hotkey,
    CallCommand,
)
from ..utils import render_template

_cmd_LaunchAndRename_tpl = f"""
    <SendPC %1%>
        <Run "{Config.WOW_EXE_PATH}">
            <RenameWin "World of Warcraft" %2%>
"""

cmd_LaunchAndRename = Command(
    name="LaunchAndRename",
    content=_cmd_LaunchAndRename_tpl,
)

# --- use one of following Command to overwrite cmd_LaunchAndRenameGameClientWindow
# 注意!!! 在 HotketNet 界面菜单上的 Options -> Settings 中有一项
# Window name match 一定要勾选 Exact Match. 如果勾选的是 Partial Match,
# 则你在调用 WoW1 窗口的时候, 由于是用的部分匹配, WoW10 也会被匹配到,
# 导致你的 WoW1 和 WoW10 无法被区分开来.
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

_cmd_LaunchAndRenameWoW1ToWoW18_tpl = """
    {%- for i in range(1, 18+1) %}
    {{ cmd.call("Local", "WoW" + i|string) }}
    {%- endfor %}
""".strip()

cmd_LaunchAndRenameWoW1ToWoW18 = Command(
    name="LaunchAndRenameWoW1ToWoW18",
    content=render_template(_cmd_LaunchAndRenameWoW1ToWoW18_tpl, cmd=cmd_LaunchAndRename),
)

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

# --- use one of following Command to overwrite cmd_BatchLogin
_cmd_BatchLoginFatmulti1To18_tpl = f"""
    <Wait 3000> // 等待一段时间
    <{cmd_EnterUsernamePasssword.name} WoW1 {Config.fatmulti1_username} {Config.fatmulti1_password}>
    <{cmd_EnterUsernamePasssword.name} WoW2 {Config.fatmulti2_username} {Config.fatmulti2_password}>
    <{cmd_EnterUsernamePasssword.name} WoW3 {Config.fatmulti3_username} {Config.fatmulti3_password}>
    <{cmd_EnterUsernamePasssword.name} WoW4 {Config.fatmulti4_username} {Config.fatmulti4_password}>
    <{cmd_EnterUsernamePasssword.name} WoW5 {Config.fatmulti5_username} {Config.fatmulti5_password}>
    <{cmd_EnterUsernamePasssword.name} WoW6 {Config.fitsheep_username} {Config.fitsheep_password}>
    <{cmd_EnterUsernamePasssword.name} WoW7 {Config.fatmulti6_username} {Config.fatmulti6_password}>
    <{cmd_EnterUsernamePasssword.name} WoW8 {Config.fatmulti8_username} {Config.fatmulti8_password}>
    <{cmd_EnterUsernamePasssword.name} WoW9 {Config.fatmulti9_username} {Config.fatmulti9_password}>
    <{cmd_EnterUsernamePasssword.name} WoW10 {Config.fatmulti10_username} {Config.fatmulti10_password}>
    <{cmd_EnterUsernamePasssword.name} WoW11 {Config.fatmulti11_username} {Config.fatmulti11_password}>
    <{cmd_EnterUsernamePasssword.name} WoW12 {Config.fatmulti12_username} {Config.fatmulti12_password}>
    <{cmd_EnterUsernamePasssword.name} WoW13 {Config.fatmulti13_username} {Config.fatmulti13_password}>
    <{cmd_EnterUsernamePasssword.name} WoW14 {Config.fatmulti14_username} {Config.fatmulti14_password}>
    <{cmd_EnterUsernamePasssword.name} WoW15 {Config.fatmulti15_username} {Config.fatmulti15_password}>
    <{cmd_EnterUsernamePasssword.name} WoW16 {Config.fatmulti16_username} {Config.fatmulti16_password}>
    <{cmd_EnterUsernamePasssword.name} WoW17 {Config.fatmulti17_username} {Config.fatmulti17_password}>
    <{cmd_EnterUsernamePasssword.name} WoW18 {Config.fatmulti18_username} {Config.fatmulti18_password}>
    <Restore>
"""

cmd_BatchLoginFatmulti1To18 = Command(
    name="BatchLoginFatmulti1To18",
    content=_cmd_BatchLoginFatmulti1To18_tpl,
)

_cmd_BatchLoginFatmulti1To5_tpl = f"""
    <Wait 3000> // 等待一段时间
    <{cmd_EnterUsernamePasssword.name} WoW1 {Config.fatmulti1_username} {Config.fatmulti1_password}>
    <{cmd_EnterUsernamePasssword.name} WoW2 {Config.fatmulti2_username} {Config.fatmulti2_password}>
    <{cmd_EnterUsernamePasssword.name} WoW3 {Config.fatmulti3_username} {Config.fatmulti3_password}>
    <{cmd_EnterUsernamePasssword.name} WoW4 {Config.fatmulti4_username} {Config.fatmulti4_password}>
    <{cmd_EnterUsernamePasssword.name} WoW5 {Config.fatmulti5_username} {Config.fatmulti5_password}>
    <Restore>
"""

cmd_BatchLoginFatmulti1To5 = Command(
    name="BatchLoginFatmulti1To5",
    content=_cmd_BatchLoginFatmulti1To5_tpl,
)

_cmd_BatchLoginFatmulti6To10_tpl = f"""
    <Wait 3000> // 等待一段时间
    <{cmd_EnterUsernamePasssword.name} WoW6 {Config.fitsheep_username} {Config.fitsheep_password}>
    <{cmd_EnterUsernamePasssword.name} WoW7 {Config.fatmulti6_username} {Config.fatmulti6_password}>
    <{cmd_EnterUsernamePasssword.name} WoW8 {Config.fatmulti8_username} {Config.fatmulti8_password}>
    <{cmd_EnterUsernamePasssword.name} WoW9 {Config.fatmulti9_username} {Config.fatmulti9_password}>
    <{cmd_EnterUsernamePasssword.name} WoW10 {Config.fatmulti10_username} {Config.fatmulti10_password}>
    <Restore>
"""

cmd_BatchLoginFatmulti6To10 = Command(
    name="BatchLoginFatmulti6To10",
    content=_cmd_BatchLoginFatmulti6To10_tpl,
)

_cmd_BatchLoginFatmulti1To10_tpl = f"""
    <Wait 3000> // 等待一段时间
    <{cmd_EnterUsernamePasssword.name} WoW1 {Config.fatmulti1_username} {Config.fatmulti1_password}>
    <{cmd_EnterUsernamePasssword.name} WoW2 {Config.fatmulti2_username} {Config.fatmulti2_password}>
    <{cmd_EnterUsernamePasssword.name} WoW3 {Config.fatmulti3_username} {Config.fatmulti3_password}>
    <{cmd_EnterUsernamePasssword.name} WoW4 {Config.fatmulti4_username} {Config.fatmulti4_password}>
    <{cmd_EnterUsernamePasssword.name} WoW5 {Config.fatmulti5_username} {Config.fatmulti5_password}>
    <{cmd_EnterUsernamePasssword.name} WoW6 {Config.fitsheep_username} {Config.fitsheep_password}>
    <{cmd_EnterUsernamePasssword.name} WoW7 {Config.fatmulti6_username} {Config.fatmulti6_password}>
    <{cmd_EnterUsernamePasssword.name} WoW8 {Config.fatmulti8_username} {Config.fatmulti8_password}>
    <{cmd_EnterUsernamePasssword.name} WoW9 {Config.fatmulti9_username} {Config.fatmulti9_password}>
    <{cmd_EnterUsernamePasssword.name} WoW10 {Config.fatmulti10_username} {Config.fatmulti10_password}>
    <Restore>
"""

cmd_BatchLoginFatmulti1To10 = Command(
    name="BatchLoginFatmulti1To10",
    content=_cmd_BatchLoginFatmulti1To10_tpl,
)

_cmd_BatchLogin10DruidPvP_tpl = f"""
    <Wait 3000> // 等待一段时间
    <{cmd_EnterUsernamePasssword.name} WoW3 {Config.fatmulti3_username} {Config.fatmulti3_password}>
    <{cmd_EnterUsernamePasssword.name} WoW8 {Config.fatmulti8_username} {Config.fatmulti8_password}>
    <{cmd_EnterUsernamePasssword.name} WoW11 {Config.fatmulti11_username} {Config.fatmulti11_password}>
    <{cmd_EnterUsernamePasssword.name} WoW12 {Config.fatmulti12_username} {Config.fatmulti12_password}>
    <{cmd_EnterUsernamePasssword.name} WoW13 {Config.fatmulti13_username} {Config.fatmulti13_password}>
    <{cmd_EnterUsernamePasssword.name} WoW14 {Config.fatmulti14_username} {Config.fatmulti14_password}>
    <{cmd_EnterUsernamePasssword.name} WoW15 {Config.fatmulti15_username} {Config.fatmulti15_password}>
    <{cmd_EnterUsernamePasssword.name} WoW16 {Config.fatmulti16_username} {Config.fatmulti16_password}>
    <{cmd_EnterUsernamePasssword.name} WoW17 {Config.fatmulti17_username} {Config.fatmulti17_password}>
    <{cmd_EnterUsernamePasssword.name} WoW18 {Config.fatmulti18_username} {Config.fatmulti18_password}>
    <Restore>
"""

cmd_BatchLogin10DruidPvP_tpl = Command(
    name="BatchLogin10DruidPvP",
    content=_cmd_BatchLogin10DruidPvP_tpl,
)

cmd_BatchLogin = None  # type: Command


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
def create_base_script() -> Script:
    script = Script()

    script.add_command(cmd_LaunchAndRename)
    script.add_command(cmd_LaunchAndRenameGameClientWindow)
    script.add_command(cmd_BringToForeground)

    script.add_command(cmd_EnterUsernamePasssword)
    script.add_command(cmd_BatchLogin)

    # --- HOTKEY ---
    hk_LaunchAndRenameGameClientWindow = Hotkey(
        name="LaunchAndRenameGameClientWindow",
        key=keyname.SCROLOCK_ON(keyname.CTRL_ALT_(keyname.S)),
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

    hk_BatchLogin = Hotkey(
        name="BatchLogin",
        key=keyname.SCROLOCK_ON(keyname.CTRL_ALT_(keyname.L)),
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
