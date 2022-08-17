.. _Command:

Command
==============================================================================
Creates a user-defined command that can be used as a subroutine or entered on a command line.

Syntax::

    <Command name>

Parameters

    Name is the name of a command that you will be able to use as a subroutine or enter on a command line.

Remarks

    To learn how this command is used, see :ref:`14-user-defined-commands` and :ref:`15-Subroutines` in the instruction section.

    User-defined commands can be used exactly like built-in commands.

    Unlike built-in commands, user-defined commands can be used with :ref:`CommandLine` or :ref:`ThirdPartyCommandLine`.

    The body of your command can refer to its arguments as either individual words or a continuous string of text. For example, to refer to the second word, use ``%2%`` in the command. To refer to all the input together, use ``%ALL%``.

Limitations

    In the current version of the program, labels and if-statements cannot be used in commands. This restriction will be removed in future versions.

Example

    The following command causes two characters to say "something" when you enter "broadcast something" on a command line.

    ::

        <Command broadcast>
            <SendPC local>
                <SendWinM Ubertastic>
                    <Text /say %all%><Key enter>
                <SendWinM UberTwo>
                    <Text /say %all%><Key enter>

    The following command illustrates the difference between ``%#%`` and ``%ALL%``.

    ::

        <Command test>
            <SendPC local>
                <SendWin Untitled>
                    <Text Arg 1 = %1%><key enter>
                    <Text Arg 2 = %2%><key enter>
                    <Text All = %all%><key enter>

Related topics

- :ref:`14-user-defined-commands`
- :ref:`15-Subroutines`
- :ref:`CommandLine`
- :ref:`ThirdPartyCommandLine`
