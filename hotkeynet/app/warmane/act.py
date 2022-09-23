# -*- coding: utf-8 -*-

"""
本模块定义了各个人物, 职业的详细动作条设置. 哪个技能以及哪个宏应该绑定什么快捷键.

本模块还实现了 Key 和 Mouse 行为的抽象化, 用人类可读, 有具体含义的代码, 形如:
``Paladin.PROTECT_SPEC_JUDGEMENT`` 这样的代码来代替意义不明确的 <Key 1>. 使得
Hotkey 代码本身就能反映出想要实现的功能, 避免了写注释. 因为保持注释和代码一致非常麻烦.
这种抽象化能使得你能专注于实现各个 Hotkey 的具体功能. 而当某个功能, 例如防护圣骑士

要使得此脚本按照预期工作, 必须按照本模块中的定义绑定技能和快捷键.

注: 在游戏中按照本模块的设置绑定好所有按键后, 一定要记得备份 WFT 中的配置文件, 以及 Domino
动作条的数据文件.

**开发者注意**

请参考 :meth:`hotkeynet.script.Block.__enter__` 中的文档. 因为上下文机制的存在,
这里所有的属性都 **不能够** 直接定义预先被创建好的 Block 实例. 而是要用工厂函数定义成
一个函数. 这样才能保证被引用的 Block 自动被添加到上下文中去.
"""

import typing as TP

from hotkeynet.keyname import *
from hotkeynet.script import (
    Block, Key, ClickMouse, ModifiedClickMouse
)
from hotkeynet.game.wow.model import Window


class KeyMaker:
    def __init__(self, key: str):
        self.key = key

    def __call__(self):
        return Key(key=self.key)


def convert_to_key_maker(klass: TP.Type):
    """
    该函数有什么用?

    我们在定义的按键的时候, 由于是人在写代码, 所以希望用最少的代码来完成枚举. 所以用到的是
    字符串形式的 Keyname. 但是在编写 Script 的时候, 我们要用的是 <Key ...> 这样的
    :class:`~hotkeynet.script.Key` 对象. 该函数能将 Keyname 自动转化成 Key 对象.
    既方便了编码, 又实现了功能
    """
    for key, value in klass.__dict__.items():
        if not key.startswith("_"):
            if isinstance(value, Block):
                raise TypeError("You cannot use BLOCK here! you will break the Context!")
            elif isinstance(value, str):
                setattr(klass, key, KeyMaker(key=value))
            else:
                pass


class Movement:
    """
    移动类的按键绑定. 所有职业都需要按照这个设置. 以下设置如果没有特殊说明, 都是
    在游戏内的按键绑定实现的.
    """
    MOVE_LEFT = Q  # 往左平移
    MOVE_RIGHT = E  # 往右平移
    MOVE_FORWARD = UP  # 往前
    MOVE_BACKWARD = DOWN  # 往后
    MOVE_LEFT_TOP = f"{MOVE_LEFT} {MOVE_FORWARD}"  # 左上
    MOVE_RIGHT_TOP = f"{MOVE_RIGHT} {MOVE_FORWARD}"  # 右上
    MOVE_LEFT_BOTTOM = f"{MOVE_LEFT} {MOVE_BACKWARD}"  # 左下
    MOVE_RIGHT_BOTTOM = f"{MOVE_RIGHT} {MOVE_BACKWARD}"  # 右下
    TURN_LEFT = LEFT  # 向左转
    TURN_RIGHT = RIGHT  # 向右转
    JUMP = SPACE  # 跳跃
    TOGGLE_AUTO_RUN = OEM3_WAVE_OR_BACK_QUOTE  # 切换自动奔跑
    FOLLOW_TARGET = OEM5_PIPE_OR_BACK_SLASH  # 跟随目标
    FOLLOW_FOCUS = NUMPAD_12_MULTIPLY  # 跟随焦点目标
    PITCH_UP = INSERT  # 在水中/空中上浮
    PITCH_DOWN = DELETE  # 在水中/空中下沉


convert_to_key_maker(Movement)


class PetAction:
    """
    操作宠物的按键绑定. 所有职业都需要按照这个设置. 以下设置如果没有特殊说明, 都是
    在游戏内的按键绑定实现的.
    """
    ATTACK = CTRL_(KEY_1)  # 宠物攻击主人的目标
    FOLLOW = CTRL_(KEY_2)  # 宠物跟随主人
    STAY = CTRL_(KEY_3)  # 宠物停留
    AGGRESSIVE = CTRL_(KEY_1)  # 进攻模式
    DEFENSIVE = CTRL_(KEY_2)  # 防御模式
    PASSIVE = CTRL_(KEY_3)  # 被动模式


convert_to_key_maker(PetAction)


class Target:
    """
    选择目标相关的按键绑定. 所有职业都需要按照这个设置. 以下设置如果没有特殊说明, 都是
    在游戏内的按键绑定实现的.

    1. 如果无需用宏, 例如选择最近的敌人可以用 Tab, 选择自己可以用 F1 这些都是游戏自带按键
        设定. 你在游戏按键设定中按照这个设置好即可.
    2. 如果需要用到宏, 例如选择某个特定的坦克, 那么你需要做宏, 并且将其放置在动作条的特定位置
        上, 然后把动作条的特定位置添加上按键绑定.
    """
    TARGET_NEAREST_ENEMY = TAB
    TARGET_NEAREST_FRIEND = CTRL_(TAB)
    TARGET_SELF = F1
    TARGET_PARTY_MEMBER_1 = F2
    TARGET_PARTY_MEMBER_2 = F3
    TARGET_PARTY_MEMBER_3 = F4
    TARGET_PARTY_MEMBER_4 = F5

    INTERACT_WITH_TARGET = J
    INTERACT_WITH_MOUSE_OVER = UNKNOWN
    ASSIST_TARGET = F

    SET_TARGET_AS_FOCUS = CTRL_ALT_(F)
    TARGET_FOCUS = COMMA
    TARGET_LAST_TARGET = PERIOD

    TARGET_PARTY = NUMPAD_1
    """
    The ``MB-TgtParty`` Macro, randomly select a party member, if in camera::

        /targetparty
    """

    TARGET_RAID = NUMPAD_2
    """
    The ``MB-TgtRaid`` Macro, randomly select a raid member, if in camera::

        /targetraid
    """

    TARGET_FOCUS_TARGET = NUMPAD_3
    """
    The ``MB-TgtFcsTgt`` Macro, when focus is tank, usually it assist the leader::

        /assist focus
    """

    TARGET_FOCUS_TARGET_TARGET = NUMPAD_4
    """
    The ``MB-TgtFcsTgtTgt`` Macro, when focus is tank, usually it select the 
    boss current target player::

        /assist focus
        /assist
    """

    # --- Target specific person
    # w1
    TARGET_W1_BATLEFURY = SHIFT_(INSERT)
    TARGET_W1_LITGOATSSA = SHIFT_(INSERT)
    TARGET_W1_LITGOATDKA = SHIFT_(INSERT)

    # w3
    TARGET_W3_OPIITOU = SHIFT_(HOME)

    # w6
    TARGET_W6_KINDHEARTED = SHIFT_(PAGE_UP)
    TARGET_W6_SWEETMONK = SHIFT_(PAGE_UP)

    # w7
    TARGET_w7_KAPACUK = SHIFT_(DELETE)

    # w9
    TARGET_w9_GLOWYY = SHIFT_(END)

    # w10
    TARGET_W10_LUXIAOFENG = SHIFT_(PAGE_DOWN)
    TARGET_W10_GANJJ = SHIFT_(PAGE_DOWN)
    TARGET_W10_LAOSHOU = SHIFT_(PAGE_DOWN)
    TARGET_W10_FLYDPS = SHIFT_(PAGE_DOWN)
    TARGET_W10_STOPHEALING = SHIFT_(PAGE_DOWN)

    # w11
    TARGET_W11_LITGUGUA = ALT_(INSERT)
    TARGET_W11_LITGUGUE = ALT_(INSERT)

    # w15
    TARGET_W15_LGMSI = ALT_(HOME)

    # w19
    TARGET_W19_LGSMM = ALT_(PAGE_UP)

    #
    TARGET_LEADER_1 = UNKNOWN

    #
    TARGET_LEADER_2 = UNKNOWN


convert_to_key_maker(Target)

