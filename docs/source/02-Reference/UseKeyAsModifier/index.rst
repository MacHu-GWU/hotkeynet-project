.. _UseKeyAsModifier:

UseKeyAsModifier
==============================================================================
Designates a key that will be used as a modifier in hotkey triggers. The key's normal function is disabled until you load a new hotkey file, turn hotkeys off, or close HotkeyNet.

**Syntax**:

    <UseKeyAsModifier key>

**Parameter**

    Key is the name of a key.

**Remarks**

    There are six modifiers on the keyboard: the shift keys, control keys, and alt keys. They are called modifiers because you can use them as prefixes in hotkey triggers like this::

        <Hotkey Shift F3>

    But suppose you want to use a non-modifier like Q in place of Shift::

        <Hotkey Q F3>

    Normally you can't do that, but UseKeyAsModifer makes it possible. Simply put the following line at the top of your hotkey file::

        <UseKeyAsModifier Q>

    Now you can use Q like any other modifier. For example, you could write::

        <Hotkey Q F3>
        <Hotkey lshift Q X>
        <Hotkey Q alt F1>
        <Hotkey ralt Q rctrl backspace>

    The downside is that the new modifier no longer performs its normal function. For example, when Q is a modifier it no longer types the letter Q. Normal function is restored when you load a new hotkey file, turn hotkeys off, or close HotkeyNet.

    You can have up to sixteen additional modifiers active at one time.

**Example**

    The following lines add three modifiers::

        <UseKeyAsModifier 1>
        <UseKeyAsModifier Tab>
        <UseKeyAsModifier NumpadPgUp>

**Related topics**

    - :ref:`Hotkey`
