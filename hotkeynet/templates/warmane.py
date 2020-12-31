# -*- coding: utf-8 -*-

from ..script import Script, Command, Hotkey, render_template
from .. import keyname

# Use Monkey Patch to replace this value
WOW_EXE_PATH = r"D:\HSH\Games\WOW Private\Client\World of Warcraft 3.3.5 enUS (Warman wod models)\Wow.exe"
WRONG_PASSWORD_POP_UP_X_AT_1920_1080 = 890
WRONG_PASSWORD_POP_UP_Y_AT_1920_1080 = 565
WRONG_PASSWORD_POP_UP_X_AT_1600_900 = 792
WRONG_PASSWORD_POP_UP_Y_AT_1600_900 = 502
USERNAME_INPUT_BOX_X_AT_1920_1080 = 900
USERNAME_INPUT_BOX_Y_AT_1920_1080 = 505
USERNAME_INPUT_BOX_X_AT_1600_900 = 788
USERNAME_INPUT_BOX_Y_AT_1600_900 = 451

wrong_password_pop_up_x = WRONG_PASSWORD_POP_UP_X_AT_1600_900
wrong_password_pop_up_y = WRONG_PASSWORD_POP_UP_Y_AT_1600_900
username_input_box_x = USERNAME_INPUT_BOX_X_AT_1600_900
username_input_box_y = USERNAME_INPUT_BOX_Y_AT_1600_900

script = Script()

_cmd_LaunchAndRename_tpl = f"""
    <SendPC %1%>
        <Run "{WOW_EXE_PATH}">
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
    wrong_password_pop_up_x=wrong_password_pop_up_x,
    wrong_password_pop_up_y=wrong_password_pop_up_y,
    username_input_box_x=username_input_box_x,
    username_input_box_y=username_input_box_y,
)

cmd_EnterUsernamePasssword = Command(
    name="EnterUsernamePasssword",
    content=_cmd_EnterUsernamePasssword_tpl,
)


hk_LaunchAndRenameGameClientWindow = Hotkey(
    name="LaunchAndRenameGameClientWindow",

)