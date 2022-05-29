.. _Hotkey:

Hotkey, HotkeyUp
==============================================================================
Declares the key combination that triggers a hotkey.

Syntax::

    <Hotkey [mods] mainlist [; [mods] mainlist...]>
    <HotkeyUp [mods] mainlist [; [mods] mainlist...]>

Parameters

    Mods is a list of modifiers separated by spaces. Each modifier can be:

    — A normal modifier: Shift, LShift, RShift, Ctrl, LCtrl, RCtrl, Alt, LAlt, RAlt.
    — Any other key if it's declared first with UseKeyAsModifier.
    — A toggle modifier: CapsLockOn, CapsLockOff, ScrollLockOn, ScrollLockOff, NumLockOn, NumLockOff.

    You can include up to eleven modifiers, but keep in mind that most keyboards are limited to five simultaneous keypresses (the sixth won't generate a signal).

    You can write modifiers in any order.

    Mainlist can be the name of a single non-modifier key or a list of them. You can list them by separating the names with commas or by using any syntax that's allowed for KeyList.

Remarks

    If you supply more than one trigger, HotkeyNet will create a separate hotkey for each one. This is useful for broadcasting keys with %Trigger%.

    To learn the name of a key, press it while looking at "Last key press" in the upper right corner of HotkeyNet's main window.

    The difference between Hotkey and HotkeyUp is whether the action occurs when the main key is pressed or released. For example, if you write::

        <Hotkey shift alt F3>

    the action occurs when F3 is pressed. But if you write HotkeyUp instead, like this::

        <HotkeyUp shift alt F3>

    the action occurs when F3 is released.

    Most of the time you should use Hotkey by itself. But to make characters move in games, you need to use Hotkey and HotkeyUp together. For more information, see Movement Keys.

Common misunderstandings

    People often assume that the trigger (the key combination they press to make the hotkey fire) is automatically passed along to whatever program they are using. This is not the case. HotkeyNet doesn't do that because it's a hotkey program, not a key broadcast program. Hotkey programs can do everything broadcast programs do, and much more besides.

    If you want the trigger to be sent to the active window, you must say so explicitly. HotkeyNet gives you three ways to do this: with PassThrough, with SendFocusWin, or by naming the window like you do when you send to any other window. Here's an example with PassThrough that sends "3" to both the local and remote PCs::

        <Hotkey 3>
        <PassThrough>
        <SendPC 192.168.1.103>
        <SendWin MyGameWindow>
        <Text 3>

    People also frequently assume that the hotkey trigger must be the same as the hotkey's output. Not so.To illustrate this, here's a hotkey that gets triggered by "3" like the one above but sends "4"::

        <Hotkey 3>
        <SendPC local>
        <SendWin MyGameWindow>
        <Text 4>

Examples

    Here's a simple example without modifiers::

        <Hotkey F1>
        <Key %Trigger%>

    Here's an example with one regular modifier::

    <Hotkey RCtrl F1>
    <Key %Trigger%>

Here's an example with a custom modifier::

    <UseKeyAsModifier Esc>
    <Hotkey Esc F1>
    <Key %Trigger%>

Here's an example that fires only when NumLock is on and ScrollLock is off::

    <Hotkey NumLockOn ScrollLockOff F1>
    <Key %Trigger%>

Here's an example that creates hotkeys for every letter between A and Z except J::

    <Hotkey A-Z except J>
    <Key %Trigger%>

Here's an example that creates hotkeys for every letter between A and Z, both when those keys are shifted and unshifted::

    <Hotkey A-Z; Shift A-Z>
    <Key %Trigger%>

Here's an example that uses a list combined with three modifiers::

    <KeyList MyList A-Z, 0-9>
    <Hotkey shift MyList; alt MyList; ctrl MyList>
    <Key %Trigger%>
