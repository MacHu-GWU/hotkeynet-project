
<Command LaunchAndRename>

    <SendPC %1%>
        <Run "D:\HSH\Games\WOW Private\Client\World of Warcraft 3.3.5 enUS (Warman wod models)\Wow.exe">
            <RenameWin "World of Warcraft" %2%>


<Command LaunchAndRenameWoW1ToWoW5>

    <LaunchAndRename Local WoW1>
    <LaunchAndRename Local WoW2>
    <LaunchAndRename Local WoW3>
    <LaunchAndRename Local WoW4>
    <LaunchAndRename Local WoW5>

<Command EnterUsernamePasssword>

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




<Hotkey ScrollLockOn Ctrl Alt S>
    <LaunchAndRenameWoW1ToWoW5>
