.. _CreateColoredButton:

CreateColoredButton
==============================================================================
Creates a colored button on the screen.

**Syntax**::

    <CreateColoredButton name x y width height bkcolor textcolor [text]>

**Parameters**

    Name is the name of the button.

    X is the horizontal screen coordinate of the window's upper left corner.

    Y is the vertical screen coordinate of the window's upper left corner.

    Width is the window's width.

    Height is the window's height.

    Bkcolor is the background color.

    Textcolor is the text color.

    Text is the caption that appears on the button.

**Remarks**

    The program has thee button styles. This command creates the colored style. You can create the other styles with CreateButton and CreatePictureButton.

    For more information about buttons, see CreateButton.

**Colors**

    Colors are specified with hexadecimal RGB values. For an explanation, see SetButtonColors.

**Use AutoExec**

    You should create all your buttons and panels in an AutoExec command that executes automatically when the script loads.

**Example**::

    <Command AutoExec>
        <CreateColoredButton Button1 100 100 50 50 0x40409 0xFFFFFF On>

**Related topics**

- :ref:`CreateButton`
