.. _TurnCapsLockOff:

TurnCapsLockOff
==============================================================================
This command is new in build 117

Many thanks to dcreager for suggesting this command.

Turns CapsLock off.

**Syntax**

::

    <TurnCapsLockOff>

**Parameters**

    None.

**Remarks**

    If CapsLock was off before this command was called, it can be turned back on with :ref:`RestoreCapsLock`.

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