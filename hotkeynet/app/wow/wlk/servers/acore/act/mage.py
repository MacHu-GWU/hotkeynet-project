# -*- coding: utf-8 -*-

from hotkeynet.keyname import *
from hotkeynet import (
    ActFactory,
    CN,
)


class Arcane(ActFactory):
    # 奥系主打攻击技能
    Arcane_Missiles = None  # 奥术飞弹
    Arcane_Blast = None  # 奥术冲击
    Arcane_Barrage = None  # 奥术弹幕, 奥系天赋技能

    Arcane_Explosion = None  # 奥术爆炸
    Presence_of_Mind = None  # 气定神闲, 下一个法术瞬发, 奥系天赋技能
    Arcane_Power = None  # 奥术强化, 俗称奥强, 奥系天赋技能

    Slow = None  # 缓速术

    # Buff
    Arcane_Intellect = None  # 奥术智力
    Arcane_Brilliance = None  # 奥术光辉
    Amplify_Magic = None  # 法力增效
    Dampen_Magic = None  # 魔法抑制
    Focus_Magic = None  # 专注魔法, 奥系天赋技能

    Mage_Armor = None  # 法师护甲
    Blink = SHIFT_(R)  # 闪现术
    Counterspell = R  # 魔法反制
    """
    智能魔法反制宏::
    
        #showtooltip
        /stopcasting
        /cast [target=focus,harm] Counter Spell; [target=focustarget,harm] Counter Spell; [] Counter Spell
    """
    Remove_Curse = T  # 移除诅咒
    Evocation = CTRL_(F)  # 唤醒
    Invisibility = ALT_(E)  # 隐身术
    Mirror_Image = SHIFT_(F2)  # 镜像术
    Mana_Shield = None  # 法力护盾
    Polymorph = CTRL_(E)  # 变形术
    Slow_Fall = ALT_(F1)  # 缓落术
    Spellsteal = None  # 偷取魔法

    Conjure_Mana_Gem = None  # 制造法力宝石
    Conjure_Food = None  # 制造魔法食物
    Conjure_Water = None  # 制造魔法饮料
    Conjure_Refreshment = None  # 制造魔法餐点
    Ritual_of_Refreshment = None  # 召唤餐点仪式

    Teleport_Dalaran = None  # 传送 达拉然
    Teleport_Darnassus_Alliance = None  # 传送 达纳苏斯
    Teleport_Exodar_Alliance = None  # 传送 埃索达
    Teleport_Ironforge_Alliance = None  # 传送 铁炉堡
    Teleport_Orgrimmar_Horde = None  # 传送 奥格瑞玛
    Teleport_Shattrath_Alliance = None  # 传送 沙塔斯城
    Teleport_Shattrath_Horde = None  # 传送 沙塔城
    Teleport_Silvermoon_Horde = None  # 传送 银月城
    Teleport_Stonard_Horde = None  # 传送 斯通纳德
    Teleport_Stormwind_Alliance = None  # 传送 暴风城
    Teleport_Theramore_Alliance = None  # 传送 塞拉摩
    Teleport_Thunder_Bluff_Horde = None  # 传送 雷霆崖
    Teleport_Undercity_Horde = None  # 传送 幽暗城

    Portal_Dalaran = None  # 传送门 达拉然
    Portal_Darnassus_Alliance = None  # 传送门 达纳苏斯
    Portal_Exodar_Alliance = None  # 传送门 埃索达
    Portal_Ironforge_Alliance = None  # 传送门 铁炉堡
    Portal_Orgrimmar_Horde = None  # 传送门 奥格瑞玛
    Portal_Shattrath_Alliance = None  # 传送门 沙塔斯城
    Portal_Shattrath_Horde = None  # 传送门 沙塔城
    Portal_Silvermoon_Horde = None  # 传送门 银月城
    Portal_Stonard_Horde = None  # 传送门 斯通纳德
    Portal_Stormwind_Alliance = None  # 传送门 暴风城
    Portal_Theramore_Alliance = None  # 传送门 塞拉摩
    Portal_Thunder_Bluff_Horde = None  # 传送门 雷霆崖
    Portal_Undercity_Horde = None  # 传送门 幽暗城


