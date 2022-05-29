.. _DoToggles:

DoToggles
==============================================================================
Executes a hotkey repeatedly until all its toggles, starting with the current one, have executed.

**Syntax**::

    <DoToggles hotkey>

**Parameters**

    Hotkey is the keyword and trigger that define the hotkey you are triggering. See below for an example.

**Remarks**

    To execute all of a hotkey's toggles starting with the first, set the hotkey's toggle to 1 with SetToggle before calling this command.

**Example**

    Suppose you have a hotkey with toggles like this one::

        <Hotkey F1>
           <Toggle>
              <Text 1>
           <Toggle>
              <Text 2>
           <Toggle>
              <Text 3>
           <Toggle>
              <Text 4>

    Suppose you want to execute all those toggles in order with a single keypress. You can do it with a second hotkey that uses DoToggles::

        <Hotkey F2>
           <SetToggle 1 Hotkey F1>
           <DoToggles Hotkey F1>

    This will cause all of F1's toggles to execute.

    That's one way to use this command. But it can be used in another way too. Suppose you press the hotkey just shown, but right after that, before F1 can finish all its toggles, you interrupt F1 by pressing a third hotkey that contains Cancel.

    To make this example very specific, let's imagine you cancel F1 after it has completed its first two toggles. Now you want to press a single hotkey that makes F1 execute its remaining toggles (the third and fourth). You can do that like this::

        <Hotkey F3>
           <DoToggles Hotkey F1>

**Related topics**

- :ref:`Toggle`
- :ref:`ResetToggles`
- :ref:`SetToggle`
- :ref:`DoHotkey`
