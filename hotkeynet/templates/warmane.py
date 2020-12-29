# -*- coding: utf-8 -*-

from ..script import Script, Command, Hotkey, render_template
from .. import keyname

# Use Monkey Patch to replace this value
WOW_EXE_PATH = r"D:\HSH\Games\WOW Private\Client\World of Warcraft 3.3.5 enUS (Warman wod models)\Wow.exe"

cmd_LaunchAndRename = Command(
    name="LaunchAndRename",
    content=f"""
        <SendPC %1%>
            <Run "{WOW_EXE_PATH}">
                <RenameWin "World of Warcraft" %2%>
    """
)

# 注意!!! 在 HotketNet 界面菜单上的 Options -> Settings 中有一项
# Window name match 一定要勾选 Exact Match. 如果勾选的是 Partial Match,
# 则你在调用 WoW1 窗口的时候, 由于是用的部分匹配, WoW10 也会被匹配到,
# 导致你的 WoW1 和 WoW10 无法被区分开来.
cmd_LaunchAndRenameWoW1ToWoW10 = Command(
    name="LaunchAndRenameWoW1ToWoW10",
    content=render_template("""
        {%- for i in range(1, 10+1) %}
        {{ cmd.call("Local", "WoW" + i|string) }}
        {%- endfor %}
    """.strip(), cmd=cmd_LaunchAndRename)
)


cmd_LaunchAndRenameWoW1ToWoW18 = Command(
    name="LaunchAndRenameWoW1ToWoW18",
    content=render_template("""
        {%- for i in range(1, 18+1) %}
        {{ cmd.call("Local", "WoW" + i|string) }}
        {%- endfor %}
    """.strip(), cmd=cmd_LaunchAndRename)
)


cmd_EnterUsernamePasssword = Command(
    name="EnterUsernamePasssword",
    content="""
    <Command CommandEnterUsernamePassword>
        <SendPC Local>
            <SendWin %1%>
                // Wait to bring window foreground; 等待将窗口带到最前端
                <Wait 500>
                // Click OK on Wrong Pass Word Pop Out; 清除可能的密码错误窗口, 移除遮挡
                <ClickMouse LButton Both Window 890 565 NoRestore>
                <Wait 300>
                // Click on username Input Box; 在用户名输入框点击左键
                <ClickMouse LButton Both Window 900 505 NoRestore>
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
        wrong_password_pop_up_x
    )
)
"""

"""