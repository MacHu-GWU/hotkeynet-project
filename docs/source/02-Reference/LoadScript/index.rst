.. _LoadScript:

LoadScript
==============================================================================
Loads a script.

**Syntax**

::

    <LoadScript [pathname]>

**Parameters**

    ``Pathname`` is optional. It's the path and name of the script.

**Remarks**

    HotkeyNet automatically unloads the previously loaded script before loading the new one.

    If pathname is omitted, a file selection window pops up.

    If pathname is provided, the file is loaded without a pop up window.

    If the pathname contains spaces, you must put quotation marks around it.

**Examples**

    The following example loads a specified script on a remote machine without popping up a window::

        <Hotkey RAlt F12>
           <SendPC 192.168.1.102>
           <LoadScript c:\yadayada.txt>

    The following example makes a selection window pop up on the local machine so you can choose a script and load it::

        <Hotkey RAlt F12>
           <SendPC Local>
           <LoadScript>

**Related topics**

- :ref:`UnloadScript`
