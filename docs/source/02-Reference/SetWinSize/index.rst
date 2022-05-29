.. _SetWinSize:

SetWinSize
==============================================================================
Changes the size of the currently targeted window.

**Syntax**::

    <SetWinSize x y [SimMouse]>

**Parameters**

    X is the horizontal size in pixels.

    Y is the vertical size in pixels.

    SimMouse is the optional word "SimMouse." See remarks.

**Remarks**

    This command changes the size of the window that was targeted with :ref:`TargetWin`, :ref:`TargetChild`, :ref:`SendWin`, etc.

    It calls the operating system command MoveWindow.

    If you add the word SimMouse, HotkeyNet makes the target program think a mouse was used to set the new size. This is useful for Aion.

    Note: SimMouse only works if the window has a resizing frame. If the window frame has been removed, use SetFramelessWinSizeWithSimulatedMouse.

**Example**::

    <Hotkey F1>
        <TargetWin wow1>
        <SetWinSize 500 700>

**Related topics**

    - :ref:`SetFramelessWinSizeWithSimulatedMouse`
    - :ref:`SetWinPos`
    - :ref:`SetWinRect`
