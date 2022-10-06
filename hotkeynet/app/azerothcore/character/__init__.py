# -*- coding: utf-8 -*-

"""
该模块定义了在 AzerothCore 服务器上所拥有的角色. 并且提供了一系列函数方便于我们对角色进行排列组合.

这个模块里的所有类都是一个 namespace, 仅仅是为了方便引用而提供的类. 这些类下面的方法其实
都可以是 ``staticmethod``. 但是为了免去为每个方法写 ``@staticmethod`` 的麻烦, 我们就
把类名起一个以下划线开头的名字, 然后创建一个名称像类名的实例.
"""

from .character_factory import char_fact, char_group
from .login_character_factory import login_char_fact
from .active_character_factory import (
    raid_active_char_fact,
    dungeon_active_char_fact,
)
