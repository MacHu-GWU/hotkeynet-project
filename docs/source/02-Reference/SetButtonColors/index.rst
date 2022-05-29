.. _SetButtonColors:

SetButtonColors
==============================================================================
Sets the background and text colors of a button.

**Syntax**::

    <SetButtonColors name bkcolor [textcolor]>

**Parameters**

    Name is the name of the button.

    Bkcolor is the background color.

    Textcolor is the text color.

**Remarks**

    This command's effects are visible only when the button's style is set to colored.

    To set the style to colored, use SetButtonStyle or make the button with CreateColoredButton.

    Colors are specified as 6-digit hexadecimal RGB values. The first two digits are the red component; the second two digits are the green component; and the last two digits are the blue component. Here are some examples:

    - 0xFFFFFF is white.
    - 0x000000 is black.
    - 0xFF0000 is nominally red (but actually slightly orange).
    - 0x00FF00 is bright green.
    - 0x0000FF is vivid blue.
    - 0x808080 is medium gray.

**Example**

This hotkey reverses a button's colors each time it's pressed::

    <Hotkey F1>
       <Toggle>
          <SetButtonColors Button1 0x000000 0xFFFFFF>
       <Toggle>
          <SetButtonColors Button1 0xFFFFFF 0x000000>

**Related topics**

- :ref:`CreateButton`
- :ref:`CreateColoredButton`
- :ref:`SetButtonColors`
- :ref:`SetButtonHotkey`
- :ref:`SetButtonText`
- :ref:`SetButtonStyle`
- :ref:`TargetButton`
