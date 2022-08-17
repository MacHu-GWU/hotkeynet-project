.. _CreatePictureButton:

CreatePictureButton
==============================================================================
Creates a button with a picture on it.

**Syntax**

::

    <CreatePictureButton name x y file [text]>

**Parameters**

    - ``Name`` is the name of the button.
    - ``X`` is the horizontal screen coordinate of the window's upper left corner.
    - ``Y`` is the vertical screen coordinate of the window's upper left corner.
    - ``File`` is the pathname of the picture file.
    - ``Text`` is the caption that appears on the button.

**Remarks**

    A newly created picture button is the same size as its picture. After you create it you can change its size with :ref:`SetWinSize` or :ref:`SetWinRect`. If you do this, the picture will stretch or shrink to fit the new dimensions.

    The program has three button styles. This command creates the picture style. You can create the other styles with :ref:`CreateButton` and :ref:`CreateColoredButton`.

    For more information about buttons, see :ref:`CreateButton`.

**Picture files**

    Your picture file can be a GIF, JPEG, PNG, TIFF, Exif, WMF, or EMF.

**Use AutoExec**

    You should create all your buttons and panels in an AutoExec command that executes automatically when the script loads.

**Example**

::

    <Command AutoExec>
        <CreatePictureButton B1 100 100 "c:\\doodads\pix\button.jpg">

**Related topics**

- :ref:`CreateButton`
