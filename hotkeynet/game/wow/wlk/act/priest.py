# -*- coding: utf-8 -*-

from hotkeynet.keyname import *
from hotkeynet import (
    ActFactory,
    CN,
)


class Discipline(ActFactory):
    # 戒律系主打技能
    Penance = None  # 苦修, 通道型治疗技能, 戒律系天赋技能
    Power_Word_Shield = None  # 真言术盾
    Dispel_Magic = None  # 驱散魔法
    Mass_Dispel = None  # 群体驱散

    Inner_Focus = None  # 心灵专注, 使你的下一个法术必暴击, 戒律系天赋技能
    Power_Infusion = None  # 能量灌注, 使目标的施法速度提高, 戒律系天赋技能
    Pain_Suppression = None  # 痛苦压制, 减伤技能, 戒律系天赋技能

    Power_Word_Fortitude = None  # 真言术韧
    Prayer_of_Fortitude = None  # 真言术韧祷言
    Divine_Spirit = None  # 神圣精神
    Prayer_of_Spirit = None  # 神圣精神祷言

    Mana_Burn = None  # 法力燃烧
    Inner_Fire = None  # 心灵之火
    Levitate = None  # 漂浮术
    Fear_Ward = None  # 防护恐惧结界

    Shackle_Undead = None  # 束缚亡灵, 控制技能


class Holy(ActFactory):
    # 神圣系主打技能
    Renew = None  # 恢复
    Prayer_of_Healing = None  # 愈合祷言
    Binding_Heal = None  # 联结治疗, 治疗目标与你自己
    Flash_Heal = None  # 快速治疗
    Greater_Heal = None  # 超级治疗术
    Holy_Nova = None  # 神圣新星
    Circle_of_Healing = None  # 治疗之环, 群体治疗技能, 神圣系天赋技能
    Desperate_Prayer = None  # 绝望祷言, 神圣系天赋技能
    Lightwell = None  # 光明之井, 神圣系天赋技能
    Guardian_Spirit = None  # 守护天使, 保护目标不被一击必杀一次, 神圣系天赋技能

    Smite = None  # 惩击
    Holy_Fire = None  # 神圣之火, 神圣系天赋技能

    Abolish_Disease = None  # 驱除疾病

    Divine_Hymn = None  # 神圣赞美诗, 长 CD 团队回血技能
    Hymn_of_Hope = None  # 希望颂歌, 长 CD 团队回蓝技能

    Resurrection = None  # 复活


class Shadow(ActFactory):
    # 暗影系主打攻击技能
    Shadow_Word_Pain = None  # 暗言术 痛
    Devouring_Plague = None  # 噬灵瘟疫
    Vampiric_Touch = None  # 吸血鬼之触
    Mind_Flay = None  # 精神鞭笞
    Mind_Blast = None  # 心灵震爆
    Mind_Sear = None  # 精神灼烧
    Psychic_Horror = None  # 心灵惊骇, 远程恐惧单体目标, 暗影系天赋技能

    Silence = None  # 沉默, 暗影系天赋技能
    Shadowform = None  # 暗影形态, 暗影系天赋技能
    Vampiric_Embrace = None  # 吸血鬼的拥抱, 暗影系天赋技能
    Dispersion = None  # 影散, 回蓝和减伤技能, 暗影系天赋技能
    Shadow_Word_Death = None  # 暗言术 死
    Shadowfiend = None  # 暗影恶魔

    Fade = None  # 渐隐术, 暂时降低仇恨

    Mind_Control = None  # 精神控制
    Mind_Soothe = None  # 精神安抚
    Mind_Vision = None  # 精神视界
    Psychic_Scream = None  # 精神尖啸, 群体恐惧
    Shadow_Protection = None  # 暗影防护
    Prayer_of_Shadow_Protection = None  # 暗影防护祷言


class Healbot(ActFactory):
    Power_Word_Shield = None  # 真言术盾
    Penance = None  # 苦修, 通道型治疗技能, 戒律系天赋技能
    Pain_Suppression = None  # 痛苦压制, 减伤技能, 戒律系天赋技能
    Dispel_Magic = None  # 驱散魔法
    Abolish_Disease = None  # 驱除疾病
    Renew = None  # 恢复
    Prayer_of_Healing = None  # 愈合祷言
    Binding_Heal = None  # 联结治疗, 治疗目标与你自己
    Flash_Heal = None  # 快速治疗
    Greater_Heal = None  # 超级治疗术
    Holy_Nova = None  # 神圣新星
    Circle_of_Healing = None  # 治疗之环, 群体治疗技能, 神圣系天赋技能
    Guardian_Spirit = None  # 守护天使, 保护目标不被一击必杀一次, 神圣系天赋技能
    Fear_Ward = None  # 防护恐惧结界


class Priest(Discipline, Holy, Shadow, Healbot):
    pass


class PriestDiscipline(Priest):
    Inner_Focus = None  # 心灵专注, 使你的下一个法术必暴击, 戒律系天赋技能
    Power_Infusion = None  # 能量灌注, 使目标的施法速度提高, 戒律系天赋技能
    Pain_Suppression = None  # 痛苦压制, 减伤技能, 戒律系天赋技能
    Penance = None  # 苦修, 通道型治疗技能, 戒律系天赋技能


class PriestHoly(Priest):
    Desperate_Prayer = None  # 绝望祷言, 神圣系天赋技能
    Holy_Fire = None  # 神圣之火, 神圣系天赋技能
    Circle_of_Healing = None  # 治疗之环, 群体治疗技能, 神圣系天赋技能
    Lightwell = None  # 光明之井, 神圣系天赋技能
    Guardian_Spirit = None  # 守护天使, 保护目标不被一击必杀一次, 神圣系天赋技能


class PriestShadow(Priest):
    Mind_Flay = None  # 精神鞭笞
    Vampiric_Embrace = None  # 吸血鬼的拥抱, 暗影系天赋技能
    Shadowform = None  # 暗影形态, 暗影系天赋技能
    Psychic_Horror = None  # 心灵惊骇, 远程恐惧单体目标, 暗影系天赋技能Silence = None  # 沉默, 暗影系天赋技能
    Vampiric_Touch = None  # 吸血鬼之触
    Dispersion = None  # 影散, 回蓝和减伤技能, 暗影系天赋技能


priest = Priest()
priest_discipline = PriestDiscipline()
priest_holy = PriestHoly()
priest_shadow = PriestShadow()
