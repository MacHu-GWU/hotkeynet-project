.. _KeyList:

KeyList
==============================================================================
Creates a list of key names that can be used for hotkey triggers.

**Syntax**

::

    <KeyList name item [, item [, item]]] [except item [, item [, item]]]>

**Parameters**

    - ``Name`` is the name you give to the list.
    - ``Except`` is the word "except." Items to the left of it are added to the list; items to the right are subtracted.
    - Each ``item`` is either the name of a key, a range of keys (two key names separated by a hyphen), or the name of another list.

**Remarks**

    An item can be the name of a list you created yourself or the predefined list AllMainKeys.

    For ranges (two key names separated by a hyphen), HotkeyNet uses virtual key codes. For example, you could write::

        <KeyList MyList Plus-Oem3>

    The virtual key codes for those two keys are ``0xBB`` and ``0xC0``, so HotkeyNet adds to the list all the keys with virtual key codes between those two numbers. Those keys happen to be:

    - Plus
    - Comma
    - Minus
    - Period
    - Oem2
    - Oem3

    For a list of virtual key codes, go to http://msdn.microsoft.com.

**Example**

    The following definition creates a list with 1, 2, 4, and 5. One key, 3, is left out::

        <KeyList List1 1-5 except 3>

    The following definition creates a list that contains the previous list plus A, B, C, and D::

        <KeyList List2 List1, A, B, C, D>

    The following definition creates a list that contains all the letter keys and all the number keys except for B, D, E, 2, 3, and 4::

        <MKeyList List3 a-z, 0-9 except b-e, 2-4>

    The following definition creates a list that contains all the function keys::

        <KeyList List4 F1-F24>

    The following definition creates a list that contains all non-modifier keys::

        <KeyList List5 AllMainKeys>


**Related topics**

- :ref:`Hotkey`