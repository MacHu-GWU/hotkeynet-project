.. _SetPanelLayout:

SetPanelLayout
==============================================================================
This command is new in build 192

Makes a panel automatically arrange the locations and sizes of its buttons according to your instructions.

**Syntax**

::

    <SetPanelLayout Panel RowLength Margin [ButtonWidth ButtonHeight]>

    # or

    <SetPanelLayout off>

**Parameters**

    - ``Panel`` is the name of the panel.
    - ``RowLength`` is the maximum number of buttons in a row (counting from left to right). You can specify a number or the word SingleRow.
    - ``Margin`` is the amount of white space, in pixels, between buttons.
    - ``ButtonWidth`` is the width of each button. This argument is optional.
    - ``ButtonHeight`` is the height of each button. This argument is optional.
    - ``Off`` is the word off. This makes the panel stop rearranging itself.

**Remarks**

    Once you use this command for a particular panel, that panel will keep arranging itself automatically every time you add or remove a button.

    If you omit ButtonWidth and ButtonHeight, the program doesn't change the sizes of buttons.

**Examples**

This hotkey...

::

    <Hotkey F1>


**Related topics**

- :ref:`SetPanelStyle`
