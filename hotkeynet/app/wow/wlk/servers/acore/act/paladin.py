# -*- coding: utf-8 -*-

from hotkeynet.keyname import *
from hotkeynet import (
    ActFactory,
    CN,
)


class Retribution(ActFactory):
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

    Avenging_Wrath = SHIFT_(F)  # 复仇之怒
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
    Divine_Protection = SHIFT_(F2)  # 圣佑术, 减伤
    Divine_Sacrifice = SHIFT_(C)  # 神圣牺牲, 团队减伤
    Divine_Shield = SHIFT_(F1)  # 圣盾术, 无敌

    Hammer_of_Justice = CTRL_(E)  # 制裁之锤, 控制技

    # 特殊效果的祝福
    Hand_of_Freedom = SHIFT_(R)  # 自由祝福
    Hand_of_Protection = SHIFT_(G)  # 保护祝福
    Hand_of_Sacrifice = ALT_(R)  # 牺牲祝福
    Hand_of_Salvation = CTRL_(R)  # 拯救祝福
    Seal_of_Justice = None  # 公正圣印 (有几率打晕敌人)


class Holy(ActFactory):
    # 神圣系主打技能
    Beacon_of_Light = None  # 圣光道标
    Holy_Light = X  # 圣光术
    Flash_of_Light = ALT_(X)  # 圣光闪现
    Holy_Shock = None  # 神圣冲击
    Aura_Mastery = ALT_(Z)  # 光环掌握

    # 光环
    Concentration_Aura = None  # 专注光环

    # 祝福
    Blessing_of_Wisdom = None  # 智慧祝福
    Greater_Blessing_of_Wisdom = None  # 超级智慧祝福

    Cleanse = T  # 净化术, 驱散 魔法, 中毒, 疾病
    Consecration = None  # 奉献
    Divine_Favor = None  # 神恩术, 下一个法术必暴
    Divine_Illumination = None  # 神启术, 耗蓝降低 50%
    Divine_Plea = ALT_(E)  # 神圣恳求
    Exorcism = G  # 驱邪术
    Holy_Wrath = SHIFT_(OEM3_WAVE_OR_BACK_QUOTE)  # 神圣愤怒, 对亡灵怪群晕
    Lay_on_Hands = None  # 圣疗术
    Purify = T  # 纯净术, 低等级技能, 会被 净化术 所取代
    Redemption = None  # 复活
    Sacred_Shield = CTRL_(X)  # 圣洁护盾
    Seal_of_Light = None  # 光明圣印
    Seal_of_Righteousness = None  # 公正圣印
    Seal_of_Wisdom = None  # 智慧圣印
    Sense_Undead = None  # 感知亡灵
    Turn_Evil = CTRL_(F)  # 转化亡灵, 恐惧亡灵怪


class Healbot(ActFactory):
    HB_Holy_Light = CN.left
    HB_Sacred_Shield = CN.alt_left_click
    HB_Cleanse = CN.ctrl_left_click

    HB_Flash_of_Light = CN.right
    HB_Hand_of_Freedom = CN.alt_right_click

    HB_Hand_of_Sacrifice = CN.shift_middle_click
    HB_Hand_of_Salvation = CN.alt_middle_click
    HB_Hand_of_Protection = CN.ctrl_middle_click
    HB_Righteous_Defense = None
    HB_Divine_Intervention = None
    HB_Lay_on_Hands = None
    HB_Beacon_of_Light = None
    HB_Holy_Shock = None


class Paladin(Retribution, Protection, Holy, Healbot):
    pass


class PaladinProtection(Paladin):
    Judgement_of_Light = KEY_1
    Judgement_of_Wisdom = KEY_1
    Judgement_of_Justice = KEY_1
    Hand_of_Reckoning = Z
    Hammer_of_the_Righteous = KEY_2
    Shield_of_Righteousness = ALT_(KEY_2)

    Holy_Shield = KEY_3
    Avenger_s_Shield = ALT_(KEY_3)
    Consecration = KEY_4
    Righteous_Defense = ALT_(F)


class PaladinRetribution(Paladin):
    Judgement_of_Light = KEY_1
    Judgement_of_Wisdom = KEY_1
    Judgement_of_Justice = KEY_1
    Hand_of_Reckoning = Z
    Crusader_Strike = KEY_2
    Divine_Storm = KEY_3
    Consecration = KEY_4
    Repentance = ALT_(E)
    Righteous_Defense = ALT_(F)


