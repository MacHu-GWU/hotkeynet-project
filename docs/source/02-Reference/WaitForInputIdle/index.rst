.. _WaitForInputIdle:

WaitForInputIdle
==============================================================================
Waits until the currently targeted window is waiting for user input with no input pending

**Syntax**::

    <WaitForInputIdle timeout>

**Parameters**

    Timeout is the maximum time to wait in milliseconds.

**Remarks**

    This command identifies the process that created the currently targeted window. It then waits until that window is waiting for user input with no input pending.

    The currently targeted window is the one that was most recently specified by TargetWin, SendWin, WaitForWin, etc.

    This command can be canceled with :ref:`Cancel`.

**Technical details**

    This command calls the operating system command WaitForInputIdle. For more information, see Microsoft's documentation of that command.

**Example**

    The following hotkey starts a game and waits for it to be ready for input before typing X::

        <Hotkey F1>
           <SendPC local>
              <run "C:\Program Files\UberSoft\uber.exe">
              <WaitForWin Ubertastic 20000>
              <WaitForInputIdle 20000>
              <SendWin Ubertastic>
                 <Key X>
