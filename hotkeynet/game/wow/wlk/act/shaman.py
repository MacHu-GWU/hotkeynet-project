# -*- coding: utf-8 -*-

from hotkeynet.keyname import *
from hotkeynet import (
    ActFactory,
    CN,
)


class ElementalCombat(ActFactory):
    # 元素系主打技能
    Lightning_Bolt = None  # 闪电箭
    Chain_Lightning = None  # 闪电链
    Lava_Burst = None  # 熔岩爆发
    Thunderstorm = None  # 雷霆风暴, 元素系天赋技能

    # 震击
    Flame_Shock = None  # 火焰震击
    Earth_Shock = None  # 大地震击
    Frost_Shock = None  # 冰霜震击

    Elemental_Mastery = None  # 元素掌握, 增加施法速度, 爆发技能, 元素系天赋技能
    Fire_Nova = None  # 火焰新星, 火系图腾 AOE 伤害
    Hex = None  # 妖术
    Purge = None  # 净化术

    # 图腾
    Searing_Totem = None  # 灼热图腾, 攻击周围敌人
    Magma_Totem = None  # 熔岩爆裂图腾, 周期性 AOE 伤害
    Stoneclaw_Totem = None  # 石爪图腾, 嘲讽周围敌人保护施法者
    Earthbind_Totem = None  # 地缚图腾, 进入范围内的敌人减速
    Wind_Shear = None  # 削风术, 打断敌人施法
    Fire_Elemental_Totem = None  # 火元素图腾
    Totem_of_Wrath = None  # 愤怒图腾, 增加周围友军的法伤, 元素系天赋技能

    Call_of_the_Ancestors = None  # 一次性插 4 个图腾, 组合 1
    Call_of_the_Elements = None  # 一次性插 4 个图腾, 组合 2
    Call_of_the_Spirits = None  # 一次性插 4 个图腾, 组合 3


class Enhancement(ActFactory):
    # 增强系主打技能
    Stormstrike = None  # 风暴打击, 同时用双手武器攻击, 增强西天赋技能
    Lava_Lash = None  # 熔岩猛击, 用副手武器攻击, 增强系天赋技能

    Bloodlust_or_Heroism = None  # 嗜血 / 英勇, 为团队提高急速
    Astral_Recall = None  # 先祖召回, 跟炉石一样
    Far_Sight = None  # 远视
    Feral_Spirit = None  # 召唤幽灵狼, 增强系天赋技能

    # 抗性图腾
    Fire_Resistance_Totem = None  # 火焰抗性图腾
    Frost_Resistance_Totem = None  # 冰霜抗性图腾
    Nature_Resistance_Totem = None  # 自然抗性图腾

    Stoneskin_Totem = None  # 石肤图腾, 为周围的团队成员增加护甲
    Strength_of_Earth_Totem = None  # 大地之力图腾, 为周围的团队成员增加力量敏捷
    Flametongue_Totem = None  # 火舌图腾, 为周围的团队成员增加法伤
    Windfury_Totem = None  # 风怒图腾, 为周围的团队成员增加近战急速
    Wrath_of_Air_Totem = None  # 空气之怒图腾, 为周围的团队成员增加施法急速
    Sentry_Totem = None  # 哨兵图腾, 可以切换视野
    Grounding_Totem = None  # 根基图腾, 吸收指向性技能
    Earth_Elemental_Totem = None  # 土元素图腾

    # 武器 Buff
    Flametongue_Weapon = None  # 火舌武器, 增加法伤, 攻击时带火焰伤害
    Frostbrand_Weapon = None  # 冰霜武器, 攻击时带减移动速度
    Rockbiter_Weapon = None  # 石化武器, 提高武器伤害
    Windfury_Weapon = None  # 风怒武器, 让你的攻击有可能触发连击效果

    Lightning_Shield = None  # 闪电盾
    Ghost_Wolf = None  # 变形幽灵狼

    Water_Breathing = None  # 水下呼吸
    Water_Walking = None  # 水上行走

    Shamanistic_Rage = None  # 萨满之怒, 天赋技能, 减伤并为普通攻击增加回蓝效果


