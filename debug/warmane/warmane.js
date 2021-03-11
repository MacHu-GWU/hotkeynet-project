
<Command LaunchAndRenameGameClient>
    <SendPC %1%>
        <Run "D:\HSH\Games\WOW Private\Client\World of Warcraft 3.3.5 enUS (Warman wod models)\Wow.exe">
        <RenameWin "World of Warcraft" %2%>

<Command LaunchAndRenameAllGameClient>
    <LaunchAndRenameGameClient Local WoW1>
    <LaunchAndRenameGameClient Local WoW2>
    <LaunchAndRenameGameClient Local WoW3>
    <LaunchAndRenameGameClient Local WoW4>
    <LaunchAndRenameGameClient Local WoW5>
    <LaunchAndRenameGameClient Local WoW6>
    <LaunchAndRenameGameClient Local WoW7>
    <LaunchAndRenameGameClient Local WoW8>
    <LaunchAndRenameGameClient Local WoW9>
    <LaunchAndRenameGameClient Local WoW10>

<Command BringWindowToForeground>
    <SendPC Local>
        <TargetWin %1%>
            <Wait 50>
            <SetForegroundWin> // This command response fast
            // <SetActiveWin> // This command cause big delay

<Command ResizeAndRelocateWindow>
    <SendPC Local>
        <Wait 50>
        <SendWinM %1%>
            <SetWinRect None None 1800 1012>

<Command CenterOverlapLayout>
    <ResizeAndRelocateWindow WoW1>
    <ResizeAndRelocateWindow WoW2>
    <ResizeAndRelocateWindow WoW3>
    <ResizeAndRelocateWindow WoW4>
    <ResizeAndRelocateWindow WoW5>
    <ResizeAndRelocateWindow WoW6>
    <ResizeAndRelocateWindow WoW7>
    <ResizeAndRelocateWindow WoW8>
    <ResizeAndRelocateWindow WoW9>
    <ResizeAndRelocateWindow WoW10>

<Command EnterUsernameAndPasssword>
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

<Command BatchLogin>
    <Wait 3000> // 等待一段时间, 让你有时间将错误的输入法切换对
    <EnterUsernameAndPasssword WoW1 fatmulti1 H43AvmJQoDM8>
    <EnterUsernameAndPasssword WoW2 fatmulti2 VAv4r7kztbX1>
    <EnterUsernameAndPasssword WoW3 fatmulti3 x58WPe9Lv2gI>
    <EnterUsernameAndPasssword WoW4 fatmulti4 ya6zCfKH9l8s>
    <EnterUsernameAndPasssword WoW5 fatmulti5 z4TGRy1PuuCY>
    <EnterUsernameAndPasssword WoW6 fitsheep K90vmRf7XFez>
    <EnterUsernameAndPasssword WoW7 fatmulti6 R5bsm86gy9q4>
    <EnterUsernameAndPasssword WoW8 fatmulti8 rKC165sVp8FP>
    <EnterUsernameAndPasssword WoW9 fatmulti9 gtx1b4Ecf9Jz>
    <EnterUsernameAndPasssword WoW10 monkey130 sunna521.ss>
    <Restore>


// HotkeyNet 中有两个命令可以发送键盘鼠标按键到窗口,
// 一个是 SendWin (或是 SendWinM 等) 系列, 一个是 SendLabel.
// SendWin 需要将该窗口放到最前端, 这个动作需要时间, 并不适合对后台窗口进行操作.
// 而 SendLabel 则是一个异步操作, 只是将命令发送到后台窗口执行.
// 我们后面的多开同步操作主要是通过 SendLabel 实现的. 所以我们需要先对其进行定义.
<Label w1 Local SendWinM WoW1>

<Label w2 Local SendWinM WoW2>

<Label w3 Local SendWinM WoW3>

<Label w4 Local SendWinM WoW4>

<Label w5 Local SendWinM WoW5>

<Label w6 Local SendWinM WoW6>

<Label w7 Local SendWinM WoW7>

<Label w8 Local SendWinM WoW8>

<Label w9 Local SendWinM WoW9>

<Label w10 Local SendWinM WoW10>
