# -*- coding: utf-8 -*-

ESC = "Esc"

F1 = "F1"
F2 = "F2"
F3 = "F3"
F4 = "F4"
F5 = "F5"
F6 = "F6"
F7 = "F7"
F8 = "F8"
F9 = "F9"
F10 = "F10"
F11 = "F11"
F12 = "F12"

OEM3_WAVE = "Oem3"
KEY_1 = "1"
KEY_2 = "2"
KEY_3 = "3"
KEY_4 = "4"
KEY_5 = "5"
KEY_6 = "6"
KEY_7 = "7"
KEY_8 = "8"
KEY_9 = "9"
KEY_0 = "0"
KEY_11_MINUS = "Minus"
KEY_12_PLUS = "Plus"
BACKSPACE = "Backspace"

TAB = "Tab"
CAPSLOCK = "CapsLock"
SHIFT = "Shift"
CTRL = "Ctrl"
ALT = "Alt"

LSHIFT = "LShift"
RSHIFT = "RShift"
LCTRL = "LCtrl"
RCTRL = "RCtrl"
LALT = "LAlt"
RALT = "RAlt"

SPACE = "Space"

A = "A"
B = "B"
C = "C"
D = "D"
E = "E"
F = "F"
G = "G"
H = "H"
I = "I"
J = "J"
K = "K"
L = "L"
M = "M"
N = "N"
O = "O"
P = "P"
Q = "Q"
R = "R"
S = "S"
T = "T"
U = "U"
V = "V"
W = "W"
X = "X"
Y = "Y"
Z = "Z"

OEM4_SQUARE_BRACKET_LEFT = "Oem4"
OEM6_SQUARE_BRACKET_RIGHT = "Oem6"
OEM5_PIPE = "Oem5"
OEM1_SEMICOLUMN = "Oem1"
OEM7_QUOTE = "Oem7"
COMMA = "Comma"
PERIOD = "Period"
OEM2_QUESTION = "Oem2"
ENTER = "Enter"

INSERT = "Insert"
HOME = "Home"
PAGE_UP = "PgUp"
DELETE = "Delete"
END = "End"
PAGE_DOWN = "PgDn"

LEFT = "Left"
UP = "Up"
RIGHT = "Right"
DOWN = "Down"

NUMPAD_0 = "Numpad0"
NUMPAD_1 = "Numpad1"
NUMPAD_2 = "Numpad2"
NUMPAD_3 = "Numpad3"
NUMPAD_4 = "Numpad4"
NUMPAD_5 = "Numpad5"
NUMPAD_6 = "Numpad6"
NUMPAD_7 = "Numpad7"
NUMPAD_8 = "Numpad8"
NUMPAD_9 = "Numpad9"
NUMPAD_11_DIVIDE = "Divide"
NUMPAD_12_MULTIPLY = "Multiply"

NUMPAD_MINUS = "NumpadMinus"
NUMPAD_PLUS = "NumpadPlus"
NUMPAD_ENTER = "NumpadEnter"
NUMPAD_DELETE = "NumpadDelete"

NUMPAD_SHIFT_1_END = "NumpadEnd"
NUMPAD_SHIFT_2_DOWN = "NumpadDown"
NUMPAD_SHIFT_3_PAGE_DOWN = "NumpadPgDn"
NUMPAD_SHIFT_4_LEFT = "NumpadLeft"
NUMPAD_SHIFT_5_CLEAR = "Clear"
NUMPAD_SHIFT_6_RIGHT = "NumpadRight"
NUMPAD_SHIFT_7_HOME = "NumpadHome"
NUMPAD_SHIFT_8_UP = "NumpadUp"
NUMPAD_SHIFT_9_PAGE_UP = "NumpadPgUp"

MOUSE_LButton = "LButton"
MOUSE_RButton = "RButton"
MOUSE_MButton = "MButton"
MOUSE_Button4 = "Button4"
MOUSE_Button5 = "Button5"


def CTRL_(*keys):
    return "{} {}".format(CTRL, ", ".join(keys))


