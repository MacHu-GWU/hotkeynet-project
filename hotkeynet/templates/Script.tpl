{% for command in script.commands.values() %}
{{ command.dump() }}
{% endfor %}

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
<Label w11 Local SendWinM WoW11>
<Label w12 Local SendWinM WoW12>
<Label w13 Local SendWinM WoW13>
<Label w14 Local SendWinM WoW14>
<Label w15 Local SendWinM WoW15>
<Label w16 Local SendWinM WoW16>
<Label w17 Local SendWinM WoW17>
<Label w18 Local SendWinM WoW18>

{% for hotkey in script.hotkeys.values() %}
{{ hotkey.dump() }}
{% endfor %}
