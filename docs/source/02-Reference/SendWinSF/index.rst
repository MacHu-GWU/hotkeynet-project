.. _SendWinSF:

SendWinSF
==============================================================================
Specifies the window that will receive keystrokes and mouse clicks. Tries even harder than SendWinS to send keystrokes to background windows.

**Syntax**

::

    <SendWinSF window>

**Parameters**

    Window is the name of the window that will receive keystrokes and mouse clicks.

**Important note**

    You usually have to adjust a setting to make SendWinSF work. See below for details.

**Remarks**

    SendWinSF is used with background windows. It calls the operating system command SendMesssage which waits after each character for a response from the receiving thread. This makes SendWinSF very slow but possibly more reliable than SendWinMF.

    SendWinSF is similar to :ref:`SendWinS` but makes even greater efforts to force background windows to accept keystrokes.

    If SendWinSF is stronger than :ref:`SendWinS`, why not use it all the time? Because it's more complicated. It requires an adjustment.

    To make SendWinSF work, you usually have to adjust the background focus delays

    SendWinSF pauses briefly before and after it sends keystrokes. These pauses are called background focus delays. You should usually keep the length of the first pause at zero. Make the second one longer if keystrokes don't reach the background window. Make the second one shorter if manually-typed keystrokes leak from the foreground window into the background one.

    There are two ways to make the adjustment: the Settings panel or :ref:`SetBackgroundFocusDelays`.

**Note to World of Warcraft Players**

    As mentioned above, SendWinSF pauses briefly before and after sending keystrokes. This is done only for technical reasons and the pauses are usually too short to affect game play. If you are concerned that these delays might violate the rules in World of Warcraft, use SendWinS instead. SendWinS works fine for sending single keystrokes in WoW. SendWinSF is required only for chat line commands (which may violate the rules for other reasons).

**Example**

::

    <Hotkey F1>
       <SendPC local>
          <SendWinSF Ubertronic>
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