target_leader_key_mapper = {
    Window.make(1).label: Target.TARGET_W1_BATLEFURY,
    Window.make(3).label: Target.TARGET_W3_OPIITOU,
    Window.make(6).label: Target.TARGET_W6_KINDHEARTED,
    Window.make(7).label: Target.TARGET_w7_KAPACUK,
    Window.make(9).label: Target.TARGET_w9_GLOWYY,
    Window.make(10).label: Target.TARGET_W10_LUXIAOFENG,
    Window.make(11).label: Target.TARGET_W11_LITGUGUA,
    Window.make(15).label: Target.TARGET_W15_LGMSI,
    Window.make(19).label: Target.TARGET_W19_LGSMM,
}


class Camera:
    """
    视角, 摄像头相关的按键绑定, 所有职业都需要按照这个设置. 以下设置如果没有特殊说明, 都是
    在游戏内的按键绑定实现的.

    保持所有人物角色的视角统一有助于用使用需要选择施法区域的技能.
    """
    # 第一个视角永远是视角拉到最近, 第一人称视角, 也就是按下 Home 键的效果.
    SET_FIRST_CAMERA_VIEW_1 = CTRL_SHIFT_ALT(INSERT)
    # 第二个视角永远是视角拉到最远, 并且开启摄像头永远跟随的模式时系统自动的高度.
    SET_FIRST_CAMERA_VIEW_2 = CTRL_SHIFT_ALT(HOME)
    # 第三个视角备用
    SET_FIRST_CAMERA_VIEW_3 = CTRL_SHIFT_ALT(PAGE_UP)

    SAVE_FIRST_CAMERA_VIEW_1 = CTRL_SHIFT_ALT(DELETE)
    SAVE_FIRST_CAMERA_VIEW_2 = CTRL_SHIFT_ALT(END)
    SAVE_FIRST_CAMERA_VIEW_3 = CTRL_SHIFT_ALT(PAGE_DOWN)


convert_to_key_maker(Camera)


class System:
    """
    客户端系统相关的按键绑定, 所有职业都需要按照这个设置. 以下设置如果没有特殊说明, 都是
    在游戏内的按键绑定实现的.
    """
    MASTER_VOLUME_DOWN = CTRL_(KEY_11_MINUS)  # 音量调大
    MASTER_VOLUME_UP = CTRL_(KEY_12_PLUS)  # 音量调小
    TOGGLE_USER_INTERFACE = CTRL_(F12)  # 开关用户界面


convert_to_key_maker(System)


class General:
    """
    通用类功能的按键绑定. 所有职业都需要按照这个设置.  以下设置如果没有特殊说明, 都是
    在游戏内的按键绑定实现的.
    """
    ESC = ESC  # 按 ECS 键
    TRIGGER = TRIGGER

    STOP_CASTING_KEY_OEM1_SEMICOLUMN = OEM1_SEMICOLUMN  # 取消施法
    STOP_ATTACKING_KEY_OEM7_QUOTE = OEM7_QUOTE  # 取消攻击
    LEAVE_PARTY_MACRO_KEY_ALT_END = ALT_(END)  # 离开队伍宏
    """
    The ``MB-LeaveParty`` Macro::
    
        /script LeavePart()
    """

    CONFIRM_MACRO_KEY_NUMPAD_5 = NUMPAD_5  # 按下接受按钮宏, 可以用于接收组队, 进入随机地下城
    """
    The ``MB-Confirm`` Macro::

        /click StaticPopup1Button1
    """

    SET_FOCUS_KEY_NUMPAD_6 = NUMPAD_6  # 设置当前目标为焦点宏
    """
    The ``MB-FocusSet`` Macro::

        /focus
    """

    CLEAR_FOCUS_NUMPAD_7 = NUMPAD_7  # 取消已设置的焦点
    """
    The ``MB-FocusClear`` Macro::

        /clearfocus
    """

    MOUNT_UP_MACRO_KEY_NUMPAD_11_DIVIDE = NUMPAD_11_DIVIDE
    """
    The ``MountUp`` Macro. 简单来说逻辑是如果已经在 坐骑上, 或是进入了飞行模式, 则 
    stopmacro; 其他情况根据当地是否可以飞行, 使用不同的坐骑和进入德鲁伊飞行形态::

        #showtooltip
        /stopmacro [mounted]
        /stopmacro [stance:6] # 平衡恢复用 6, 野性用 5, 非德鲁伊职业不需要这行
        /cast [flyable] ${YourFlyMountSpellNameOrDruidFlightFormSkill}
        /cast [noflyable] ${YourLandMountSpellName}
    """

    MOUNT_DOWN_MACRO_CTRL_OEM3_WAVE = CTRL_(OEM3_WAVE_OR_BACK_QUOTE)
    """
    The ``MountDown`` Macro. 简单来说就是尝试清除掉坐骑和飞行形态的光环::
    
        #showtooltip
        /cancelaura ${YourLandMountSpellName}
        /cancelaura ${YourFlyMountSpellName}
        /cancelaura Swift Flight Form, 非德鲁伊职业不需要这行
    """

    LAND_MOUNT_SPELL_KEY_CTRL_Z = CTRL_(Z)  # 陆地坐骑, 不是宏
    """
    陆地专用坐骑.
    """

    EAT_FOOD_KEY_CTRL_T = CTRL_(T)  # 吃喝食物

    BUFF_SELF_MACRO_KEY_8 = KEY_8  # 给自己刷 Buff 的宏
    """
    用于给自己刷 Buff 的宏或技能, 这个因职业而异
    
    例如防惩骑士的是::
    
        #showtooltip
        /target player
        /castsequence [spec:1] reset=target Seal of Vengeance, !Retribution Aura, Greater Blessing of Kings
        /castsequence [spec:2] reset=target Righteous Fury, Seal of Vengeance, !Devotion Aura, Greater Blessing of Sanctuary
    """

    BUFF_RAID_MACRO_KEY_9 = KEY_9  # 给团队刷 Buff
    """
    用于给团队刷 Buff 的宏或技能, 这个因职业而异
    """

    RACIAL_SKILL_KEY_ALT_A = ALT_(A)  # 种族天赋 1
    USE_TRINKET_1_KEY_ALT_S = ALT_(S)  # 使用饰品 1
    USE_TRINKET_2_KEY_ALT_D = ALT_(D)  # 使用饰品 2

    DPS_BURST_MACRO_KEY_ALT_D = ALT_(D)  # DPS 爆发宏
    """
    The DPS Burst Skill macro, different class game different macro.

    caster may game something like::

        #showtooltip
        /stopcasting
        /cast ${NonGCDBurstSkillName}
        /game ${TrinketOrEngineeringEnchantingItemName}
    """

    SHOOT_WAND_OR_RANGE_WEAPON_KEY_SHIFT_TAB = SHIFT_(TAB)  # 使用魔杖宏
    """
    Mage / Warlock / Priest shoot wand, Warrior / Rogue shoot range weapon
    """

    TOGGLE_MAIN_GAME_MENU = CTRL_SHIFT_ALT(E)  # 开关游戏选项界面, 可以用于一键登出


convert_to_key_maker(General)


class Warrior:
    """
    战士职业的按键绑定.
    """
    pass


