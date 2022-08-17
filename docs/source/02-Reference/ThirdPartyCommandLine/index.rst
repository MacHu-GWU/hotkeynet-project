.. _ThirdPartyCommandLine:

ThirdPartyCommandLine
==============================================================================
Allows you to enter commands to HotkeyNet using a text-entry field in a third-party program.

**Syntax**

    <ThirdPartyCommandLine name prefix suffix delay>

**Parameters**

    Name is a command that you've defined with the :ref:`Command` command. This word will be displayed at the beginning of the command line to save you the trouble of typing it. If you don't want a word to be displayed this way, specify 0 (zero) for this parameter.

    ``Prefix`` is the name of a key that will be sent to the foreground window before you enter text. If you don't want to send this key, write 0 (zero).

    ``Suffix`` is the name of a key that will be sent to the foreground window after you enter text. If you don't want to send this key, write 0 (zero).

    ``Delay`` is the number of milliseconds that HotkeyNet waits after it types the prefix. This pause is often needed because many games take a long time to move their cursors from their main windows to their chat lines.

**Remarks**

    To learn how this command is used, read :ref:`14-user-defined-commands` in the instruction section.

    This command works exactly like :ref:`CommandLine`. They both let you type commands that you've defined with HotkeyNet. There's just one crucial difference.

    With CommandLine, you enter your command in HotkeyNet's pop-up window. With this command, you enter your command in a text-entry field that belongs to some other program you're using. For example, you could type your command on the chat line of a game.

    Why does this second command exist? Because CommandLine doesn't work in full screen mode. This one does.

    As an option, this command will automatically move your cursor to the text-entry field. It can also erase what you've typed there after HotkeyNet receives the command so the other program doesn't respond to it. You make these things happen by specifying keystrokes that HotkeyNet sends before and after you type the command. In many games, for example, the "/" key makes the cursor enter the chat line and the escape key erases whatever you typed there. See the examples below for the exact syntax.

    To cancel a command, press Esc. To tell HotkeyNet that you're finished typing, press Enter.

    This command always targets the foreground window and always uses SendWin to send the prefix and suffix keystrokes. If you want to target some other window, bring it to the foreground before calling ThirdPartyCommandLine with :ref:`TargetWin` and :ref:`SetForeground`.

**Examples**

    The following hotkey makes the cursor jump to the chat line of a typical game so you can enter a command called "port" to HotkeyNet. We assume here that you've defined "port" with the :ref:`Command` command. OEM_2 is the name of the slash key on U.S. keyboards; if you're in another country, click here to learn how to find the name for your keyboard::

        <Hotkey F7>
            <SendPC local>
            <ThirdPartyCommandLine port OEM_2 ESC 100>

    The previous hotkey targets the window that happens to be in the foreground. Normally this is what you want to do (if it's not, you should probably use :ref:`CommandLine` instead). But if you want to target some other window, bring it to the foreground first, like this::

        <Hotkey F7>
            <SendPC local>
            <TargetWin SomeOtherWindow>
            <SetForeground>
            <Wait 100>
            <ThirdPartyCommandLine port OEM_2 ESC 100>

**Related pages**

- :ref:`Command`
- :ref:`CommandLine`
- :ref:`14-user-defined-commands`
