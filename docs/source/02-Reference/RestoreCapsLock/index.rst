.. _RestoreCapsLock:

RestoreCapsLock
==============================================================================
This command is new in build 117

Many thanks to dcreager for suggesting this command.

Turns CapsLock back on after it was turned off with TurnCapsLockOff.

**Syntax**

::

    <RestoreCapsLock>

**Parameters**

    None.

**Example**

::

    <Hotkey F1>
        <SendPC 192.168.1.105>
        <TurnCapsLockOff>

    <Hotkey F2>
        <SendPC 192.168.1.105>
        <RestoreCapsLock>

**Related topics**

- :ref:`TurnLockKeysOff`
- :ref:`RestoreLockKeys`
- :ref:`TurnCapsLockOff`
- :ref:`RestoreCapsLock`
