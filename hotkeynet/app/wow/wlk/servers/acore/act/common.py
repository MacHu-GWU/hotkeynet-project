# -*- coding: utf-8 -*-

"""
跟职业无关的常用快捷键绑定.
"""

from hotkeynet import ActFactory
from hotkeynet.keyname import *
from hotkeynet.game.wow.model import Window


class Key(ActFactory):
    Key_1 = KEY_1
    Key_2 = KEY_2
    Key_3 = KEY_3
    Key_4 = KEY_4
    Key_5 = KEY_5
    Key_6 = KEY_6
    Key_7 = KEY_7
    Key_8 = KEY_8
    Key_9 = KEY_9
    Key_10 = KEY_0
    Key_11 = KEY_11_MINUS
    Key_12 = KEY_12_PLUS


key = Key()


class Movement(ActFactory):
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


movement = Movement()


class PetAction(ActFactory):
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


pet_action = PetAction()


class Target(ActFactory):
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
    # 以下的几个设置需要配合宏命令
    # w01
    TARGET_W01_RA = SHIFT_(INSERT)

    # w10
    TARGET_W10_RJ = SHIFT_(HOME)


target = Target()


target_leader_key_mapper = {
    Window.make(1).label: Target.TARGET_W01_RA,
    Window.make(10).label: Target.TARGET_W10_RJ,
}


class Camera(ActFactory):
    """
    视角, 摄像头相关的按键绑定, 所有职业都需要按照这个设置. 以下设置如果没有特殊说明, 都是
    在游戏内的按键绑定实现的.

    保持所有人物角色的视角统一有助于用使用需要选择施法区域的技能.
    """

    # 移动摄像机, 将其移动到第 N 套设置 ...
    # 第一个视角永远是视角拉到最近, 第一人称视角, 也就是按下 Home 键的效果.
    SET_FIRST_CAMERA_VIEW_1 = CTRL_SHIFT_ALT(INSERT)
    # 第二个视角永远是视角拉到最远, 并且开启摄像头永远跟随的模式时系统自动的高度.
    SET_FIRST_CAMERA_VIEW_2 = CTRL_SHIFT_ALT(HOME)
    # 第三个视角备用
    SET_FIRST_CAMERA_VIEW_3 = CTRL_SHIFT_ALT(PAGE_UP)

    # 将当前视角设置保存为第 N 套 ...
    SAVE_FIRST_CAMERA_VIEW_1 = CTRL_SHIFT_ALT(DELETE)
    SAVE_FIRST_CAMERA_VIEW_2 = CTRL_SHIFT_ALT(END)
    SAVE_FIRST_CAMERA_VIEW_3 = CTRL_SHIFT_ALT(PAGE_DOWN)


camera = Camera()


class System(ActFactory):
    """
    客户端系统相关的按键绑定, 所有职业都需要按照这个设置. 以下设置如果没有特殊说明, 都是
    在游戏内的按键绑定实现的.
    """

    MASTER_VOLUME_DOWN = CTRL_(KEY_11_MINUS)  # 音量调大
    MASTER_VOLUME_UP = CTRL_(KEY_12_PLUS)  # 音量调小
    TOGGLE_USER_INTERFACE = CTRL_(F12)  # 开关用户界面


system = System()


class General(ActFactory):
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


general = General()