class Paladin:
    """
    圣骑士职业的按键绑定.
    """
    ALL_SPEC_DIVINE_PLEA = lambda: ClickMouse(button=MOUSE_MButton)  # 神圣恩求 (回蓝技能)
    ALL_SPEC_AVENGING_WRATH = SHIFT_(F)  # 复仇之怒 (爆发技能)

    # --- Defensive CD 防御性CD技能 ---
    ALL_SPEC_DIVINE_SHIELD = SHIFT_(F1)  # 圣盾术 (无敌)
    ALL_SPEC_DIVINE_PROTECTION = SHIFT_(F2)  # 圣佑术 (50% 减伤)
    ALL_SPEC_DIVINE_SACRIFICE = SHIFT_(C)  # 神圣牺牲 (团队减伤技能)
    ALL_SPEC_AURA_MASTERY = ALT_(Z)  # 光环掌握

    # --- Hand Of xxx 给他人释放的功能性的祝福 ---
    ALL_SPEC_HAND_OF_PROTECTION = SHIFT_(G)  # 保护祝福
    ALL_SPEC_HAND_OF_SALVATION = CTRL_(R)  # 拯救祝福
    ALL_SPEC_HAND_OF_SACRIFICE = ALT_(R)  # 牺牲祝福
    ALL_SPEC_HAND_OF_FREEDOM = SHIFT_(R)  # 自由祝福

    # --- CC 控制类技能 ---
    ALL_SPEC_HAMMER_OF_JUSTICE = CTRL_(E)  # 制裁之锤
    ALL_SPEC_HOLY_WRATH = SHIFT_(OEM3_WAVE_OR_BACK_QUOTE)  # 神圣愤怒 (对亡灵群体昏迷) Shift + ~
    ALL_SPEC_TURN_EVIL = CTRL_(F)  # 恐惧亡灵

    # --- 治疗类技能 ---
    ALL_SPEC_FLASH_OF_LIGHT = X  # 圣光闪现
    ALL_SPEC_HOLY_LIGHT = ALT_(X)  # 圣光术
    ALL_SPEC_CLEANSE = T  # 清洁术
    ALL_SPEC_SACRED_SHIELD = CTRL_(X)  # 圣洁护盾

    # --- 其他 ----
    ALL_SPEC_EXORCISM = G  # 驱邪术 (读条施法攻击技能, 对亡灵必爆)

    # --- 防护天赋下专属键位 ---
    PROTECT_SPEC_KEY_1_JUDGEMENT = KEY_1  # 智慧 | 光明 | 公正 审判
    PROTECT_SPEC_KEY_ALT_1_HAND_OF_RECKONING = Z  # 嘲讽 (单体嘲讽)
    PROTECT_SPEC_KEY_2_HAMMER_OF_THE_RIGHTEOUS = KEY_2  # 公正之锤 (防护 51 点天赋技能, 近战群拉高仇恨)
    PROTECT_SPEC_KEY_ALT_2_SHIELD_OF_RIGHTEOUSNESS = ALT_(KEY_2)  # 复仇之盾, 近战单体仇恨技能
    PROTECT_SPEC_KEY_3_HOLY_SHIELD = KEY_3  # 神圣之盾 (防护 31 点天赋技能, 短CD加大量格挡)
    PROTECT_SPEC_KEY_ALT_3_AVENGER_SHIELD = ALT_(KEY_3)  # 防御者之盾 (防护 41点天赋技能, 远程群体攻击, 打断施法并减速)
    PROTECT_SPEC_KEY_4_CONSECRATION = KEY_4  # 奉献 (AOE)
    PROTECT_SPEC_KEY_2_SACRED_SHIELD = KEY_5  # 圣洁护盾
    PROTECT_SPEC_KEY_Z_HAND_OF_RECKONING = Z  # 嘲讽 (单体嘲讽)
    PROTECT_SPEC_KEY_ALT_F_RIGHTEOUS_DEFENCE = ALT_(F)  # 正义防护 (群体嘲讽)

    # --- 惩戒天赋下专属键位 ---
    RETRIBUTION_SPEC_KEY_1_JUDGEMENT = KEY_1  # 智慧 | 光明 | 公正 审判
    RETRIBUTION_SPEC_KEY_ALT_1_HAND_OF_RECKONING = Z  # 嘲讽 (单体嘲讽)
    RETRIBUTION_SPEC_KEY_2_CRUSADER_STRIKE = KEY_2  # 十字军打击 (惩戒 41 点天赋技能)
    RETRIBUTION_SPEC_KEY_3_DIVINE_STORM = KEY_3  # 神圣风暴 (惩戒 51 点天赋技能)
    RETRIBUTION_SPEC_KEY_4_CONSECRATION = KEY_4  # 奉献 （AOE)
    RETRIBUTION_SPEC_KEY_5_SACRED_SHIELD = KEY_5  # 圣洁护盾
    RETRIBUTION_SPEC_KEY_ALT_E_REPENTANCE = ALT_(E)  # 忏悔 (惩戒 31 点天赋技能)
    RETRIBUTION_SPEC_KEY_Z_HAND_OF_RECKONING = Z  # 嘲讽 (单体嘲讽)
    RETRIBUTION_SPEC_KEY_ALT_F_RIGHTEOUS_DEFENCE = ALT_(F)  # 正义防护 (群体嘲讽)

    # --- 神圣天赋下专属键位 ---
    HOLY_SPEC_KEY_1_ONE_MINUTE_HEAL_ROTATION_MACRO = KEY_1
    """
    以1分钟为一个循环 (根据你的急速) 的治疗宏
    以 /castsequence reset=30 为起始, 以 4 圣闪 1 圣光 或者 3闪 1 光, 或是 2 闪 2 光
    为一个 5 - 6 秒的循环, 在第30秒的时候释放 神圣恳求 回蓝, 然后根据你的急速填充满 60 秒循环
    例如:

    /castsequence reset=30 Flash of Light,Flash of Light,Flash of Light,Holy Light,Flash of Light,Flash of Light,Flash of Light,Holy Light,Flash of Light,Flash of Light,Flash of Light,Holy Light,Flash of Light,Flash of Light,Flash of Light,Holy Light,Divine Plea,Flash of Light,Flash of Light,Flash of Light,Holy Light,Flash of Light,Flash of Light,Flash of Light,Holy Light,Flash of Light,Flash of Light,Flash of Light,Holy Light,Flash of Light,Flash of Light,Flash of Light,Holy Light,Flash of Light,Flash of Light,Flash of Light,Holy Light,
    """
    HOLY_SPEC_KEY_2_ONE_MINUTE_HEAL_ROTATION_MACRO = KEY_2

    HOLY_SPEC_KEY_3_PERIODICAL_BEACON_OF_LIGHT_ON_FOCUS_MACRO = KEY_3
    """
    每 1.5 分钟一次的给焦点刷新圣光道标宏. 里面的,的数量决定了刷新道标的概率.
    例如有 9 个逗号, 意味着按 10 下该技能会生效一次. 在坦克模式平均你每 30 秒会按 10 下
    键盘 3. 那么也就是 30 秒会刷新一次道标.

    #showtooltip
    /target focus
    /castsequence Beacon of Light,,,,,,,,,,,,,,,,,,
    """

    HOLY_SPEC_KEY_4_PERIODICAL_JUDGEMENT_OF_LIGHT_ON_FOCUS_TARGET_MACRO = KEY_4
    """
    每 15 秒一次的对焦点的目标打审判宏. 偶尔给自己补圣洁护盾

    #showtooltip
    /assist focus
    /startattack
    /castsequence Judgement of Light,Judgement of Light,Sacred Shield
    """
    HOLY_SPEC_KEY_5_HOLY_LIGHT = KEY_5  # 圣光术, 只有在神圣天赋下该键位有效
    HOLY_SPEC_KEY_6_FLASH_OF_LIGHT = KEY_6  # 圣光闪现, 只有在神圣天赋下该键位有效
    HOLY_SPEC_KEY_7_HOLY_LIGHT = KEY_7  # 圣光术, 只有在神圣天赋下该键位有效
    HOLY_SPEC_KEY_Z_HOLY_SHOCK = Z  # 神圣震击 (神圣 31 点天赋技能)
    HOLY_SPEC_KEY_R_FOCUS_JUDGEMENT = R
    """
    如果焦点是敌人, 则对焦点, 如果焦点是友方, 则对焦点目标打审判.
    通常用于设置坦克或者Boss为焦点的情况下使用, 避免选择目标的麻烦.

    #showtooltip
    /cast [target=focustarget,harm][target=focus,harm][] Judgement of Light;
    """
    HOLY_SPEC_KEY_0_BEACON_OF_LIGHT = KEY_0  # 圣光道标 (神圣 51 点天赋)

    # --- Healbot 团队框架快捷键 ---
    """
    由于奶骑按照职业顺序 (板甲 -> 布甲, 单一职业 -> 混合职业) 是第一个治疗职业, 而 Healbot
    的快捷键我们是按照一定的逻辑来的. 这里我们就来解说一下这个逻辑.
    
    - 左键 / 右键 是最高频的治疗技能
    - Shift / Alt + 左键 / 右键 是次高频的治疗技能
    - Ctrl + 左键 / 右键 是驱散类技能, 其中 Ctrl + 左键为更主要的驱散技能
    - 中键 是临时性的技能, 例如骑士给保护祝福, 德鲁伊给激活等 
    """
    # Left | Shift / Ctrl / Alt + Left
    HEAL_BOT_LEFT_CLICK_HOLY_LIGHT = lambda: ClickMouse(button=MOUSE_LButton)  # 圣光术
    HEAL_BOT_SHIFT_LEFT_BEACON_OF_LIGHT = lambda: ModifiedClickMouse.shift_left_click()  # 圣光道标
    HEAL_BOT_ALT_LEFT_SACRED_SHIELD = lambda: ModifiedClickMouse.alt_left_click()  # 圣洁护盾
    HEAL_BOT_CLEANSE = lambda: ModifiedClickMouse.ctrl_left_click()  # 清洁术

    # Left | Shift / Ctrl / Alt + Left
    HEAL_BOT_RIGHT_CLICK_FLASH_OF_LIGHT = lambda: ClickMouse(button=MOUSE_RButton)  # 圣光闪现
    HEAL_BOT_HOLY_SHOCK = lambda: ModifiedClickMouse.shift_right_click()  # 神圣震击
    HEAL_BOT_HAND_OF_FREEDOM = lambda: ModifiedClickMouse.alt_right_click()  # 自由祝福

    HEAL_BOT_MIDDLE_CLICK_BEACON_OF_LIGHT = lambda: ClickMouse(button=MOUSE_MButton)  # 圣光道标

    # Shift | Alt | Ctrl + Left Click

    # Shift | Alt | Ctrl + Right Click
    # HEAL_BOT_UNKNOWN = ModifiedMouseClick.ctrl_left_click()  #

    # Shift | Alt | Ctrl + Middle Click
    HEAL_BOT_HAND_OF_SACRIFICE = lambda: ModifiedClickMouse.shift_middle_click()  # 牺牲祝福
    HEAL_BOT_HAND_OF_SALVATION = lambda: ModifiedClickMouse.alt_middle_click()  # 拯救祝福
    HEAL_BOT_HAND_OF_PROTECTION = lambda: ModifiedClickMouse.ctrl_middle_click()  # 保护祝福


