.. _TurnHotkeysOff:

TurnHotkeysOff
==============================================================================
Turns hotkeys off.

**Syntax**::

    <TurnHotkeysOff>

**Parameters**

    None.

**Remarks**

    When you turn hotkeys off on a pc, pressing a key on that machine's keyboard will no longer trigger hotkeys. However, that pc will continue to execute hotkey commands that it receives from other pc's.

    You can also turn hotkeys on and off with ToggleHotkeys.

**Example**

    You can use this command to disable hotkeys on the local machine like this::

        <Hotkey F1>
           <SendPC Local>
              <TurnHotkeysOff>

    You can also use it to disable hotkeys on a remote machine like this::

        <Hotkey F1>
           <sendpc 192.168.1.108>
              <TurnHotkeysOff>

**Related topics**

    - :ref:`ToggleHotkeys`
    - :ref:`TurnHotkeysOn`
