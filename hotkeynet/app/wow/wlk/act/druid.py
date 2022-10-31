# -*- coding: utf-8 -*-

from hotkeynet.keyname import *
from hotkeynet import (
    ActFactory,
    CN,
)


class Balance(ActFactory):
    # 平衡系主打技能
    Moonfire = None  # 月火术
    Insect_Swarm = None  # 虫群, Dot, 平衡系天赋技能
    Wrath = None  # 愤怒
    Starfire = None  # 星火术
    Starfall = None  # 星落术, 强大的 AOE 技能, 平衡系天赋技能
    Hurricane = ALT_(X)  # 飓风, 主力 AOE 技能
    Typhoon = None  # 台风, 俗称推推, 造成伤害并将目标向后退
    Force_of_Nature = None  # 自然之力, 召唤树人, 平衡系天赋技能
    Moonkin_FormShapeshift = None  # 枭兽形态, 平衡系天赋技能

    # 控制技能
    Cyclone = ALT_(E)  # 龙卷风, 控制技能, 使目标无法做任何动作, 也无法被攻击
    Entangling_Roots = CTRL_(E)  # 纠缠根须, 控制技能, 使目标无法移动
    Hibernate = ALT_(T)  # 催眠, 控制技能, 只能对动物和龙类使用
    Nature_s_Grasp = None  # 自然之握, 使你被击中后自动召唤纠缠根须定身攻击者

    # 其他
    Barkskin = SHIFT_(F1)  # 树皮术
    Faerie_Fire = R  # 精灵之火, 破隐形, 降低护甲
    Innervate = CTRL_(F)  # 激活, 为目标回复大量法力
    Thorns = None  # 荆棘术
    Soothe_Animal = ALT_(Z)  # 安抚动物, 使目标的仇恨范围降低
    Teleport_Moonglade = None  # 传送 月光林地


class Restoration(ActFactory):
    # 恢复系主打技能
    Rejuvenation = Z  # 回春术
    Regrowth = None  # 愈合
    Nourish = None  # 滋养
    Lifebloom = None  # 生命之花, hot, 周期结束后会返回部分蓝耗
    Wild_Growth = None  # 野性生长, 群体治疗, 恢复系天赋技能
    Swiftmend = None  # 迅捷治愈, 恢复系天赋技能
    Tree_of_LifeShapeshift = None  # 治疗之树形态

    # Buff
    Gift_of_the_Wild = None  # 野性赐福
    Mark_of_the_Wild = None  # 野性印记

    # 驱散
    Abolish_Poison = ALT_(R)  # 驱毒术
    Cure_Poison = None  # 治疗中毒
    Remove_Curse = T  # 驱散诅咒

    Nature_s_Swiftness = None  # 自然迅捷, 下一个技能瞬发, 恢复系天赋技能
    Healing_Touch = None  # 治疗之触

    Revive = None  # 复活
    Rebirth = CTRL_(X)  # 战斗复活
    Tranquility = CTRL_(G)  # 宁静, 长 CD 小队治疗


