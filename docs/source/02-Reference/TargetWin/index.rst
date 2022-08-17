.. _TargetWin:

TargetWin
==============================================================================
Sets the targeted window. This is the window to which keystrokes and mouseclicks get sent. Use this command when the target is a main (top-level) window.

**Syntax**

::

    <TargetWin window>

**Parameters**

    Window is the name of the window that will receive keystrokes and mouse clicks.

**Remarks**

    Use this command to target a high-level window. To target a child, target the parent with this command, then use TargetChild.

**Example**

    The following definition::

        <hotkey F1>
           <sendpc local>
               <TargetWin "My difficult background Window">
               <SetSendMode PostMessage>
               <text hi boss!>

    is equivalent to this one::

        <hotkey F1>
           <sendpc local>
               <SendWinM "My difficult background Window">
               <text hi boss!>

**Related topics**

- :ref:`TargetChild`
