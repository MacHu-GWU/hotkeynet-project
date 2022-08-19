.. _AddButtonToPanel:

AddButtonToPanel
==============================================================================
This command is new in build 187

Moves a button onto a panel.

**Syntax**

::

    <AddButtonToPanel button panel [x y [width height]]>

**Parameters**

    - ``Button`` is the name of the button.
    - ``Panel`` is the name of the panel.
    - ``X`` is the horizontal coordinate of the button's upper left corner.
    - ``Y`` is the vertical coordinate of the button's upper left corner.
    - ``Width`` is the button's width.
    - ``Height`` is the button's height.

**Remarks**

    The position (x and y) is relative to the client area of the panel.

    You don't have to specify x, y, width or height. You can set them later, after the button has been added, with SetWinPos, SetWinSize, and SetWinRect.

**Example**

::

    <Hotkey F1>
        <AddButtonToPanel MyButton MyPanel>

**Related topics**

- :ref:`CreateButton`
- :ref:`CreatePanel`
