.. _Open:

Open
==============================================================================
Starts a program.

**Syntax**

::

    <open pathname [arguments]>

**Parameters**

    Pathname is the path and name of the executable file.

    Arguments are command line arguments. If there is more than one argument, put them all together in double quotation marks.

**Remarks**

    You can use either Run or Open to start a program. The advantages of Run are that it automatically targets the program's top-level window, and you don't need to use Wait after it. The advantage of Open is that it uses a less intrusive method (unlike Run, it doesn't start the program as a child process).

    Run calls the operating system function CreateProcess. Open calls ShellExecute.

    The pathname is the complete path and name of the file starting from the drive letter. Microsoft calls this a "fully qualified pathname." Here are some examples::

        "c:\Program files\windows\system32\notepad.exe"
        "c:\Program files\windows\World of Warcraft\Wow.exe"
        "c:\Documents and Settings\Owner\Desktop\HotkeyNet.exe"

    Those examples are inside quotation marks because they have spaces in them.

    The second parameter is optional. If there is more than one symbol or argument in this parameter, enclose it in quotation marks.

**Examples**

    The following example starts Notepad on the local PC::

        <Hotkey F1>
        <SendPC local>
        <Open "c:\program files\windows\system32\notepad.exe">

    The following example starts Notepad on a remote PC::

    <Hotkey F1>
    <SendPC 192.168.1.101>
    <Open "c:\program files\windows\system32\notepad.exe">

**Related topics**

- :ref:`CloseWin`
- :ref:`Run`
