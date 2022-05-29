.. _ToggleWin:

ToggleWin
==============================================================================
Each time you press this, the next window on the list is brought to the foreground.

**Syntax**::

    <ToggleWin window1 [window2 [window3 [window4...]]]>

**Parameters**

    The parameters are the names of windows that get toggled.

    You can specify between one and nine windows.

    If only one window is specified, it is always brought to the foreground.

    If none of the listed windows is in the foreground, the first window on the list is brought to the foreground.

**Example**::

    <hotkey F1>
        <SendPC local>
        <ToggleWin Uber1 Uber2 Uber3>

**Related topics**

    - :ref:`ToggleHotkeys`
    - :ref:`SetForegroundWin`
