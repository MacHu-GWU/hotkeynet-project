.. _Else:

Else
==============================================================================
This keyword is new in build 140

Used with :ref:`If <If>`.

**Syntax**

    <Else>

         or

    <Else If condition arg>

**Parameters**

    Else can be used two ways:

    1. By itself.
    2. With If. See If for information about its parameters.

**Example**

    <Hotkey F1>
        <If ActiveWinIs wow1>
            <SendLabel w1>
            <Key 1>
        <Else If ActiveWinIs wow2>
            <Sendlabel w2>
            <Key 2>
        <Else>
            <SendFocusWin>
            <Key %Trigger%>

**Related topics**

- :ref:`If`
- :ref:`EndIf`
