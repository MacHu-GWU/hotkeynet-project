.. _comparison-chart-of-send-modes:

Comparison chart of send modes
==============================================================================
**Foreground Modes**

- :ref:`SendWin`: Uses operating system command SendInput. This is the most reliable, most accurate method, but it requires the target window to be in the foreground. If the target is in the background, HotkeyNet will bring it forward automatically, but this takes time and usually requires a <Wait> command in the hotkey definition to cover the delay.
- :ref:`SendFocusWin`: Like SendWin except you can't name a particular target window. HotkeyNet uses whichever window happens to be in the foreground.

**Semi-Background Modes**

- :ref:`SendWinX`: Like SendWin except the targeted window is activated without bringing it to the foreground, i.e., it receives focus but the Z-order doesn't change. This mode is experimental and may not work properly.

**Background Modes**

Note: All four background modes have trouble delivering modified key combinations like Alt-X, Ctrl-Alt-F3, etc. This may improve in future builds.

- :ref:`SendWinM`: Uses operating system command PostMessage, i.e., doesn't wait for response from receiving thread. Therefore it's very fast. Converts characters to lowercase.
- :ref:`SendWinMF`: Same as SendWinM except it plays some games with the Windows API to try to make the target window think it's in the foreground. Requires pauses added explicitly by HotkeyNet. User must adjust the length of these pauses with "Background Focus Delay" settings
- :ref:`SendWinS`: Uses operating system command SendMesssage, i.e., waits for response from receiving thread. Therefore it's extremely slow but possibly more reliable than SendWinM. Converts characters to shifted ones, therefore letters get capitalized.
- :ref:`SendWinSF`: Same as SendWinS except it plays some games with the Windows API to try to make the target window think it's in the foreground. Requires pauses added explicitly by HotkeyNet. User must adjust the length of these pauses with Background Focus Delay settings.
