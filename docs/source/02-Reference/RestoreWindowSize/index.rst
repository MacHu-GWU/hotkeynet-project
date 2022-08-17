.. _RestoreWinSize:

RestoreWinSize
==============================================================================
Restores the currently targeted window to normal size.

**Syntax**

::

    <RestoreWinSize>

**Parameters**

    None.

**Remarks**

    Restores the size of the window that was targeted with TargetWin,  SendWin, etc.

**Example**

::

    <Hotkey F1>
       <SendPC local>
           <TargetWin Uber666>
           <RestoreWinSize>

**Related topics**

- :ref:`HideWin`
- :ref:`MaximizeWin`
- :ref:`MinimizeWin`
- :ref:`RestoreWinSize`
- :ref:`ShowWin`
