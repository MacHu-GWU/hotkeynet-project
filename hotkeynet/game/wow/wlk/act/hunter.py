# -*- coding: utf-8 -*-

from hotkeynet import ActFactory


class BeastMastery(ActFactory):
    # 兽王系主打技能
    Bestial_Wrath = None  # 狂野怒火, 让你的宠物在短时间内增加大量伤害, 兽王系天赋技能
    Intimidation = None  # 胁迫, 控制技, 兽王系天赋技能
    The_Beast_Within = None  # 人面兽心, 俗称小红人, 人和宠物都免疫控制, 兽王系天赋技能
    Kill_Command = None  # 杀戮命令
    Master_s_Call = None  # 主人的呼唤, 解除宠物身上的控制技能

    # 守护
    Aspect_of_the_Beast = None  # 野兽守护, 让自己变得无法追踪
    Aspect_of_the_Cheetah = None  # 猎豹守护, 单体加移动速度
    Aspect_of_the_Dragonhawk = None  # 龙鹰守护, 同时具有雄鹰守护和灵猴守护的效果
    Aspect_of_the_Hawk = None  # 雄鹰守护, 加远程攻击强度
    Aspect_of_the_Monkey = None  # 灵猴守护, 加 18% 躲闪
    Aspect_of_the_Pack = None  # 豹群守护, 群体加移动速度
    Aspect_of_the_Viper = None  # 蝮蛇守护, 回蓝
    Aspect_of_the_Wild = None  # 野性守护, 加自然抗性

    # 宠物相关
    Beast_Lore = None  # 野兽知识
    Call_Pet = None  # 召唤宠物
    Dismiss_Pet = None  # 解散宠物
    Feed_Pet = None  # 喂食
    Mend_Pet = None  # 治疗宠物
    Revive_Pet = None  # 复活宠物
    Tame_Beast = None  # 驯服野兽
    Eyes_of_the_Beast = None  # 野兽之眼, 以你的宠物的视角操控你它

    Eagle_Eye = None  # 鹰眼术

    Scare_Beast = None  # 恐吓野兽


class Marksmanship(ActFactory):
    # 射击系主打技能
    Serpent_Sting = None  # 毒蛇钉刺
    Steady_Shot = None  # 稳固射击
    Chimera_Shot = None  # 奇美拉设计, 射击系天赋技能
    Aimed_Shot = None  # 瞄准射击
    Silencing_Shot = None  # 沉默射击, 射击系天赋技能
    Kill_Shot = None  # 杀戮射击, 对血量低于一定值的目标可用, 斩杀阶段技能
    Multi_Shot = None  # 多重射击
    Volley = None  # 乱射
    Trueshot_Aura = None  # 强击光环

    Hunter_s_Mark = None  # 猎人印记

    Viper_Sting = None  # 蝮蛇钉刺, 吸蓝效果

    Arcane_Shot = None  # 奥术射击
    Concussive_Shot = None  # 震荡射击
    Tranquilizing_Shot = None  # 宁神射击, 移除激怒效果

    Distracting_Shot = None  # 扰乱, 使目标攻击你, 猎人的嘲讽
    Flare = None  # 照明弹, 侦测隐形

    Rapid_Fire = None  # 急速射击, 长 CD 冷却技能
    Readiness = None  # 预备, 重置你的技能 CD, 射击系天赋技能


class Survival(ActFactory):
    # 生存系主打技能
    Black_Arrow = None  # 黑蚀箭, 生存系天赋技能
    Wyvern_Sting = None  # 奇美拉钉刺, 使目标进入沉睡, 苏醒后造成伤害, 生存系天赋技能
    Explosive_Shot = None  # 爆炸射击, 生存系天赋技能

    # 生存类技能
    Counterattack = None  # 还击, 近战技能, 招架后使用, 造成伤害并使得目标定身, 生存系天赋技能
    Deterrence = None  # 威慑, 100% 躲闪以及偏斜法术, 保命技能
    Disengage = None  # 逃脱, 向后跳, 位移技能
    Mongoose_Bite = None  # 近战攻击技能
    Raptor_Strike = None  # 猛禽以及, 近战攻击技能
    Feign_Death = None  # 假死

    # 陷阱
    Immolation_Trap = None  # 献祭陷阱
    Snake_Trap = None  # 毒蛇陷阱

    # 控制类技能
    Scatter_Shot = None  # 驱散射击, 控制技能, 生存系天赋技能
    Freezing_Arrow = None  # 冰冻箭, 远程版本的冰冻陷阱
    Freezing_Trap = None  # 冰冻陷阱, 使目标无法做出任何动作, 控制技能
    Frost_Trap = None  # 冰霜陷阱, 使进入范围内的敌人移动速度降低
    Wing_Clip = None  # 摔绊, 近战技能, 使目标减速

    # 追踪
    Track_Beasts = None  # 追踪野兽
    Track_Demons = None  # 追踪恶魔
    Track_Dragonkin = None  # 追踪龙类
    Track_Elementals = None  # 追踪元素
    Track_Giants = None  # 追踪巨人
    Track_Hidden = None  # 追踪隐形
    Track_Humanoids = None  # 追踪人形生物
    Track_Undead = None  # 追踪亡灵

    Misdirection = None  # 误导, 使你下几次攻击造成的仇恨转移到指定目标身上


class Healbot(ActFactory):
    Misdirection = None  # 误导, 使你下几次攻击造成的仇恨转移到指定目标身上


class Hunter(BeastMastery, Marksmanship, Survival, Healbot):
    pass


class HunterBeastMastery(Hunter):
    Bestial_Wrath = None  # 狂野怒火, 让你的宠物在短时间内增加大量伤害, 兽王系天赋技能
    Intimidation = None  # 胁迫, 控制技, 兽王系天赋技能
    The_Beast_Within = None  # 人面兽心, 俗称小红人, 人和宠物都免疫控制, 兽王系天赋技能


class HunterMarksmanship(Hunter):
    Chimera_Shot = None  # 奇美拉设计, 射击系天赋技能
    Silencing_Shot = None  # 沉默射击, 射击系天赋技能
    Trueshot_Aura = None  # 强击光环
    Readiness = None  # 预备, 重置你的技能 CD, 射击系天赋技能


class HunterSurvival(Hunter):
    Counterattack = None  # 还击, 近战技能, 招架后使用, 造成伤害并使得目标定身, 生存系天赋技能
    Black_Arrow = None  # 黑蚀箭, 生存系天赋技能
    Wyvern_Sting = None  # 奇美拉钉刺, 使目标进入沉睡, 苏醒后造成伤害, 生存系天赋技能
    Explosive_Shot = None  # 爆炸射击, 生存系天赋技能


hunter = Hunter()
hunter_beastMastery = HunterBeastMastery()
hunter_marksmanship = HunterMarksmanship()
hunter_survival = HunterSurvival()