convert_to_key_maker(Paladin)


class DK:
    """
    死亡骑士职业的按键绑定.
    """
    ALL_SPEC_BLOOD_STRIKE = KEY_1  # 鲜血打击
    ALL_SPEC_HEART_STRIKE = KEY_1  # 心脏打击 (血天赋)

    ALL_SPEC_PESTILENCE_ALT_1 = ALT_(KEY_1)  # 传染
    ALL_SPEC_PESTILENCE_SHIFT_OEM3 = SHIFT_(OEM3_WAVE_OR_BACK_QUOTE)  # 传染

    ALL_SPEC_ICE_TOUCH = KEY_2  # 冰冷触摸

    ALL_SPEC_CHAIN_OF_ICE_ALT_2 = ALT_(KEY_2)  # 寒冰锁链 (减速)
    ALL_SPEC_CHAIN_OF_ICE_CTRL_E = CTRL_(E)  # 寒冰锁链 (减速)

    ALL_SPEC_UNHOLY_STRIKE = KEY_3  # 邪恶打击
    ALL_SPEC_DEATH_COIL = ALT_(KEY_3)  # 死亡缠绕
    ALL_SPEC_FROST_STRIKE = ALT_(KEY_3)  # 冰霜打击 (冰天赋技能, 可以取代 死亡缠绕)

    ALL_SPEC_DEATH_STRIKE = KEY_4  # 死亡打击 (回血技能)
    """
    #showtooltip
    #spec1=unholy dps,spec2=frost dps
    /cast [mod:alt,spec:1] Scourge Strike; [mod:alt,spec:2] Obliterate; Death Strike
    """
    ALL_SPEC_OBLITERATE = ALT_(KEY_4)  # 湮没
    ALL_SPEC_SCOURGE_STRIKE = ALT_(KEY_4)  # 天灾打击 (邪天赋技能, 可以取代 湮没)

    ALL_SPEC_BLOOD_BOIL = KEY_5  # 血液沸腾
    ALL_SPEC_BLOOD_PRESENCE = SHIFT_(Q)  # 鲜血领域
    ALL_SPEC_FROST_PRESENCE = SHIFT_(W)  # 冰霜领域
    ALL_SPEC_UNHOLY_PRESENCE = SHIFT_(E)  # 邪恶领域

    ALL_SPEC_DARK_COMMAND_KEY_Z = Z  # 黑暗命令 (嘲讽)
    ALL_SPEC_RUNE_TAP_KEY_T = T  # 符文分流 (血天赋, 回血技能)
    ALL_SPEC_DEATH_GRIP_KEY_G = G  # 死亡之握 (远程嘲讽 加 拉人)
    ALL_SPEC_DEATH_AND_DECAY_KEY_ALT_X = ALT_(X)  # 死亡凋零
    ALL_SPEC_MIND_FREEZE_KEY_R = R  # 心灵冻结 (打断施法)
    ALL_SPEC_RUNE_STRIKE_KEY_ALT_E = ALT_(E)  # 符文打击 (类似于战士的打击, 高仇恨技能)
    ALL_SPEC_ICE_BOUND_FORTITUDE_KEY_SHIFT_F1 = SHIFT_(F1)  # 冰固坚韧
    ALL_SPEC_HORN_OF_WINTER_KEY_SHIFT_TAB = SHIFT_(TAB)  # 凛冬号角 (力量敏捷 Buff)
    ALL_SPEC_ANTI_MAGIC_SHIELD_KEY_SHIFT_F = SHIFT_(F)  # 反魔法护盾
    ALL_SPEC_EMPOWERED_RUNED_WEAPON_KEY_CTRL_R = CTRL_(R)  # 强化符文武器

    BLOOD_SPEC_VAMPIRIC_BLOOD = SHIFT_(F2)  # 吸血鬼之血 (DK版 战士的 破釜沉舟 技能)
    BLOOD_SPEC_HYSTERIA = SHIFT_(C)  # 狂血术
    BLOOD_SPEC_MARK_OF_BLOOD = ALT_(F)  # 鲜血印记
    BLOOD_SPEC_DANCING_RUNE_WEAPON = CTRL_(F)  # 符文武器之舞

    UNHOLY_SPEC_BONE_SHIELD = SHIFT_(F2)  # 骨盾
    UNHOLY_SPEC_SUMMON_GARGOYLE = SHIFT_(C)  # 召唤石像鬼
    UNHOLY_SPEC_ANTI_MAGIC_ZONE = SHIFT_(G)  # 反魔法领域
    UNHOLY_SPEC_CORPSE_EXPLOSION_ALF_F = ALT_(F)  # 尸体爆炸
    UNHOLY_SPEC_DPS_ROTATE_MACRO = KEY_2
    """
    #showtooltip
    /castsequence reset=9 Icy Touch,Plague Strike,Pestilence,Scourge Strike,Blood Strike,Death Coil,Scourge Strike,Blood Strike,Scourge Strike,Blood Strike,Death Coil
    """
    UNHOLY_SPEC_BUFF_SELF_MACRO = KEY_8
    """
    #showtooltip
    /castsequence !Unholy Presence,Raise Dead
    """

    FROST_SPEC_UNBREAKABLE_ARMOR = SHIFT_(F2)  # 铜墙铁壁 (提高护甲和力量)
    FROST_SPEC_DEATH_CHILL = SHIFT_(C)  # 死亡之寒 (下一击必爆)
    FROST_SPEC_HUNGERING_COLD = CTRL_(F)  # 饥饿之寒 (群体定身)
    FROST_SPEC_HOWLING_BLAST = ALT_(F)  # 凛风冲击 (远程瞬发AOE, 没有数量上限)


convert_to_key_maker(DK)


