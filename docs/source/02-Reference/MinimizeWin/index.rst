.. _MinimizeWin:

MinimizeWin
==============================================================================
This command was called Minimize before build 107.

Minimizes the currently targeted window.

**Syntax**

::

    <MinimizeWin>

**Parameters**

    None.

**Remarks**

    Minimizes the window that was targeted with TargetWin,  SendWin, etc.

**Example**

::

    <Hotkey F1>
        <SendPC local>
            <TargetWin Uber666>
            <MinimizeWin>

**Related topics**

- :ref:`HideWin`
- :ref:`MaximizeWin`
- :ref:`MinimizeWin`
- :ref:`RestoreWinSize`
- :ref:`ShowWin`
