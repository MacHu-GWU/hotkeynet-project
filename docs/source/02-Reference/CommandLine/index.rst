.. _CommandLine:

CommandLine
==============================================================================
Makes the command line window open.

**Syntax**

    <CommandLine name>

**Parameters**

    Name is optional. If it's specified, it gets entered automatically on the command line when the command line opens, and HotkeyNet expects it to be the name of a user-defined command that you created with :ref:`Command`.

**Remarks**

    To learn how to use this command, see :ref:`14-user-defined-commands` in the instruction section.

    ThirdPartyCommandLine does the same thing as this command. Use CommandLine in windowed mode and ThirdPartyCommandLine in full-screen mode.

**Examples**

    The following hotkey makes the command window open with "broadcast" already typed in it. The word "broadcast" is defined elsewhere in the file with :ref:`Command`::

        <Hotkey F7>
             <CommandLine broadcast>

**Related pages**

- :ref:`Command`
- :ref:`ThirdPartyCommandLine`
- :ref:`14-user-defined-commands`
