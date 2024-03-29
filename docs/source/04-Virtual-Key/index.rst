.. _虚拟按键表:

04 虚拟按键表速查
==============================================================================
HotkeyNet 的核心是一个一个的键盘按键, 也就是 Key. 比如你按下快捷键后, HotkeyNet 对几个窗口同时按下按键 ``X``. 你需要给 HotkeyNet 脚本定义一个 KeyName, 这样脚本才知道应该按下什么键.

``HotkeyNetVirutalKey.tsv`` 是 HotkeyNet 的文档, 里面定义了每个键盘和鼠标按键的 KeyName. 但是对于有些特殊符号比如键盘 1 左边的按键, 按键名就不是那么直观了. 这些特殊按键的按键名通常以 ``OEM``, 指的是键盘生产厂商的自定义按键, 比如多媒体按键. 但是大多数键盘厂商对于一些常见的特殊按键的 ``OEM`` 值还是一致的. 这些特殊符号的按键名可以在 ``虚拟按键码.tsv`` 文件中找到.


HotkeyNetVirutalKey
------------------------------------------------------------------------------
.. literalinclude:: ./HotkeyNetVirutalKey.tsv
   :linenos:


虚拟按键码
------------------------------------------------------------------------------
.. literalinclude:: ./虚拟按键码.tsv
   :linenos:
