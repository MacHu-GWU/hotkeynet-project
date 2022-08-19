.. _SetPanelStyle:

SetPanelStyle
==============================================================================
This command is new in build 187

Changes a panel's appearance.

**Syntax**

::

    <SetPanelStyle name style>

**Parameters**

    Name is the name of the panel.

    Style is one of the following:

    - Transparent
    - Frameless
    - Frame
    - TitleAndFrame

**Remarks**

    "Transparent" makes the panel's background invisible so only the buttons can be seen and clicked.

    You can also make the entire panel (including buttons) translucent with SetWindowOpacity.

**Example**

    This hotkey toggles the appearance of a panel.

    ::

        <Hotkey F1>
           <Toggle>
              <SetPanelStyle MyPanel Transparent>
           <Toggle>
              <SetPanelStyle MyPanel Frameless>
           <Toggle>
              <SetPanelStyle MyPanel Frame>
           <Toggle>
              <SetPanelStyle MyPanel TitleAndFrame>

**Related topics**

- :ref:`CreatePanel`
