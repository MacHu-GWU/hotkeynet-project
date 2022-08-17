.. _TargetForegroundWin:

TargetForegroundWin
==============================================================================
Targets whichever window is in the foreground.

**Syntax**

::

    <TargetForegroundWin>

**Parameters**

    None.

**Example**

    The following definition targets the foreground window and renames it::

        <hotkey F1>
           <sendpc local>
               <TargetForegroundWin>
               <RenameTargetWin NewName>

**Related topics**

- :ref:`TargetChild`
- :ref:`TargetWin`
