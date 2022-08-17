.. _SendWinS:

SendWinS
==============================================================================
Specifies the window that will receive keystrokes and mouse clicks. Designed for background windows.

**Syntax**

::

    <SendWinS window>

**Parameters**

    Window is the name of the window that will receive keystrokes and mouse clicks.

**Remarks**

    SendWinS is used with background windows. It calls the operating system command SendMesssage which waits after each character for a response from the receiving thread. This makes SendWinS very slow but possibly more reliable than SendWinM.

**Example**

::

    <Hotkey F1>
       <SendPC local>
          <SendWinS Ubertronic>
             <Key F7>

**Related topics**

- :ref:`comparison-chart-of-send-modes`
- :ref:`9-Sending-Keystokes-to-Windows`
- :ref:`10-Sending-to-Background-Windows`
- :ref:`SendWin`
- :ref:`SendFocusWin`
- :ref:`SendWinM`
- :ref:`SendWinMF`
- :ref:`SendWinS`
- :ref:`SendWinSF`
