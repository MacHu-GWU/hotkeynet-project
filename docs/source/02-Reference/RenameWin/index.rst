.. _RenameWin:

RenameWin
==============================================================================
Changes the name of a window.

**Syntax**

::

    <RenameWin oldname newname>

**Parameters**

    - ``Oldname`` is the window's current name.
    - ``Newname`` is the window's new name.

**Remarks**

    You can also rename windows with :ref:`RenameFromPath` or :ref:`RenameTargetWin`.

    You don't have to type the entire old name.

**Examples**

    The following hotkey changes the name of a window called "Bloodlust" to "MyGame."::

        <Hotkey RAlt NumpadEnter>
             <RenameWin Bloodlust MyGame>


    If the name of a window contains space, put quotation marks around it::

        <Hotkey F2>
             <RenameWin "Guts and Glory" MyGame>


**Related topics**

- :ref:`RenameFromPath`
- :ref:`RenameTargetWin`
