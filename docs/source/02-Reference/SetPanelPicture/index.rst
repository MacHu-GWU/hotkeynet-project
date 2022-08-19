.. _SetPanelPicture:

SetPanelPicture
==============================================================================
This command is new in build 193

Many thanks to Katharsis for suggesting this command.

Specifies a picture for a panel's background.

**Syntax**

::

    <SetPanelPicture panel file>

**Parameters**

    - ``Panel`` is the name of the panel.
    - ``File`` is the pathname of the picture file.

**Remarks**

    Your picture file can be a GIF, JPEG, PNG, TIFF, Exif, WMF, or EMF.

**Example**

::

    <Hotkey F1>
       <CreatePanel MyPanel 100 200 600 400>
       <SetPanelPicture MyPanel c:\art\icon5.jpg>

**Related topics**

- :ref:`CreatePanel`
