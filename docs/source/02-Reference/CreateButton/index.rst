.. _CreateButton:

CreateButton
==============================================================================
Creates a button on the screen.

**Syntax**::

    <CreateButton name x y width height [text]>

**Parameters**

    - Name is the name of the button.
    - X is the horizontal screen coordinate of the window's upper left corner.
    - Y is the vertical screen coordinate of the window's upper left corner.

    - Width is the window's width.
    - Height is the window's height.
    - Text is the caption that appears on the button.

**Remarks**

    The program has three button styles. This command creates the system style. You can create the other styles with :ref:`CreateColoredButton` and :ref:`CreatePictureButton`.

    To assign a hotkey to a button, use :ref:`SetButtonHotkey`.

    To assign a command to a button, use :ref:`SetButtonCommand`.

    To change a button's style from system to colored or vice versa, use :ref:`SetButtonStyle`.

    To move a button, use :ref:`TargetButton` and :ref:`SetWinPos` or :ref:`SetWinRect`.

    To change a button's size, use :ref:`TargetButton` and :ref:`SetWinSize` or :ref:`SetWinRect`.

    To change a button's text, use :ref:`SetButtonText`.

    To change a button's colors, use :ref:`SetButtonColors`.

    To hide a button, use :ref:`TargetButton` and :ref:`HideWin`.

    To redisplay a hidden button, use :ref:`TargetButton` and :ref:`ShowWin`.

    To create a group of buttons that you move as a unit, use :ref:`CreatePanel`.

    To add a button to a panel, use :ref:`AddButtonToPanel`.

    To display a list of all your buttons and panels, use :ref:`ListButtons`.


**Use AutoExec**

    You should create all your buttons and panels in an AutoExec command that executes automatically when the script loads.

    Destroying a button

    Buttons get destroyed when you load or unload a script.

**Example**

    <Command AutoExec>
        <CreateButton Button1 100 100 50 50 On>

**Related topics**

- :ref:`AddButtonToPanel`
- :ref:`CreateButton`
- :ref:`CreateColoredButton`
- :ref:`CreatePictureButton`
- :ref:`CreatePanel`
- :ref:`ListButtons`
- :ref:`SetButtonColors`
- :ref:`SetButtonCommand`
- :ref:`SetButtonHotkey`
- :ref:`SetButtonText`
- :ref:`SetButtonStyle`
- :ref:`TargetButton`