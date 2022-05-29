.. _PostMessage:

PostMessage
==============================================================================
Posts a message to a window using the system ``PostMessage()`` command.

**Syntax**::

    <PostMessage id wparam lparam>

**Parameters**

    - ID is the message identifier.
    - Wparam is the WPARAM argument.
    - Lparam is the LPARAM argument.

**Remarks**

    - Arguments can be written in decimal or hex.
    - The message is sent to the window that was targeted with TargetWin, SendWin, etc.
    - This command simply calls the system command with the same name. For more information, see Microsoft's documentation for SendMessage().

**Example**::

    <hotkey F1>
       <sendpc local>
          <TargetWin Untitled>
          <PostMessage 0x7a3 29 0>

**Related topics**

- :ref:`PostMessage`
- :ref:`SendMessage`
- :ref:`SendCopyDataMessage`
- :ref:`SendRegisteredMessage`
