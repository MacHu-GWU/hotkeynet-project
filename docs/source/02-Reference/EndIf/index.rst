.. _EndIf:

EndIf
==============================================================================
Used with :ref:`If`.

**Syntax**::

    <EndIf>

**Parameters**

    None.

**Remarks**

    It isn't necessary to write EndIf unless you want to add instructions that should always execute after an If-block, like in the second example below.

**Example**

::

    <Hotkey F1>
        <If ActiveWinIs wow1>
            <SendLabel w1>
            <Key 1>
        <EndIf>
        <SendFocusWin> // THIS WILL ALWAYS EXECUTE
        <Text burp>

**Related topics**

- :ref:`If`
- :ref:`Else`
