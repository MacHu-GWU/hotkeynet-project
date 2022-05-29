.. _SetButtonStyle:

SetButtonStyle
==============================================================================
Changes a button's appearance.

**Syntax**:

    <SetButtonType name style>

**Parameters**

    Name is the name of the button.

    Style is system or colored.

**Picture buttons**

    You can't change a button into a picture button with this command. Picture buttons can only be created with CreatePictureButton.

**Example**

    This hotkey toggles the appearance of a button::

        <Hotkey F1>
           <Toggle>
              <SetButtonType Button1 colored>
           <Toggle>
              <SetButtonType Button1 system>

**Related topics**

    - :ref:`CreateButton`
