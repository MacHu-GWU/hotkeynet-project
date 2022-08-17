.. _Run:

Run
==============================================================================
Starts a program and targets its top-level window.

**Syntax**

::

    <run pathname [arguments] [as user [password]]>

**Parameters**

    - ``Pathname`` is the path and name of the executable file.
    - ``Arguments`` are command line arguments. If there is more than one argument, put them all together in double quotation marks.
    - ``As`` is the word "as." You must include this word if you specify a user account.
    - ``User`` is the name of the Windows user.
    - ``Password`` is the Windows user's password.

**Remarks**

    You can use either :ref:`Run` or :ref:`Open` to start a program. The advantages of :ref:`Run` are that it automatically targets the program's top-level window, and you don't need to use Wait after it. The advantage of :ref:`Open` is that it uses a less intrusive method (unlike Run, it doesn't start the program as a child process).

    Run calls the operating system function ``CreateProcess``. Open calls ``ShellExecute``.

    The pathname is the complete path and name of the file starting from the drive letter. Microsoft calls this a "fully qualified pathname." Here are some examples::

        "c:\Program files\windows\system32\notepad.exe"
        "c:\Program files\windows\World of Warcraft\Wow.exe"
        "c:\Documents and Settings\Owner\Desktop\HotkeyNet.exe"

    Those examples are inside quotation marks because they have spaces in them.

    The second parameter is optional. If there is more than one symbol or argument in this parameter, enclose it in quotation marks.

**Batch files**

    To run a batch file, you must run Windows's command interpreter with either the /c or /k option and pass the name of the batch file as an argument::

        <Run C:\Windows\System32\cmd.exe "/c C:/MyBat.bat">

    Note that /c is included as part of the argument to cmd.exe. This causes the command window to close after the batch file finshes. If you want the window to stay open, use /k instead.

**Examples**

    The following example starts Notepad on the local PC::

        <Hotkey F1>
        <SendPC local>
        <Run "c:\program files\windows\system32\notepad.exe">

    The following example starts Notepad on a remote PC::

        <Hotkey F1>
        <SendPC 192.168.1.101>
        <Run "c:\program files\windows\system32\notepad.exe">

    The following example starts Notepad on the local PC using Joe's account and password::

        <Hotkey F1>
        <SendPC Local>
        <Run "c:\program files\windows\system32\notepad.exe"
              as Joe goo714>

**Related topics**

- :ref:`CloseWin`
- :ref:`Open`
