.. _15-Subroutines:

15. Subroutines
==============================================================================
User-defined commands can be used as subroutines by including them inside other commands or hotkey definitions. Here's an example.

Suppose you have a hotkey that sends a keystroke to a window, waits 500 milliseconds, and sends the keystroke again. It would look like this::

    <Hotkey F1>
       <SendPC local>
          <SendWinM WoW1>
             <Key 5>
             <Wait 500>
             <Key 7>

That definition is pretty short, so it works fine. But suppose you want the hotkey to perform the same action in five different windows? The definition would be very long. A subroutine can help by making it shorter. To do this, create a user-defined command::

    <Command SendTwoKeys>
       <SendPC %1%>
          <SendWinM %2%>
             <Key %3%>
             <Wait 500>
             <Key %4%>

And define the hotkey like this::

    <Hotkey F1>
       <SendTwoKeys local wow1 5 7>
       <SendTwoKeys local wow2 5 7>
       <SendTwoKeys local wow3 5 7>
       <SendTwoKeys local wow4 5 7>
       <SendTwoKeys local wow5 5 7>

Subroutines on remote PCs

In the previous example, all the windows are on the local PC where you press the hotkey. But what if some of the windows are on remote PCs? In that case, performance is improved if you load the subroutine on the remote PCs and call it from the local PC. To do this, remove SendPC from the command (it will be included in the hotkey instead) and then load the command definition in hotkey files on every PC::

    <Command SendTwoKeys> // NEW VERSION
       <SendWinM %1%>     // LOAD THIS ON ALL PCs
             <Key %2%>
             <Wait 500>
             <Key %3%>

Now we define the hotkey like this::

    <Hotkey F1>
       <SendPC Local>
          <SendTwoKeys wow1 5 7>
          <SendTwoKeys wow2 5 7>
       <SendPC 192.168.1.102>
          <SendTwoKeys wow1 5 7>
          <SendTwoKeys wow2 5 7>

Technical note

You can use a hotkey as a subroutine too. Call it with DoHotkey. This can be useful because some keywords can be included in hotkeys but not in commands.

Related topics

Command
CommandLine
ThirdPartyCommandLine

