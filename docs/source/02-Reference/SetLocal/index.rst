.. _SetLocal:

SetLocal
==============================================================================
This keyword is new in build 172

Overrides a global setting for an individual hotkey.

**Syntax**

::

    <SetLocal option argument>

**Parameters**

    Option can have the following value:


    - ``ClearModifiers``: Overrides "Clear modifiers before executing hotkey" which is set globally on the Settings Panel. The argument must be either "on" or "off."

**Remarks**

    SetLocal takes effect just before the hotkey begins to execute regardless of where you write it in the hotkey definition.

**Example**

::

    <Hotkey F1>
        <SetLocal ClearModifiers off>
            <SendLabel w1>
                <Key 1>