class PaladinHoly(Paladin):
    """
    由于奶骑按照职业顺序 (板甲 -> 布甲, 单一职业 -> 混合职业) 是第一个治疗职业, 而 Healbot
    的快捷键我们是按照一定的逻辑来的. 这里我们就来解说一下这个逻辑.

    - 左键 / 右键 是最高频的治疗技能
    - Shift / Alt + 左键 / 右键 是次高频的治疗技能
    - Ctrl + 左键 / 右键 是驱散类技能, 其中 Ctrl + 左键为更主要的驱散技能
    - 中键 是临时性的技能, 例如骑士给保护祝福, 德鲁伊给激活等
    """
    Beacon_of_Light = KEY_0

    # --- 神圣天赋下专属键位 ---
    One_Minute_Heal_Rotation_Macro_copy_1 = KEY_1
    """
    以 1 分钟为一个循环 (根据你的急速) 的治疗宏
    以 /castsequence reset=30 为起始, 以 X 圣闪 Y 圣光 的比例组成一个 5 - 6 秒的循环, 
    在第 30 秒的时候施放 神圣恳求 回蓝. 这个 X, Y 的比例取决于你的缺不缺蓝. 你不缺蓝则圣光
    多一点, 缺蓝则圣闪多一些. 然后根据你的急速填充满 60 秒循环.
    
    宏命令的例子如下:

    /castsequence reset=30 Flash of Light,Flash of Light,Flash of Light,Holy Light,Flash of Light,Flash of Light,Flash of Light,Holy Light,Flash of Light,Flash of Light,Flash of Light,Holy Light,Flash of Light,Flash of Light,Flash of Light,Holy Light,Divine Plea,Flash of Light,Flash of Light,Flash of Light,Holy Light,Flash of Light,Flash of Light,Flash of Light,Holy Light,Flash of Light,Flash of Light,Flash of Light,Holy Light,Flash of Light,Flash of Light,Flash of Light,Holy Light,Flash of Light,Flash of Light,Flash of Light,Holy Light,
    """
    One_Minute_Heal_Rotation_Macro_copy_2 = KEY_2  # 和上面的技能效果一样, 不过放在了另一个键位, 我们有特殊原因.

    Periodical_Beacon_of_Light_on_Focus_Macro = KEY_3
    """
    每 1.5 分钟一次的给焦点刷新圣光道标宏. 里面的 ``,`` 的数量决定了刷新道标的概率. 注意,
    这个宏里不能有 ``/stopcasting``, 不然你一按到这个键就打断当前治疗施法可不行. 也就是说
    这个宏即使我们轮到了施放圣光道标, 也不一定会成功, 我们就算这个概率是 50% 好了.
    例如有 9 个逗号, 意味着按 10 下该技能会生效一次. 如果你平均每 3 秒按一下这个键, 那么
    平均 30 秒会放一次圣光道标, 结合 50% 的概率, 平均每 60 秒刷新一次道标.

    #showtooltip
    /target focus
    /castsequence Beacon of Light,,,,,,,,,,,,,,,,,,
    """

    Periodical_Judgement_of_Light_on_Focus_Target_Macro = KEY_4
    """
    每 15 秒一次的对焦点的目标打审判宏以触发奶骑的急速 Buff. 偶尔给自己补圣洁护盾.
    这个也是一个用概率来实现周期性施法的宏. 例如我们平均 15 秒按一次这个技能, 大部分的时候
    我们是打审判, 偶尔是放圣洁护盾.

    #showtooltip
    /assist focus
    /startattack
    /castsequence Judgement of Light,Judgement of Light,Sacred Shield
    """

    Holy_Shock = Z
    Focus_Judgement = R
    """
    如果焦点是敌人, 则对焦点打审判. 如果焦点是友方, 则对焦点目标打审判.
    通常用于设置坦克或者Boss为焦点的情况下使用, 避免选择目标的麻烦.

    #showtooltip
    /cast [target=focustarget,harm][target=focus,harm][] Judgement of Light;
    """

    HB_Beacon_of_Light = CN.middle
    HB_Holy_Shock = CN.shift_right_click


paladin = Paladin()
paladin_retribution = PaladinRetribution()
paladin_protection = PaladinProtection()
paladin_holy = PaladinHoly()
