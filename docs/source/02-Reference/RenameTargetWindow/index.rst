.. _RenameTargetWin:

RenameTargetWin
==============================================================================
Changes the name of the currently targeted window.

**Syntax**

::

    <RenameTargetWin newname>

**Parameters**

    Newname is the window's new name.

**Remarks**

    This command renames the window that was targeted with TargetWin, SendWin, etc.

    You can also rename windows with RenameFromPath or RenameWin.

**Examples**

    The following hotkey changes the name of a window called "Bloodlust" to "MyGame."::

        <Hotkey F1>
             <TargetWin Bloodlust>
             <RenameTargetWin MyGame>

**Related topics**

- :ref:`RenameFromPath`
- :ref:`RenameWin`
