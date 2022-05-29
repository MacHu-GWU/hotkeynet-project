.. _SetWinPos:

SetWinPos
==============================================================================
Moves the currently targeted window to a new location.

**Syntax**::

    <SetWinPos x y>

**Parameters**

    X is the horizontal screen coordinate in pixels.

    Y is the vertical screen coordinate in pixels.

**Remarks**

    This command changes the position of the window that was targeted with TargetWin, TargetChild, SendWin, etc.

    It calls the operating system command MoveWindow.

**Example**::

    <Hotkey F1>
        <TargetWin wow1>
        <SetWinPos 500 700>

**Related topics**

    - :ref:`SetWinRect`
    - :ref:`SetWinSize`
