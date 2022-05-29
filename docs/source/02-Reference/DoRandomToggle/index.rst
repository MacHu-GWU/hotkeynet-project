.. _DoRandomToggle:

DoRandomToggle
==============================================================================
Sets a hotkey's toggle to a random number and triggers the hotkey.

**Syntax**::

    <DoRandomToggle hotkey>

**Parameters**

    Hotkey is the keyword and trigger that define the hotkey. See below for examples.

**Remarks**

    You must specify one particular hotkey with this command. You can't specify a range of triggers. For example, suppose you wanted to randomize toggles for this hotkey::

        <Hotkey F1>

    you'd do it this way::

        <DoRandomToggle Hotkey F1>

    For this hotkey::

        <HotkeyUp Shift Alt X>

    you'd write this::

        <DoRandomToggle HotkeyUp Shift Alt X>

    But this definition::

        <Hotkey A-Z>

    can't be randomized because it refers to 26 separate hotkeys.

**Example**

    Suppose you want to talk to yourself and say random things. First make a hotkey with toggles that contain your words of wisdom::

        <Hotkey F1>
           <Toggle>
              <Text Hi Mr. K>
           <Toggle>
              <Text Nice day, huh?>
           <Toggle>
              <Text If it quacks like a duck...>
           <Toggle>
              <Text ...it's probably a giraffe.>
           <Toggle>
              <Text Don't take any wooden nickels.>
           <Toggle>
              <Text Full speed ahead.>
           <Toggle>
              <Text It's later than you think.>

    To avoid boredom you'd probably want a lot more toggles than this, but you get the idea. Now make a second hotkey that executes a random Toggle from the first hotkey::

        <Hotkey Ctrl T>
           <DoRandomToggle Hotkey F1>

**Related topics**

    - :ref:`Toggle`
    - :ref:`ResetToggles`
    - :ref:`DoHotkey`
    - :ref:`Toggling PIP Windows with World of Warcraft`
