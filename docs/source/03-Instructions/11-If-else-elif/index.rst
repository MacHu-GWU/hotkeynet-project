.. _11-If–Else–EndIf:

11. If–Else–EndIf
==============================================================================
Sometimes you want a hotkey to do things only when you're working with a particular window. For example, here's a hotkey that types "hi", but only when you're working with a window called w1::

    <Hotkey F1>
        <If ActiveWinIs w1>
            <SendLabel w1>
            <Text hi>

This example is a little too simple because if you're working with some other window, you want F1 (the trigger key) to be seen by the other window like it would if the hotkey wasn't defined. To make that happen we need to add an Else block::

    <Hotkey F1>
        <If ActiveWinIs w1>
            <SendLabel w1>
            <Text hi>
        <Else>
            <SendFocusWin>
            <Key %Trigger%>

You can have more than one If-block. For example, let's add a few more lines so the hotkey types "bye" if you're working with a second window named w2::

    <Hotkey F1>
        <If ActiveWinIs w1>
            <SendLabel w1>
            <Text hi>
        <Else If ActiveWinIs w2>
            <SendLabel w1>
            <Text bye>
        <Else>
            <SendFocusWin>
            <Key %Trigger%>

All these examples used ActiveWinIs to check which window you're working with. But there are many other conditions that you can check for. To see a complete list, go here.

Some technical notes:

    The condition is tested only on the local PC (the one where you press the hotkey).

    If-blocks always nest inside Toggle-blocks. You can see how HotkeyNet interprets nesting of your definitions by pressing "Show loaded hotkeys."

    With the current version of the program, you can't nest If-blocks inside other If-blocks.

    If, Else, and EndIf can be used only in hotkeys, not commands. If you need to put them in a subroutine, you can use a hotkey as a subroutine in place of a command. Call the hotkey with DoHotkey.

    It isn't necessary to write EndIf unless you want to add instructions that should always execute after an If-block.

Related topics

Else
EndIf
If
