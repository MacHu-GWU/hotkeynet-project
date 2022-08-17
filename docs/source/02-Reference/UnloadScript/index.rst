.. _UnloadScript:

UnloadScript
==============================================================================
Removes a script and all its definitions from HotkeyNet's memory.

**Syntax**

::

    <UnloadScript>

**Parameters**

    None.

**Remarks**

    This command is rarely needed. You don't need to use it when you load a script because HotkeyNet automatically unloads the old script each time it loads a new one.

**Example**

::

    <Hotkey F1>
        <UnloadScript>

**Related topics**

- :ref:`LoadScript`
