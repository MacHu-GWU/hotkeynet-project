.. _ClickMouse:

ClickMouse
==============================================================================
Moves the mouse cursor to a specified location and clicks a mouse button. You can choose from a number of different ways to set the location.

**Syntax**

::

    <ClickMouse Button Stroke Target Mode Restore>

**Parameters**

    Button indicates which button to click. This parameter can be LButton, MButton, RButton, Button4, or Button5. This parameter is optional. If you omit it, the default is LButton.

    Stroke indicates whether the button is pressed or released. This parameter can be Down, Up, Both, or NoClick. This parameter is optional. If you omit it, the default is Both.

    Target indicates whether the cursor gets positioned relative to the window or screen. This parameter can be Window or Screen. This parameter is optional. If you omit it, the default is Window.

    Mode indicates how the position of the cursor is set. This parameter is optional. If you omit it, the default is Scale. This parameter can be one of the following:

        ``NoMove``

        The cursor will not be moved. The click will happen wherever the cursor happens to be.

        ``# #``

        You can specify the cursor coordinates of the clicked cursor with two numbers separated by a space. If target is Screen, the coordinates are relative to the screen; if target is Window, the coordinates are relative to the window.

        ``Dupe``

        Clicked cursor's coordinates are the same as coordinates of cursor on machine where hotkey is pressed. If target is Screen, the coordinates are relative to the screen; if target is Window, the coordinates are relative to the window.

        ``Scale``

        Same as Dupe, except coordinates are adjusted for difference in screen resolution (if target is Screen) or window size (if target is window).

        ``#% #%``

        Same as Scale, except you specify the scaling factors for the x and y coordinates with two numbers, each followed by a percent sign.

        ``±# ±#``

        Use plus or minus symbols in front of numbers to specify a cursor offset. For example, if you want to click your target window 50 pixels to the left and 40 pixels below the point where the click would otherwise occur, write –50 +40. Offsets are added or subtracted before scaling.

    Restore indicates whether the cursor gets moved back to its original location after the click. This parameter can be Restore or NoRestore. If you omit this parameter, the default is Restore.

**Adjustment of ClickMouse Delays**

    If ClickMouse works erratically, that's a sign that you need to raise ClickMouse Delays on the Settings panel of the targeted PC.

    1. Raise both settings until ClickMouse works every time (i.e., try 25 25, then 35 35, then 45 45, etc.).

    2. After the delays are high enough for ClickMouse to work every time, you can fine tune the delays by reducing them one at a time to the lowest number that works perfectly. The numbers don't have to be the same.

**Remarks**

    Your choice of SendWin or SendWinM or SendWinMF affects ClickMouse. If you use SendWin and target a window, HotkeyNet will bring that window to the foreground if necessary to deliver the click. If you want to deliver a mouseclick to a window in the background without bringing it to the foreground, use SendWinM or SendWinMF.

    You can write parameters in any order.

    ClickMouse performs three distinct actions in the following order:

    1. Moves the mouse cursor to the appropriate location.
    2. Sends a button click.
    3. Moves the mouse cursor back to its original location.

These events often take place too fast for the receiving window to notice the correct location of the mouse click. If this happens, the hotkey will appear to work erratically or may not work at all. This is a sign that you need to increase one or both ClickMouse delays on the Settings Panel. These delays are inserted by HotkeyNet between the three actions to ensure that the target window sees the events in the correct order. See "Adjustment of ClickMouse Delays" above for instructions.

**Note to World of Warcraft Players**

    By default, this command inserts tiny delays as described above in Remarks. The delays occur only for technical reasons and the default values are too short to affect game play. If you are concerned that these delays might violate the rules in World of Warcraft you can disable them by setting ClickMouse delays to "0 0" (zero zero) on the Settings Panel. Unfortunately, without the delays it's very difficult to get ClickMouse to work.

    The need for these delays may be eliminated in future builds.

**Examples**

    The following hotkey left clicks a window. The location of the click will be determined by the location of the cursor on the machine where the hotkey is pressed. If the windows have different sizes, the location will be scaled::

        <Sendwin MyGame>
             <ClickMouse>

    The following hotkey is the same as the previous one, except that since it uses SendWinM, it will attempt to click on background windows without bringing them to the foreground::

        <SendWinM MyGame>
             <ClickMouse>

    The following hotkey right clicks the screen at coordinates 400, 800 — in other words, at the point which is 400 pixels from the left edge of the screen and 800 pixels from the top of the screen::

        <ClickMouse Screen 400 800>

    The following hotkey is similar to the last one except that it clicks the window at the point which is 400 pixels from the left edge of the window and 800 pixels from the top of the window::

        <ClickMouse Window 400 800>

    The following hotkey left clicks the screen wherever the cursor happens to be::

        <ClickMouse Screen NoMove>

    The following hotkey left clicks simultaneously on the same spot in three different WoW windows. The windows can be covered by other windows while the clicks occur::

        <Hotkey F1>
        <SendPC Local>
            <SendWinM wow1>
            <ClickMouse>
            <SendWinM wow2>
            <ClickMouse>
            <SendWinM wow3>
            <ClickMouse>

**Related Topics**

- :ref:`ClickMouse`
- :ref:`MoveMouse`
- :ref:`RestoreMousePos`
- :ref:`SaveMousePos`