class Hunter:
    """
    猎人职业的按键绑定.
    """
    ALL_SPEC_HUNTERS_MARK = CTRL_(G)  # 猎人印记

    ALL_SPEC_SERPENT_STING = KEY_1  # 毒蛇钉刺 (Dot 伤害)
    ALL_SPEC_MISDIRECTION = ALT_(KEY_1)  # 误导
    ALL_SPEC_MISDIRECTION_FOCUS_MACRO = ALT_(Z)  # 误导焦点宏
    """
    ::
    
        #showtooltip
        /cast [target=focus,noharm] Misdirection; [target=focustarget,noharm] Misdirection
        #/target [target=focus,noharm] focus; [] focustarget
    """
    ALL_SPEC_STEADY_SHOT = KEY_2  # 稳固射击
    ALL_SPEC_AIMED_SHOT = KEY_4  # 瞄准射击
    ALL_SPEC_MULTI_SHOT = ALT_(KEY_4)  # 多重射击
    ALL_SPEC_KILL_SHOT = KEY_5  # 杀戮射击
    ALL_SPEC_ARCANE_SHOT = KEY_6  # 奥术射击

    ALL_SPEC_CONCUSSIVE_SHOT = Z  # 震荡射击
    ALL_SPEC_WIND_CLIP = T  # 摔绊 (减速)
    ALL_SPEC_KILL_COMMAND_X = X  # 杀戮命令 (宠物加攻速)

    ALL_SPEC_SCORPID_STING = KEY_1  # 毒蝎钉刺 (降低命中)

    ALL_SPEC_FREEZING_TRAP = CTRL_(E)  # 冰冻陷阱
    ALL_SPEC_FROST_TRAP = CTRL_(R)  # 冰霜陷阱
    ALL_SPEC_FREEZING_ARROW = ALT_(R)  # 冰冻箭
    ALL_SPEC_SNAKE_TRAP = SHIFT_(MOUSE_MButton)  # 毒蛇陷阱
    ALL_SPEC_EXPLOSIVE_TRAP = CTRL_(MOUSE_MButton)  # 爆裂陷阱

    ALL_SPEC_VOLLEY_ALT_X = ALT_(X)  # 乱射 (AOE)

    ALL_SPEC_DETERRENCE = SHIFT_(F1)  # 胁迫 (招架所有攻击和法术)
    ALL_SPEC_FEIGN_DEATH = ALT_(E)  # 假死
    ALL_SPEC_DISENGAGE = SHIFT_(R)  # 逃脱 (向后跳)

    ALL_SPEC_DISTRACTING_SHOT = SHIFT_(OEM3_WAVE_OR_BACK_QUOTE)  # 扰乱射击
    ALL_SPEC_TRANQUILIZING_SHOT = SHIFT_(TAB)  # 凝神射击
    ALL_SPEC_VIPER_STING = CTRL_(X)  # 蝮蛇钉刺 (吸蓝)

    ALL_SPEC_ASPECT_OF_PACT_OR_DRAGON_HAWK = SHIFT_(F)  # 豹群 和 龙鹰 守护相互切换
    ALL_SPEC_ASPECT_OF_VIPER_OR_DRAGON_HAWK = SHIFT_(G)  # 蝮蛇 和 龙鹰 守护相互切换
    ALL_SPEC_TRUE_SHOT_AURA = KEY_9  # 强击光环

    # 射击天赋
    MARKSMAN_SPEC_DPS_ROTATE_MACRO = KEY_2  # 射击猎人 用于 dps 循环的宏
    """
    """
    MARKSMAN_SPEC_CHIMERA_SHOT = KEY_3  # 奇美拉射击
    MARKSMAN_SPEC_SILENCING_SHOT = R  # 沉默射击
    MARKSMAN_SPEC_HUNTERS_MARK = KEY_6  # 猎人印记

    # 生存天赋
    SURVIVAL_SPEC_DPS_ROTATE_MACRO = KEY_2  # 生存猎人 用于 dps 循环的宏
    """
    """
    SURVIVAL_SPEC_WYVERN_STING = KEY_1  # 翼龙钉刺 (使目标沉睡)
    SURVIVAL_SPEC_BLACK_ARROW = KEY_1  # 黑噬箭 (debuff 使你对该目标的伤害获得加成)
    SURVIVAL_SPEC_EXPLOSIVE_ARROW = KEY_1  # // 爆裂箭 (debuff 使你对该目标的每次攻击都会造成爆炸额外伤害)
    SURVIVAL_SPEC_HUNTERS_MARK = KEY_6  # 猎人印记

    # 兽王天赋
    BEAST_SPEC_DPS_ROTATE_MACRO = KEY_1  # 生存猎人 用于 dps 循环的宏
    """
    """
    BEAST_SPEC_INTIMIDATION = KEY_1  # 胁迫 (兽王天赋 宝宝昏迷目标, 并造成大量威胁值)
    BEAST_SPEC_BESTIAL_WRATH = KEY_1  # 狂野怒火 (兽王天赋 宝宝和自身免疫控制, 提高造成的伤害)
    BEAST_SPEC_HUNTER_MARK = KEY_6  # 猎人印记

    HEAL_BOT_MISDIECTION = MOUSE_RButton  # 对团队框架的目标施放误导


convert_to_key_maker(Hunter)


class Shaman:
    """
    萨满职业的按键绑定.
    """
    ALL_SPEC_CALL_OF_THE_ELEMENTS = SHIFT_(OEM3_WAVE_OR_BACK_QUOTE)  # 远古呼唤, 同时召唤 4 个图腾
    ALL_SPEC_TOTEMIC_RECALL = SHIFT_(TAB)  # 召回图腾

    # earth totem
    ALL_SPEC_TREMOR_TOTEM = ALT_(F1)  # 战栗图腾 (解除恐惧)
    ALL_SPEC_EARTHBIND_TOTEM = SHIFT_(F)  # 地缚图腾 (类似冰霜陷阱, 减速)
    ALL_SPEC_EARTH_ELEMENTAL_TOTEM = ALT_(MOUSE_MButton)  # 大地元素图腾
    ALL_SPEC_STONECLAW_TOTEM = SHIFT_(F1)  # 石爪图腾 (嘲讽怪物)

    # fire totem
    ALL_SPEC_FIRE_ELEMENTAL_TOTEM = SHIFT_(MOUSE_MButton)  # 火元素图腾

    # water totem
    ALL_SPEC_CLEANSING_TOTEM = ALT_(F2)  # 净化图腾 (驱除疾病和毒)
    ALL_SPEC_HEALING_STREAM_TOTEM = KEY_1  # 生命之泉
    ALL_SPEC_MANA_SPRING_TOTEM = KEY_1  # 法力之泉

    # air totem
    ALL_SPEC_GROUNDINIG_TOTEM = SHIFT_(G)  # 根基图腾 (吸收指向性法术)

    # elemental shield
    ALL_SPEC_KEY_G_WATER_SHELD = G  # 水之盾
    ALL_SPEC_KEY_G_LIGHTNING_SHIELD = G  # 闪电盾
    ALL_SPEC_KEY_0_WATER_OR_LIGHTNING_SHIELD = KEY_0  # 水盾或电盾

    ALL_SPEC_FROST_SHOCK = Z  # 冰霜震击
    ALL_SPEC_BLOOD_THIRST_HEROISM = CTRL_(F)  # 嗜血, 英勇
    ALL_SPEC_FIRE_NOVA = CTRL_(X)  # 火焰新星

    # utility spell
    ALL_SPEC_HEX = CTRL_(E)  # 妖术
    ALL_SPEC_PURGE = CTRL_(R)  # 进攻魔法驱散
    ALL_SPEC_CURE_TOXINS = ALT_(R)  # 驱毒术
    ALL_SPEC_GHOST_WOLF = SHIFT_(R)  # 幽灵狼形态
    ALL_SPEC_WIND_SHEAR_MACRO = R  # 打断施法
    """
    This should be a macro
    
    #showtooltip
    /stopcasting
    /cast [target=focus,harm] Wind Shear; [target=focustarget,harm] Wind Shear; [] Wind Shear
    """
    ALL_SPEC_DISPEL = T  # 驱散

    """
    风剪术 宏, 没有焦点时对目标打断, 有焦点时焦点打  断 (如果焦点是敌人则打断敌人, 如果是友方则打断焦点的目标)::

        #showtooltip
        /stopcasting
        /cast [target=focus,harm] Wind Shear; [target=focustarget,harm] Wind Shear; [] Wind Shear
    """

    ALL_SPEC_CHAIN_HEAL = CTRL_(G)  # 治疗链
    ALL_SPEC_LESS_HEALING_WAVE = ALT_(X)  # 治疗链
    ALL_SPEC_HEAL_WAVE = X  # 治疗链

    RESTO_SPEC_EARTH_SHIELD = ALT_(G)  # 大地之盾
    RESTO_SPEC_LESS_HEALING_WAVE_KEY_6 = KEY_6  # 次级治疗波
    RESTO_SPEC_LESS_HEALING_WAVE_KEY_X = X  # 次级治疗波
    RESTO_SPEC_HEALING_WAVE_KEY_7 = KEY_7  # 治疗波
    RESTO_SPEC_HEALING_WAVE_KEY_ALT_X = ALT_(X)  # 治疗波
    RESTO_SPEC_RIPTIDE = ALT_(F)  # 激流
    RESTO_SPEC_CLEANSING_SPIRIT = T  # 灵魂净化 (驱散)

    RESTO_SPEC_TIDAL_FORCE = SHIFT_(C)  # 潮汐之力 (恢复系天赋 提高下三次治疗法术的暴击)
    RESTO_SPEC_MANA_TIDE_TOTEM = ALT_(E)  # 法力之潮图腾 (恢复系天赋 团队恢复大量法力)
    RESTO_SPEC_NATURE_SWIFTNESS = MOUSE_MButton  # 自然迅捷 (恢复系天赋 下一个技能瞬发)

    ELEMENTAL_SPEC_DPS_ROTATE_MACRO = KEY_2  # 元素萨满 输出循环
    """
    """
    ELEMENTAL_SPEC_ELEMENTAL_MASTERY = SHIFT_(C)  # 元素精通
    ELEMENTAL_SPEC_THUNDER_STORM = ALT_(F)  # 雷霆风暴
    ELEMENTAL_SPEC_CURE_TOXIC = T  # 净化疾病中毒

    ENHANCEMENT_SPEC_DPS_ROTATE_MACRO = KEY_2  # 增强萨满 输出循环
    ENHANCEMENT_SPEC_FERAL_SPIRIT = SHIFT_(C)  # 野性之魂
    ENHANCEMENT_SPEC_SHAMANISTIC_RAGE = ALT_(F)  # 萨满之怒
    ENHANCEMENT_SPEC_CURE_TOXIC = T  # 净化疾病中毒

    # Left | Right | Middle
    HEAL_BOT_HEALING_WAVE_LEFT_CLICK = lambda: ClickMouse(button=MOUSE_LButton)  # 治疗波
    HEAL_BOT_RIPTIDE_RIGHT_CLICK = lambda: ClickMouse(button=MOUSE_RButton)  # 激流
    HEAL_BOT_CHAIN_HEAL_MIDDLE_CLICK = lambda: ClickMouse(button=MOUSE_MButton)  # 治疗链

    # Shift, Alt, Ctrl Left Click
    HEAL_BOT_CHAIN_HEAL_SHIFT_LEFT_CLIICK = lambda: ModifiedClickMouse.shift_left_click()  # 治疗链
    HEAL_BOT_LESS_HEALING_WAVE_ALT_LEFT_CLICK = lambda: ModifiedClickMouse.alt_left_click()  # 次级治疗波
    HEAL_BOT_CLEANSE_CTRL_LEFT_CLICK = lambda: ModifiedClickMouse.ctrl_left_click()  # 先祖驱散

    # Shift, Alt, Ctrl Right Click
    HEAL_BOT_EARTH_SHIELD_ALT_RIGHT_CLICK = lambda: ModifiedClickMouse.alt_right_click()  # 大地之盾
    HEAL_BOT_CURE_TOXINS_CTRL_RIGHT_CLICK = lambda: ModifiedClickMouse.ctrl_right_click()  # 驱毒术