def SHIFT_(*keys):
    return "{} {}".format(SHIFT, ", ".join(keys))


def ALT_(*keys):
    return "{} {}".format(ALT, ", ".join(keys))


def CTRL_ALT_(*keys):
    return "{} {} {}".format(CTRL, ALT, ", ".join(keys))


def CTRL_SHIFT_(*keys):
    return "{} {} {}".format(CTRL, SHIFT, ", ".join(keys))


def ALT_SHIFT_(*keys):
    return "{} {} {}".format(ALT, SHIFT, ", ".join(keys))


def CTRL_SHIFT_ALT(*keys):
    return "{} {} {} {}".format(CTRL, SHIFT, ALT, ", ".join(keys))


def SCROLOCK_ON(key):
    return "ScrollLockOn {}".format(key)


def CAPSLOCK_ON(key):
    return "CapsLockOn {}".format(key)


class Multibox:
    f1_to_f18 = [
        F1, F2, F3, F4, F5, F6, F7, F8, F9, F10, F11, F12,
        INSERT, HOME, PAGE_UP, DELETE, END, PAGE_DOWN,
    ]


class Paladin:
    ALL_SPEC_DIVINE_PLEA = MOUSE_MButton  # 神圣恩求 (回蓝技能)
    ALL_SPEC_AVENGING_WRATH = SHIFT_(F)  # 复仇之怒 (爆发技能)

    # --- Defensive CD 防御性CD技能 ---
    ALL_SPEC_DIVINE_SHIELD = SHIFT_(F1)  # 圣盾术 (无敌)
    ALL_SPEC_DIVINE_PROTECTION = SHIFT_(F2)  # 圣佑术 (50% 减伤)
    ALL_SPEC_DIVINE_SACRIFICE = SHIFT_(C)  # 神圣牺牲 (团队减伤技能)
    ALL_SPEC_AURA_MASTERY = ALT_(Z)  # 光环掌握

    # --- Hand Of xxx 给他人释放的功能性的祝福 ---
    ALL_SPEC_HAND_OF_PROTECTION = SHIFT_(G)  # 保护祝福
    ALL_SPEC_HAND_OF_SALVATION = CTRL_(R)  # 拯救祝福
    ALL_SPEC_HAND_OF_SACRIFICE = ALT_(E)  # 牺牲祝福
    ALL_SPEC_HAND_OF_FREEDOM = SHIFT_(R)  # 自由祝福

    # --- CC 控制类技能 ---
    ALL_SPEC_HAMMER_OF_JUSTICE = CTRL_(E)  # 制裁之锤
    ALL_SPEC_HOLY_WRATH = SHIFT_(OEM3_WAVE)  # 神圣愤怒 (对亡灵群体昏迷) Shift + ~
    ALL_SPEC_TURN_EVIL = CTRL_(F)  # 恐惧亡灵

    # --- 治疗类技能 ---
    ALL_SPEC_FLASH_OF_LIGHT = X  # 圣光闪现
    ALL_SPEC_HOLY_LIGHT = ALT_(X)  # 圣光术
    ALL_SPEC_CLEANSE = T  # 清洁术
    ALL_SPEC_SACRED_SHIELD = CTRL_(X)  # 圣洁护盾

    # --- 其他 ----
    ALL_SPEC_EXORCISM = G  # 驱邪术 (读条施法攻击技能, 对亡灵必爆)

    # --- 防护天赋下专属键位 ---
    PROTECT_SPEC_JUDGEMENT = KEY_1  # 智慧 | 光明 | 公正 审判
    PROTECT_SPEC_HAMMER_OF_THE_RIGHTEOUS = KEY_2  # 公正之锤 (防护 51 点天赋技能, 近战群拉高仇恨)
    PROTECT_SPEC_SHIELD_OF_RIGHTEOUSNESS = ALT_(KEY_2)  # 复仇之盾, 近战单体仇恨技能
    PROTECT_SPEC_HOLY_SHIELD = KEY_3  # 神圣之盾 (防护 31 点天赋技能, 短CD加大量格挡)
    PROTECT_SPEC_AVENGER_SHIELD = ALT_(KEY_3)  # 防御者之盾 (防护 41点天赋技能, 远程群体攻击, 打断施法并减速)
    PROTECT_SPEC_CONSECRATION = KEY_4  # 奉献 (AOE)
    PROTECT_SPEC_SACRED_SHIELD = KEY_5  # 圣洁护盾
    PROTECT_SPEC_HAND_OF_RECKONING = Z  # 嘲讽 (单体嘲讽)
    PROTECT_SPEC_RIGHTEOUS_DEFENCE = ALT_(F)  # 正义防护 (群体嘲讽)

    # --- 惩戒天赋下专属键位 ---
    RETRIBUTION_SPEC_JUDGEMENT = KEY_1  # 智慧 | 光明 | 公正 审判
    RETRIBUTION_SPEC_CRUSADER_STRIKE = KEY_2  # 十字军打击 (惩戒 41 点天赋技能)
    RETRIBUTION_SPEC_DIVINE_STORM = KEY_3  # 神圣风暴 (惩戒 51 点天赋技能)
    RETRIBUTION_SPEC_CONSECRATION = KEY_4  # 奉献 （AOE)
    RETRIBUTION_SPEC_SACRED_SHIELD = KEY_5  # 圣洁护盾
    RETRIBUTION_SPEC_REPENTANCE = ALT_(E)  # 忏悔 (惩戒 31 点天赋技能)
    RETRIBUTION_SPEC_HAND_OF_RECKONING = Z  # 嘲讽 (单体嘲讽)
    RETRIBUTION_SPEC_RIGHTEOUS_DEFENCE = ALT_(F)  # 正义防护 (群体嘲讽)

    # --- 神圣天赋下专属键位 ---
    HOLY_SPEC_ONE_MINUTE_HEAL_ROTATION_KEY_1 = KEY_1
    """
    以1分钟为一个循环 (根据你的急速) 的治疗宏
    以 /castsequence reset=30 为起始, 以 4 圣闪 1 圣光 或者 3闪 1 光, 或是 2 闪 2 光
    为一个 5 - 6 秒的循环, 在第30秒的时候释放 神圣恳求 回蓝, 然后根据你的急速填充满 60 秒循环
    例如:
    
    /castsequence reset=30 Flash of Light,Flash of Light,Flash of Light,Holy Light,Flash of Light,Flash of Light,Flash of Light,Holy Light,Flash of Light,Flash of Light,Flash of Light,Holy Light,Flash of Light,Flash of Light,Flash of Light,Holy Light,Divine Plea,Flash of Light,Flash of Light,Flash of Light,Holy Light,Flash of Light,Flash of Light,Flash of Light,Holy Light,Flash of Light,Flash of Light,Flash of Light,Holy Light,Flash of Light,Flash of Light,Flash of Light,Holy Light,Flash of Light,Flash of Light,Flash of Light,Holy Light,
    """
    HOLY_SPEC_ONE_MINUTE_HEAL_ROTATION_KEY_2 = KEY_2

    HOLY_SPEC_PERIODICAL_BEACON_OF_LIGHT_ON_FOCUS = KEY_3
    """
    每 1.5 分钟一次的给焦点刷新圣光道标宏
    
    #showtooltip
    /target focus
    /castsequence Beacon of Light,,,,,,,,,,,,,,,,,,
    """

    HOLY_SPEC_PERIODICAL_JUDGEMENT_OF_LIGHT_ON_FOCUS_TARGET = KEY_4
    """
    每 15 秒一次的对焦点的目标打审判宏. 偶尔给自己补圣洁护盾
    
    #showtooltip
    /assist focus
    /startattack
    /castsequence Judgement of Light,Judgement of Light,Sacred Shield
    """
    HOLY_SPEC_HOLY_LIGHT_KEY_5 = KEY_5  # 圣光术, 只有在神圣天赋下该键位有效
    HOLY_SPEC_FLASH_OF_LIGHT = KEY_6  # 圣光闪现, 只有在神圣天赋下该键位有效
    HOLY_SPEC_HOLY_LIGHT_KEY_7 = KEY_7  # 圣光术, 只有在神圣天赋下该键位有效
    HOLY_SPEC_HOLY_SHOCK = Z  # 神圣震击 (神圣 31 点天赋技能)
    HOLY_SPEC_FOCUS_JUDGEMENT = R
    """
    如果焦点是敌人, 则对焦点, 如果焦点是友方, 则对焦点目标打审判.
    通常用于设置坦克或者Boss为焦点的情况下使用, 避免选择目标的麻烦.
    
    #showtooltip
    /cast [target=focustarget,harm][target=focus,harm][] Judgement of Light;
    """
    HOLY_SPEC_BEACON_OF_LIGHT = KEY_0  # 圣光道标 (神圣 51 点天赋)

    # --- Healbot 团队框架快捷键 ---
    # Left | Right | Middle Click
    HEALBOT_LEFT_CLICK_HOLY_LIGHT = MOUSE_LButton
    HEALBOT_RIGHT_CLICK_FLASH_OF_LIGHT = MOUSE_RButton
    HEALBOT_MIDDLE_CLICK_BEACON_OF_LIGHT = MOUSE_MButton

    # <Template PaladinHealbotHolyLightLeftClick> // 圣光术
    #     <ClickMouse LButton>
    # <EndTemplate>
    #
    # <Template PaladinHealbotFlashOfLightRightClick> // 圣光闪现
    #     <ClickMouse RButton>
    # <EndTemplate>
    #
    # <Template PaladinHealbotBeaconOfLightMiddleClick> // 圣光道标
    #     <ClickMouse MButton>
    # <EndTemplate>
    #
    # // Shift | Alt | Ctrl + Left Click
    # <Template PaladinHealbotBeaconOfLightShiftLeftClick> // 圣光道标
    #     <KeyDown Shift>
    #     <ClickMouse LButton Down>
    #     <ClickMouse LButton Up>
    #     <KeyUp Shift>
    # <EndTemplate>
    #
    # <Template PaladinHealbotSacredShieldAltLeftClick> // 圣洁护盾
    #     <KeyDown Alt>
    #     <ClickMouse LButton Down>
    #     <ClickMouse LButton Up>
    #     <KeyUp Alt>
    # <EndTemplate>
    #
    # <Template PaladinHealbotCleanseCtrlLeftClick> // 清洁术
    #     <KeyDown Ctrl>
    #     <ClickMouse LButton Down>
    #     <ClickMouse LButton Up>
    #     <KeyUp Ctrl>
    # <EndTemplate>
    #
    # // Shift | Alt | Ctrl + Right Click
    # <Template PaladinHealbotHolyShockShiftRightClick> // 神圣震击
    #     <KeyDown Shift>
    #     <ClickMouse RButton Down>
    #     <ClickMouse RButton Up>
    #     <KeyUp Shift>
    # <EndTemplate>
    #
    # <Template PaladinHealbotHandOfFreedomAltRightClick> // 自由祝福
    #     <KeyDown Alt>
    #     <ClickMouse RButton Down>
    #     <ClickMouse RButton Up>
    #     <KeyUp Alt>
    # <EndTemplate>
    #
    # // <Template PaladinHealbot${SkillName}CtrlRightClick> //
    # //     <KeyDown Ctrl>
    # //     <ClickMouse RButton Down>
    # //     <ClickMouse RButton Up>
    # //     <KeyUp Ctrl>
    # // <EndTemplate>
    #
    # // Shift | Alt | Ctrl + Middle Click
    # <Template PaladinHealbotHandOfProtectionShiftMiddleClick> // 保护祝福
    #     <KeyDown Shift>
    #     <ClickMouse MButton Down>
    #     <ClickMouse MButton Up>
    #     <KeyUp Shift>
    # <EndTemplate>
    #
    # <Template PaladinHealbotHandOfSalvationAltMiddleClick> // 拯救祝福
    #     <KeyDown Alt>
    #     <ClickMouse MButton Down>
    #     <ClickMouse MButton Up>
    #     <KeyUp Alt>
    # <EndTemplate>
    #
    # <Template PaladinHealbotHandOfSacrificeCtrlMiddleClick> // 牺牲祝福
    #     <KeyDown Ctrl>
    #     <ClickMouse MButton Down>
    #     <ClickMouse MButton Up>
    #     <KeyUp Ctrl>
    # <EndTemplate>


