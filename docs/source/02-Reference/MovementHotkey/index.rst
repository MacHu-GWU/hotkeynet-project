.. _MovementHotkey:

MovementHotkey
==============================================================================
Creates one or more movement hotkeys that can be used for movement in games.

**Syntax**

::

    <MovementHotkey [mods] mainlist [; [mods] mainlist...]>

**Parameters**

    Same as Hotkey.

**Remarks**

    Only the following keywords can be used in a MovementHotkey definition:

    - :ref:`PassThrough`
    - :ref:`SendLabel`
    - :ref:`Key`
    - :ref:`If`
    - :ref:`Else`
    - :ref:`Endif`

    If you need to make a hold down hotkey that is more complicated than this, you can do it with Hotkey and HotkeyUp. For more information, see :ref:`7-Movement-Keys`.

**Example**

    The following example creates four movement hotkeys that control two characters::

        <MakeLabel joe local SendWin game1>
        <MakeLabel sam 192.168.1.102 SendWin game1>

        <MovementHotkey w, a, s, d>
        <SendLabel sam, joe>
        <Key %Trigger%>

    The following example creates one movement hotkey. The trigger and output key are different::

        <MakeLabel joe local SendWin game1>
        <MakeLabel sam 192.168.1.102 SendWin game1>

        <MovementHotkey Ctrl F1>
        <SendLabel sam, joe>
        <Key F9>

**Related pages**

- :ref:`MakeLabel`
- :ref:`7-Movement-Keys`
- :ref:`PassThrough`
- :ref:`SendLabel`
- :ref:`Trigger`
