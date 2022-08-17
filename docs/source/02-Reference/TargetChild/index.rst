.. _TargetChild:

TargetChild
==============================================================================
Sets the targeted window. This is the window to which keystrokes and mouseclicks get sent. Use this command when the target is a child window or control.

**Syntax**

::

    <TargetChild class number>

**Parameters**

    Class is the class name of the child window that will receive keystrokes and mouse clicks.

    Number is the index of the child window. For example, if a main window contains four controls with the same class name, and you want to target the third, you would write "3" for number.

**Remarks**

    In order to send keystrokes to a child window or control when it's in the background, you must use this command. You must also use either the PostMesage or SendMessage send modes. These can be chosen explicitly with SetSendMode or implicitly with SendWinM or SendWinMF.

    TargetChild looks for the specified child window inside the main window that is already targeted.

    If no main window is targeted, TargetChild doesn't know where to look.

    Therefore, before using TargetChild, you must use a command that targets a main window such as TargetWin, SendWin, SendWinMF, etc.

    If you want to target a child of a child, call TargetChild repeatedly.

**Example**

    The following definition sends to Notepad in the background::

        <hotkey F1>
           <sendpc local>
               <TargetWin Untitled>
               <TargetChild Edit 1>
               <SetSendMode PostMessage>
               <text wow this works>

**Related topics**

- :ref:`TargetWin`
