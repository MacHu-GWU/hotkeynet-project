.. _SendCopyDataMessage:

SendCopyDataMessage
==============================================================================
Sends a ``WM_COPYDATA`` message to the previously targeted window.

**Syntax**::

    <SendCopyDataMessage text>

**Parameters**

    Text is the payload of the WM_COPYDATA message.

**Remarks**

The text is sent as Unicode. The dwData member of the ``COPYDATASTRUCT`` is set to zero. If the text contains white space, enclose it in double quotation marks.

**Example**::

    <Hotkey F1>
        <TargetWin SomeWindow>
        <SendCopyDataMessage "This will get sent">

**Related topics**

- :ref:`PostMessage`
- :ref:`SendMessage`
- :ref:`SendCopyDataMessage`
- :ref:`SendRegisteredMessage`