convert_to_key_maker(Shaman)


class Rogue:
    """
    盗贼职业的按键绑定.
    """
    pass


class Druid:
    """
    德鲁伊职业的按键绑定.
    """
    ALL_SPEC_ENTANGLING_ROOTS = CTRL_(E)  # 纠缠根须
    ALL_SPEC_REJUVENATION = Z  # 回春
    ALL_SPEC_REVIVE = KEY_1  # 复活
    ALL_SPEC_REBIRTH = CTRL_(X)  # 战斗复活
    ALL_SPEC_INNERVATE = CTRL_(F)  # 激活
    ALL_SPEC_TRANQUILITY = CTRL_(G)  # 宁静
    ALL_SPEC_FAERI_FIRE = R  # 精灵之火
    ALL_SPEC_CYCLONE = ALT_(E)  # 龙卷风 (强力 CC 技能, 期间目标无法被攻击)
    ALL_SPEC_HURRICANE = ALT_(X)  # 飓风 (主力 AOE 技能)
    ALL_SPEC_BARK_SKIN = SHIFT_(F1)  # 树皮术
    ALL_SPEC_ABOLISH_POISON = ALT_(R)  # 清毒术
    ALL_SPEC_REMOVE_CURSE = T  # 驱除诅咒
    ALL_SPEC_SOOTHE_ANIMAL = ALT_(Z)  # 安抚野兽龙类
    ALL_SPEC_HIBERNATE = ALT_(T)  # 睡眠野兽龙类

    ALL_SPEC_CAT_STEALTH_MACRO = ALT_(F1)  # 强制进入潜行状态

    SHAPE_SHIFT_BEAR_FORM = SHIFT_(Q)  # 熊形态
    SHAPE_SHIFT_CAT_FORM = SHIFT_(W)  # 猫形态
    SHAPE_SHIFT_TRAVEL_FORM = SHIFT_(Q)  # 旅行形态
    SHAPE_SHIFT_SWIM_FORM = ALT_(F2)  # 游泳形态
    SHAPE_SHIFT_MOONKIN_FORM = SHIFT_(E)  # 枭兽形态
    SHAPE_SHIFT_TREE_OF_LIFE_FORM = SHIFT_(E)  # 生命之树形态
    SHAPE_SHIFT_FLIGHT_FORM = NUMPAD_11_DIVIDE  # 飞行形态

    BALANCE_SPEC_MOON_FIRE_KEY_1 = KEY_1  # 月火术 (Dot)
    BALANCE_SPEC_WRATH_KEY_2 = KEY_2  # 愤怒 (施法较快的直接攻击法术)
    BALANCE_SPEC_STAR_FIRE_KEY_3 = KEY_3  # 星火术 (施法较快的直接攻击法术)
    BALANCE_SPEC_INSECT_SWARM_KEY_4 = KEY_4  # 虫群 (Dot, 天赋技能)
    BALANCE_SPEC_HURRICANE_KEY_5 = KEY_5  # 飓风 (主力 AOE 技能)
    BALANCE_SPEC_FAERI_FIRE_KEY_6 = KEY_6  # 精灵之火
    BALANCE_SPEC_STAR_FALL_ALT_F = ALT_(F)  # 星落 (强力 AOE 技能, 天赋技能)
    BALANCE_SPEC_TYPHOON_KEY_G = G  # 台风 (击退面前的敌人)
    BALANCE_SPEC_FORCE_OF_NATURE = lambda: ClickMouse(button=MOUSE_LButton)  # 自然之力 (召唤树人)

    BALANCE_SPEC_DPS_ROTATE_MACRO = KEY_2
    """
    一键 DPS 循环宏::
    
        #showtooltip
        /castsequence reset=30 [nonchannel] 愤怒, 星火术
    """

    RESTO_SPEC_HOT_HEAL_MACRO = KEY_1
    """
    给目标上 Hot 宏::
        
        #showtooltip
        /castsequence reset=target 回春, 愈合, 生命之花, 生命之花, 生命之花,,,,,,
    """

    RESTO_SPEC_HEAL_RAID_MACRO_KEY_2 = KEY_2
    """
    团队随机治疗宏::
        
        #showtooltip
        /castsequence reset=30 野性生长, 回春, 回春, 回春, 回春, 回春
    """

    RESTO_SPEC_NOURISH_KEY_3 = KEY_3  # 滋养
    RESTO_SPEC_REGROWTH_KEY3 = ALT_(KEY_3)  # 愈合
    RESTO_SPEC_SWIFT_MEND_KEY_4 = KEY_4  # 迅捷治愈
    RESTO_SPEC_WILD_GROWTH_KEY_5 = KEY_5  # 野性生长 (恢复系 51 天赋)
    RESTO_SPEC_REJUVENATION_KEY_6 = KEY_6  # 回春术
    RESTO_SPEC_NOURISH_KEY_7 = KEY_7  # 滋养

    RESTO_SPEC_LIFE_BLOOM = KEY_1  # 自然之花
    RESTO_SPEC_NATURE_SWIFTNESS = lambda: ClickMouse(button=MOUSE_MButton)  # 自然迅捷
    RESTO_SPEC_HEALING_TOUCH = KEY_1  # 治疗之触

    FERAL_SPEC_SURVIVAL_INSTINCT = SHIFT_(F2)  # 生存本能 (类似于战士的破釜沉舟)

    # Left | Right | Middle
    HEAL_BOT_LEFT_CLICK_REJUVENATION = lambda: ClickMouse(button=MOUSE_LButton)  # 回春术
    HEAL_BOT_RIGHT_CLICK_NOURISH = lambda: ClickMouse(button=MOUSE_RButton)  # 滋养
    HEAL_BOT_MIDDLE_CLICK_INNERVATE = lambda: ClickMouse(button=MOUSE_MButton)  # 激活

    # Shift | Alt | Ctrl + Left
    HEAL_BOT_WILD_GROWTH = lambda: ModifiedClickMouse.shift_left_click()
    HEAL_BOT_REGROWTH = lambda: ModifiedClickMouse.alt_left_click()
    HEAL_BOT_REMOVE_CURSE = lambda: ModifiedClickMouse.ctrl_left_click()

    # Shift | Alt | Ctrl + Right
    HEAL_BOT_HEALING_TOUCH = lambda: ModifiedClickMouse.shift_right_click()
    HEAL_BOT_SWIFT_MEND = lambda: ModifiedClickMouse.alt_right_click()
    HEAL_BOT_ABOLISH_POISON = lambda: ModifiedClickMouse.ctrl_right_click()


convert_to_key_maker(Druid)


