.. _16-Templates:

16. Templates
==============================================================================
注: 由于 hotkeynet Python 项目能直接生成 Template 代码, 代码复用能力比原生 Template 更强大, Template 就没有存在的必要了.

Templates are chunks of text that get copied in a script. HotkeyNet makes the copies with macro substitutions so each copy is different from the others. Here's an example.

Suppose you want to create two hotkeys that have only a few differences which are shown in red::

    <Hotkey F1>
       <ToggleWin X Y>

    <Hotkey F2>
       <ToggleWin W Z>

Instead of typing the hotkey twice you could make a template::

    <Template MyTemplate>
       <Hotkey %1%>
          <ToggleWin %2% %3%>
    <EndTemplate>

Now create each of the two hotkeys with a single line::

    <ApplyTemplate MyTemplate F1 X Y>
    <ApplyTemplate MyTemplate F2 W Z>

To see the results of your copying, press Show Loaded Hotkeys on HotkeyNet's main window.