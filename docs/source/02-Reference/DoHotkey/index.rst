.. _DoHotkey:

DoHotkey
==============================================================================
Triggers a hotkey from a command or another hotkey.

**Syntax**

::

    <DoHotkey hotkey>

**Parameters**

    Hotkey is the keyword and trigger that define the hotkey you are triggering. See below for examples.

**Remarks**

    DoHotkey works exactly like triggering a hotkey with your fingers. If you press the trigger while another hotkey is executing, the new hotkey waits until the first one finishes. DoHotkey does the same thing. It waits until the first hotkey or command finishes before executing the new one.

    If you want to execute a piece of code immediately, without waiting, you should use a user-defined command, not DoHotkey.

    You must specify one particular hotkey with this command. You can't specify a range of triggers. For example, if you wanted to trigger the following hotkey::

        <Hotkey F1>

    you'd do it this way::

        <DoHotkey Hotkey F1>

    And if you wanted to trigger this hotkey::

        <HotkeyUp Shift Alt X>

    you'd write this::

        <DoHotkey HotkeyUp Shift Alt X>

    But this definition::

        <Hotkey A-Z>

    can't be triggered with DoHotkey because it refers to 26 separate hotkeys.

**Example**

    The first hotkey will get triggered by the second one::

        <Hotkey Ctrl Shift Y>
           <Key X>

        <Hotkey F1>
           <DoHotkey Hotkey Ctrl Shift Y>

**Related topics**

- :ref:`DoRandomToggle`
