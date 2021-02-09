{%- for command in script.commands.values() %}
{{ command.dump() }}
{% endfor %}

// HotkeyNet 中有两个命令可以发送键盘鼠标按键到窗口,
// 一个是 SendWin (或是 SendWinM 等) 系列, 一个是 SendLabel.
// SendWin 需要将该窗口放到最前端, 这个动作需要时间, 并不适合对后台窗口进行操作.
// 而 SendLabel 则是一个异步操作, 只是将命令发送到后台窗口执行.
// 我们后面的多开同步操作主要是通过 SendLabel 实现的. 所以我们需要先对其进行定义.
{%- for label, window in script.labels.items() %}
<Label {{ label }} Local SendWinM {{ window }}>
{% endfor %}

{%- for hotkey in script.hotkeys.values() %}
{{ hotkey.dump() }}
{% endfor %}
