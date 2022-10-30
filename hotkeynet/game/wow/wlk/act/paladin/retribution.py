# -*- coding: utf-8 -*-

from ......act_factory import ActFactory


class Retribution(ActFactory):
    # 惩戒系主打技能
    Judgement_of_Light = None
    Judgement_of_Wisdom = None
    Judgement_of_Justice = None
    Crusader_Strike = None  # 十字军打击
    Divine_Storm = None  # 神圣风暴

    # 光环
    Retribution_Aura = None  # 惩戒光环
    Crusader_Aura = None  # 十字军光环

    # 祝福
    Blessing_of_Might = None  # 力量祝福
    Greater_Blessing_of_Might = None  # 强效力量祝福

    Avenging_Wrath = None  # 正义之怒
    Hammer_of_Wrath = None  # 愤怒之锤
    Repentance = None  # 忏悔
    Seal_of_Command = None  # 命令声音
    Seal_of_Vengeance_Corruption = None  # 复仇/腐蚀 圣印


class Protection(ActFactory):
    # 防护系主打技能
    Shield_of_Righteousness = None  # 复仇之盾
    Hammer_of_the_Righteous = None  # # 公正之锤
    Avenger_s_Shield = None  # 复仇者之盾
    Holy_Shield = None  # 神圣之盾

    # 坦克技能
    Righteous_Fury = None  # 正义之怒
    Hand_of_Reckoning = None  # 清算之手, 嘲讽
    Righteous_Defense = None  # 正义防御

    # 光环
    Devotion_Aura = None  # 虔诚光环
    Fire_Resistance_Aura = None
    Frost_Resistance_Aura = None
    Shadow_Resistance_Aura = None

    # 祝福
    Blessing_of_Kings = None
    Blessing_of_Sanctuary = None
    Greater_Blessing_of_Kings = None
    Greater_Blessing_of_Sanctuary = None

    Divine_Intervention = None  # 神圣干涉
    Divine_Protection = None  # 圣佑术, 减伤
    Divine_Sacrifice = None  # 神圣牺牲, 团队减伤
    Divine_Shield = None  # 神圣之盾, 无敌

    Hammer_of_Justice = None  # 制裁之锤, 控制技

    # 特殊效果的祝福
    Hand_of_Freedom = None  # 自由祝福
    Hand_of_Protection = None  # 保护祝福
    Hand_of_Sacrifice = None  # 牺牲祝福
    Hand_of_Salvation = None  # 拯救祝福
    Seal_of_Justice = None  # 公正圣印 (有几率打晕敌人)


class Holy:
    # 神圣系主打技能
    Beacon_of_Light = None  # 圣光道标
    Holy_Light = None  # 圣光术
    Flash_of_Light = None  # 圣光闪现
    Holy_Shock = None  # 神圣冲击
    Aura_Mastery = None  # 光环掌握

    # 光环
    Concentration_Aura = None  # 专注光环

    # 祝福
    Blessing_of_Wisdom = None  # 智慧祝福
    Greater_Blessing_of_Wisdom = None  # 超级智慧祝福

    Cleanse = None  # 净化术, 驱散 魔法, 中毒, 疾病
    Consecration = None  # 奉献
    Divine_Favor = None  # 神恩术, 下一个法术必暴
    Divine_Illumination = None  # 神启术, 耗蓝降低 50%
    Divine_Plea = None  # 神圣恳求
    Exorcism = None  # 驱邪术
    Holy_Wrath = None  # 神圣愤怒, 对亡灵怪群晕
    Lay_on_Hands = None  # 圣疗术
    Purify = None  # 纯净术, 低等级技能, 会被 净化术 所取代
    Redemption = None  # 复活
    Sacred_Shield = None  # 神圣护盾
    Seal_of_Light = None  # 光明圣印
    Seal_of_Righteousness = None  # 公正圣印
    Seal_of_Wisdom = None  # 智慧圣印
    Sense_Undead = None  # 感知亡灵
    Turn_Evil = None  # 转化亡灵, 恐惧亡灵怪


class Healbot(ActFactory):
    pass


class Paladin(Retribution, Protection, Holy, Healbot):
    pass
