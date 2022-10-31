# -*- coding: utf-8 -*-

from hotkeynet.keyname import *
from hotkeynet import (
    ActFactory,
    CN,
)


class Affliction(ActFactory):
    # 痛苦系主打技能
    Corruption = SHIFT_(OEM3_WAVE_OR_BACK_QUOTE)  # 腐蚀术
    Curse_of_Agony = None  # 痛苦诅咒
    Seed_of_Corruption = R  # 腐蚀之种, AOE 技能
    Unstable_Affliction = None  # 不稳定的痛苦, 痛苦系天赋技能
    Haunt = None  # 鬼影重重, 痛苦系天赋技能

    Death_Coil = None  # 死亡缠绕

    # 诅咒
    Curse_of_Doom = ALT_(E)  # 厄运诅咒
    Curse_of_Exhaustion = None  # 疲劳诅咒, 痛苦系天赋技能
    Curse_of_the_Elements = T  # 元素诅咒
    Curse_of_Tongues = G  # 语言诅咒
    Curse_of_Weakness = ALT_(T)  # 虚弱诅咒

    Drain_Life = SHIFT_(F)  # 吸取生命
    Drain_Mana = SHIFT_(G)  # 吸取法力
    Drain_Soul = CTRL_(R)  # 吸取灵魂碎片

    # 恐惧
    Fear = CTRL_(E)  # 恐惧
    Howl_of_Terror = ALT_(F1)  # 恐惧咆哮, 群体恐惧

    # 回蓝
    Life_Tap = Z  # 生命分流, 生命转法力
    Dark_Pact = None  # 黑暗契约, 从宠物身上吸取法力, 痛苦系天赋技能


class Demonology(ActFactory):
    # 恶魔系主打技能
    Metamorphosis = None  # 恶魔形态
    Challenging_Howl_Demon = None  # 挑战咆哮, 恶魔形态技能, 恶魔系天赋技能
    Demon_Charge_Demon = None  # 恶魔冲锋, 恶魔形态技能, 恶魔系天赋技能
    Shadow_Cleave_Demon = None  # 暗影顺劈斩, 恶魔形态技能, 恶魔系天赋技能
    Immolation_Aura_Demon = None  # 献祭光环, 恶魔形态技能, 恶魔系天赋技能

    Demonic_Empowerment = None  # 恶魔增效, 恶魔系天赋技能
    Soul_Link = None  # 灵魂链接, 让你的恶魔帮你分担受到的伤害, 恶魔系天赋技能

    Create_Firestone = None  # 创造火焰石
    Create_Healthstone = None  # 创造治疗石
    Create_Soulstone = None  # 创造灵魂石
    Create_Spellstone = None  # 创造法术石

    Demon_Armor = None  # 恶魔护甲
    Fel_Armor = KEY_0  # 邪甲术

    Demonic_Circle_Summon = ALT_(R)  # 恶魔之环 召唤
    Demonic_Circle_Teleport = SHIFT_(R)  # 恶魔之环 传送
    Ritual_of_Souls = None  # 灵魂仪式, 俗称发糖
    Ritual_of_Summoning = None  # 召唤仪式, 俗称拉人
    Inferno = None  # 召唤地狱火
    Ritual_of_Doom = None  # 末日仪式, 召唤地狱守卫
    Eye_of_KilroggSummon = None  # 基尔罗格之眼

    Detect_Invisibility = None  # 侦测隐形
    Unending_Breath = None  # 水下呼吸

    Sense_Demons = None  # 感知恶魔
    Enslave_Demon = None  # 奴役恶魔
    Fel_Domination = None  # 恶魔支配, 瞬发召唤恶魔
    Health_Funnel = None  # 生命通道, 治疗你的恶魔

    Shadow_Ward = None  # 暗影防护结界
    Soulshatter = None  # 灵魂碎裂, 减仇恨技能

    Banish = None  # 放逐术, 放逐元素生物

    Summon_Imp = None  # 召唤小鬼
    Summon_Voidwalker = None  # 召唤虚空行者
    Summon_Succubus = None  # 召唤魅魔
    Summon_Felhunter = None  # 召唤地狱犬
    Summon_Felguard = None  # 召唤恶魔卫士


class Destruction(ActFactory):
    # 毁灭系主打技能
    Immolate = None  # 献祭
    Conflagrate = None  # 点燃, 毁灭系天赋技能
    Shadow_Bolt = None  # 暗影箭
    Incinerate = None  # 烧尽
    Chaos_Bolt = None  # 混乱箭, 能穿透伤害吸收盾, 毁灭系天赋技能
    Searing_Pain = None  # 灼热之痛, 高仇恨技能

    Shadowburn = None  # 暗影灼烧, 瞬发直接伤害技能, 毁灭系天赋技能
    Shadowflame = X  # 暗影烈焰, 群体 AOE 技能, 毁灭系天赋技能
    Shadowfury = None  # 暗影之怒, 群体控制技能, 毁灭系天赋技能
    Soul_Fire = None  # 灵魂之火

    # AOE
    Hellfire = CTRL_(G)  # 地狱火, 俗称自燃
    Rain_of_Fire = ALT_(X)  # 火焰之雨


class Healbot(ActFactory):
    pass


class Warlock(Affliction, Demonology, Destruction, Healbot):
    pass


class WarlockAffliction(Warlock):
    Unstable_Affliction = None  # 不稳定的痛苦, 痛苦系天赋技能
    Haunt = None  # 鬼影重重, 痛苦系天赋技能
    Dark_Pact = None  # 黑暗契约, 从宠物身上吸取法力, 痛苦系天赋技能


class WarlockDemonology(Warlock):
    Metamorphosis = ALT_(D)  # 恶魔形态
    Challenging_Howl_Demon = None  # 挑战咆哮, 恶魔形态技能, 恶魔系天赋技能
    Demon_Charge_Demon = None  # 恶魔冲锋, 恶魔形态技能, 恶魔系天赋技能
    Shadow_Cleave_Demon = None  # 暗影顺劈斩, 恶魔形态技能, 恶魔系天赋技能
    Immolation_Aura_Demon = None  # 献祭光环, 恶魔形态技能, 恶魔系天赋技能
    Soul_Link = None  # 灵魂链接, 让你的恶魔帮你分担受到的伤害, 恶魔系天赋技能
    Summon_Felguard = None  # 召唤恶魔卫士
    Demonic_Empowerment = ALT_(F)  # 恶魔增效, 恶魔系天赋技能
    Fel_Domination = SHIFT_(C)  # 恶魔支配, 瞬发召唤恶魔


class WarlockDestruction(Warlock):
    Conflagrate = None  # 点燃, 毁灭系天赋技能
    Chaos_Bolt = None  # 混乱箭, 能穿透伤害吸收盾, 毁灭系天赋技能
    Shadowburn = SHIFT_(C)  # 暗影灼烧, 瞬发直接伤害技能, 毁灭系天赋技能
    Shadowflame = None  # 暗影烈焰, 群体 AOE 技能, 毁灭系天赋技能
    Shadowfury = ALT_(F)  # 暗影之怒, 群体控制技能, 毁灭系天赋技能


warlock = Warlock()
warlock_affliction = WarlockAffliction()
warlock_demonology = WarlockDemonology()
warlock_destruction = WarlockDestruction()
