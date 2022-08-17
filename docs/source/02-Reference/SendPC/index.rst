.. _SendPC:

SendPC
==============================================================================
Identifies the PC to which instructions get sent.

Syntax::

    <SendPC pc>

Parameters

    PC must be either an IP address or the word "local".

Remarks

    The local machine is the one the hotkey file is on. For this machine, you must write "local."

    For other machines, write the IP address.

    If you omit SendPC from a hotkey definition, "local" is used by default.

Example

    The following hotkey sends "L" to the local machine and "R" to a remote machine::

        <Hotkey F1>
           <SendPC local>
              <SendFocusWin>
              <Text L>
           <SendPC 192.168.1.102>
              <SendFocusWin>
              <Text R>

    SendPC is missing from the following definition, so "local" is used by default::

        <Hotkey F1>
           <toggle Wow1 Wow2>

    The following two definitions show how to use a variable with SendPC. When F1 is pressed, the variable gets replaced by "local" and an IP address, and "Y" gets typed on both machines::

        <Command TypeY>
           <SendPC %1%>
              <SendFocusWin>
              <Text Y>

        <Hotkey F1>
           <TypeY local>
           <TypeY 192.168.1.102>
