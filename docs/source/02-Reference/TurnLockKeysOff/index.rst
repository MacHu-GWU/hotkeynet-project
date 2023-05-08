.. _TurnLockKeysOff:

TurnLockKeysOff
==============================================================================
This command is new in build 116

Many thanks to dcreager for suggesting this command.

Turns lock keys off.

**Syntax**

::

    <TurnLockKeysOff>

**Parameters**

    None.

**Remarks**

    The three lock keys are CapsLock, NumLock, and ScrollLock.

    Keys that were turned off with this command can be turned back on with :ref:`RestoreLockKeys`.

**Example**

::

    <Hotkey F1>
        <SendPC 192.168.1.105>
        <TurnLockKeysOff>


    <Hotkey F2>
        <SendPC 192.168.1.105>
        <RestoreLockKeys>

**Related topics**

- :ref:`TurnLockKeysOff`
- :ref:`RestoreLockKeys`
- :ref:`TurnCapsLockOff`
- :ref:`RestoreCapsLock`
