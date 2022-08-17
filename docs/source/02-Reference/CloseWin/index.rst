.. _CloseWin:

CloseWin
==============================================================================
Asks the currently targeted window to destroy itself.

**Syntax**

::

    <CloseWin>

**Parameters**

    None.

**Remarks**

    "Close" is Microsoft's terminology for destroying a window.

    Before calling this command, target a window with TargetWin, SendWin, SendWinM, etc.

    This command asks but does not force a window to close. If the window belongs to another program, it may not comply.

**Example**

::

    <Hotkey F1>
       <TargetWin MarkedForDeath>
       <CloseWin>


**Related topic**

- :ref:`Open`
- :ref:`Run`
