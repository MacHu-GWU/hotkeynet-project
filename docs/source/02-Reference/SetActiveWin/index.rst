.. _SetActiveWin:

SetActiveWin
==============================================================================
Activates the currently targeted window.

**Syntax**:

    <SetActiveWin>

**Parameters**

    None.

**Remarks**

    SetActiveWin activates the window that was targeted with TargetWin, TargetChild, SendWin, etc.

    It calls the operating system command SetActiveWindow.

**Example**::

    <hotkey F1>
       <sendpc local>
           <TargetWin "My difficult background Window">
           <TargetChild "Obscure control class">
           <SetActiveWin>
           <text woot it worked>

**Related topics**

    - :ref:`SetForegroundWin`
    - :ref:`SetFocusWin`
