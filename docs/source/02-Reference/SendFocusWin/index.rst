.. _SendFocusWin:

SendFocusWin
==============================================================================
Sends keystrokes to the window that has the focus.

**Syntax**::

    <SendFocusWin>

**Parameters**

    None.

**Remarks**

    SendFocusWin sends keystrokes to the window that has the focus. That's the window that would receive keystrokes if you typed at the keyboard.

    SendFocusWin can be used to to imitate a key broadcasting program. This is shown in the second example below.

    The following two lines are equivalent::

       <SendFocusWin>
       <SetSendMode SendInput NoTarget>

    SendFocusWin uses the same send method as :ref:`SendWin`. The only difference between them is that :ref:`SendWin` brings a specified window to the foreground before it types keystrokes. SendFocusWin does not.

    SendFocusWin 和 SendWin 的区别是, SendWin 会把指定窗口带到最前面, 而 SendFocusWin 不会, 因为它不接受 Label 作为参数, 已经是把动作发送到最前面的窗口了, 没有必要 "带到最前面".

**Examples**

    The following hotkey types "Happy birthday to you!" into the window that has the focus::

        <Hotkey F1 >
            <SendPC local>
               <SendFocusWin>
               <Text Happy birthday to you!>


    The following hotkey passes the trigger key "G" to the window that has the focus. (You can also use PassThrough for this purpose)::

        <Hotkey G>
            <SendPC local>
               <SendFocusWin>
               <Key G>

**Related topics**

    - :ref:`SetForegroundWin`
    - :ref:`SetActiveWin`
