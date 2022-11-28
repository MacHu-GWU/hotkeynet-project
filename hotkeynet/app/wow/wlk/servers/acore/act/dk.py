# -*- coding: utf-8 -*-

from hotkeynet.keyname import *
from hotkeynet import (
    ActFactory,
    CN,
)


class Blood(ActFactory):
    # 鲜血系系主打技能
    Blood_Presence = SHIFT_(Q)  # 血之领域
    Blood_Strike = None  # 鲜血打击
    Heart_Strike = None  # 心脏打击, 鲜血系天赋技能

    # 天赋技能
    Rune_Tap = None  # 符文分流, 瞬发治疗技能, 鲜血系天赋技能
    Mark_of_Blood = None  # 鲜血印记, 鲜血系天赋技能
    Hysteria = None  # 狂血术, 鲜血系天赋技能
    Vampiric_Blood = None  # 吸血鬼之血, 类似战士的破釜沉舟, 鲜血系天赋技能
    Dancing_Rune_Weapon = None  # 召唤符文武器, 鲜血系天赋技能

    # 其他
    Dark_Command = Z  # 黑暗命令, 嘲讽
    Pestilence = SHIFT_(OEM3_WAVE_OR_BACK_QUOTE)  # 传染
    Blood_Boil = None  # 血液沸腾, AOE 伤害
    Death_Pact = None  # 血之契约
    Blood_Tap = None  # 鲜血分流
    Strangulate = None  # 绞袭


class Frost(ActFactory):
    # 冰霜系主打技能
    Frost_Presence = SHIFT_(E)  # 冰霜领域
    Icy_Touch = None  # 冰冷触摸, 在冰霜领域下高仇恨技能, 散播冰霜疫病
    Obliterate = None  # 湮没

    # 天赋技能
    Lichborne = None  # 巫妖之躯, 冰霜系天赋技能
    Deathchill = None  # 黑锋冰寒
    Hungering_Cold = None  # 饥饿之寒, 群体控制
    Unbreakable_Armor = None  # 铜墙铁壁, 提高护甲和力量, 冰霜系天赋技能
    Frost_Strike = None  # 冰霜打击, 冰霜系天赋技能
    Howling_Blast = None  # 凛风冲击, 冰霜系天赋技能

    # 其他
    Chains_of_Ice = ALT_(KEY_2)  # 寒冰锁链
    Empower_Rune_Weapon = None  # 强化符文武器
    Horn_of_Winter = SHIFT_(TAB)  # 寒冬号角, buff 技能

    Icebound_Fortitude = SHIFT_(F1)  # 冰固坚韧, 减伤技能
    Mind_Freeze = None  # 心灵冰冻, 打断施法技能
    Path_of_Frost = None  # 冰霜之径, 群体水上行走
    Rune_Strike = None  # 符文打击, 高仇恨技能, 只能在躲闪招架之后使用


class Unholy(ActFactory):
    # 邪恶系主打技能
    Unholy_Presence = SHIFT_(W)  # 邪恶领域
    Plague_Strike = None  # 瘟疫打击, 散播血之疫病
    Death_Strike = None  # 死之打击, 按照疾病数量回血
    Scourge_Strike = None  # 天灾打击
    Death_Coil = None  # 死亡缠绕

    # 天赋技能
    Ghoul_Frenzy = None  # 食尸鬼狂乱
    Anti_Magic_Zone = None  # 反魔法领域
    Bone_Shield = None  # 骨盾
    Summon_Gargoyle = None  # 召唤石像鬼

    # 其他
    Anti_Magic_Shell = SHIFT_(F)  # 反魔法护盾
    Army_of_the_Dead = None  # 亡者大军
    Corpse_Explosion = None  # 尸体爆炸
    Death_and_Decay = ALT_(X)  # 死亡凋零
    Death_Gate = None  # 死亡之门
    Death_Grip = None  # 死亡之握

    Raise_Ally = None  # 复活友军
    Raise_Dead = None  # 复活死者


class Healbot(ActFactory):
    pass


class DK(Blood, Frost, Unholy, Healbot):
    pass


class DKBlood(DK):
    Heart_Strike = None  # 心脏打击, 鲜血系天赋技能
    Rune_Tap = None  # 符文分流, 瞬发治疗技能, 鲜血系天赋技能
    Mark_of_Blood = ALT_(F)  # 鲜血印记, 鲜血系天赋技能
    Hysteria = SHIFT_(C)  # 狂血术, 鲜血系天赋技能
    Vampiric_Blood = SHIFT_(F2)  # 吸血鬼之血, 类似战士的破釜沉舟, 鲜血系天赋技能
    Dancing_Rune_Weapon = CTRL_(F)  # 召唤符文武器, 鲜血系天赋技能


class DKFrost(DK):
    Lichborne = None  # 巫妖之躯, 冰霜系天赋技能
    Deathchill = SHIFT_(C)  # 黑锋冰寒
    Hungering_Cold = CTRL_(F)  # 饥饿之寒, 群体控制
    Unbreakable_Armor = SHIFT_(F2)  # 铜墙铁壁, 提高护甲和力量, 冰霜系天赋技能
    Frost_Strike = None  # 冰霜打击, 冰霜系天赋技能
    Howling_Blast = ALT_(F)  # 凛风冲击, 冰霜系天赋技能


class DKUnholy(DK):
    Scourge_Strike = None  # 天灾打击
    Ghoul_Frenzy = None  # 食尸鬼狂乱
    Anti_Magic_Zone = SHIFT_(G)  # 反魔法领域
    Bone_Shield = SHIFT_(F2)  # 骨盾
    Summon_Gargoyle = SHIFT_(C)  # 召唤石像鬼


dk = DK()
dk_blood = DKBlood()
dk_frost = DKFrost()
dk_unholy = DKUnholy()
