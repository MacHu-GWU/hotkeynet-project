.. _MaximizeWin:

MaximizeWin
==============================================================================
This command was called Maximize before build 107.

Maximizes the currently targeted window.

**Syntax**

::

    <MaximizeWin>

**Parameters**

    None.

**Remarks**

    Maximizes the window that was targeted with TargetWin,  SendWin, etc.


**Example**

::

    <Hotkey F1>
        <SendPC local>
            <TargetWin Uber666>
            <MaximizeWin>

**Related topics**

- :ref:`HideWin`
- :ref:`MaximizeWin`
- :ref:`MinimizeWin`
- :ref:`RestoreWinSize`
- :ref:`ShowWin`
