.. _SetButtonText:

SetButtonText
==============================================================================
Sets the text that is displayed on a button.

**Syntax**::

    <SetButtonText name [text]>

**Parameters**

    Name is the name of the button.

    Text is the caption on the button.

**Remarks**

    If Text is omitted, the button is blank (has no caption).

**Example**

    This hotkey toggles a button's caption from "On" to "Off" and back again::

        <Hotkey F1>
           <Toggle>
              <SetButtonText Button1 On>
           <Toggle>
              <SetButtonText Button1 Off>

**Related topics**

- :ref:`CreateButton`
- :ref:`CreateColoredButton`
- :ref:`SetButtonColors`
- :ref:`SetButtonHotkey`
- :ref:`SetButtonText`
- :ref:`SetButtonStyle`
- :ref:`TargetButton`