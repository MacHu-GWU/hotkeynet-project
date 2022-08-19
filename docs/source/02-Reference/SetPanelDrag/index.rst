.. _SetPanelDrag:

SetPanelDrag
==============================================================================
This command is new in build 189

Many thanks to Aldarys for suggesting this command.

Turns on, turns off, or toggles panel dragging.

**Syntax**

::

    <SetPanelDrag Switch>

**Parameters**

    Switch must be On, Off , or Toggle.

**Remarks**

    Normally you need to click on a window's title bar to drag it with the mouse. But people often remove a panel's title bar with SetPanelStyle, making it impossible to drag. This command solves that problem.

    When panel dragging is on, you can move a panel by dragging its background or a button. When you're finished dragging, turn panel dragging off so buttons work normally again.

    Panel dragging can be used to move "naked" buttons as well as panels.

    You can use menus instead

    You don't need to use this command. You can also turn panel dragging on and off with menus. Click "Start dragging panels" and "Stop dragging panels" on the Action Menu or Tray Menu.

**Examples**

    The following hotkey turns on panel dragging.

    ::

        <Hotkey F1>
           <SetPanelDrag on>

    The following hotkey turns dragging off.

    ::

        <Hotkey F1>
           <SetPanelDrag off>

    The following hotkey turns dragging on if it's off and off if it's on.

    ::

        <Hotkey F1>
            <SetPanelDrag toggle>