class DK:
    ALL_SPEC_BLOOD_STRIKE = KEY_1  # 鲜血打击
    ALL_SPEC_HEART_STRIKE = KEY_1  # 心脏打击 (血天赋)

    ALL_SPEC_PESTILENCE_ALT_1 = ALT_(KEY_1)  # 传染
    ALL_SPEC_PESTILENCE_SHIFT_OEM3 = SHIFT_(OEM3_WAVE)  # 传染

    ALL_SPEC_ICE_TOUCH = KEY_2  # 冰冷触摸

    ALL_SPEC_CHAIN_OF_ICE_ALT_2 = ALT_(KEY_2)  # 寒冰锁链 (减速)
    ALL_SPEC_CHAIN_OF_ICE_CTRL_E = CTRL_(E)  # 寒冰锁链 (减速)

    ALL_SPEC_UNHOLY_STRIKE = KEY_3  # 邪恶打击
    ALL_SPEC_DEATH_COIL = ALT_(KEY_3)  # 死亡缠绕
    ALL_SPEC_FROST_STRIKE = ALT_(KEY_3)  # 冰霜打击 (冰天赋技能, 可以取代 死亡缠绕)

    ALL_SPEC_DEATH_STRIKE = KEY_4 # 死亡打击 (回血技能)
    ALL_SPEC_OBLITERATE = ALT_(KEY_4) # 湮没
    ALL_SPEC_SCOURGE_STRIKE = ALT_(KEY_4)  # 天灾打击 (邪天赋技能, 可以取代 湮没)

    ALL_SPEC_BLOOD_BOIL = KEY_5 # 血液沸腾
    ALL_SPEC_BLOOD_PRESENCE = SHIFT_(Q)  # 鲜血领域
    ALL_SPEC_FROST_PRESENCE = SHIFT_(W)  # 冰霜领域
    ALL_SPEC_UNHOLY_PRESENCE = SHIFT_(E)  # 邪恶领域

    ALL_SPEC_DARK_COMMAND = Z # 黑暗命令 (嘲讽)
    ALL_SPEC_RUNE_TAP = T # 符文分流 (血天赋, 回血技能)
    ALL_SPEC_DEATH_GRIP = G # 死亡之握 (远程嘲讽 加 拉人)
    ALL_SPEC_DEATH_AND_DECAY = X # 死亡凋零
    ALL_SPEC_MIND_FREEZE = R # 心灵冻结 (打断施法)
    ALL_SPEC_RUNE_STRIKE = ALT_(E) # 符文打击 (类似于战士的打击, 高仇恨技能)
    ALL_SPEC_ICE_BOUND_FORTITUDE = SHIFT_(F1) # 冰固坚韧
    ALL_SPEC_HORN_OF_WINTER = SHIFT_(TAB) # 凛冬号角 (力量敏捷 Buff)
    ALL_SPEC_ANTI_MAGIC_SHIELD = SHIFT_(F) # 反魔法护盾

    BLOOD_SPEC_VAMPIRIC_BLOOD = SHIFT_(F2) # 吸血鬼之血 (DK版 战士的 破釜沉舟 技能)
    BLOOD_SPEC_HYSTERIA = SHIFT_(C) # 狂血术
    BLOOD_SPEC_MARK_OF_BLOOD = ALT_(F) # 鲜血印记
    BLOOD_SPEC_DANCING_RUNE_WEAPON = CTRL_(F) # 符文武器之舞

    UNHOLY_SPEC_BONE_SHIELD = SHIFT_(F2) # 骨盾
    UNHOLY_SPEC_SUMMON_GARGOYLE = SHIFT_(C) # 召唤石像鬼
    UNHOLY_SPEC_ANTI_MAGIC_ZONE = SHIFT_(G) # 反魔法领域
    UNHOLY_SPEC_CORPSE_EXPLOSION = ALT_(F) # 尸体爆炸

    FROST_SPEC_UNBREAKABLE_ARMOR = SHIFT_(F2) # 铜墙铁壁 (提高护甲和力量)
    FROST_SPEC_DEATH_CHILL = SHIFT_(C) # 死亡之寒 (下一击必爆)
    FROST_SPEC_HUNGERING_COLD = CTRL_(F) # 饥饿之寒 (群体定身)
    FROST_SPEC_HOWLING_BLAST = ALT_(F) # 凛风冲击 (远程瞬发AOE, 没有数量上限)


