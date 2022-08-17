.. _SendWinMF:

SendWinMF
==============================================================================
Specifies the window that will receive keystrokes and mouse clicks. Tries even harder than SendWinM to send keystrokes to background windows.

**Important note**

You usually have to adjust a setting to make SendWinMF work. See below for details.

**Syntax**

::

    <SendWinMF window>

**Parameters**

    Window is the name of the window that will receive keystrokes and mouse clicks.

**Remarks**

    SendWinMF is HotkeyNet's strongest method for sending keystrokes to background windows. It's similar to SendWinM but makes even greater efforts to force background windows to accept keystrokes.

    If SendWinMF is stronger than SendWinM, why not use it all the time? Because it's more complicated. It requires an adjustment.

    To make SendWinMF work, you usually have to adjust the background focus delays

    SendWinMF pauses briefly before and after it sends keystrokes. These pauses are called background focus delays. You should usually keep the length of the first pause at zero. Make the second one longer if keystrokes don't reach the background window. Make the second one shorter if manually-typed keystrokes leak from the foreground window into the background one.

    There are two ways to make the adjustment: the Settings panel or SetBackgroundFocusDelays.

**Note to World of Warcraft Players**

    As mentioned above, SendWinMF pauses briefly before and after sending keystrokes. This is done only for technical reasons and the pauses are usually too short to affect game play. If you are concerned that these delays might violate the rules in World of Warcraft, use SendWinM instead. SendWinM works fine for sending single keystrokes in WoW. SendWinMF is required only for chat line commands (which may violate the rules for other reasons).

**Limitations**

    SendWinMF converts capital letters to lowercase ones.

    To avoid this limitation, use the new versions of SendWinS or SendWinSF instead.

**Example**

::

    <hotkey F1>
       <sendpc local>
          <sendwinMF UberOne>
             <text hi!>
          <sendwinMF UberTwo>
             <text bye!>

**Related topics**

- :ref:`comparison-chart-of-send-modes`
- :ref:`9-Sending-Keystokes-to-Windows`
- :ref:`10-Sending-to-Background-Windows`
- :ref:`SendWin`
- :ref:`SendWinM`
- :ref:`SetBackgroundFocusDelays`
