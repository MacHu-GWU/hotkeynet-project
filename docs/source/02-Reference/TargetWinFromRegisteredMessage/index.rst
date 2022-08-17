.. _TargetWinFromRegisteredMessage:

TargetWinFromRegisteredMessage
==============================================================================
Sends a registered message to all top-level windows and targets the first window that returns "TRUE."

**Syntax**

::

    <TargetWinFromRegisteredMessage text>

**Parameters**

    Text is the text identifier of the registered message.

**Example**

::

    <Hotkey F1>
       <TargetWinFromRegisteredMessage MessageID>

**Related topics**

- :ref:`SendRegisteredMessage`
