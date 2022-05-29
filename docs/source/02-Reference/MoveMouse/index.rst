.. _MoveMouse:

MoveMouse
==============================================================================
Many thanks to Binaryzero for suggesting this command.

Moves the mouse cursor to the specified location.

**Syntax**

    <MoveMouse x y [target]>

**Parameters**

    - X is the horizontal coordinate in pixels.
    - Y is the vertical coordinate in pixels.
    - Target is optional. It can be screen or window.

**Remarks**

    If you specify screen, the location is relative to the upper left corner of the screen. If you specify window, it's relative to the client area of the currently targeted window. If you specify neither, the default is window.

**Example**

    The following hotkey moves the mouse cursor to a point that's 100 pixels from the left and upper edges of the screen on a remote PC::

        <Hotkey F1>
            <SendPC 192.168.1.105>
            <MoveMouse screen 100 100>

    The following hotkey does the same thing except the point is 100 pixels from the left and upper edges of the client area of a particular window::

        <Hotkey F1>
            <SendPC 192.168.1.105>
            <TargetWin WoW1>
            <MoveMouse 100 100>

**Related topics**

- :ref:`ClickMouse`
- :ref:`MoveMouse`
- :ref:`RestoreMousePos`
- :ref:`SaveMousePos`
