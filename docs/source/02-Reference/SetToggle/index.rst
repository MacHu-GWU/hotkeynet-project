.. _SetToggle:

SetToggle
==============================================================================
Sets a hotkey's toggle to a specified number

**Syntax**::

    <SetToggle number hotkey>

**Parameters**

    Number is the toggle number.

    Hotkey is the keyword and trigger that define the hotkey.

**Remarks**

    Here's how this command is used. Suppose you've defined F1 as a hotkey with three toggles::

        <Hotkey F1>
           <Toggle>
              <Text First thing!>
           <Toggle>
              <Text Second thing!>
           <Toggle>
              <Text Third thing!>

    If you want to set that hotkey to its third toggle so it prints "Third thing!" you could make another hotkey like this::

        <Hotkey F2>
           <SetToggle 3 Hotkey F1>

**Limitations**

    You can only set the toggle of one hotkey at a time. For example, the following won't work because it tries to set multiple hotkeys::

        <SetToggle 3 Hotkey A-Z> // DOOESN'T WORK

**Related topics**

    - :ref:`DoToggles`
    - :ref:`Toggle`
    - :ref:`ResetToggles`
    - :ref:`DoHotkey`
    - :ref:`Toggling PIP Windows with World of Warcraft`
