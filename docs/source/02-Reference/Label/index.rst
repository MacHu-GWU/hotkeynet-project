.. _Label:

Label
==============================================================================
Creates a mailing label.

**Syntax**

::

    <Label name ip sendmode [window]>

**Parameters**

    Name is the name you'll use to refer to this label.

    IP is "local" or an IP address.

    Sendmode is :ref:`SendWin`, :ref:`SendFocusWin`, :ref:`SendWinM`, :ref:`SendWinMF`, :ref:`SendWinS`, or :ref:`SendWinSF`.

    Window is the name of the target window. This parameter should be omitted when Sendmode is SendFocusWin; otherwise it is required. This parameter is case-sensitive like all window names in HotkeyNet.

**Remarks**

    Labels are used with :ref:`SendLabel`.

**Example**

    The following example creates a hotkey that sends a keystroke to both Joe and Sam::

        <Label joe Local SendWin Game1>
        <Label sam 192.168.1.102 SendWin Game2>

        <Hotkey F1>
           <SendLabel sam, joe>
              <Key %Trigger%>

**Related pages**

    :ref:`SendLabel`
