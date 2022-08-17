.. _RemoveWinFrame:

RemoveWinFrame
==============================================================================
Removes the frame from the currently targeted window.

**Syntax**

::

    <RemoveWinFrame>

**Parameters**

    None.

**Remarks**

    RemoveWinFrame removes the border and title bar from the window that was targeted with TargetWin, TargetChild, SendWin, etc.

**Example**

::

    <hotkey F1>
       <sendpc local>
           <TargetWin "World of Warcraft">
           <RemoveWinFrame>
