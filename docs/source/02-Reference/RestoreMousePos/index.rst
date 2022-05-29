.. _RestoreMousePos:

RestoreMousePos
==============================================================================
Moves the mouse cursor back to a previously saved position.

**Syntax**

::

    <RestoreMousePos>

**Parameters**

    None.

**Remarks**

    The position gets saved automatically the first time you use MoveMouse or ClickMouse in a hotkey. You can override that automatic behavior, or substitute for it, with SaveMousePos.

**Example**

::

    <HotKey F1>
       <SendPC local>
           <SaveMousePos>
           <MoveMouse 404 137>
           <RestoreMousePos>

**Related topics**

- :ref:`ClickMouse`
- :ref:`MoveMouse`
- :ref:`RestoreMousePos`
- :ref:`SaveMousePos`
