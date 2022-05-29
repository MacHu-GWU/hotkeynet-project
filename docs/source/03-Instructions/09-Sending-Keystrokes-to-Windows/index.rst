.. _9-Sending-Keystokes-to-Windows:

9. Sending Keystrokes to Windows
==============================================================================
HotkeyNet provides several ways to send keystrokes to windows. Each way has advantages and disadvantages.

**SendWin**

SendWin is the recommended way to send keystrokes. It sends every keystroke correctly and never fails. Programs treat SendWin's keystrokes exactly like real ones.

If Sendwin is so great, why do you need any other methods? Because Sendwin can only send to the foreground window. That's the window in front of all the others.

If you use SendWin on a background window, HotkeyNet moves the window to the front as if you alt-tabbed and then it sends the keystrokes. This works perfectly well, but it's a little slow because alt-tabbing takes time. (You can put the windows back in their original order with Restore.)

The bottom line:

    - If you are sending to a foreground window, use SendWin because it works perfectly.
    - If you are sending to a background window and you don't mind a short delay while SendWin alt-tabs the window to the foreground, use SendWin because it delivers every keystroke correctly and never fails.
    - If you want to send to a background window while it stays in the background, see the next page.

**SendFocusWin**

    SendFocusWin is another method for sending keystrokes to the foreground window. It's exactly the same as SendWin except that it sends keystrokes to the window that has the focus (the window that would receive keystrokes if you typed them at the keyboard). In contrast, SendWin delivers keystrokes to a particular window that you specify by name. SendFocusWin never moves windows to the foreground because the focus window is already there.
