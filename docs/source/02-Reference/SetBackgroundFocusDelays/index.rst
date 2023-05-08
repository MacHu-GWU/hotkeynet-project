.. _SetBackgroundFocusDelays:

SetBackgroundFocusDelays
==============================================================================
This command adjusts the timing of the background focus delays which are used by SendWinMF.

**Syntax**

::

    <SetBackgroundFocusDelays number1 number2>

**Parameters**

    - Number1 is the length of the delay in milliseconds before keystrokes are sent. The default length is zero.
    - Number2 is the length of the delay in milliseconds after keystrokes are sent. The default length is 15.

**Remarks**

    This command is used with SendWinMF and the BackgroundFocusDelays option of SetSendMode. You only have to use it under the following circumstances:

    If keystrokes are not getting through to the background window, make the second number longer.

    If you want to be able to type manually into the foreground window while keystrokes get sent to a background window, but the typed characters are affecting both windows, make the second number shorter.
    You can adjust these numbers in two ways:

    Adjust them for a particular hotkey with this command, or

    Adjust their default values (for all hotkeys) on the Settings panel.
    It's generally easier and more useful to adjust them on the Settings panel, but sometimes you need to vary their values from one hotkey definition to another. That's what this command is for.

    The first number should usually be zero.

    The default values for these numbers are zero and 15.

**Examples**

    If keystrokes aren't reaching the background window, make the second number longer than the default value of 15, like this::

        <hotkey F1>
           <sendpc local>
              <SetBackgroundFocusDelays 0 50>
              <sendwinMF Uber1>
                 <text hi!>
              <sendwinMF UberTwo>
                 <text bye!>

    If you want to be able to type manually into the foreground window while a macro executes in the background, but the typed characters are affecting both windows, make the second number shorter, like this::

        <hotkey F1>
           <sendpc local>
              <SetBackgroundFocusDelays 0 10>
              <sendwinMF Uber1>
                 <text hi!>
              <sendwinMF UberTwo>
                 <text bye!>
