.. _TurnHotkeysOn:

TurnHotkeysOn
==============================================================================
Turns hotkeys on.

**Syntax**::

    <TurnHotkeysOn>

**Parameters**

    None.

**Remarks**

    You can also turn hotkeys on and off with ToggleHotkeys.

    If a hotkey contains this command, that hotkey will get triggered even when hotkeys are off.

**Example**

    You can use this command to enable hotkeys on the local machine like this::

        <Hotkey F1>
           <SendPC Local>
              <TurnHotkeysOn>

    You can also use it to enable hotkeys on a remote machine like this::

        <Hotkey F1>
           <SendPC 192.168.1.108>
              <TurnHotkeysOn>

**Related topics**

    - :ref:`ToggleHotkeys`
    - :ref:`TurnHotkeysOff`