class Fire(ActFactory):
    # 火系主打攻击技能
    Fireball = None  # 火球术
    Fire_Blast = None  # 火焰冲击
    Scorch = None  # 灼烧
    Pyroblast = None  # 炎爆术, 火系天赋技能
    Living_Bomb = None  # 活体炸弹, 火系天赋技能
    Frostfire_Bolt = None  # 霜火箭

    # AOE
    Flamestrike = X  # 烈焰风暴
    Blast_Wave = None  # 冲击波, 火系天赋技能
    Dragon_s_Breath = None  # 龙息术, 火系天赋技能

    Molten_Armor = None  # 熔岩护甲
    Combustion = None  # 燃魂, 火系天赋技能
    Fire_Ward = SHIFT_(F)  # 火焰防护结界


class Frost(ActFactory):
    # 冰系主打攻击技能
    Frostbolt = None  # 寒冰箭
    Ice_Lance = None  # 冰枪术
    Deep_Freeze = None  # 深度冻结, 冰系天赋技能

    # AOE
    Cone_of_Cold = None  # 冰锥术
    Blizzard = ALT_(X)  # 暴风雪
    Frost_Nova = None  # 冰霜新星

    # 爆发技能
    Icy_Veins = SHIFT_(C)  # 冰冷血脉, 使你的施法速度提高, 冰系天赋技能
    Cold_Snap = None  # 急速冷却, 重置你的冰系技能 CD, 冰系天赋技能

    # 防护技能
    Ice_Armor = None  # 冰甲术
    Frost_Ward = SHIFT_(G)  # 冰霜防护结界
    Ice_Barrier = None  # 寒冰护盾, 冰系天赋技能
    Ice_Block = SHIFT_(F1)  # 寒冰屏障, 俗称冰箱

    Summon_Water_Elemental = None  # 召唤水元素


class Healbot:
    HB_Amplify_Magic = None  # 法力增效
    HB_Dampen_Magic = None  # 魔法抑制
    HB_Remove_Curse_for_mbox = CN.middle  # 移除诅咒
    HB_Remove_Curse = CN.ctrl_left_click  # 移除诅咒
    HB_Focus_Magic = CN.right  # 专注魔法, 奥系天赋技能


class Mage(Arcane, Fire, Frost, Healbot):
    pass


class MageArcane(Mage):
    Arcane_Barrage = ALT_(F)  # 奥术弹幕, 奥系天赋技能
    Presence_of_Mind = CN.middle  # 气定神闲, 下一个法术瞬发, 奥系天赋技能
    Arcane_Power = ALT_(G)  # 奥术强化, 俗称奥强, 奥系天赋技能
    Slow = G  # 缓速术


class MageFire(Mage):
    Pyroblast = None  # 炎爆术, 火系天赋技能
    Living_Bomb = G  # 活体炸弹, 火系天赋技能
    Blast_Wave = ALT_(G)  # 冲击波, 火系天赋技能
    Dragon_s_Breath = ALT_(F)  # 龙息术, 火系天赋技能
    Combustion = ALT_(D)  # 燃魂, 火系天赋技能


class MageFrost(Mage):
    Deep_Freeze = ALT_(F)  # 深度冻结, 冰系天赋技能
    Icy_Veins = SHIFT_(C)  # 冰冷血脉, 使你的施法速度提高, 冰系天赋技能
    Cold_Snap = CN.middle  # 急速冷却, 重置你的冰系技能 CD, 冰系天赋技能
    Summon_Water_Elemental = G  # 召唤水元素
    Water_Elemental_Nova = G  # 水元素的冰冻术技能


mage = Mage()

mage_arcane = MageArcane()
mage_fire = MageFire()
mage_frost = MageFrost()
