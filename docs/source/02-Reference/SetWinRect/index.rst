.. _SetWinRect:

SetWinRect
==============================================================================
Moves the currently targeted window to a new location and changes its size.

**Syntax**::

    <SetWinRect x y width height [SimMouse]>

**Parameters**

    X is the horizontal screen coordinate of the window's upper left corner.

    Y is the vertical screen coordinate of the window's upper left corner.

    Width is the window's width.

    Height is the window's height.

    SimMouse is the optional word "SimMouse." See remarks.

**Remarks**

    This command affects the window that was targeted with :ref:`TargetWin`, :ref:`TargetChild`, :ref:`SendWin`, etc.

    It calls the operating system command MoveWindow.

    If you add the word SimMouse, HotkeyNet makes the target program think a mouse was used to set the new size. This is useful for Aion.

    Note: SimMouse only works if the window has a resizing frame. If the window frame has been removed, use SetFramelessWinSizeWithSimulatedMouse.

**Example**::

    <Hotkey F1>
        <TargetWin wow1>
        <SetWinRect 100 100 500 700>

**Related topics**

    - :ref:`SetFramelessWinSizeWithSimulatedMouse`
    - :ref:`SetWinPos`
    - :ref:`SetWinSize`
