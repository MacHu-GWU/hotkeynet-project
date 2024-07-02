使用 Python 编写 HotkeyNet 脚本
==============================================================================


Quick Start
------------------------------------------------------------------------------
本项目 ``hotkeynet`` 是一个 Python 库. 和其他 Python 库一样, 都需要 import 后再使用. 其中所有稳定的 API 都位于 ``hotkeynet.api`` 这一模块下. 在使用的时候请不要手动 import 其他模块里的东西. 没有在 ``hotkeynet.api`` 模块下的东西都是不稳定的, 随时可能改变.

下面是一段用 Python 来写 Hotkeynet 脚本的示例代码:

.. code-block:: python

    import hotkeynet.api as hk
    from hotkeynet.api import KN, CAN

    with hk.Script() as script:
        hk.Label(name="w1", window="WoW1")
        hk.Label(name="w2", window="WoW2")

        with hk.Command(
            name="LaunchAndRenameGameClient",
        ) as cmd_launch_and_rename_game_client:
            with hk.SendPC():
                hk.Run.make("C:\\Program Files (x86)\\World of Warcraft\\Wow.exe")
                hk.RenameWin(old="WoW", new=hk.CommandArgEnum.Arg1)

        with hk.Hotkey(key=hk.KN.KEY_1) as hk_1:
            with hk.SendLabel(to=["w1", "w2"]):
                hk.CAN.KEY_1()

    script.render()

Generated Hotkeynet Script::

    <Label w1 local SendWinM WoW1>
    <Label w2 local SendWinM WoW2>

    <Command LaunchAndRenameGameClient>
        <SendPC local>
            <Run "C:\Program Files (x86)\World of Warcraft\Wow.exe">
            <RenameWin WoW %1%>

    <Hotkey 1>
        <SendLabel w1, w2>
            <Key 1>


Important Public API
------------------------------------------------------------------------------
- :mod:`hotkeynet.api.KN <hotkeynet.keyname>`: 对所有的 Hotkeynet 脚本中的 Key name 的枚举. 你可以用 ``KN.KEY_1`` 这样的形式来引用这些 Key name.

.. dropdown:: 所有的 Key enum 列表

    .. literalinclude:: ../../../../hotkeynet/keyname.py
       :language: python
       :linenos:

- :class:`hotkeynet.api.Key <hotkeynet.script.Key>`: 用来创建一个 Key 对象, 最终会在脚本中生成一个 XML Tag.
- :class:`hotkeynet.api.ClickMouse <hotkeynet.script.ClickMouse>`: 用来创建一个 ClickMouse 对象, 最终会在脚本中生成一个 XML Tag.
- :class:`hotkeynet.api.KeyMaker <hotkeynet.maker.KeyMaker>`: 一个用来创建 :class:`hotkeynet.api.Key <hotkeynet.script.Key>` 对象的工厂类.
- :class:`hotkeynet.api.ClickMaker <hotkeynet.maker.ClickMaker>`: 一个用来创建 :class:`hotkeynet.api.ClickMouse <hotkeynet.script.ClickMouse>` 对象的工厂类.
- :class:`hotkeynet.api.ModifiedClickMaker <hotkeynet.maker.ModifiedClickMaker>`: 类似上面这个, 但是是 CTRL | ALT | SHIFT + Click.
- :mod:`hotkeynet.api.CAN <hotkeynet.canned>`: :class:`hotkeynet.api.Key <hotkeynet.script.Key>` 和 :class:`hotkeynet.api.ClickMouse <hotkeynet.script.ClickMouse>` 是键盘和鼠标操作的基本单位. 这两个都是对象, 而在 Python 中对象是 mutable 的, 有可能造成一些很难 debug 的问题. 这个模块中枚举了很多 :class:`hotkeynet.api.KeyMaker <hotkeynet.maker.KeyMaker>` 和 :class:`hotkeynet.api.ClickMaker <hotkeynet.maker.ClickMaker>` 对象, 用于快速创建一个新的这些对象.

.. dropdown:: 所有的 CANNED key enum 列表

    .. literalinclude:: ../../../../hotkeynet/canned.py
       :language: python
       :linenos:

- :class:`hotkeynet.api.SendLabel <hotkeynet.script.SendLabel>`: 在脚本中选择将 Key 和 ClickMouse 事件发送到多个窗口, 是脚本中的高频 API 之一.
- :class:`hotkeynet.api.Hotkey <hotkeynet.script.Hotkey>`: 在脚本中定义的快捷键. Hotkey (快捷键) + SendLabel (决定发送到哪些窗口) + Key/ClickMouse (决定发送什么事件) 三者的排列组合就构成了千变万化的键盘鼠标自动化脚本.
- :class:`hotkeynet.api.Script <hotkeynet.script.Script>`: 代表一个完整的 Hotkeynet script 文件, 也是一个其他所有对象的容器.


