.. _SendMessage:

SendMessage
==============================================================================
Sends a message to a window using the system SendMessage() command.

**Syntax**

::

    <SendMessage id wparam lparam>

**Parameters**

    - ID is the message identifier.
    - Wparam is the WPARAM argument.
    - Lparam is the LPARAM argument.

**Remarks**

    Arguments can be written in decimal or hex. An example of hex notation is shown below.

    The message is sent to the window that was targeted with :ref:`TargetWin`, :ref:`SendWin`, etc.

    This command calls the system command with the same name. For more information, see Microsoft's documentation for SendMessage().

**Example**

::

    <hotkey F1>
       <sendpc local>
          <TargetWin Untitled>
          <SendMessage 0x7a3 29 0>

**Related topics**

- :ref:`PostMessage`
- :ref:`SendMessage`
- :ref:`SendCopyDataMessage`
- :ref:`SendRegisteredMessage`
