# -*- coding: utf-8 -*-

from ..script import (
    Script, Command, Hotkey,
    Action, Key, Mouse, SendLabel, CallCommand,
)
from ..utils import render_template
from .. import keyname
from .warmane_config import Config


_cmd_LaunchAndRename_tpl = f"""
    <SendPC %1%>
        <Run "{Config.WOW_EXE_PATH}">
            <RenameWin "World of Warcraft" %2%>
"""

cmd_LaunchAndRename = Command(
    name="LaunchAndRename",
    content=_cmd_LaunchAndRename_tpl,
)

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

cmd_LaunchAndRenameGameClientWindow = None # type: Command


_cmd_BatchLoginFatmulti1To5_tpl = f"""
    <Wait 3000> // 等待一段时间
    <{cmd_EnterUsernamePasssword} WoW1 {config.fatmulti1_username} {config.fatmulti1_password}>
    <{cmd_EnterUsernamePasssword} WoW2 {config.fatmulti2_username} {config.fatmulti2_password}>
    <{cmd_EnterUsernamePasssword} WoW3 {config.fatmulti3_username} {config.fatmulti3_password}>
    <{cmd_EnterUsernamePasssword} WoW4 {config.fatmulti4_username} {config.fatmulti4_password}>
    <{cmd_EnterUsernamePasssword} WoW5 {config.fatmulti5_username} {config.fatmulti5_password}>
    <{cmd_EnterUsernamePasssword} WoW6 {config.fitsheep_username} {config.fitsheep_password}>
    <{cmd_EnterUsernamePasssword} WoW7 {config.fatmulti6_username} {config.fatmulti6_password}>
    <{cmd_EnterUsernamePasssword} WoW8 {config.fatmulti8_username} {config.fatmulti8_password}>
    <{cmd_EnterUsernamePasssword} WoW9 {config.fatmulti9_username} {config.fatmulti9_password}>
    <{cmd_EnterUsernamePasssword} WoW10 {config.fatmulti10_username} {config.fatmulti10_password}>
    <{cmd_EnterUsernamePasssword} WoW11 {config.fatmulti11_username} {config.fatmulti11_password}>
    <{cmd_EnterUsernamePasssword} WoW12 {config.fatmulti12_username} {config.fatmulti12_password}>
    <{cmd_EnterUsernamePasssword} WoW13 {config.fatmulti13_username} {config.fatmulti13_password}>
    <{cmd_EnterUsernamePasssword} WoW14 {config.fatmulti14_username} {config.fatmulti14_password}>
    <{cmd_EnterUsernamePasssword} WoW15 {config.fatmulti15_username} {config.fatmulti15_password}>
    <{cmd_EnterUsernamePasssword} WoW16 {config.fatmulti16_username} {config.fatmulti16_password}>
    <{cmd_EnterUsernamePasssword} WoW17 {config.fatmulti17_username} {config.fatmulti17_password}>
    <{cmd_EnterUsernamePasssword} WoW18 {config.fatmulti18_username} {config.fatmulti18_password}>
    <Restore>
"""

cmd_BatchLoginFatmulti1To5 = Command(

)


cmd_BatchLogin = None # type: Command



def create_base_script() -> Script:
    script = Script()

    script.add_command(cmd_LaunchAndRename)
    script.add_command(cmd_LaunchAndRenameGameClientWindow)
    script.add_command(cmd_EnterUsernamePasssword)

    #--- hotkey
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
    return script