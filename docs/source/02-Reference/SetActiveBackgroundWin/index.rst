.. _SetActiveBackgroundWin:

SetActiveBackgroundWin
==============================================================================
This command will be added in build 118

Activates the currently targeted window without changing Z order.

**Syntax**

::

    <SetActiveBackgroundWin>

**Parameters**

    None.

**Remarks**

    SetActiveBackgroundWin activates the window that was targeted with :ref:`TargetWin`, :ref:`TargetChild`, :ref:`SendWin`, etc.

    This command is the equivalent of calling the operating system command SetActiveWindow except that the target window remains in the background (is not brought to the top of the Z order).

**Limitations**

    The title bar of the targeted window does not get highlighted even though the window has the focus.

    Sometimes pieces of an underlying window get drawn in the targeted window by mistake.

**Example**

::

    <hotkey F1>
       <sendpc local>
           <TargetWin wow1>
           <SetActiveBackgroundWin>
           <SendFocusWin>
           <Key 5>

**Related topics**

- :ref:`SetForegroundWin`
- :ref:`SetFocusWin`
