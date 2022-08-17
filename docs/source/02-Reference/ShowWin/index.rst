.. _ShowWin:

ShowWin
==============================================================================
Makes a hidden (invisible) window visible.

**Syntax**

::

    <ShowWin>

**Parameters**

    None.

**Remarks**

    Shows (makes visible) the window that was targeted with TargetWin, SendWin, etc. To make a window invisible, use HideWin.

**Example**

::

    <Hotkey F1>
       <SendPC local>
           <TargetWin Uber666>
           <ShowWin>

**Related topics**

- :ref:`HideWin`
- :ref:`MaximizeWin`
- :ref:`MinimizeWin`
- :ref:`RestoreWinSize`
- :ref:`ShowWin`
