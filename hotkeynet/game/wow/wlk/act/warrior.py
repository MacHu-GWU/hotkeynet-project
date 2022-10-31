# -*- coding: utf-8 -*-

from hotkeynet.keyname import *
from hotkeynet import (
    ActFactory,
    CN,
)


class Arm(ActFactory):
    # 战斗姿态主打技能
    Battle_Stance = None  # 战斗姿态

    Rend = None  # 撕裂, 造成流血伤害
    Heroic_Strike = None  # 英勇打击
    Overpower = None  # 压制, 在目标躲闪招架后可以使用
    Mortal_Strike = None  # 致死打击, 武器系天赋技能
    Thunder_Clap = None  # 雷霆一击, 群体降低攻击速度

    # 天赋技能
    Retaliation = None  # 反击风暴, 武器系天赋技能
    Bladestorm = None  # 剑刃风暴, 武器系天赋技能

    Charge = None  # 冲锋
    Hamstring = None  # 断筋, 减速技能
    Heroic_Throw = None  # 英勇投掷
    Mocking_Blow = None  # 惩戒痛击

    Shattering_Throw = None  # 破甲投掷
    Sweeping_Strikes = None  # 横扫攻击, 武器系天赋技能


class Fury(ActFactory):
    # 狂暴姿态主打技能
    Berserker_Stance = None  # 狂暴姿态

    Bloodthirst = None  # 嗜血术
    Whirlwind = None  # 旋风斩
    Cleave = None  # 顺劈斩
    Slam = None  # 猛击
    Execute = None  # 斩杀

    # 天赋技能
    Piercing_Howl = None  # 刺耳咆哮, 群体减速, 狂暴系天赋技能
    Death_Wish = None  # 死亡之愿, 狂暴系天赋技能
    Heroic_Fury = None  # 英勇狂怒, 移除定身效果

    # 其他
    Berserker_Rage = None  # 狂暴之怒, 免疫恐惧

    Commanding_Shout = None  # 命令咆哮, 增加血量上线
    Battle_Shout = None  # 战斗咆哮, 增加攻击强度
    Demoralizing_Shout = None  # 挫志咆哮, 降低敌人的攻击强度
    Challenging_Shout = None  # 挑战咆哮, 群体嘲讽

    Intercept = None  # 拦截
    Intimidating_Shout = None  # 战栗咆哮, 群体恐惧
    Recklessness = None  # 鲁莽
    Pummel = None  # 拳击, 打断施法
    Victory_Rush = None  # 胜利追击


class Protection(ActFactory):
    # 防御姿态主打技能
    Defensive_Stance = None  # 防御姿态

    Taunt = None  # 嘲讽
    Sunder_Armor = None  # 破甲
    Revenge = None  # 复仇
    Shield_Block = None  # 盾牌格挡
    Shield_Slam = None  # 盾牌猛击
    Devastate = None  # 毁灭, 防护系天赋技能
    Shockwave = None  # 冲击破, 群体控制, 高仇恨, 防护系天赋技能
    Bloodrage = None  # 血性狂暴

    Concussion_Blow = None  # 震荡猛击, 控制技, 昏迷目标, 防护系天赋技能
    Disarm = None  # 缴械
    Shield_Bash = None  # 盾击

    Last_Stand = None  # 破釜沉舟, 增加生命上限, 防护系天赋技能
    Shield_Wall = None  # 盾墙

    Spell_Reflection = None  # 法术反射

    Intervene = None  # 援护, 拦下对目标的下一次攻击
    Vigilance = None  # 警戒


class Healbot(ActFactory):
    pass


class Warrior(Arm, Fury, Protection, Healbot):
    pass


class WarriorArm(Warrior):
    Mortal_Strike = None  # 致死打击, 武器系天赋技能
    Retaliation = None  # 反击风暴, 武器系天赋技能
    Bladestorm = None  # 剑刃风暴, 武器系天赋技能


class WarriorFury(Warrior):
    Bloodthirst = None  # 嗜血术
    Piercing_Howl = None  # 刺耳咆哮, 群体减速, 狂暴系天赋技能
    Death_Wish = None  # 死亡之愿, 狂暴系天赋技能
    Heroic_Fury = None  # 英勇狂怒, 移除定身效果


class WarriorProtection(Warrior):
    Concussion_Blow = None  # 震荡猛击, 控制技, 昏迷目标, 防护系天赋技能
    Vigilance = None  # 警戒
    Devastate = None  # 毁灭, 防护系天赋技能
    Shockwave = None  # 冲击破, 群体控制, 高仇恨, 防护系天赋技能


warrior = Warrior()
warrior_arm = WarriorArm()
warrior_fury = WarriorFury()
warrior_protection = WarriorProtection()
