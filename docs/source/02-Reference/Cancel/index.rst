.. _Cancel:

Cancel
==============================================================================
Cancels current and pending actions.

**Syntax**::

    <Cancel>

**Parameters**

    None.

**Remarks**

    You must send this to each PC where you want to cancel actions.

**Examples**

    The following hotkey cancels actions on the local PC::

        <Hotkey F1>
           <SendPC local>
              <Cancel>

    The following hotkey cancels actions on a remote PC::

        <Hotkey F1>
           <SendPC 192.168.1.106>
              <Cancel>

    The following hotkey cancels actions on three PCs::

        <Hotkey F1>
           <SendPC local>
              <Cancel>
           <SendPC 192.168.1.103>
              <Cancel>
           <SendPC 192.168.1.105>
              <Cancel>
