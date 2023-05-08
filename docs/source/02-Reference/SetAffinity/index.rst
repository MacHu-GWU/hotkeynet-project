.. _SetAffinity:

SetAffinity
==============================================================================
Many thanks to Xanthic42 for suggesting this command.

Sets the CPU affinity of the process that created the currently targeted window.

**Syntax**

::

    <SetAffinity cpu [cpu [cpu...]]>

    or

    <SetAffinity all>

**Parameters**

    CPU is a number between 0 and 31 that indicates a logical processor. You must specify at least one.

    The word "all" means all logical CPUs in the machine.

**Remarks**

    This command does the same thing as Windows's Processor Affinity pop up:

    Before you call this command, you must target a window with SendWin, SendWinMF, TargetWin, TargetChild, etc. This command acts on the process that created that targeted window.

    CPUs are numbered starting with zero. This means, for example, that the fourth CPU is number three.

    SetAffinity calls the operating system command SetProcessAffinityMask.

    The 32-CPU limit is built into Windows, not HotkeyNet. Considering that Intel plans to release chips with 16 logical CPUs in late 2008, Microsoft doesn't seem to be looking very far ahead.

**Example**

    The following hotkey assigns a process on the local PC to the first logical CPU, which is number zero::

        <Hotkey F1>
           <SendPC local>
              <TargetWin "Dark Age of Camelot">
              <SetAffinity 0>

    The following hotkey assigns a process on a remote PC to the second and fourth logical CPUs, which are numbers one and three::

        <Hotkey F9>
           <SendPC 192.168.1.104>
              <TargetWin MyBelovedWindow>
              <SetAffinity 1 3>

    The following hotkey allows the process to run on all logical CPUs::

        <Hotkey F9>
           <SendPC 192.168.1.104>
              <TargetWin MyBelovedWindow>
              <SetAffinity all>
