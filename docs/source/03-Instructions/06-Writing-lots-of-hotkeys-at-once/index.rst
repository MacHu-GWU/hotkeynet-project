.. _6-Writing-Lots-of-Hotkeys-at-Once:

6. Writing Lots of Hotkeys at Once
==============================================================================
So far in these instructions we've made one hotkey at a time. For example, the following definition makes a hotkey for a single key, X::

    <Hotkey X>
       <SendPC 192.168.1.101>
          <SendWin WoW1>
             <Key X>

We could write practically the same thing and define three hotkeys at once, like this::

    <Hotkey X, Y, Z>
       <SendPC 192.168.1.101>
          <SendWin WoW1>
             <Key %TRIGGER%>

When HotkeyNet loads this three-key definition, it expands it into three separate hotkeys, one for X and one for Y and one for Z.. In each case the special word %TRIGGER% gets replaced by the trigger key. You can see the expansion by pressing "Show loaded hotkeys." Here's what the program will show you.






You're not limited to three hotkeys. Here's a definition that creates 48 of them::

    <Hotkey A-Z, 0-9, F1-F12>
       <SendPC 192.168.1.101>
          <SendWin WoW1>
             <Key %TRIGGER%>

But that's chickenfeed. Here's a definition that creates about four hundred hotkeys::

    <Hotkey AllMainKeys; Shift AllMainKeys>
       <SendPC 192.168.1.101>
          <SendWin WoW1>
             <Key %TRIGGER%>

These examples only hint at the power and potential complexity of key lists. For more information, see Hotkey and KeyList.