class Mage:
    """
    法师职业的按键绑定.
    """
    ALL_SPEC_ICE_BLOCK = SHIFT_(F1)  # 寒冰屏障 (冰箱)
    ALL_SPEC_MIRROR_IMAGE = SHIFT_(F2)  # 镜像术 (暂时丢失仇恨)
    ALL_SPEC_BLINK = SHIFT_(R)  # 闪现
    ALL_SPEC_FIRE_WARD = SHIFT_(F)  # 火焰护盾
    ALL_SPEC_FROST_WARD = SHIFT_(G)  # 并刷昂护盾
    ALL_SPEC_POLYMORPH = CTRL_(E)  # 变羊术
    ALL_SPEC_SPELL_STEAL = CTRL_(R)  # 法术偷取
    ALL_SPEC_EVOCATION = CTRL_(F)  # 唤醒术
    ALL_SPEC_INVISIBILITY = ALT_(E)  # 隐身术

    ALL_SPEC_FIRE_BLAST = KEY_3  # 火焰冲击
    ALL_SPEC_SCROTCH = ALT_(KEY_3)  # 灼烧
    ALL_SPEC_DAMPEN_MAGIC = KEY_3  # 魔法抑制, 跟宏绑定, 当目标是友方时使用该技能
    ALL_SPEC_AMPLIFY_MAGIC = ALT_(KEY_3)  # 魔法增效, 跟宏绑定, 当目标是友方时使用该技能
    ALL_SPEC_FROST_NOVA = KEY_4  # 冰霜新星
    ALL_SPEC_CONE_OF_COLD = KEY_5  # 冰锥术
    ALL_SPEC_MANA_SHIELD = ALT_(KEY_5)  # 法力护盾
    ALL_SPEC_ARCANE_EXPLOSION = Z  # 奥爆术
    ALL_SPEC_COUNTER_SPELL_MACRO = R  # 法术反制
    """
    This should be a macro
    
    #showtooltip
    /stopcasting
    /cast [target=focus,harm] Counter Spell; [target=focustarget,harm] Counter Spell; [] Counter Spell
    """
    ALL_SPEC_REMOVE_CURSE = T  # 解除诅咒
    ALL_SPEC_FLAME_STRIKE = X  # 烈焰风暴
    ALL_SPEC_BLIZZARD = ALT_(X)  # 暴风雪
    ALL_SPEC_ICE_LANCE = SHIFT_(OEM3_WAVE_OR_BACK_QUOTE)  # 冰枪术
    ALL_SPEC_FROST_FIRE_BOLT = CTRL_(X)  # 霜火箭
    ALL_SPEC_FOCUS_MAGIC = ALT_(Z)  # 专注魔法
    ALL_SPEC_SLOW_FALL = ALT_(F1)  # 缓落术

    FIRE_SPEC_DPS_ROTATE_MACRO = KEY_2  # 火法 用于 dps 循环的宏
    FIRE_SPEC_PYROBLAST = KEY_1  # 炎爆术
    FIRE_SPEC_FIRE_BALL = KEY_2  # 火球术
    FIRE_SPEC_LIVING_BOMB = G  # 活体炸弹

    FIRE_SPEC_COMBUSTION = SHIFT_(C)  # 燃烧
    FIRE_SPEC_BLAST_WAVE = ALT_(G)  # 冲击波
    FIRE_SPEC_DRAON_BREATH = ALT_(F)  # 龙息

    ARCANE_SPEC_DPS_ROTATE_MACRO = KEY_2  # 奥法 用于 dps 循环的宏
    """
    ::
    
        #showtooltip
        /castsequence reset=15 [nochanneling] Arcane Blast, Arcane Blast, Arcane Blast, Arcane Missiles
    """
    ARCANE_SPEC_ARCANE_MISSLE_KEY_1 = KEY_1  # 奥术飞弹
    ARCANE_SPEC_ARCANE_BLAST_KEY_2 = KEY_2  # 奥术冲击
    ARCANE_SPEC_SLOW_KEY_6 = KEY_6  # 减速术 (奥系天赋 减少 移动, 施法, 远程攻击速度)
    ARCANE_SPEC_ARCANE_BARRAGE = ALT_(F)  # 奥术弹幕
    ARCANE_SPEC_ARCANE_POWER = ALT_(G)  # 奥术强化
    ARCANE_SPEC_ICY_VEINS = SHIFT_(C)  # 冰冷血脉 (冰系天赋 短时间内提高施法速度, 施法无法不受伤害影响)
    ARCANE_SPEC_SLOW = G  # 减速术 (奥系天赋 减少 移动, 施法, 远程攻击速度)
    ARCANE_SPEC_PRESENCE_OF_MIND = lambda: ClickMouse(button=MOUSE_MButton)  # 气定神闲 (奥系天赋, 法术瞬发)

    FROST_SPEC_DPS_ROTATE_MACRO = KEY_1  # 冰法 用于 dps 循环的宏
    """
    ::
    
        #showtooltip
        /castsequence reset=15 [nochanneling] Frostbolt,Frostbolt,Frostbolt,Frostbolt,Frostbolt,Frostfire Bolt
    """
    FROST_SPEC_ICE_BARRIER = ALT_(G)  # 寒冰护盾 (冰天赋 吸收伤害盾)
    FROST_SPEC_ICY_VEIN = SHIFT_(C)  # 冰冷血脉 (冰系天赋 短时间内提高施法速度, 施法无法不受伤害影响)
    FROST_SPEC_DEEP_FREEZE = ALT_(F)  # 深度冻结
    FROST_SPEC_ELEMENTAL_WATER = G  # 召唤水元素
    FROST_SPEC_ELEMENTAL_WATER_NOVA = G  # 水元素霜冻新星
    FROST_SPEC_ = KEY_1  # 技能

    HEAL_BOT_TARGET_RAID_FRAME = lambda: ClickMouse(button=MOUSE_LButton)  # 选择目标
    HEAL_BOT_FOCUS_MAGIC = lambda: ClickMouse(button=MOUSE_RButton)  # 专注魔法
    HEAL_BOT_REMOVE_CURSE = lambda: ClickMouse(button=MOUSE_MButton)  # 驱散诅咒
    HEAL_BOT_REMOVE_CURSE_CTRL_LEFT = lambda: ModifiedClickMouse.ctrl_left_click()  # 驱散诅咒


convert_to_key_maker(Mage)


class Warlock:
    """
    术士职业的按键绑定.
    """
    # curse
    ALL_SPEC_CURSE_OF_AGONY = KEY_1  # 痛苦诅咒
    ALL_SPEC_CURSE_OF_DOOM = ALT_(E)  # 厄运诅咒
    ALL_SPEC_CURSE_OF_ELEMENT = T  # 元素诅咒
    ALL_SPEC_TONGUES = G  # 语言诅咒
    ALL_SPEC_CURSE_OF_WEEKNESS = ALT_(T)  # 虚弱诅咒
    ALL_SPEC_CURSE_OF_EXHAUSION = ALT_(G)  # 疲劳诅咒

    ALL_SPEC_USE_HEALTH_STONE = SHIFT_(F1)  # 使用生命石
    ALL_SPEC_SHADOW_WARD = SHIFT_(F2)  # 灵魂碎裂 (减仇恨)

    ALL_SPEC_DRAIN_LIFE = SHIFT_(F)  # 生命吸取
    ALL_SPEC_DRAIN_MANA = SHIFT_(G)  # 法力吸取

    ALL_SPEC_FEAR = CTRL_(E)  # 恐惧
    ALL_SPEC_DRAIN_SOUL = CTRL_(R)  # 吸取灵魂
    ALL_SPEC_DEATH_COIL = CTRL_(F)  # 死亡缠绕
    ALL_SPEC_HOWL_OF_TERROR = ALT_(F1)  # 恐怖嚎叫

    ALL_SPEC_LIFE_TAP = Z  # 生命分流 (血转蓝)
    ALL_SPEC_SHADOW_FLAME = X  # 暗影烈焰
    ALL_SPEC_RAIN_OF_FIRE = ALT_(X)  # 火焰之雨

    ALL_SPEC_HELL_FIRE = CTRL_(G)  # 地狱烈焰
    ALL_SPEC_BANISH = CTRL_(X)  # 放逐
    ALL_SPEC_FEL_ARMOR = KEY_0  # 邪甲术

    ALL_SPEC_DEMONIC_CIRCLE_SUMMON = ALT_(R)  # 恶魔法阵: 召唤
    ALL_SPEC_DEMONIC_CIRCLE_TELEPORT = SHIFT_(R)  # 恶魔法阵: 传送
    ALL_SPEC_SOUL_SHATTLE = ALT_(Z)  # 灵魂碎裂 (减仇恨)

    ALL_SPEC_CORRUPTION = SHIFT_(OEM3_WAVE_OR_BACK_QUOTE)  # 腐蚀术
    ALL_SPEC_SEED_OF_CORRUPTION = R  # 腐蚀之种

    DEMON_SPEC_DPS_ROTATE = KEY_2  # 恶魔术 用于 dps 循环的宏
    """
    ::
    
        #showtooltip
    """
    DEMON_SPEC_METAMORPHOSIS = ALT_(D)  # 恶魔变身 (恶魔系 51点天赋)
    DEMON_SPEC_DEMONIC_EMPOWERMENT = ALT_(F)  # 恶魔增效
    DEMON_SPEC_FEL_DOMINATION = SHIFT_(C)  # 恶魔支配 (瞬发召唤恶魔)

    AFFLICTION_SPEC_DPS_ROTATE = KEY_2  # 痛苦术 用于 dps 循环的宏
    """
    ::
    
        #showtooltip
    """
    AFFLICTION_SPEC_UNSTABLE_AFFLICTION = KEY_1  # 技能名
    AFFLICTION_SPEC_HAUNT = KEY_1  # 技能名

    DESTRUCTION_SPEC_DPS_ROTATE = KEY_2  # 毁灭术 用于 dps 循环的宏
    """
    ::
    
        #showtooltip
    """
    DESTRUCTION_SPEC_SHADOW_FURY = ALT_(F)  # 暗影之怒
    DESTRUCTION_SPEC_SHADOW_BURN = SHIFT_(C)  # 暗影灼烧

    DESTRUCTION_SPEC_CONFLAGRATE = KEY_1  # 点燃
    DESTRUCTION_SPEC_CHAOS_BOLT = KEY_1  # 混乱箭

    HEAL_BOT_TARGET_RAID_FRAME = lambda: ClickMouse(button=MOUSE_LButton)  # 选择团队框架成员


