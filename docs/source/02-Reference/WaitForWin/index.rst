.. _WaitForWin:

WaitForWin
==============================================================================
Waits for a window to open.

**Syntax**::

    <WaitForWin window timeout>

**Parameters**

    Window is the name of the window.

    Timeout is the maximum time to wait in milliseconds.

**Remarks**

    If the window opens, it becomes the currently targeted window.

    This command can be canceled with :ref:`Cancel`.

**Technical details**

    This command polls at 500 millisecond intervals to see if the window exists yet.

**Example**

    The following hotkey starts a game, waits for it to open, renames it, and changes its position::

    <Hotkey F1>
       <run "C:\Program Files\UberSoft\uber.exe">
          <WaitForWin Ubertastic 20000>
          <Rename Ubertastic uber1>
          <SetWinPos uber1 471 142>
