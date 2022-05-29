.. _SetButtonCommand:

SetButtonCommand
==============================================================================
Assigns a command to a button so you can trigger the command by left-clicking the button.

**Syntax**::

    <SetButtonCommand button command [args]>

**Parameters**

    Button is the name of the button.

    Command is the name of the command.

    Args are arguments that get passed to the command. They are optional.

**Remarks**

    A button can trigger hotkeys or a command but not both.

    The button's command gets triggered when you press the left mouse button. If instead you want it to happen when you release the button, you must use SetButtonHotkey and call the command from a hotkey that was defined with HotkeyUp.

**Example**

    Suppose you create the following button::

        <CreateButton B1 0 0 80 100>

    And you also create the following command::

        <Command C1>
           <ToggleWin %1% %2%>

    And you want the command to execute when you click the button. You can make that happen like this::

        <SetButtonCommand B1 C1 win1 win2>

The previous line has to be put in a hotkey or command somewhere so it executes and takes effect.

**Related topics**

    - :ref:`Command`
    - :ref:`CreateButton`
    - :ref:`SetButtonHotkey`
