.. _WaitForWinEnabled:

WaitForWinEnabled
==============================================================================
Waits until the currently targeted window is enabled.

**Syntax**::

    <WaitForWinEnabled timeout>

**Parameters**

    Timeout is the maximum time to wait in milliseconds.

**Remarks**

    This command waits until the window that was previously targeted with TargetWin, WaitForWin, SendWin, SendWinMF, TargetChild, etc., is enabled.

    This command can be interrupted with :ref:`Cancel`.

**Technical details**

    This command calls the system function IsWindowEnabled at 500 millisecond intervals.

**Example**

    The following hotkey starts a game, waits for it to open, waits for it to be enabled, and sends a keystroke to it::

    <Hotkey F1>
       <run "C:\Program Files\UberSoft\uber.exe">
          <WaitForWin Ubertastic 20000>
          <WaitForWinEnabled 20000>
          <Key X>
