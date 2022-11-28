# -*- coding: utf-8 -*-

"""
本模块定义了各个人物, 职业的详细动作条设置. 哪个技能以及哪个宏应该绑定什么快捷键.

本模块还实现了 Key 和 Mouse 行为的抽象化, 用人类可读, 有具体含义的代码, 形如:
``Paladin.PROTECT_SPEC_JUDGEMENT`` 这样的代码来代替意义不明确的 <Key 1>. 使得
Hotkey 代码本身就能反映出想要实现的功能, 避免了写注释. 因为保持注释和代码一致非常麻烦.
这种抽象化能使得你能专注于实现各个 Hotkey 的具体功能. 而当某个功能, 例如防护圣骑士

要使得此脚本按照预期工作, 必须按照本模块中的定义绑定技能和快捷键.

注: 在游戏中按照本模块的设置绑定好所有按键后, 一定要记得备份 WFT 中的配置文件, 以及 Domino
动作条的数据文件.

**开发者注意**

请参考 :meth:`hotkeynet.script.Block.__enter__` 中的文档. 因为上下文机制的存在,
这里所有的属性都 **不能够** 直接定义预先被创建好的 Block 实例. 而是要用工厂函数定义成
一个函数. 这样才能保证被引用的 Block 自动被添加到上下文中去.

**用户注意**

该模块是一套 Act 的模版. 你会发现所有的按键名都被定义, 但是值都是 None. 请拷贝后再在拷贝上
修改. 这里的 ``hotkeynet.game.wow.wlk.act`` 模块中的代码请不要动!
"""

from .warrior import warrior, warrior_arm, warrior_fury, warrior_protection
from .paladin import paladin, paladin_retribution, paladin_protection, paladin_holy
from .dk import dk, dk_blood, dk_frost, dk_unholy
from .shaman import shaman, shaman_elemental_combat, shaman_enhancement, shaman_restoration
from .hunter import hunter, hunter_beastMastery, hunter_marksmanship, hunter_survival
from .druid import druid, druid_balance, druid_restoration, druid_feral
from .warlock import warlock, warlock_affliction, warlock_demonology, warlock_destruction
from .mage import mage, mage_arcane, mage_fire, mage_frost
from .priest import priest, priest_discipline, priest_holy, priest_shadow
