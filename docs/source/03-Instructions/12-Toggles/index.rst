.. _12-Toggles:

12. Toggles (round robin)
==============================================================================
Toggles make a hotkey do something different each time you press it. You can use them to make round-robin hotkeys for games.

For example, here's a hotkey that sends X the first time you press it. The second time it sends Y, and the third time it sends Z. The fourth time it starts over from the beginning::

    <Hotkey F1>
       <Toggle>
          <SendLabel w1>
             <Key X>
       <Toggle>
          <SendLabel w1>
             <Key Y >
       <Toggle>
          <SendLabel w1>
             <Key Z>


You can include as many Toggles as you want in a hotkey.

You can reset your toggles to the first action with ResetToggles.

You can change which toggle block gets triggered by the next keypress with SetToggle.

Toggles can be used only in hotkeys, not commands. If you need to call toggles from a command, make a hotkey that will be used as a subroutine and call it with DoHotkey.

For more information, see Toggle in the reference section.
