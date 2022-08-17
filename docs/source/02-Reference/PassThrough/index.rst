.. _PassThrough:

PassThrough
==============================================================================
Passes the hotkey trigger key to the window that has the focus.

简单来说你定义 Hotkey 的时候, 通常要指定发送到哪个窗口, 那么显然如果你当前窗口如果不在定义中, 当前窗口是没有反应的. 该命令就是能然不影响对其他窗口的操作的前提下, 把 Hotkey 直接发送到当前窗口.

**Syntax**

::

    <PassThrough>

**Parameters**

    None.

**Remarks**

    When you press a hotkey, HotkeyNet is normally the only program that sees the pressed key. If you want the keystroke to have its normal effect in addition to triggering the hotkey, you have to say so like this::

        <Hotkey A>
           <PassThrough>
           <SendLabel w1>
              <Key A>

    This hotkey allows "A" to pass through to whichever window has the focus on the local PC. Then the hotkey types "A" into the window specified by label w1.

    上面的例子是, 不仅把 A 发送到 w1, 还发送到当前窗口.

**Technical remarks**

    If you write PassThrough anywhere in a hotkey defnition, it always executes immediately when you press the hotkey before any other part of the hotkey is executed.

    This means PassThrough is not subject to If-conditions.

    The program is designed this way because PassThrough is executed by the keyboard hook, and the hook needs to run as fast as possible, without slowing down to examine If-conditions.

    If you want to put PassThrough inside an If-block, use SendFocusWin instead as shown in :ref:`this example <11-If–Else–EndIf>`.

**Related topics**

- :ref:`SendFocusWin`
