.. _Toggle:

Toggle
==============================================================================
Makes a hotkey do different things each time you press it.

**Syntax**::

    <Toggle>

**Parameters**

    None.

**Remarks**

    Suppose you want a hotkey that does different things each time you press it. For example:

    — The first time you press it, it types "Hello" on a remote PC.
    — The second time, it renames a window on the local PC.
    — The third time, it types "Goodbye" on a third PC.
    — The fourth time, it starts the cycle again.

    You can make a hotkey do that by writing <Toggle> before each set of actions::

        <Hotkey F1>
           <Toggle>
              <SendPC 192.168.1.102>
                 <Text Hello>
           <Toggle>
              <SendPC Local>
                 <RenameWin Glob Gloop>
           <Toggle>
              <SendPC 192.168.1.103>
                 <Text Goodbye>

    A hotkey can contain as many Toggles as you like. There's no limit.

    You can make all your hotkeys return to their first action with ResetToggles.

**Related topics**

    - :ref:`DoToggles`
    - :ref:`Toggle`
    - :ref:`SetToggle`
    - :ref:`ResetToggles`
    - :ref:`DoRandomToggle`
    - :ref:`Toggling PIP Windows with World of Warcraft`
