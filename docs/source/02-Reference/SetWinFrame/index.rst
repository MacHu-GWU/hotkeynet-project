.. _SetWinFrame:

SetWinFrame
==============================================================================
Sets or removes frame styles for the currently targeted window.

**Syntax**::

    <SetWinFrame styles>

**Parameters**

    Styles must be None or any combination of the following:

    - ThickFrame
    - Caption
    - Border
    - DlgFrame
    - ClientEdge
    - DlgModalFrame
    - StaticEdge
    - WindowEdge

**Remarks**

    SetWinFrame affects the window that was targeted with :ref:`TargetWin`, :ref:`SendWin`, etc.

    SetWinFrame calls the operating system function SetWindowLong.

**Examples**

    The following hotkey removes the window frame from World of Warcraft::

        <Hotkey F1>
            <TargetWin "World of Warcraft">
            <SetWinFrame None>

    The following hotkey restores the window frame to World of Warcraft::

        <Hotkey F2>
            <TargetWin "World of Warcraft">
            <SetWinFrame Caption Border>

    The following hotkey toggles the window frame off and on::

        <Hotkey F3>
            <Toggle>
                <TargetWin "World of Warcraft">
                <SetWinFrame None>
            <Toggle>
                <TargetWin "World of Warcraft">
                <SetWinFrame Caption Border>

**Related Topics**

    - :ref:`RemoveWinFrame`