class Hunter:
    ALL_SPEC_HUNTERS_MARK = 1

    """
    
    //--- Attack Skill
    <Template HunterHuntersMark> // 猎人印记
        <Key Ctrl Oem3>
    <EndTemplate>

    <Template HunterConcussiveShot> // 震荡射击
        <Key Z>
    <EndTemplate>

    <Template HunterFeignDeath> // 假死
        <Key Alt E>
    <EndTemplate>

    <Template HunterMisdirection> // 误导
        <Key Alt 1>
    <EndTemplate>

    <Template HunterSerpentSting> // 毒蛇钉刺 (Dot 伤害)
        <Key 1>
    <EndTemplate>

    <Template HunterScorpidSting> // 毒蝎钉刺 (降低命中)
        <Key 1>
    <EndTemplate>

    <Template HunterViperSting> // 蝮蛇钉刺 (吸蓝)
        <Key Ctrl X>
    <EndTemplate>

    <Template HunterWyvernSting> // 翼龙钉刺 (使目标沉睡)
        <Key 1>
    <EndTemplate>

    <Template HunterConcussiveShot> // 震荡射击
        <Key Z>
    <EndTemplate>

    <Template HunterArcaneShot> // 奥术射击
        <Key 1>
    <EndTemplate>

    <Template HunterMultiShot> // 多重射击
        <Key 1>
    <EndTemplate>

    <Template HunterAimedShot> // 瞄准射击
        <Key 1>
    <EndTemplate>

    <Template HunterChimeraShot> // 奇美拉射击
        <Key 1>
    <EndTemplate>

    <Template HunterSilencingShot> // 沉默射击
        <Key R>
    <EndTemplate>

    <Template HunterSteadyShot> // 稳固射击
        <Key 1>
    <EndTemplate>

    <Template HunterVolley> // 乱射 (AOE)
        <Key X>
    <EndTemplate>

    <Template HunterBlackArrow> // 黑噬箭 (debuff 使你对该目标的伤害获得加成)
        <Key 1>
    <EndTemplate>

    <Template HunterExplosiveArrow> // 爆裂箭 (debuff 使你对该目标的每次攻击都会造成爆炸额外伤害)
        <Key 1>
    <EndTemplate>

    <Template HunterDistractingShot> // 扰乱射击
        <Key Shift Oem3>
    <EndTemplate>

    <Template HunterTranquilizingShot> // 凝神射击
        <Key Shift Tab>
    <EndTemplate>

    //---Trap
    <Template HunterFrostTrap> // 冰霜陷阱
        <Key Ctrl R>
    <EndTemplate>

    <Template HunterFreezingTrap> // 冰冻陷阱
        <Key Ctrl E>
    <EndTemplate>

    <Template HunterFreezingArrow> // 冰冻箭
        <Key Alt R>
    <EndTemplate>

    <Template HunterSnakeTrap> // 毒蛇陷阱
        <Key Shift MButton>
    <EndTemplate>

    <Template HunterExplosiveTrap> // 爆裂陷阱
        <Key Ctrl MButton>
    <EndTemplate>

    <Template HunterDisengage> // 逃脱 (向后跳)
        <Key Shift R>
    <EndTemplate>

    <Template HunterDeterrence> // 胁迫 (招架所有攻击和法术)
        <Key Shift F1>
    <EndTemplate>

    <Template HunterWindClip> // 摔绊 (减速)
        <Key T>
    <EndTemplate>
    """