.. _10-Sending-to-Background-Windows:

10. Sending to Background Windows
==============================================================================
Windows isn't designed to send keystrokes to background windows. HotkeyNet has to play tricks with the Windows API to make it happen, and the results are less than perfect.

    Background sending can never work perfectly because Windows isn't designed to do it. It works with some keystrokes and some programs, but not all.

HotkeyNet offers four ways to send to background windows: :ref:`SendWinM`, :ref:`SendWinS`, :ref:`SendWinMF`, and :ref:`SendWinSF`.

**SendWinM**

    :ref:`SendWinM` uses Windows’s WM_KEYDOWN and WM_KEYUP messages to deliver keystrokes. The advantage of :ref:`SendWinM` is that you don't have to adjust any settings. Just put it in a hotkey definition and if it works, it works.

**SendwinMF**

    :ref:`SendWinMF` is a supercharged version of SendWinM. It takes additional steps to try to force windows to accept keystrokes while they are in the background. Its advantage is that it works with more programs than :ref:`SendWinM` does. Its disadvantage is that you usually have to adjust a setting to make it work properly.

    You usually have to adjust the Background Focus Delays setting to make :ref:`SendWinMF` work properly.

    You can make this adjustment on the Settings panel or with the :ref:`SetBackgroundFocusDelays` command. See SendWinMF for more information.

**SendWinS and SendwinSF**

    :ref:`SendWinS` and :ref:`SendWinSF` are simlar to the methods just described except that they use the operating system function SendMessage instead of PostMessage. For more information, click on the links.

    (简单来说 SendMessage 是 sync, 需要等待 window 的 thread 相应, 而 PostMessage 是 async, 请参考: https://docs.microsoft.com/en-us/windows/win32/wintouch/sendmessage--postmessage--and-related-functions)

**Limitations**

    Background modes work with some applications but not all.

    When you use a background mode, you may have to target a child window (control) which is not the the main window you see on the screeen.

    If you want to send shifted (upper and lower case) characters properly, you must use the new version of SendWinS or SendWinSF. Select the new version on the Send Mode Settings Panel.

**Note to World of Warcraft Players**

    As described above, SendWinMF inserts tiny delays. This is done only for technical reasons and the default values are too short to affect game play. If you are concerned that these delays might violate the rules in World of Warcraft, use SendWinM instead. SendWinM works fine for sending single keystrokes in WoW. SendWinMF is required only for chatline commands which may violate the rules for other reasons.
