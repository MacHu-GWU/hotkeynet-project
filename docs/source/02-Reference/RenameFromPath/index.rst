.. _RenameFromPath:

RenameFromPath
==============================================================================
Finds the window that was started from the specified file or directory, and renames it.

**Syntax**

::

    <RenameFromPath path newname>

**Parameters**

    Path is the location of the file from which the window started.

    Newname is the window's new name.

**Remarks**

    The path must begin with the drive letter and root folder. In other words, it must be fully qualified.

    You don't have to type the entire path including the file name. You can include just enough of the path to distinguish the window from other open windows.

    You can also rename windows with Rename.

**Examples**

    The following hotkey finds the window that was started from the specified exe file, and changes its name to Uber1::

        <Hotkey ctrl R>
            <SendPC Local>
                <RenameFromPath C:\uber\uber.exe Uber1>

    You don't have to specify the entire path. For example, you could type just the directory::

        <Hotkey ctrl R>
            <SendPC Local>
                <RenameFromPath C:\uber\ Uber1>

    If a path or name contains spaces, put quotes around it::

        <Hotkey ctrl R>
            <SendPC Local>
                <RenameFromPath "c:\my path\" "new name">

**Related topics**

- :ref:`Rename`
- :ref:`RenameTargetWin`