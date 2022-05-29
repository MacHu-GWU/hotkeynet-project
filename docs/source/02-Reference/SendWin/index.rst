.. _SendWin:

SendWin
==============================================================================
Specifies window that will receive keystrokes and mouse clicks. Input will be injected with Windows's SendInput command.

Syntax::

    <SendWin window>

Parameters

    Window is the name of the window that will receive keystrokes and mouse clicks.

Remarks

    If you use SendWin with a background window, HotkeyNet tells the operating system to bring the window to the foreground. The operating system takes a long time to do this. But HotkeyNet doesn't wait. It sends your keystrokes immediately. If they are sent before the window arrives in the foreground, they won't be received by the window. To avoid this problem, add a Wait after SendWin. This is illustrated in the second example below.

    If you use SendWin with a background window, you can use Restore at the end of the hotkey to put the original foreground window back.

    SendWin is only one of several send modes. One of the others may be more suitable for your purpose. See Related Topics below for more information.

Examples

    ::

        <Hotkey F1>
           <SendPC local>
              <SendWin UberOne>
                 <Text hi!>
              <SendWin UberTwo>
                 <Text bye!>
            <Restore>

    As explained above in remarks, you may need to add a <Wait> to give SendWin time to bring its target to the foreground.

    ::

        <Hotkey F1>
           <SendPC local>
              <Wait 50>
              <SendWin UberOne>
                 <Text slowpoke!>
