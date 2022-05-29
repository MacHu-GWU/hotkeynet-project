.. _SetForegroundWin:

SetForegroundWin
==============================================================================
Brings the currently targeted window to the foreground.

**Syntax**::

    <SetForegroundWin>

**Parameters**

    None.

**Remarks**

    SetForeground brings to the foreground the window that was targeted with TargetWin,  TargetChild,  SendWin, etc.

    It calls the Windows system command SetForegroundWindow().

**Example**

    <Hotkey F1>
       <SendPC local>
           <TargetWin Uber666>
           <SetForegroundWin>

**Related topics**

    - :ref:`SetFocusWin`
    - :ref:`SetActiveWin`
