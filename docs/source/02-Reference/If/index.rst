.. _If:

If
==============================================================================
Many thanks to FuzzyBoy and Olipcs for their suggestions.

Tests a condition and performs your instructions only if the condition is true.

**Syntax**::

    <If condition arguments>

          or

    <If variable Is value>

          or

    <If variable IsNot value>

**Parameters**

    Condition and arguments can be one of the following.

    ``ActiveWinIs`` Name
    ``ActiveWinIsNot`` Name
    ``HotkeysAreOn``
    ``HotkeysAreOff``
    ``WinExists`` Name
    ``WinDoesNotExist`` Name
    ``MouseIsOverWindow`` Name
    ``MouseIsNotOverWindow`` Name
    ``MouseIsOverWindowRect`` Name PosX PosY Width Height
    ``MouseIsNotOverWindowRect`` Name PosX PosY Width Height
    ``MouseIsOverScreenRect`` PosX PosY Width Height
    ``MouseIsNotOverScreenRect`` PosX PosY Width Height
    ``WinPosIs`` Name PosX PosY
    ``WinPosIsNot`` Name PosX PosY
    ``WinSizeIs`` Name Width Height
    ``WinSizeIsNot`` Name Width Height
    ``WinRectIs`` Name PosX PosY Width Height
    ``WinRectIsNot`` Name PosX PosY Width Height

    Name is the name of a window. As always with HotkeyNet, window names are case-sensitive. You can truncate window names if "Partial match" is checked on the Settings Panel.

    Variable is the name of a variable that has been created with SetVar.

    Value is the value of a variable that has been set with SetVar.

    PosX and PosY are the x and y-coordinates of the upper left corner of a rectangle. If the rectangle is relative to a window, it's specified in client pixels; if relative to the screen, in screen pixels.

    Width and Height are dimensions of a rectangle in pixels.

**Mouse stuff**

    Instead of using conditions like MouseIsOverWindowRect, it may be more convenient to create buttons.

**Remarks**

    The condition is tested only on the local PC (the one where you press the hotkey).

    If-blocks always nest inside Toggle-blocks. You can see how HotkeyNet interprets nesting of your definitions by pressing "Show loaded hotkeys."

    It isn't necessary to write EndIf unless you want to add instructions that should always execute after an If-block, like in the second example below.

**Limitations**

    If-blocks cannot be used in commands. If you If you need to put If-blocks inside a subroutine, make a hotkey that will be used as a subroutine and call it with DoHotkey.

    If-blocks cannot nest inside other If-blocks. You can work around this limitation by putting the controlled block of the outer If-statement in a separate hotkey and calling that hotkey with DoHotkey.

**Example**

::

    <Hotkey F1>
        <If ActiveWinIs wow1>
            <SendLabel w1>
            <Key 1>
        <Else If ActiveWinIs wow2>
            <Sendlabel w2>
            <Key 2>
        <Else>
            <SendFocusWin>
            <Key %Trigger%>

The following example shows a case where EndIf is needed::

    <Hotkey F1>
        <If ActiveWinIs wow1>
            <SendLabel w1>
            <Key 1>
        <EndIf>
        <SendFocusWin> // THIS WILL ALWAYS EXECUTE
        <Text burp>

Related topics

    Else
    EndIf
