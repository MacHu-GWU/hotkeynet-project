.. _TargetButton:

TargetButton
==============================================================================
Sets the targeted window. Use this command when the target is a button.

**Syntax**::

    <TargetButton name>

**Parameters**

    Name is the name of a button.

**Remarks**

    Use this command to target a button which has been created by HotkeyNet.

**Examples**

    The following hotkey changes the size of a button::

        <Hotkey F1>
            <TargetButton Button1>
                <SetWinSize 100 100>

    The following hotkey makes a button stay always on top::

        <Hotkey F2>
            <TargetButton Button1>
                <AlwaysOnTop on>

**Related topics**

- :ref:`CreateButton`
- :ref:`CreateColoredButton`
