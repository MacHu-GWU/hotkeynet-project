.. _Wait:

Wait
==============================================================================
Pauses for a specified number of milliseconds.

**Syntax**::

    <wait milliseconds>

**Parameters**

    Milliseconds is the length of the pause in thousandths of a second.

**Remarks**

    Sometimes you need to pause for 50 or 100 milliseconds or even longer in your hotkey definitions to give the target program time to get ready for the next keystroke. This is especially true if you are moving windows in and out of the foreground.

**Note to World of Warcraft Players**

    Use of this command can violate the rules in World of Warcraft.

**Example**

    The following hotkey pauses for half a second::

        <wait 500>
