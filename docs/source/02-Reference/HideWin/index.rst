.. _HideWin:

HideWin
==============================================================================
This command was called Hide before build 107.

Makes a window invisible.

**Syntax**

::

    <HideWin>

**Parameters**

    None.

**Remarks**

    This command hides the window that was targeted by :ref:`TargetWin`, :ref:`SendWin`, etc. A hidden window is invisible. If you want to shrink a window, use :ref:`MinimizeWin`.

**Example**

::

    <Hotkey F1>
       <SendPC local>
           <TargetWin Uber666>
           <HideWin>

**Related topics**

- :ref:`HideWin`
- :ref:`MaximizeWin`
- :ref:`MinimizeWin`
- :ref:`RestoreWinSize`
- :ref:`ShowWin`
