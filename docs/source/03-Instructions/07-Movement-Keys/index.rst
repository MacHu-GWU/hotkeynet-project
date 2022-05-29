.. _7-Movement-Keys:

7. Movement Keys
==============================================================================
To make characters move in games, you need a special type of hotkey that continues acting as long as you hold the trigger down.

If your hotkey controls movement in two or more windows on the same PC, you have to use either SendWinM or SendWinS.

There are two ways to make this kind of hotkey: an easy way and a hard way.

**The easy way**

Step one. Make mailing labels for your characters. Each label has a name, IP address, send method, and window name. For example::

    <Label joe local SendWinM wow1>
    <Label sam 192.168.1.101 SendWinM wow2>

Step two. Create the hotkeys with MovementHotkey. The following example makes eight hotkeys::

    <MovementHotkey w, a, s, d, up, down, left, right>
    <SendLabel joe, sam>
    <Key %Trigger%>

**The hard way**

In case you need to do something complicated, there's also a hard way to make movement keys. The basic idea is that you define two hotkeys. The first one determines what happens when you press the trigger and the second determines what happens when you release the trigger. The second uses HotkeyUp instead of Hotkey.

For example, here's a definition that makes two characters spread out. In the first part, keys are pressed with KeyDown. In the second part, keys are released with KeyUp. (If you wanted the definition to perform non-movement actions at the same time, you would write them normally in the first part of the definition under Hotkey)::

    <Hotkey F1>
    <SendLabel joe>
       <KeyDown Q>
    <SendLabel sam>
       <KeyDown E>

    <HotkeyUp F1>
    <SendLabel joe>
       <KeyUp Q>
    <SendLabel sam>
       <KeyUp E>
