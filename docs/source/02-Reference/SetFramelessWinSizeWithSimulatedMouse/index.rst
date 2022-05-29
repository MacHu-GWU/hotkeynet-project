.. _SetFramelessWinSizeWithSimulatedMouse:

SetFramelessWinSizeWithSimulatedMouse
==============================================================================
Changes the size of the currently targeted window. This command is rarely needed. See remarks.

**Syntax**:

    <SetFramelessWinSizeWithSimulatedMouse x y [delay]>

**Parameters**

    X is the horizontal size in pixels.

    Y is the vertical size in pixels.

    Delay is an optional number. If given, it specifes the length of a delay in milliseconds.

**Remarks**

    Normally you should use SetWinSize or SetWinRect instead of this command to change a window's size.

    This command is designed to be used only when both of the following circumstances exist:

    1. The target is a program like Aion that requires resizing to be done with a mouse, and

    2. The target's window is frameless.

    If 1 is true but the window has a frame, use SetWinSize or SetWinRect with "SimMouse."

    This command doesn't work perfectly yet (the frame isn't always removed at the end.) Specifying a delay of around 55 seems to help on my test PC.

    This command changes the size of the window that was targeted with TargetWin, TargetChild, SendWin, etc.

    Note to Aion players

    Aion doesn't allow its client area to be made smaller than 800 x 600. Because of the way this command works, the minimum size you can specify is around 816 x 636 (the size of an 800 x 600 client area enclosed in a window frame with a caption). Smaller sizes will cause Aion to redraw itself improperly.

**Example**::

    <Hotkey F1>
    <TargetWin AION>
    <SetFramelessWinSizeWithSimulatedMouse 900 700 55>

**Related topics**

    - :ref:`SetWinPos`
    - :ref:`SetWinRect`
    - :ref:`SetWinSize`
