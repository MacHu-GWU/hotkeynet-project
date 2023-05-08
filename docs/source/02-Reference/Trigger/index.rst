.. _Trigger:

%Trigger%, %TriggerMainKey%
==============================================================================
These keywords get replaced by the key combination or main key that triggers the hotkey.

**Syntax**

::

    <Key %Trigger%>

    or

    <Key %TriggerMainKey%>

**Parameters**

    None.

**Remarks**

    These keywords are normally used as the argument for Key.

**Examples**

    Suppose you write a definition with two triggers::

        <Hotkey Shift F1-F2 > // YOU WRITE THIS
        <Key %Trigger%>

    When HotkeyNet loads the example above, it converts it into two separate hotkeys. The keyword gets replaced by the entire trigger::

        <Hotkey Shift F1> // HOTKEYNET LOADS THIS
        <Key Shift F1>

        <Hotkey Shift F2>
        <Key Shift F2>

    Suppose the definition had been written with %TriggerMainKey% instead::

        <Hotkey Shift F1-F2 > // YOU WRITE THIS
        <Key %TriggerMainKey%>

    In this case the replacements are the main trigger keys F1 and F2 without Shift::

        <Hotkey Shift F1> // HOTKEYNET LOADS THIS
        <Key F1>

        <Hotkey Shift F2>
        <Key F2>
