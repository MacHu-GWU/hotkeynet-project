使用 Python 编写 HotkeyNet 脚本
==============================================================================
本项目 ``hotkeynet`` 是一个 Python 库. 和其他 Python 库一样, 都需要 import 后再使用. 其中所有稳定的 API 都位于 ``hotkeynet.api`` 这一模块下. 在使用的时候请不要手动 import 其他模块里的东西. 没有在 ``hotkeynet.api`` 模块下的东西都是不稳定的, 随时可能改变.

下面是一段用 Python 来写 Hotkeynet 脚本的示例代码:

.. code-block:: python

    from hotkeynet import api
    from hotkeynet.api import KN, CAN

    with api.Script() as script:
        api.Label(name="w1", window="WoW1")
        api.Label(name="w2", window="WoW2")

        with api.Command(
            name="LaunchAndRenameGameClient",
        ) as cmd_launch_and_rename_game_client:
            with api.SendPC():
                api.Run.make("C:\\Program Files (x86)\\World of Warcraft\\Wow.exe")
                api.RenameWin(old="WoW", new=api.CommandArgEnum.Arg1)

        with api.Hotkey(key=api.KN.KEY_1) as hk_1:
            with api.SendLabel(to=["w1", "w2"]):
                api.CAN.KEY_1()

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
