.. _SendWinM:

SendWinM
==============================================================================
Specifies the window that will receive keystrokes and mouse clicks. Designed for background windows.

**Syntax**

::

    <SendWinM window>

**Parameters**

    Window is the name of the window that will receive keystrokes and mouse clicks.

**Remarks**

    SendWinM is used with background windows. It calls the operating system command PostMesssage which does not wait after each character for a response from the receiving thread. This makes SendWinM fast but possibly less reliable than SendWinS.

**Limitations**

    SendWinM converts characters to lowercase.. This may be fixed in future versions.

    Like all background modes, SendWinM has trouble sending modified key combinations like Alt X, Shift Ctrl F3, etc.

    To avoid these limitations use the new versions of SendWinS or SendWinSF instead.

**Example**

::

    <Hotkey F1>
       <SendPC local>
          <SendWinM Ubertronic>
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