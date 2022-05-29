.. _Key:

Key, KeyDown, and KeyUp
==============================================================================
These commands simulate keystrokes. You can include modifiers (shift, alt, ctrl, or the left and right variants of shift, alt, and ctrl).

**Syntax**::

    <Key          name [name [name [name...]]]>
    <KeyDown name [name [name [name...]]]>
    <KeyUp   name [name [name [name...]]]>

**Parameters**

    Name is the name of a key. You must specify at least one. There is usually no reason to specify more than four, like this::

        <Key lshift lalt lctrl F3>

    However, the program lets you specify more keys if you want.

    Starting in build 128, you can use the keywords %Trigger% and %TriggerMainKey% to specify the keys that are pressed to trigger the hotkey.

**Remarks**

    These commands press and release keys.

    — Key moves keys up and down.
    — KeyDown moves keys only down.
    — KeyUp moves keys only up.

    To simulate a normal keystroke, use Key. To simulate holding a key down (like you do when you make a character run in a game), use KeyDown followed later by KeyUp.

    Here's an example that shows how these commands differ::

        <Key rshift ralt rctrl F3>

    That instruction makes HotkeyNet perform the following actions in order::

        # blue actions
        press rshift
        press ralt
        press rctrl
        press F3

        # red actions
        release F3
        release rctrl
        release ralt
        release rshift

    The actions are color coded to show what the other commands do. KeyDown is exactly the same as Key, except it performs only the blue actions. KeyUp is also the same but it performs only the red actions.

**When to use KeyDown and KeyUp**

    KeyDown and KeyUp are used mainly for movement keys in games, where you want a character to run for as long as you hold a key down. For more information, see :ref:`Movement` Keys.

    KeyDown and KeyUp are almost always used together. If you send KeyDown to a window without following it with KeyUp, that window will think the key is permanently pressed.

**The difference between Key and Text**

    The three Key commands simulate key presses. You use them with the names of keys. The Text comand sends text. You use it with printable characters. For example::

        <Key backspace>

    presses and releases the backspace key. But::

        <Text backspace>

    types the word "backspace."

    Sometimes you can use either. For example, the following instructions do the same thing::

        <Key 5>
        <Text 5>

    In a case like that, you should use Text instead of Key because it's slightly faster.

**Examples**::

    <Key enter>
    <KeyDown alt Y>
    <Key lshift lalt backspace>
    <KeyUp shift F1>
    <Key LALT RCTRL NUMPAD_ENTER>
    <KeyDown ctrl alt shift home>

**Related topics**

- :ref:`Text`
- :ref:`7-Movement-Keys`
