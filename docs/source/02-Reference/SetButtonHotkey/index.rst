.. _SetButtonHotkey:

SetButtonHotkey
==============================================================================
Assigns a hotkey to a button so you can trigger the hotkey by left-clicking the button.

**Syntax**::

    <SetButtonHotkey button hotkey>

**Parameters**

    - Button is the name of the button.
    - Hotkey is the name of the hotkey.

**Remarks**

    - You can assign one "down" hotkey and one "up" hotkey to a button.
    - A button can trigger hotkeys or a command but not both.
    - The name of the hotkey includes the keyword (Hotkey, HotkeyUp, or MovementHotkey) all modifiers including lock states (NumLock, ScrollLock, and CapsLock), and the main trigger key.

See the examples below.

**Examples**::

    <SetButtonHotkey Button1 Hotkey F1>
    <SetButtonHotkey Button2 MovementHotkey W>
    <SetButtonHotkey Button3 Hotkey ScrollLockOn F7>
    <SetButtonHotkey Button4 Hotkey LAlt RShift X>

**Related topics**

- :ref:`CreateButton`
- :ref:`CreateColoredButton`
- :ref:`SetButtonColors`
- :ref:`SetButtonCommand`
- :ref:`SetButtonHotkey`
- :ref:`SetButtonText`
- :ref:`SetButtonStyle`
- :ref:`TargetButton`
