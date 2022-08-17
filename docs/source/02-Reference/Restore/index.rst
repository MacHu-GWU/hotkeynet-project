.. _Restore:

Restore
==============================================================================
Puts the original window back in the foreground after :ref:`SendWin` finishes.

简单来说该命令只和配合使用, 因为 SendWin 会将后台的窗口带到前面来, 然后你可以用 Restore 切换回原来的窗口. 但是既然你要这么做, 你不如用 :ref:`SendWinM` 直接发送动作到后台.

**Syntax**

::

    <Restore>

**Parameters**

    None.

**Remarks**

    When :ref:`SendWin` is used with background windows, it brings them to the foreground. If you use :ref:`Restore` at the end of the hotkey definition, the original foreground window will be put back in place.

    (A window is in the foreground when it's on top of all the others. It's in the background when its underneath others.)

**Example**

::

    <Hotkey F1>
       <SendPC local>
          <SendWin UberOne>
             <Text hi!>
          <SendWin UberTwo>
             <Text bye!>
          <Restore>
