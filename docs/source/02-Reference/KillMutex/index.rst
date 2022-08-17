.. _KillMutex:

KillMutex
==============================================================================
Deletes a mutex.

**Syntax**

::

    <KillMutex name>

**Parameters**

    Name is the name of a mutex.

**Remarks**

    Some programs prevent you from starting more than a certain number of copies of themselves. If you try to launch one of these programs while it's already running, you get either an error message or the window you started earlier.

    This command removes those limits. It lets you run as many copies as you want until you run out of RAM or other resources.

    This command works by deleting a mutex, which is a kind of temporary software object created by the operating system. Mutexes are not part of the program you're trying to influence. This command doesn't do anything to that program directly. The deletion is temporary — the objects come back each time the target program starts running.

**Windows 7**

    In the current version of HotkeyNet, KillMutex doesn't work with Windows 7. This will be fixed in a future version.
