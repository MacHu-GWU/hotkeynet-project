.. _SetWinRegion:

SetWinRegion
==============================================================================
Makes a transparent hole in the currently targeted window.

**Syntax**::

    <SetWinRegion x y width height>

    or

    <SetWinRegion none>

**Parameters**

    X is the horizontal coordinate of the upper left corner of the hole.

    Y is the vertical coordinate of the upper left corner of the hole.

    Width is the width of the hole.

    Height is the height of the hole.

    None indicates that the window should be restored to normal.

**Remarks**

    You can make several holes in a window by repeating this command with different numbers.

    The upper left corner's coordinates are relative to the window as a whole, not the window's client area.

    The hole is made in the window that was targeted with TargetWin, SendWin, etc.

**Example**

    The following hotkey makes a hole in a window called WoW. The left edge of the hole is 100 pixels from the left edge of the window. The top of the hole is 200 pixels below the top of the window. The hole is 300 pixels wide and 400 pixels high::

        <Hotkey F1>
            <TargetWin WoW>
            <SetWinRegion 100 200 300 400>

    The following hotkey restores the window to normal::

        <Hotkey F2>
            <TargetWin WoW>
            <SetWinRegion none>
