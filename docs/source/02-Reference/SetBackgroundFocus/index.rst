.. _SetBackgroundFocus:

SetBackgroundFocus
==============================================================================
This command can sometimes force a background window to accept keystrokes and mouse clicks.

**Syntax**

::

    <SetBackgroundFocus>

**Parameters**

    None.

**Remarks**

    This command affects the window that was targeted with TargetWin, SendWinM, etc.

    This is a low-level command. It's usually more convenient to use a higher-level command, SendWinMF, which includes this command automatically.

    This command is designed to help you send keystrokes to windows while they are in the background. Windows is not designed to allow that to happen, so HotkeyNet has a repertoire of tricks that you can try. One of its tricks is called background focus. There are several ways to make your hotkeys perform this trick:

    1. Use this command.
    2. Use SetSendMode with its BackgroundFocus option.
    3. Use SendWinMF.

**Example**

::

    <hotkey F1>
       <sendpc local>
          <TargetWin Game2>
          <SetSendMode SendMessage>
          <SetBackgroundFocus>
          <Text Our father who art in Heaven>
          <KillBackgroundFocus>