More Public API
------------------------------------------------------------------------------
- :class:`hotkeynet.api.context <hotkeynet.script.context>`
- :class:`hotkeynet.api.Block <hotkeynet.script.Block>`
- :class:`hotkeynet.api.SendModeEnum <hotkeynet.script.SendModeEnum>`
- :class:`hotkeynet.api.Label <hotkeynet.script.Label>` (常用)
- :class:`hotkeynet.api.Command <hotkeynet.script.Command>` (常用)
- :class:`hotkeynet.api.CommandArgEnum <hotkeynet.script.CommandArgEnum>`
- :class:`hotkeynet.api.CallCommand <hotkeynet.script.CallCommand>` (常用)
- :class:`hotkeynet.api.SendPC <hotkeynet.script.SendPC>` (常用)
- :class:`hotkeynet.api.Run <hotkeynet.script.Run>`
- :class:`hotkeynet.api.MovementHotkey <hotkeynet.script.MovementHotkey>` (常用)
- :class:`hotkeynet.api.KeyUp <hotkeynet.script.KeyUp>` (常用)
- :class:`hotkeynet.api.KeyDown <hotkeynet.script.KeyDown>` (常用)
- :class:`hotkeynet.api.MouseButtonEnum <hotkeynet.script.MouseButtonEnum>`
- :class:`hotkeynet.api.MouseStrokeEnum <hotkeynet.script.MouseStrokeEnum>`
- :class:`hotkeynet.api.MouseTargetEnum <hotkeynet.script.MouseTargetEnum>`
- :class:`hotkeynet.api.MouseModeEnum <hotkeynet.script.MouseModeEnum>`
- :class:`hotkeynet.api.MoveMouse <hotkeynet.script.MoveMouse>` (常用)
- :class:`hotkeynet.api.RenameWin <hotkeynet.script.RenameWin>` (常用)
- :class:`hotkeynet.api.TargetWin <hotkeynet.script.TargetWin>` (常用)
- :class:`hotkeynet.api.Wait <hotkeynet.script.Wait>` (常用)
- :class:`hotkeynet.api.WaitForWin <hotkeynet.script.WaitForWin>`
- :class:`hotkeynet.api.WaitForWinEnabled <hotkeynet.script.WaitForWinEnabled>`
- :class:`hotkeynet.api.SetForegroundWin <hotkeynet.script.SetForegroundWin>`
- :class:`hotkeynet.api.SetActiveWin <hotkeynet.script.SetActiveWin>`
- :class:`hotkeynet.api.Toggle <hotkeynet.script.Toggle>` (常用)
- :class:`hotkeynet.api.ToggleHotkeys <hotkeynet.script.ToggleHotkeys>`
- :class:`hotkeynet.api.ToggleWin <hotkeynet.script.ToggleWin>` (常用)
- :class:`hotkeynet.api.SendWin <hotkeynet.script.SendWin>` (常用)
- :class:`hotkeynet.api.SendWinM <hotkeynet.script.SendWinM>`
- :class:`hotkeynet.api.SendWinMF <hotkeynet.script.SendWinMF>`
- :class:`hotkeynet.api.SendWinS <hotkeynet.script.SendWinS>`
- :class:`hotkeynet.api.SendWinSF <hotkeynet.script.SendWinSF>`
- :class:`hotkeynet.api.SendFocusWin <hotkeynet.script.SendFocusWin>`
- :class:`hotkeynet.api.SetWinPos <hotkeynet.script.SetWinPos>` (常用)
- :class:`hotkeynet.api.SetWinSize <hotkeynet.script.SetWinSize>` (常用)
- :class:`hotkeynet.api.SetWinRect <hotkeynet.script.SetWinRect>` (常用)
- :class:`hotkeynet.api.Text <hotkeynet.script.Text>`
- :class:`hotkeynet.api.CreatePanel <hotkeynet.script.CreatePanel>` (常用)
- :class:`hotkeynet.api.CreateButton <hotkeynet.script.CreateButton>` (常用)
- :class:`hotkeynet.api.CreatePictureButton <hotkeynet.script.CreatePictureButton>`
- :class:`hotkeynet.api.CreateColoredButton <hotkeynet.script.CreateColoredButton>`
- :class:`hotkeynet.api.AddButtonToPanel <hotkeynet.script.AddButtonToPanel>` (常用)
- :class:`hotkeynet.api.SetButtonHotkey <hotkeynet.script.SetButtonHotkey>` (常用)
- :class:`hotkeynet.api.SetButtonCommand <hotkeynet.script.SetButtonCommand>` (常用)
- :class:`hotkeynet.api.AlwaysOnTop <hotkeynet.script.AlwaysOnTop>`
- :class:`hotkeynet.api.SetPanelLayout <hotkeynet.script.SetPanelLayout>`
