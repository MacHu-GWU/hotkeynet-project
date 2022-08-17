.. _CreatePanel:

CreatePanel
==============================================================================
Creates a window on the screen that can contain buttons.

**Syntax**

::

    <CreatePanel name x y width height>

**Parameters**

    ``Name`` is the name of the panel.
    ``X`` is the horizontal screen coordinate of the panel's upper left corner.
    ``Y`` is the vertical screen coordinate of the panel's upper left corner.
    ``Width`` is the panel's width.
    ``Height`` is the panel's height.

**Remarks**

    Panels get destroyed when you load or unload a script.

    Panels are windows. You can use all of HotkeyNet's window commands with panels.

**Use AutoExec**

    You should create all your buttons and panels in an AutoExec command that executes automatically when the script loads.

**Example**

    ::

        <Command AutoExec>
            <CreatePanel P1 100 100 50 50>


    Panels are windows, and you can use all of HotkeyNet's window commands with them. For example, here's a hotkey that makes a panel stay on top of other windows:


    ::

        <Hotkey F2>
            <TargetWin P1>
            <AlwaysOnTop on>

**Related topics**

- :ref:`AddButtonToPanel`
- :ref:`CreateButton`
- :ref:`SetPanelDrag`
- :ref:`SetPanelLayout`
- :ref:`SetPanelPicture`
- :ref:`SetPanelStyle`
