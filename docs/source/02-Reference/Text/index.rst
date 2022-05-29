.. _Text:

Text
==============================================================================
Types text.

**Syntax**::

    <Text stuff>

**Parameters**

    Stuff is whatever you want to type in the targeted window.. It can be as long as you like, and it can contain spaces.

**Remarks**

    This command ignores spaces immediately after the word Text, so if your text begins with a space, send it separately like this with the Key command::

        <Key space>

    There are two other cases where you should use Key instead of Text.

    1. For non-printing characters like <key enter>, <key numlock>, etc.
    2. For keystrokes that are modified by shift, ctrl, and alt.

**Examples**

    <Text X>
    <Text These are the times that try men's souls.>

**Related topics**

- :ref:`Key`
