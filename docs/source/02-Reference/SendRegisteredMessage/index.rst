.. _SendRegisteredMessage:

SendRegisteredMessage
==============================================================================
Posts or sends a registered message to a window.

**Syntax**::

    <SendRegisteredMessage name wparam lparam>

**Parameters**

    - Name is the registered name of the message.
    - Wparam is the WPARAM argument.
    - Lparam is the LPARAM argument.

**Remarks**

    This command calls the operating sytem command ``RegisterWindowMessage()`` to obtain the identifier of the name you specify. It then sends a message with that identifier and the two other arguments.

    The message is sent to the window that was targeted with TargetWin, SendWin, etc.

    If the current send mode is SendMessage, the message is sent with SendMessage(). Otherwise it's sent with PostMessage().

    The numeric arguments can be written in decimal or hex. An example of hex notation is shown below.

**Example**

    <hotkey F1>
       <sendpc local>
          <TargetWin Untitled>
          <SendRegisteredMessage CoolMsg 0x1AC 0xC00>

**Related topics**

- :ref:`PostMessage`
- :ref:`SendMessage`
- :ref:`SendCopyDataMessage`
- :ref:`SendRegisteredMessage`