class Feral(ActFactory):
    # 熊形态
    Bear_FormShapeshift = SHIFT_(Q)  # 熊形态

    # 仇恨技能
    Growl = None  # 嘲讽
    Lacerate = None  # 割伤, 仇恨技能
    Maul = None  # 锤击, 类似于战士的英勇打击
    Mangle_Bear = None  # 裂伤 熊形态, 野性系天赋技能
    Swipe_Bear = None  # 扫击 熊形态

    Bash = None  # 重击, 使目标昏迷, 控制技能
    Challenging_Roar = None  # 挑战咆哮, 群体嘲讽
    Demoralizing_Roar = None  # 挫志咆哮
    Feral_Charge_Bear = None  # 野性冲锋 熊形态, 野性系天赋技能

    # 其他
    Enrage = None  # 激怒, 类似于战士的血性狂暴
    Survival_Instincts = None  # 生存本能, 提高生命上限, 类似于战士的破釜沉舟
    Frenzied_Regeneration = None  # 狂暴回复, 怒气转血量

    # 猫形态
    Cat_FormShapeshift = SHIFT_(W)  # 猫形态
    Prowl = None  # 潜行

    Enter_Prowl_Macro = ALT_(F1)  # 进入潜行状态宏
    """
    #showtooltips
    /cast [stance:0/1/2/4/5] 猎豹形态
    /cast [stance:3] !潜行
    """

    # 起手技
    Pounce = None  # 突袭, 使目标昏迷, 类似与盗贼的偷袭
    Ravage = None  # 毁灭, 类似于盗贼的伏击

    # 攒星技
    Rake = None  # 斜掠, 使目标流血
    Claw = None  # 爪击, 类似于盗贼的邪恶打击
    Shred = None  # 撕碎, 类似于盗贼的背刺
    Mangle_Cat = None  # 裂伤, 猫形态, 类似于盗贼的出血, 野性系天赋技能

    # 终结技
    Ferocious_Bite = None  # 凶猛撕咬, 类似于盗贼的剔骨
    Rip = None  # 割裂, 造成持续伤害, 类似于盗贼的割裂
    Maim = None  # 割碎, 使目标昏迷, 类似于盗贼的肾击
    Savage_Roar = None  # 野蛮咆哮, 短时间内提高物理伤害

    Berserk = None  # 狂暴, 熊猫通用爆发技能, 野性系天赋技能

    # 其他
    Feral_Charge_Cat = None  # 野性冲锋 猫形态, 野性系天赋技能
    Dash = None  # 冲刺, 类似于盗贼的疾跑
    Cower = None  # 畏缩, 降低仇恨
    Swipe_Cat = None  # 扫击 猫形态

    Faerie_Fire_Feral = None  # 精灵之火 野性
    Tiger_s_Fury = None  # 猛虎之怒, 提高物理伤害

    Track_Humanoids = None  # 追踪人形生物

    Aquatic_FormShapeshift = ALT_(F2)  # 水栖形态
    Travel_FormShapeshift = None  # 旅行形态
    Flight_FormShapeshift = NUMPAD_11_DIVIDE  # 飞行形态


class Healbot(ActFactory):
    HB_Rejuvenation = None  # 回春术
    HB_Regrowth = None  # 愈合
    HB_Nourish = None  # 滋养
    HB_Lifebloom = None  # 生命之花, hot, 周期结束后会返回部分蓝耗
    HB_Wild_Growth = None  # 野性生长, 群体治疗, 恢复系天赋技能
    HB_Swiftmend = None  # 迅捷治愈, 恢复系天赋技能
    HB_Abolish_Poison = None  # 驱毒术
    HB_Remove_Curse = None  # 驱散诅咒
    HB_Innervate = CN.middle  # 激活, 为目标回复大量法力


class Druid(Balance, Restoration, Feral, Healbot):
    pass


class DruidBalance(Druid):
    Starfall = ALT_(F)  # 星落术, 强大的 AOE 技能, 平衡系天赋技能
    Typhoon = G  # 台风, 俗称推推, 造成伤害并将目标向后退
    Force_of_Nature = None  # 自然之力, 召唤树人, 平衡系天赋技能
    Moonkin_FormShapeshift = SHIFT_(E)  # 枭兽形态, 平衡系天赋技能


class DruidRestoration(Druid):
    Wild_Growth = None  # 野性生长, 群体治疗, 恢复系天赋技能
    Swiftmend = None  # 迅捷治愈, 恢复系天赋技能
    Tree_of_LifeShapeshift = SHIFT_(E)  # 治疗之树形态
    Nature_s_Swiftness = None  # 自然迅捷, 下一个技能瞬发, 恢复系天赋技能

    HB_Rejuvenation = CN.left  # 回春术
    HB_Regrowth = CN.alt_left_click  # 愈合
    HB_Nourish = CN.right  # 滋养
    HB_Lifebloom = None  # 生命之花, hot, 周期结束后会返回部分蓝耗
    HB_Wild_Growth = CN.shift_left_click  # 野性生长, 群体治疗, 恢复系天赋技能
    HB_Swiftmend = CN.alt_right_click  # 迅捷治愈, 恢复系天赋技能
    HB_Abolish_Poison = CN.ctrl_right_click  # 驱毒术
    HB_Remove_Curse = CN.ctrl_left_click  # 驱散诅咒


class DruidFeral(Druid):
    Feral_Charge_Bear = None  # 野性冲锋 熊形态, 野性系天赋技能
    Feral_Charge_Cat = None  # 野性冲锋 猫形态, 野性系天赋技能
    Berserk = None  # 狂暴, 熊猫通用爆发技能, 野性系天赋技能


druid = Druid()
druid_balance = DruidBalance()
druid_restoration = DruidRestoration()
druid_feral = DruidFeral()
