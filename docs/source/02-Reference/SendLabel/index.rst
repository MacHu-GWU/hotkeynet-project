.. _SendLabel:

SendLabel
==============================================================================
Specifies the mailing labels to which keystrokes get sent.

Syntax::

    <SendLabel label [, label [, label ...]]>

Parameters

    Each label is a mailing label that has been defined with the Label keyword. You must specify at least one. Labels are separated by commas.

Example

    The following example creates a hotkey that sends a keystroke to both Joe and Sam::

        <Label joe Local SendWin Game1>
        <Label sam 192.168.1.102 SendWin Game2>

        <Hotkey F1>
           <SendLabel sam, joe>
              <Key %Trigger%>
