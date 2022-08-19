.. _AlwaysOnTop:

AlwaysOnTop
==============================================================================
Makes the currently targeted window stay on top even when a different window has the focus.

**Syntax**

::

    <AlwaysOnTop arg>

**Parameters**

    - Arg can be either "on" or "off."
    - Use "on" to make the window stay on top. Use "off" to make the window return to normal.

**Remarks**

    AlwaysOnTop affects the window that was targeted with TargetWin, TargetChild, SendWin, etc.

**Buttons**

    Buttons must be targeted with TargetButton before using AlwaysOnTop with them. See the third example below.

**Examples**

    This hotkey makes a window called "WOW1" always stay on top::

        <Hotkey F1>
            <SendPC local>
            <TargetWin WOW1>
            <AlwaysOnTop on>

    This hotkey returns that window to normal::

        <Hotkey F2>
            <SendPC local>
            <TargetWin WOW1>
            <AlwaysOnTop off>

    This hotkey makes a button always stay on top::

        <Hotkey F2>
            <TargetButton Button1>
            <AlwaysOnTop on>
