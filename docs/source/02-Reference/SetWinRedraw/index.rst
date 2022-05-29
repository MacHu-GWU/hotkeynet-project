.. _SetWinRedraw:

SetWinRedraw
==============================================================================
Makes a window stop or start redrawing itself.

**Syntax**::

    <SetWinRedraw arg>

**Parameters**

    Arg must be "on" or "off."

**Remarks**

    SetWinRedraw acts on the window that was previously targeted with :ref:`SendWin`, :ref:`TargetWin`, etc.

    This command sends the operating system message ``WM_SETREDRAW``.

**Example**

    The following hotkey makes a window called w1 stop redrawing itself::

        <Hotkey F1>
            <TargetWin w1>
            <SetWinRedraw off>
