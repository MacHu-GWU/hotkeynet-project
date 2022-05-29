.. _ToggleHotkeys:

ToggleHotkeys
==============================================================================
Toggles hotkeys on and off.

**Syntax**::

    <ToggleHotkeys>

**Parameters**

    None.

**Remarks**

    If hotkeys are on, this turns them off. If they are off, it turns them on.

    When you turn hotkeys off on a pc, pressing keys on that machine's keyboard will no longer trigger hotkeys (except for any hotkeys that you have defined that turn hotkeys back on). However, that pc will continue to execute hotkey commands that it receives from other pc's.

    If a hotkey contains this command, that hotkey will get triggered even when hotkeys are off.

    You can also turn hotkeys on and off with :ref:`TurnHotkeysOn` and :ref:`TurnHotkeysOff`.

**Example**

    You can use this command to toggle the local machine's hotkeys::

        <hotkey F1>
           <sendpc local>
              <ToggleHotkeys>

    You can also use this command to toggle a remote machine's hotkeys::

        <hotkey F1>
           <sendpc 192.168.1.108>
              <ToggleHotkeys>

**Related topics**

    - :ref:`ToggleWin`
    - :ref:`TurnHotkeysOff`
    - :ref:`TurnHotkeysOn`
