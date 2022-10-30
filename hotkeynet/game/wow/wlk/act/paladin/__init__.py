# -*- coding: utf-8 -*-

"""
This is a sample script to configure your spell key binding for multiboxing.

You should copy and paste this script as your foundation and fill in your own
spell key binding.

这个文件有

- class $Talent1: 属于该系的职业技能, 这些技能的键位设定应该是无论你当前使用的什么天赋, 都应该是用这个键位
- class $Talent2: 同上
- class $Talent3: 同上
- class Healbot: 使用 Healbot 团队框架施放的技能, 这些技能的键位设定应该是无论你当前使用的什么天赋, 都应该是用这个键位
- class $ClassName: 汇总所有无论你当前使用的什么天赋都适用的键位. 该类继承了 $Talent1, $Talent2, $Talent3, Healbot 四个类
- class $ClassName$Talent1: 设定使用特定天赋时特定的键位, 该类继承了 $ClassName, 特定键位只要覆盖父类的属性即可
- class $ClassName$Talent2: 同上
- class $ClassName$Talent3: 同上
"""

from ......act_factory import ActFactory


class Retribution(ActFactory):
    """

    """
    # 惩戒系主打技能
    Judgement_of_Light = None  # 光明审判
    Judgement_of_Wisdom = None  # 智慧审判
    Judgement_of_Justice = None  # 公正审判
    Crusader_Strike = None  # 十字军打击
    Divine_Storm = None  # 神圣风暴

    # 光环
    Retribution_Aura = None  # 惩戒光环
    Crusader_Aura = None  # 十字军光环

    # 祝福
    Blessing_of_Might = None  # 力量祝福
    Greater_Blessing_of_Might = None  # 强效力量祝福

    Avenging_Wrath = None  # 复仇之怒
    Hammer_of_Wrath = None  # 愤怒之锤
    Repentance = None  # 忏悔
    Seal_of_Command = None  # 命令圣印
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
    Fire_Resistance_Aura = None  # 火焰抗性光环
    Frost_Resistance_Aura = None  # 冰霜抗性光环
    Shadow_Resistance_Aura = None  # 暗影抗光环

    # 祝福
    Blessing_of_Kings = None  # 王者祝福
    Greater_Blessing_of_Kings = None  # 王者祝福
    Blessing_of_Sanctuary = None  # 庇护祝福
    Greater_Blessing_of_Sanctuary = None  # 强效庇护祝福

    Divine_Intervention = None  # 神圣干涉
    Divine_Protection = None  # 圣佑术, 减伤
    Divine_Sacrifice = None  # 神圣牺牲, 团队减伤
    Divine_Shield = None  # 圣盾术, 无敌

    Hammer_of_Justice = None  # 制裁之锤, 控制技

    # 特殊效果的祝福
    Hand_of_Freedom = None  # 自由祝福
    Hand_of_Protection = None  # 保护祝福
    Hand_of_Sacrifice = None  # 牺牲祝福
    Hand_of_Salvation = None  # 拯救祝福
    Seal_of_Justice = None  # 公正圣印 (有几率打晕敌人)


class Holy(ActFactory):
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
    Sacred_Shield = None  # 圣洁护盾
    Seal_of_Light = None  # 光明圣印
    Seal_of_Righteousness = None  # 公正圣印
    Seal_of_Wisdom = None  # 智慧圣印
    Sense_Undead = None  # 感知亡灵
    Turn_Evil = None  # 转化亡灵, 恐惧亡灵怪


class Healbot(ActFactory):
    Left = None
    Shift_Left = None
    Alt_Left = None
    Ctrl_Left = None
    Right = None
    Shift_Right = None
    Alt_Right = None
    Ctrl_Right = None
    Middle = None
    Shift_Middle = None
    Alt_Middle = None
    Ctrl_Middle = None

    HB_Holy_Light = None
    HB_Flash_of_Light = None
    HB_Sacred_Shield = None
    HB_Hand_of_Protection = None
    HB_Hand_of_Salvation = None
    HB_Hand_of_Sacrifice = None
    HB_Hand_of_Freedom = None
    HB_Righteous_Defense = None
    HB_Cleanse = None
    HB_Divine_Intervention = None
    HB_Lay_on_Hands = None


class Paladin(Retribution, Protection, Holy, Healbot):
    pass


class PaladinRetribution(Paladin):
    Divine_Storm = None


class PaladinProtection(Paladin):
    Hammer_of_the_Righteous = None


class PaladinHoly(Paladin):
    Beacon_of_Light = None