class Restoration(ActFactory):
    # 恢复系主打技能
    Earth_Shield = None  # 大地之盾, 当被保护的人受到伤害时治疗他, 恢复系天赋技能
    Healing_Wave = None  # 治疗波
    Lesser_Healing_Wave = None  # 次级治疗波
    Chain_Heal = None  # 治疗链
    Riptide = None  # 激流, 恢复系天赋技能

    Ancestral_Spirit = None  # 先祖灵魂, 复活
    Cleanse_Spirit = None  # 净化灵魂, 驱散 中毒, 疾病, 诅咒, 恢复系天赋技能
    Cure_Toxins = None  # 驱毒术, 驱散 中毒, 疾病

    Earthliving_Weapon = None  # 大地生命武器,

    Healing_Stream_Totem = None  # 治疗之泉图腾
    Mana_Spring_Totem = None  # 法力之泉图腾
    Cleansing_Totem = None  # 净化图腾, 周期性为小队成员驱散 中毒, 疾病
    Mana_Tide_Totem = None  # 法力之潮图腾, 恢复系天赋技能
    Tremor_Totem = None  # 战栗图腾, 周期性为小队驱散恐惧
    Totemic_Recall = None  # 召回图腾

    Nature_s_Swiftness = None  # 自然迅捷, 使下一个自然法术瞬发, 恢复系天赋技能
    Tidal_Force = None  # 潮汐之力, 恢复系天赋技能

    Water_Shield = None  # 水之护盾


class Healbot(ActFactory):
    HB_Chain_Heal = None  # 治疗链
    HB_Cleanse_Spirit = None  # 净化灵魂, 驱散 中毒, 疾病, 诅咒, 恢复系天赋技能
    HB_Cure_Toxins = None  # 驱毒术, 驱散 中毒, 疾病
    HB_Earth_Shield = None  # 大地之盾, 当被保护的人受到伤害时治疗他, 恢复系天赋技能
    HB_Healing_Wave = None  # 治疗波
    HB_Lesser_Healing_Wave = None  # 次级治疗波
    HB_Riptide = None  # 激流, 恢复系天赋技能


class Shaman(ElementalCombat, Enhancement, Restoration, Healbot):
    pass


class ShamanElementalCombat(Shaman):
    Thunderstorm = None  # 雷霆风暴, 元素系天赋技能
    Elemental_Mastery = None  # 元素掌握, 增加施法速度, 爆发技能, 元素系天赋技能
    Totem_of_Wrath = None  # 愤怒图腾, 增加周围友军的法伤, 元素系天赋技能


class ShamanEnhancement(Shaman):
    Stormstrike = None  # 风暴打击, 同时用双手武器攻击, 增强西天赋技能
    Lava_Lash = None  # 熔岩猛击, 用副手武器攻击, 增强系天赋技能
    Feral_Spirit = None  # 召唤幽灵狼, 增强系天赋技能
    Shamanistic_Rage = None  # 萨满之怒, 天赋技能, 减伤并为普通攻击增加回蓝效果


class ShamanRestoration(Shaman):
    Earth_Shield = None  # 大地之盾, 当被保护的人受到伤害时治疗他, 恢复系天赋技能
    Riptide = None  # 激流, 恢复系天赋技能
    Cleanse_Spirit = None  # 净化灵魂, 驱散 中毒, 疾病, 诅咒, 恢复系天赋技能
    Mana_Tide_Totem = None  # 法力之潮图腾, 恢复系天赋技能
    Nature_s_Swiftness = None  # 自然迅捷, 使下一个自然法术瞬发, 恢复系天赋技能
    Tidal_Force = None  # 潮汐之力, 恢复系天赋技能


shaman = Shaman()
shaman_elemental_combat = ShamanElementalCombat()
shaman_enhancement = ShamanEnhancement()
shaman_restoration = ShamanRestoration()