convert_to_key_maker(Warlock)


class Priest:
    """
    牧师职业的按键绑定.
    """
    ALL_SPEC_FADE = SHIFT_(R)  # 渐隐术
    ALL_SPEC_FEAR_WARD = SHIFT_(F)  # 反恐惧结界
    ALL_SPEC_MANA_BURN = SHIFT_(G)  # 法力燃烧
    ALL_SPEC_SHACKLE_UNDEAD = CTRL_(E)  # 束缚亡灵
    ALL_SPEC_MIND_CONTROL = CTRL_(F)  # 精神控制

    ALL_SPEC_POWER_WORLD_SHIELD = SHIFT_(OEM3_WAVE_OR_BACK_QUOTE)  # 真言术盾

    ALL_SPEC_MASS_DISPEL = CTRL_(R)  # 群体驱散
    ALL_SPEC_ABOLISH_DISEASE = ALT_(R)  # 驱除疾病
    ALL_SPEC_DISPEL_MAGIC = T  # 驱散魔法

    ALL_SPEC_PRAYER_OF_HEALING = ALT_(G)  # 治疗祷言
    ALL_SPEC_HOLY_NOVA = G  # 神圣新星

    ALL_SPEC_HYMN_OF_HOPE = CTRL_(G)  # 希望赞歌
    ALL_SPEC_DIVINE_HYMN = CTRL_(X)  # 神圣赞美诗
    ALL_SPEC_SHADOW_FIEND = ALT_(T)  # 召唤暗影魔

    ALL_SPEC_INNER_FIRE = Z  # 心灵之火
    ALL_SPEC_FLASH_HEAL = X  # 快速治疗
    ALL_SPEC_PHYCHIC_SCREAM = lambda: ClickMouse(button=MOUSE_MButton)  # 心灵尖啸 (群体恐惧)

    # 暗影天赋下
    SHADOW_SPEC_DPS_ROTATE_SPEC = KEY_2  # 暗牧 一键输出循环宏
    SHADOW_SPEC_DISPERSION = ALT_(F)  # 影散 (暗影系 51点天赋, 大量减伤, 回蓝)
    SHADOW_SPEC_SILENCE = SHIFT_(C)  # 沉默
    SHADOW_SPEC_PSYCHIC_HORROR = ALT_(E)  # 心灵恐惧
    SHADOW_SPEC_SHADOW_FORM = KEY_1  # 暗影形态

    SHADOW_SPEC_SHADOW_WORD_PAIN = KEY_6  # 暗言术: 痛
    SHADOW_SPEC_DEVOURING_PLAGUE = KEY_1  # 噬灵瘟疫
    SHADOW_SPEC_VAMPIRIC_TOUCH = KEY_1  # 吸血鬼之触
    SHADOW_SPEC_VAMPIRIC_EMBRACE = KEY_1  # 吸血鬼之吻

    DISC_SPEC_DESPERATE_PRAYER = ALT_(F1)  # 绝望祷言
    DISC_SPEC_POWER_INFUSION = ALT_(F2)  # 灌注魔法
    DISC_SPEC_INNER_FOCUS = SHIFT_(C)  # 心灵专注
    DISC_SPEC_PAIN_SUPPRESSION = ALT_(F)  # 痛苦压制

    DISC_SPEC_PENANCE_KEY_1 = KEY_1  # 苦修 (戒律系 51点天赋, 大量治疗或伤害)
    DISC_SPEC_HEAL_RAID_MACRO_KEY_2 = KEY_2
    """
    全团套盾宏::
        
        #showtooltip
        # 1是戒律,2是神圣
        /targetraid
        /castsequence [spec:1] 真言术盾
        /castsequence [spec:2] reset=6, 治疗之环,真言术盾,真言术盾,真言术盾,真言术盾 
    """

    HOLY_SPEC_GUARDIAN_SPIRIT_ALT_F = ALT_(F)  # 守护天使
    HOLY_SPEC_RENEW = KEY_1  # 恢复
    HOLY_SPEC_FLASH_HEAL = KEY_1  # 快速治疗
    HOLY_SPEC_GREATER_HEAL = KEY_1  # 强效治疗术
    HOLY_SPEC_PRAYER_OF_MENDING_KEY_1 = KEY_1  # 愈合祷言 (受攻击后回血, 在团队中跳跃)
    HOLY_SPEC_BINDING_HEAL = KEY_1  # 联结治疗 (治疗目标和你自己)
    HOLY_SPEC_LIGHT_WELL = KEY_1  # 治疗之泉
    HOLY_SPEC_CIRCLE_OF_HEALING = R  # 治疗之环
    HOLY_SPEC_HEAL_RAID_MACRO_KEY_2 = KEY_2
    HOLY_SPEC_DESPERATE_PRAYER_ALT_F1 = ALT_(F1)  # 绝望祷言
    """
    全团治疗宏::
    
        #showtooltip
        # 1是戒律,2是神圣
        /targetraid
        /castsequence [spec:1] 真言术盾
        /castsequence [spec:2] reset=6, 治疗之环,真言术盾,真言术盾,真言术盾,真言术盾 
    """

    # Left | Right | Middle
    HEAL_BOT_TARGET_RAID_FRAME = lambda: ClickMouse(button=MOUSE_LButton)  # 选择团队框架成员
    HEAL_BOT_HOLY_SPEC_FLASH_HEAL = lambda: ClickMouse(button=MOUSE_LButton)  # 选择团队框架成员
    HEAL_BOT_POWER_WORD_SHIELD = lambda: ClickMouse(button=MOUSE_RButton)  # 真言术盾
    HEAL_BOT_RENEW = lambda: ClickMouse(button=MOUSE_MButton)  # 恢复

    # Shift | Alt | Ctrl + Left
    HEAL_BOT_FLASH_HEAL = lambda: ModifiedClickMouse.shift_left_click()  # 快速治疗
    HEAL_BOT_PRAYER_OF_MENDING = lambda: ModifiedClickMouse.alt_left_click()  # 愈合祷言
    HEAL_BOT_ABOLISH_DISEASE = lambda: ModifiedClickMouse.ctrl_left_click()  # 驱除疾病

    # Shift | Alt | Ctrl + Right
    HEAL_BOT_PENANCE = lambda: ModifiedClickMouse.alt_right_click()  # 苦修 (戒律系 51点天赋, 大量治疗或伤害)
    HEAL_BOT_CIRCLE_OF_HEALING = lambda: ModifiedClickMouse.alt_right_click()  # 苦修 (戒律系 51点天赋, 大量治疗或伤害)
    HEAL_BOT_DISPEL_MAGIC = lambda: ModifiedClickMouse.ctrl_right_click()  # 驱散魔法


convert_to_key_maker(Priest)
