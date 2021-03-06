# -*- coding: utf-8 -*-
# Use Monkey Patch to replace this value

"""

"""

import json
import typing

from pathlib_mate import PathCls as Path

credentials_file = Path(__file__).parent.parent.parent.change(new_basename="credentials.json")
credentials = json.loads(credentials_file.read_text(encoding="utf-8"))


def ensure_labels(indices):
    """
    labels 在多开中是形如 w1, w2, w3, ... 这样的用于表示各个窗口的字符串.
    为了简便起见, 我们希望用 range 这样的函数生成数字, 而自动将数字转换成 label.
    此函数能将一个列表中的所有元素强制转化成 label
    :param indices:
    :return:
    """
    return [ind if isinstance(ind, str) else "w{}".format(ind) for ind in indices]


def union_list(*lists):
    l = list(set([i for lst in lists for i in lst]))
    l.sort()
    return l


def difference_list(lst, *other_lsts):
    st = set(lst)
    for l in other_lsts:
        st.difference_update(l)
    l = list(st)
    l.sort()
    return l


def different_labels(labels, *other_labels):
    """
    用于从一个label列表中将其他label列表中的元素统统移除
    """
    labels = ensure_labels(labels)
    other_labels = [
        ensure_labels(_labels)
        for _labels in other_labels
    ]
    return difference_list(labels, *other_labels)


class Config:
    wow_exe_path = r"D:\HSH\Games\WOW Private\Client\World of Warcraft 3.3.5 enUS (Warman wod models)\Wow.exe"
    combat_mode = ""
    is_pvp_mode = False

    class Coordinate:
        wrong_password_pop_up_x_at_1920_1080 = 890
        wrong_password_pop_up_y_at_1920_1080 = 565
        username_input_box_x_at_1920_1080 = 900
        username_input_box_y_at_1920_1080 = 505

        wrong_password_pop_up_x_at_1600_900 = 792
        wrong_password_pop_up_y_at_1600_900 = 502
        username_input_box_x_at_1600_900 = 788
        username_input_box_y_at_1600_900 = 451

        wrong_password_pop_up_x = None
        wrong_password_pop_up_y = None
        username_input_box_x = None
        username_input_box_y = None

        window_width_at_1920_1080 = 1800
        window_height_at_1920_1080 = 1012
        window_width_at_1600_900 = 1600
        window_height_at_1600_900 = 900

        window_width = None
        window_height = None

        pass_item_button_x = None
        pass_item_button_1_y = None
        pass_item_button_2_y = None
        pass_item_button_3_y = None
        pass_item_button_4_y = None

    class Credential:
        # 枚举拥有的所有账号的账号密码, 以供之后引用
        fatmulti1_username = "fatmulti1"
        fatmulti1_password = credentials["fatmulti1"]

        fatmulti2_username = "fatmulti2"
        fatmulti2_password = credentials["fatmulti2"]

        fatmulti3_username = "fatmulti3"
        fatmulti3_password = credentials["fatmulti3"]

        fatmulti4_username = "fatmulti4"
        fatmulti4_password = credentials["fatmulti4"]

        fatmulti5_username = "fatmulti5"
        fatmulti5_password = credentials["fatmulti5"]

        fitsheep_username = "fitsheep"
        fitsheep_password = credentials["fitsheep"]

        fatmulti6_username = "fatmulti6"
        fatmulti6_password = credentials["fatmulti6"]

        fatmulti8_username = "fatmulti8"
        fatmulti8_password = credentials["fatmulti8"]

        fatmulti9_username = "fatmulti9"
        fatmulti9_password = credentials["fatmulti9"]

        fatmulti10_username = "fatmulti10"
        fatmulti10_password = credentials["fatmulti10"]

        makun7551_username = "makun7551"
        makun7551_password = credentials["makun7551"]

        monkey130_username = "monkey130"
        monkey130_password = credentials["monkey130"]

        fatmulti11_username = "fatmulti11"
        fatmulti11_password = credentials["fatmulti11"]

        fatmulti12_username = "fatmulti12"
        fatmulti12_password = credentials["fatmulti12"]

        fatmulti13_username = "fatmulti13"
        fatmulti13_password = credentials["fatmulti13"]

        fatmulti14_username = "fatmulti14"
        fatmulti14_password = credentials["fatmulti14"]

        fatmulti15_username = "fatmulti15"
        fatmulti15_password = credentials["fatmulti15"]

        fatmulti16_username = "fatmulti16"
        fatmulti16_password = credentials["fatmulti16"]

        fatmulti17_username = "fatmulti17"
        fatmulti17_password = credentials["fatmulti17"]

        fatmulti18_username = "fatmulti19"
        fatmulti18_password = credentials["fatmulti18"]

        fatmulti19_username = "fatmulti19"
        fatmulti19_password = credentials["fatmulti19"]

        fatmulti20_username = "fatmulti20"
        fatmulti20_password = credentials["fatmulti20"]

        fatmulti21_username = "fatmulti21"
        fatmulti21_password = credentials["fatmulti21"]

        fatmulti22_username = "fatmulti22"
        fatmulti22_password = credentials["fatmulti22"]

        fatmulti23_username = "fatmulti23"
        fatmulti23_password = credentials["fatmulti23"]

        fatmulti24_username = "fatmulti24"
        fatmulti24_password = credentials["fatmulti24"]

        fatmulti25_username = "fatmulti25"
        fatmulti25_password = credentials["fatmulti25"]

        fatmulti26_username = "fatmulti26"
        fatmulti26_password = credentials["fatmulti26"]

        # 定义了一个从 1, 2, 3, ... 到最后的账号列表. 这些账号是从上面所枚举的账号中
        # 整理出来的. 也是登录时所用的账号的默认列表. 快捷键1 对应的登录第一个账号,
        # 以此类推.
        _account_inventory = [
            dict(username=fatmulti1_username, password=fatmulti1_password),
            dict(username=fatmulti2_username, password=fatmulti2_password),
            dict(username=fatmulti3_username, password=fatmulti3_password),
            dict(username=fatmulti4_username, password=fatmulti4_password),
            dict(username=fatmulti5_username, password=fatmulti5_password),
            dict(username=fitsheep_username, password=fitsheep_password),
            dict(username=fatmulti6_username, password=fatmulti6_password),
            dict(username=fatmulti8_username, password=fatmulti8_password),
            dict(username=fatmulti9_username, password=fatmulti9_password),
            # dict(username=fatmulti10_username, password=fatmulti10_password),
            # dict(username=monkey130_username, password=monkey130_password),
            dict(username=makun7551_username, password=makun7551_password),
            dict(username=fatmulti11_username, password=fatmulti11_password),
            dict(username=fatmulti12_username, password=fatmulti12_password),
            dict(username=fatmulti13_username, password=fatmulti13_password),
            dict(username=fatmulti14_username, password=fatmulti14_password),
            dict(username=fatmulti19_username, password=fatmulti19_password),
            dict(username=fatmulti20_username, password=fatmulti20_password),
            dict(username=fatmulti21_username, password=fatmulti21_password),
            dict(username=fatmulti22_username, password=fatmulti22_password),
            dict(username=fatmulti23_username, password=fatmulti23_password),
            dict(username=fatmulti24_username, password=fatmulti24_password),
            dict(username=fatmulti25_username, password=fatmulti25_password),
            dict(username=fatmulti26_username, password=fatmulti26_password),
        ]  # type: typing.List[typing.Dict[str, str]]

        default_account_sequence = list(range(1, len(_account_inventory) + 1))

        # 该变量用来自定义 快捷键 1, 2, 3, ... 所对应的账号. 如果未定义, 则用 _account_sequence
        # 中的定义. 如果有自定义, 则根据 _account_sequence 的序号进行重新排列组合.
        custom_account_sequence = []  # type: typing.List[int]

        @classmethod
        def account_sequence(cls):
            if len(cls.custom_account_sequence):
                return [
                    cls._account_inventory[ind - 1]
                    for ind in cls.custom_account_sequence
                ]
            else:
                return [
                    cls._account_inventory[ind - 1]
                    for ind in cls.default_account_sequence
                ]

    class Windows:
        from_1_to_5 = list(range(1, 5 + 1))
        from_1_to_10 = list(range(1, 10 + 1))
        from_1_to_12 = list(range(1, 12 + 1))
        from_1_to_14 = list(range(1, 14 + 1))
        from_1_to_18 = list(range(1, 18 + 1))

        # 快捷键 Ctrl Shift Alt + F1 ~ F18 对应的 窗口名字
        launch_and_rename_windows = None  # type: typing.List[int]

        # 快捷键 Ctrl Alt S 批量登录时 按照顺序 第1到最后 登录的窗口的编号
        # 通常是 1, 2, ... , N (N为一共有多少个窗口)
        # 如果是 3, 2, 1 则表示先操作 WoW3, 再操作 WoW2 最后操作 WoW1
        batch_login_windows = None  # type: typing.List[int]

        # 快捷键 Ctrl Alt S 批量登录时 按照顺序 第1到最后 登录的账号的编号
        # 通常是 1, 2, ... , N (N为一共有多少个窗口)
        # 如果是 3, 2, 1 则表示先登录 Config.Credentials.account_sequence 中的
        # 第3个, 然后是第2个, 最后是第1个
        batch_login_accounts = None  # type: typing.List[int]

        toggle_round_robin_windows = None  # type: typing.List[int]

        toggle_specific_windows = None  # type: typing.List[int]

    class SendLabelTo:
        # 1. war
        all_protect_war = []  # type: typing.List[str]
        all_arms_war = []  # type: typing.List[str]
        all_fury_war = []  # type: typing.List[str]

        @classmethod
        def all_war(cls) -> typing.List[str]:
            return union_list(
                cls.all_protect_war,
                cls.all_arms_war,
                cls.all_fury_war,
            )

        # 2. pala
        all_protect_pala = []  # type: typing.List[str]
        all_retri_pala = []  # type: typing.List[str]
        all_holy_pala = []  # type: typing.List[str]

        @classmethod
        def all_pala(cls) -> typing.List[str]:
            return union_list(
                cls.all_protect_pala,
                cls.all_retri_pala,
                cls.all_holy_pala,
            )

        # 3. dk
        all_blood_tank_dk = []  # type: typing.List[str]
        all_unholy_tank_dk = []  # type: typing.List[str]
        all_frost_tank_dk = []  # type: typing.List[str]

        all_blood_dps_dk = []  # type: typing.List[str]
        all_unholy_dps_dk = []  # type: typing.List[str]
        all_frost_dps_dk = []  # type: typing.List[str]

        @classmethod
        def all_dk(cls) -> typing.List[str]:
            return union_list(
                cls.all_blood_tank_dk,
                cls.all_unholy_tank_dk,
                cls.all_frost_tank_dk,
                cls.all_blood_dps_dk,
                cls.all_unholy_dps_dk,
                cls.all_frost_dps_dk,
            )

        @classmethod
        def all_dps_dk(cls) -> typing.List[str]:
            return union_list(
                cls.all_unholy_dps_dk,
                cls.all_blood_dps_dk,
                cls.all_frost_dps_dk,
            )

        # 4. hunter
        all_marksman_hunter = []  # type: typing.List[str]
        all_survival_hunter = []  # type: typing.List[str]
        all_beast_hunter = []  # type: typing.List[str]

        @classmethod
        def all_hunter(cls) -> typing.List[str]:
            return union_list(
                cls.all_marksman_hunter,
                cls.all_survival_hunter,
                cls.all_beast_hunter,
            )

        # 5. shaman
        all_resto_shaman = []  # type: typing.List[str]
        all_elemental_shaman = []  # type: typing.List[str]
        all_enhancement_shaman = []  # type: typing.List[str]

        @classmethod
        def all_shaman(cls) -> typing.List[str]:
            return union_list(
                cls.all_elemental_shaman,
                cls.all_enhancement_shaman,
                cls.all_resto_shaman,
            )

        # 6. rogue
        all_combat_rogue = []  # type: typing.List[str]
        all_assass_rogue = []  # type: typing.List[str]
        all_subtlety_rogue = []  # type: typing.List[str]

        @classmethod
        def all_rogue(cls) -> typing.List[str]:
            return union_list(
                cls.all_combat_rogue,
                cls.all_assass_rogue,
                cls.all_subtlety_rogue,
            )

        # 7. druid
        all_boomkin_druid = []  # type: typing.List[str]
        all_resto_druid = []  # type: typing.List[str]
        all_bear_druid = []  # type: typing.List[str]
        all_cat_druid = []  # type: typing.List[str]

        @classmethod
        def all_druid(cls) -> typing.List[str]:
            return union_list(
                cls.all_boomkin_druid,
                cls.all_resto_druid,
                cls.all_bear_druid,
                cls.all_cat_druid,
            )

        # 8. mage
        all_fire_mage = []  # type: typing.List[str]
        all_arcane_mage = []  # type: typing.List[str]
        all_frost_mage = []  # type: typing.List[str]

        @classmethod
        def all_mage(cls) -> typing.List[str]:
            return union_list(
                cls.all_fire_mage,
                cls.all_arcane_mage,
                cls.all_frost_mage,
            )

        # 9. warlock
        all_demonic_warlock = []  # type: typing.List[str]
        all_affiliate_warlock = []  # type: typing.List[str]
        all_destruction_warlock = []  # type: typing.List[str]

        @classmethod
        def all_warlock(cls) -> typing.List[str]:
            return union_list(
                cls.all_demonic_warlock,
                cls.all_affiliate_warlock,
                cls.all_destruction_warlock,
            )

        # 10. priest
        all_shadow_priest = []  # type: typing.List[str]
        all_disco_priest = []  # type: typing.List[str]
        all_holy_priest = []  # type: typing.List[str]

        @classmethod
        def all_priest(cls) -> typing.List[str]:
            return union_list(
                cls.all_shadow_priest,
                cls.all_disco_priest,
                cls.all_holy_priest,
            )

        @classmethod
        def all_tank(cls) -> typing.List[str]:
            return union_list(
                cls.all_protect_war,
                cls.all_protect_pala,
                cls.all_blood_tank_dk,
                cls.all_unholy_tank_dk,
                cls.all_frost_tank_dk,
                cls.all_bear_druid,
            )

        @classmethod
        def non_tank(cls) -> typing.List[str]:
            return different_labels(cls.all(), cls.all_tank())

        @classmethod
        def all_dps(cls) -> typing.List[str]:
            return union_list(
                cls.all_fury_war,
                cls.all_arms_war,
                cls.all_retri_pala,
                cls.all_unholy_dps_dk,
                cls.all_blood_dps_dk,
                cls.all_frost_dps_dk,
                cls.all_hunter(),
                cls.all_elemental_shaman,
                cls.all_enhancement_shaman,
                cls.all_boomkin_druid,
                cls.all_cat_druid,
                cls.all_rogue(),
                cls.all_warlock(),
                cls.all_mage(),
                cls.all_shadow_priest,
            )

        @classmethod
        def non_dps(cls) -> typing.List[str]:
            return different_labels(cls.all(), cls.all_dps())

        @classmethod
        def all_healer(cls) -> typing.List[str]:
            return union_list(
                cls.all_holy_pala,
                cls.all_resto_shaman,
                cls.all_resto_druid,
                cls.all_holy_priest,
                cls.all_disco_priest,
            )

        @classmethod
        def non_healer(cls) -> typing.List[str]:
            return different_labels(cls.all(), cls.all_healer())

        @classmethod
        def all(cls) -> typing.List[str]:
            return union_list(
                cls.all_tank(),
                cls.all_dps(),
                cls.all_healer(),
            )

        @classmethod
        def all_dispeler(cls) -> typing.List[str]:
            return union_list(
                cls.all_pala(),
                cls.all_shaman(),
                cls.all_druid(),
                cls.all_mage(),
                cls.all_priest(),
            )

        leader_1 = []  # type: typing.List[str]

        @classmethod
        def non_leader_1(cls) -> typing.List[str]:
            return different_labels(cls.all(), cls.leader_1)

        leader_2 = []  # type: typing.List[str]

        @classmethod
        def non_leader_2(cls) -> typing.List[str]:
            return different_labels(cls.all(), cls.leader_2)

        g1_dr_protect_pala = []  # type: typing.List[str]
        g1_dr_retri_pala = []  # type: typing.List[str]
        g1_dr_holy_pala = []  # type: typing.List[str]

        g2_dr_protect_pala = []  # type: typing.List[str]
        g2_dr_retri_pala = []  # type: typing.List[str]
        g2_dr_holy_pala = []  # type: typing.List[str]

        g3_dr_protect_pala = []  # type: typing.List[str]
        g3_dr_retri_pala = []  # type: typing.List[str]
        g3_dr_holy_pala = []  # type: typing.List[str]

    @classmethod
    def use_1920_1080_resolution(cls):
        cls.Coordinate.wrong_password_pop_up_x = cls.Coordinate.wrong_password_pop_up_x_at_1920_1080
        cls.Coordinate.wrong_password_pop_up_y = cls.Coordinate.wrong_password_pop_up_y_at_1920_1080
        cls.Coordinate.wrong_password_pop_up_x = cls.Coordinate.wrong_password_pop_up_x_at_1920_1080
        cls.Coordinate.wrong_password_pop_up_y = cls.Coordinate.wrong_password_pop_up_y_at_1920_1080
        cls.Coordinate.username_input_box_x = cls.Coordinate.username_input_box_x_at_1920_1080
        cls.Coordinate.username_input_box_y = cls.Coordinate.username_input_box_y_at_1920_1080
        cls.Coordinate.window_width = cls.Coordinate.window_width_at_1920_1080
        cls.Coordinate.window_height = cls.Coordinate.window_height_at_1920_1080
        cls.Coordinate.pass_item_button_x = 1525
        cls.Coordinate.pass_item_button_1_y = 924
        cls.Coordinate.pass_item_button_2_y = 857
        cls.Coordinate.pass_item_button_3_y = 790
        cls.Coordinate.pass_item_button_4_y = 724

    @classmethod
    def use_1600_900_resolution(cls):
        cls.Coordinate.wrong_password_pop_up_x = cls.Coordinate.wrong_password_pop_up_x_at_1600_900
        cls.Coordinate.wrong_password_pop_up_y = cls.Coordinate.wrong_password_pop_up_y_at_1600_900
        cls.Coordinate.wrong_password_pop_up_x = cls.Coordinate.wrong_password_pop_up_x_at_1600_900
        cls.Coordinate.wrong_password_pop_up_y = cls.Coordinate.wrong_password_pop_up_y_at_1600_900
        cls.Coordinate.username_input_box_x = cls.Coordinate.username_input_box_x_at_1600_900
        cls.Coordinate.username_input_box_y = cls.Coordinate.username_input_box_y_at_1600_900
        cls.Coordinate.window_width = cls.Coordinate.window_width_at_1600_900
        cls.Coordinate.window_height = cls.Coordinate.window_height_at_1600_900
        cls.Coordinate.pass_item_button_x = 1361
        cls.Coordinate.pass_item_button_1_y = 824
        cls.Coordinate.pass_item_button_2_y = 766
        cls.Coordinate.pass_item_button_3_y = 705
        cls.Coordinate.pass_item_button_4_y = 647

    @classmethod
    def use_10_window(cls):
        cls.Windows.launch_and_rename_windows = cls.Windows.from_1_to_10
        cls.Windows.batch_login_windows = list(range(1, 10 + 1))
        cls.Windows.batch_login_accounts = list(range(1, 10 + 1))
        cls.Windows.toggle_round_robin_windows = list(range(1, 10 + 1))
        cls.Windows.toggle_specific_windows = list(range(1, 10 + 1))

    @classmethod
    def use_14_window(cls):
        cls.Windows.launch_and_rename_windows = cls.Windows.from_1_to_14
        cls.Windows.batch_login_windows = list(range(1, 14 + 1))
        cls.Windows.batch_login_accounts = list(range(1, 14 + 1))
        cls.Windows.toggle_round_robin_windows = list(range(1, 14 + 1))
        cls.Windows.toggle_specific_windows = list(range(1, 14 + 1))

    @classmethod
    def use_18_window(cls):
        cls.Windows.launch_and_rename_windows = cls.Windows.from_1_to_18
        cls.Windows.batch_login_windows = list(range(1, 18 + 1))
        cls.Windows.batch_login_accounts = list(range(1, 18 + 1))
        cls.Windows.toggle_round_robin_windows = list(range(1, 18 + 1))
        cls.Windows.toggle_specific_windows = list(range(1, 18 + 1))

    @classmethod
    def set_mode_temp(cls):
        cls.use_1600_900_resolution()
        cls.use_14_window()

        cls.char_fatmulti1_batlefury_paladin_protect()
        cls.char_fatmulti12_litgugub_balance_druid()
        # cls.char_fatmulti12_litgugub_resto_druid()
        # cls.char_fatmulti8_bunnysisters_resto_druid()
        # cls.char_feixue_flydps_tank_dk()
        # cls.char_fatmulti5_kangliu_priest_shadow()

        # cls.char_fatmulti1_litgoatdka_dk_dps()
        # cls.char_fatmulti2_litgoatdkb_dk_dps()
        # cls.char_fatmulti3_litgoatdkc_dk_dps()
        # cls.char_fatmulti4_litgoatdkd_dk_dps()
        # cls.char_fatmulti5_litgoatdke_dk_dps()
        # cls.char_fatmulti9_glowyy_protect_pala()

        # cls.char_fatmulti9_glowyy_protect_pala()
        # cls.char_fatmulti1_litgoatssa_warlock_demon()
        # cls.char_fatmulti2_litgoatssb_warlock_demon()
        # cls.char_fatmulti3_litgoatssc_warlock_demon()
        # cls.char_fatmulti4_litgoatssd_warlock_demon()
        # cls.char_fatmulti5_litgoatsse_warlock_demon()
        # cls.char_makun7551_laoshou_protect_pala()
        # cls.char_fatmulti8_bunnysisters_resto_druid()

        cls.SendLabelTo.leader_1 = ensure_labels([1, ])
        cls.SendLabelTo.leader_2 = ensure_labels([1, ])

    # --- 10 wiindow 10 p solo Raid ---
    @classmethod
    def set_mode_10w_10p_batlefury_luxiaofeng_high_gs_team_solo_raid(cls):
        cls.use_1920_1080_resolution()
        cls.use_10_window()

        cls.char_fatmulti1_batlefury_paladin_protect()
        cls.char_fatmulti3_opiitou_druid_balance()
        cls.char_fatmulti2_quentin_shaman_elemental()
        cls.char_fatmulti4_swagsonic_mage_arcane()
        cls.char_fatmulti5_kangliu_priest_shadow()
        cls.char_fitsheep_kindhearted_demon_warlock()
        cls.char_fatmulti6_kapacuk_marksman_hunter()
        cls.char_fatmulti8_bunnysisters_resto_druid()
        cls.char_fatmulti9_glowyy_holy_pala()
        cls.char_feixue_flydps_tank_dk()

        cls.SendLabelTo.leader_1 = ensure_labels([1, ])
        cls.SendLabelTo.leader_2 = ensure_labels([10, ])

        cls.SendLabelTo.g1_dr_protect_pala = ensure_labels([1, ])
        cls.SendLabelTo.g2_dr_holy_pala = ensure_labels([9, ])
        cls.SendLabelTo.g3_dr_holy_pala = ensure_labels([9, ])

    @classmethod
    def set_mode_10w_10p_batlefury_luxiaofeng_high_gs_team_solo_raid_onyxia(cls):
        cls.combat_mode = "batlefury_luxiaofeng_high_gs_team_solo_raid_onyxia"
        cls.set_mode_10w_10p_batlefury_luxiaofeng_high_gs_team_solo_raid()

    @classmethod
    def set_mode_10w_10p_batlefury_luxiaofeng_high_gs_team_solo_raid_icc_1_marrowgar(cls):
        cls.combat_mode = "batlefury_luxiaofeng_high_gs_team_solo_raid_icc_1_marrowgar"
        cls.set_mode_10w_10p_batlefury_luxiaofeng_high_gs_team_solo_raid()

    # --- 18 window 5 p solo RDF ---
    @classmethod
    def set_mode_18w_5p_elite_team_batlefury_quentin_opiitou_swagsonic_kangliu(cls):
        cls.use_1600_900_resolution()
        cls.use_14_window()

        cls.char_fatmulti1_batlefury_paladin_protect()
        cls.char_fatmulti2_quentin_shaman_resto()
        cls.char_fatmulti3_opiitou_druid_balance()
        cls.char_fatmulti4_swagsonic_mage_arcane()
        cls.char_fatmulti5_kangliu_priest_shadow()

        cls.SendLabelTo.leader_1 = ensure_labels([1, ])
        cls.SendLabelTo.leader_2 = ensure_labels([1, ])

    @classmethod
    def set_mode_18w_5p_glowyy_litgugu_abcd(cls):
        cls.combat_mode = "set_mode_18w_5p_glowyy_litgugu_abcd"
        cls.use_1600_900_resolution()
        cls.use_14_window()

        cls.char_fatmulti9_glowyy_protect_pala()
        cls.char_fatmulti11_litgugua_balance_druid()
        cls.char_fatmulti12_litgugub_balance_druid()
        cls.char_fatmulti13_litguguc_balance_druid()
        cls.char_fatmulti14_litgugud_resto_druid()

        cls.SendLabelTo.leader_1 = ensure_labels([9, ])
        cls.SendLabelTo.leader_2 = ensure_labels([9, ])

    @classmethod
    def set_mode_18w_5p_glowyy_litgoatss_abc_bunnysisters(cls):
        cls.use_1600_900_resolution()
        cls.use_14_window()

        cls.char_fatmulti9_glowyy_protect_pala()
        cls.char_fatmulti1_litgoatssa_warlock_demon()
        cls.char_fatmulti2_litgoatssb_warlock_demon()
        cls.char_fatmulti3_litgoatssc_warlock_demon()
        cls.char_fatmulti8_bunnysisters_resto_druid()

        cls.SendLabelTo.leader_1 = ensure_labels([9, ])
        cls.SendLabelTo.leader_2 = ensure_labels([9, ])

    @classmethod
    def set_mode_18w_5p_glowyy_litgoatss_de_laoshou_bunnysisters(cls):
        cls.use_1600_900_resolution()
        cls.use_14_window()

        cls.char_fatmulti9_glowyy_protect_pala()
        cls.char_makun7551_laoshou_protect_pala()
        cls.char_fatmulti4_litgoatssd_warlock_demon()
        cls.char_fatmulti5_litgoatsse_warlock_demon()
        cls.char_fatmulti8_bunnysisters_resto_druid()

        cls.SendLabelTo.leader_1 = ensure_labels([9, ])
        cls.SendLabelTo.leader_2 = ensure_labels([9, ])

    @classmethod
    def set_mode_18w_5p_glowyy_litgoatdk_abc_bunnysisters(cls):
        cls.use_1600_900_resolution()
        cls.use_14_window()

        cls.char_fatmulti9_glowyy_protect_pala()
        cls.char_fatmulti1_litgoatdka_dk_dps()
        cls.char_fatmulti2_litgoatdkb_dk_dps()
        cls.char_fatmulti3_litgoatdkc_dk_dps()
        cls.char_fatmulti8_bunnysisters_resto_druid()

        cls.SendLabelTo.leader_1 = ensure_labels([9, ])
        cls.SendLabelTo.leader_2 = ensure_labels([9, ])

    @classmethod
    def set_mode_18w_5p_glowyy_litgoatdk_de_ganjj_bunnysisters(cls):
        cls.use_1600_900_resolution()
        cls.use_14_window()

        cls.char_fatmulti9_glowyy_protect_pala()
        cls.char_makun7551_ganjj_tank_dk()
        cls.char_fatmulti4_litgoatdkd_dk_dps()
        cls.char_fatmulti5_litgoatdke_dk_dps()
        cls.char_fatmulti8_bunnysisters_resto_druid()

        cls.SendLabelTo.leader_1 = ensure_labels([9, ])
        cls.SendLabelTo.leader_2 = ensure_labels([9, ])

    @classmethod
    def set_mode_18w_5p_batlefury_bunnysister_kangliu_kindhearted_kapacuk(cls):
        cls.use_1600_900_resolution()
        cls.use_14_window()

        cls.char_fatmulti1_batlefury_paladin_protect()
        cls.char_fatmulti8_bunnysisters_resto_druid()
        cls.char_fatmulti5_kangliu_priest_shadow()
        cls.char_fitsheep_kindhearted_demon_warlock()
        cls.char_fatmulti6_kapacuk_marksman_hunter()

        cls.SendLabelTo.leader_1 = ensure_labels([1, ])
        cls.SendLabelTo.leader_2 = ensure_labels([1, ])

    @classmethod
    def set_mode_18w_5p_batlefury_glowyy_opiitou_quentin_swagsonic(cls):
        cls.use_1600_900_resolution()
        cls.use_14_window()

        cls.char_fatmulti1_batlefury_paladin_protect()
        cls.char_fatmulti8_bunnysisters_resto_druid()
        cls.char_fatmulti5_kangliu_priest_shadow()
        cls.char_fitsheep_kindhearted_demon_warlock()
        cls.char_fatmulti6_kapacuk_marksman_hunter()

        cls.SendLabelTo.leader_1 = ensure_labels([1, ])
        cls.SendLabelTo.leader_2 = ensure_labels([1, ])

    @classmethod
    def set_mode_18w_18p_luxiaofeng_litgoatss_litgugu_team_winter_graps(cls):
        cls.is_pvp_mode = True
        cls.combat_mode = "set_mode_18w_18p_luxiaofeng_litgoatss_litgugu_team_winter_graps"

        cls.use_1600_900_resolution()
        cls.use_18_window()

        # cls.char_fatmulti1_litgoatssa_warlock_demon()
        # cls.char_fatmulti3_litgoatssb_warlock_demon()
        # cls.char_fatmulti2_litgoatssc_warlock_demon()
        # cls.char_fatmulti4_litgoatssd_warlock_demon()
        # cls.char_fatmulti5_litgoatsse_warlock_demon()

        cls.char_fatmulti1_litgoatdka_dk_dps()
        cls.char_fatmulti2_litgoatdkb_dk_dps()
        cls.char_fatmulti3_litgoatdkc_dk_dps()
        cls.char_fatmulti4_litgoatdkd_dk_dps()
        cls.char_fatmulti5_litgoatdke_dk_dps()

        cls.char_fitsheep_kindhearted_destruction_warlock()
        cls.char_fatmulti6_kapacuk_marksman_hunter()
        cls.char_fatmulti8_bunnysisters_resto_druid()
        cls.char_fatmulti9_glowyy_holy_pala()
        cls.char_makun7551_ganjj_tank_dk()

        cls.char_fatmulti11_litgugua_balance_druid()
        cls.char_fatmulti12_litgugub_balance_druid()
        cls.char_fatmulti13_litguguc_balance_druid()
        cls.char_fatmulti14_litgugud_resto_druid()

        cls.SendLabelTo.leader_1 = ensure_labels([6, ])
        cls.SendLabelTo.leader_2 = ensure_labels([9, ])

    @classmethod
    def set_mode_18w_18p_boomy_wild(cls):
        cls.combat_mode = "set_mode_18w_18p_boomy_wild"

        cls.use_1600_900_resolution()
        cls.use_18_window()
        cls.char_fatmulti3_opiitou_druid_balance()
        cls.char_fatmulti8_bunnysisters_balance_druid()
        cls.char_fatmulti11_litgugua_balance_druid()
        cls.char_fatmulti12_litgugub_balance_druid()
        cls.char_fatmulti13_litguguc_balance_druid()
        cls.char_fatmulti14_litgugud_resto_druid()
        cls.SendLabelTo.leader_1 = ensure_labels([11, ])
        cls.SendLabelTo.leader_2 = ensure_labels([11, ])

    @classmethod
    def set_mode_18p_batlefury_luxiaofeng_litgugu_team_solo_raid(cls):
        cls.is_pvp_mode = True
        cls.use_1600_900_resolution()
        cls.use_18_window()
        cls.combat_mode = "set_mode_18p_batlefury_luxiaofeng_litgugu_team_solo_raid"

        cls.char_fatmulti1_batlefury_paladin_protect()
        cls.char_fatmulti3_opiitou_druid_balance()
        cls.char_fatmulti2_quentin_shaman_elemental()
        cls.char_fatmulti4_swagsonic_mage_arcane()
        cls.char_fatmulti5_kangliu_priest_shadow()
        cls.char_fitsheep_kindhearted_demon_warlock()
        cls.char_fatmulti6_kapacuk_marksman_hunter()
        cls.char_fatmulti8_bunnysisters_resto_druid()
        cls.char_fatmulti9_glowyy_holy_pala()
        cls.char_makun7551_ganjj_tank_dk()

        cls.char_fatmulti11_litgugua_balance_druid()
        cls.char_fatmulti12_litgugub_balance_druid()
        cls.char_fatmulti13_litguguc_balance_druid()
        cls.char_fatmulti14_litgugud_resto_druid()

        cls.SendLabelTo.leader_1 = ensure_labels([1, ])
        cls.SendLabelTo.leader_2 = ensure_labels([10, ])
        cls.SendLabelTo.g1_dr_protect_pala = ensure_labels([1, ])
        cls.SendLabelTo.g2_dr_holy_pala = ensure_labels([9, ])

    @classmethod
    def set_mode_18p_batlefury_kangliu_litgugu_team_solo_voa(cls):
        cls.use_1600_900_resolution()
        cls.use_18_window()

        cls.SendLabelTo.leader_1 = ensure_labels([1, ])
        cls.SendLabelTo.leader_2 = ensure_labels([11, ])

        cls.SendLabelTo.all = ensure_labels([1, 5, 11, 12, 13, 14, 15, 16, 17, 18])

        cls.SendLabelTo.all_boomkin_druid = ensure_labels([11, 12, 13, 15, 16, 17, ])
        cls.SendLabelTo.all_resto_druid = ensure_labels([14, 18, ])

        cls.SendLabelTo.all_shadow_priest = ensure_labels([5, ])

    #
    @classmethod
    def set_mode_18w_10p_batlefury_litgoatssb_opiitou_swagsonic_litgoatsse_ganjj_litgugu_a_to_d_solo_weekly(cls):
        """
        10开做Naxx蜘蛛周长任务
        """
        cls.use_1600_900_resolution()
        cls.use_18_window()

        cls.char_fatmulti1_batlefury_paladin_protect()
        cls.char_fatmulti2_litgoatssb_warlock_demon()
        cls.char_fatmulti3_opiitou_druid_balance()
        cls.char_fatmulti4_swagsonic_mage_arcane()
        cls.char_fatmulti5_litgoatsse_warlock_demon()

        cls.char_makun7551_ganjj_dps_dk()
        cls.char_fatmulti11_litgugua_balance_druid()
        cls.char_fatmulti12_litgugub_balance_druid()
        cls.char_fatmulti13_litguguc_balance_druid()
        cls.char_fatmulti14_litgugud_resto_druid()

        cls.SendLabelTo.leader_1 = ensure_labels([1, ])
        cls.SendLabelTo.leader_2 = ensure_labels([10, ])
        cls.SendLabelTo.g1_dr_protect_pala = ensure_labels([1, ])

    @classmethod
    def set_mode_18w_10p_luxiaofeng_glowyy_bunny_kindhearted_kapacuk_litgoatss_a_to_e_quentin_kangliu_solo_weekly(cls):
        """
        10开做Naxx蜘蛛周长任务
        """
        cls.use_1600_900_resolution()
        cls.use_18_window()

        cls.char_fatmulti1_litgoatssa_warlock_demon()
        cls.char_fatmulti2_quentin_shaman_elemental()
        cls.char_fatmulti3_litgoatssc_warlock_demon()
        cls.char_fatmulti4_litgoatssd_warlock_demon()
        cls.char_fatmulti5_kangliu_priest_shadow()

        cls.char_makun7551_laoshou_holy_pala()
        cls.char_fitsheep_kindhearted_demon_warlock()
        cls.char_fatmulti6_kapacuk_marksman_hunter()
        cls.char_fatmulti8_bunnysisters_resto_druid()
        cls.char_fatmulti9_glowyy_protect_pala()

        cls.SendLabelTo.leader_1 = ensure_labels([9, ])
        cls.SendLabelTo.leader_2 = ensure_labels([10, ])
        cls.SendLabelTo.g1_dr_protect_pala = ensure_labels([9, ])
        cls.SendLabelTo.g1_dr_protect_pala = ensure_labels([9, ])

    @classmethod
    def set_mode_18w_5p_litgoatdk_abcde_solo_weekly(cls):
        cls.use_1600_900_resolution()
        cls.use_18_window()

        cls.char_fatmulti1_litgoatdka_dk_dps()
        cls.char_fatmulti2_litgoatdkb_dk_dps()
        cls.char_fatmulti3_litgoatdkc_dk_dps()
        cls.char_fatmulti4_litgoatdkd_dk_dps()
        cls.char_fatmulti5_litgoatdke_dk_dps()

        cls.SendLabelTo.leader_1 = ensure_labels([1, ])
        cls.SendLabelTo.leader_2 = ensure_labels([1, ])

    @classmethod
    def set_mode_10w_10p_batle_to_kangliu_and_bunny_litgugu_a_to_d_daily_quest_gold_farm(cls):
        cls.use_1600_900_resolution()
        cls.use_18_window()

        cls.char_fatmulti1_batlefury_paladin_protect()
        cls.char_fatmulti3_opiitou_druid_balance()
        cls.char_fatmulti2_quentin_shaman_elemental()
        cls.char_fatmulti4_swagsonic_mage_arcane()
        cls.char_fatmulti5_kangliu_priest_shadow()

        cls.char_fatmulti8_bunnysisters_balance_druid()
        cls.char_fatmulti11_litgugua_balance_druid()
        cls.char_fatmulti12_litgugub_balance_druid()
        cls.char_fatmulti13_litguguc_balance_druid()
        cls.char_fatmulti14_litgugud_resto_druid()

        cls.SendLabelTo.leader_1 = ensure_labels([1, ])
        cls.SendLabelTo.leader_2 = ensure_labels([11, ])

    # --- Leveling
    @classmethod
    def set_mode_18w_14p_opiitou_and_batlefury_carry_leveling(cls):
        cls.combat_mode = "set_mode_18w_14p_opiitou_and_batlefury_carry_leveling"
        cls.use_1600_900_resolution()
        cls.Windows.launch_and_rename_windows = cls.Windows.from_1_to_12

        cls.Windows.batch_login_windows = [
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
        ]
        cls.Windows.batch_login_accounts = [
            3, 15, 16, 17, 18, # 野德司机队
            1, 19, 20, 21, 22, # 防骑司机队
            4, 6, # 法师, 术士
        ]
        cls.Windows.toggle_round_robin_windows = list(range(1, 18 + 1))
        cls.Windows.toggle_specific_windows = list(range(1, 18 + 1))

        # cls.SendLabelTo.all_bear_druid.append("w1")
        cls.SendLabelTo.all_boomkin_druid.append("w1")
        cls.SendLabelTo.all_holy_priest = ["w2", "w3", "w4", "w5"]

        cls.SendLabelTo.all_protect_pala.append("w6")
        cls.SendLabelTo.all_resto_shaman = ["w7", "w8", "w9", "w10"]

        cls.SendLabelTo.all_arcane_mage.append("w11")
        cls.SendLabelTo.all_demonic_warlock.append("w12")

        cls.SendLabelTo.leader_1 = ensure_labels([3, ])
        cls.SendLabelTo.leader_2 = ensure_labels([1, ])

    # --- Account, Character, Talent Definition
    # --- fatmulti 1
    @classmethod
    def char_fatmulti1_batlefury_paladin_protect(cls):
        label = "w1"
        cls.SendLabelTo.all_protect_pala.append(label)

    @classmethod
    def char_fatmulti1_batlefury_paladin_retri(cls):
        label = "w1"
        cls.SendLabelTo.all_retri_pala.append(label)

    @classmethod
    def char_fatmulti1_litgoatssa_warlock_demon(cls):
        label = "w1"
        cls.SendLabelTo.all_demonic_warlock.append(label)

    @classmethod
    def char_fatmulti1_litgoatdka_dk_tank(cls):
        label = "w1"
        cls.SendLabelTo.all_unholy_tank_dk.append(label)

    @classmethod
    def char_fatmulti1_litgoatdka_dk_dps(cls):
        label = "w1"
        cls.SendLabelTo.all_unholy_dps_dk.append(label)

    # --- fatmulti 2
    @classmethod
    def char_fatmulti2_quentin_shaman_elemental(cls):
        label = "w2"
        cls.SendLabelTo.all_elemental_shaman.append(label)

    @classmethod
    def char_fatmulti2_quentin_shaman_resto(cls):
        label = "w2"
        cls.SendLabelTo.all_resto_shaman.append(label)

    @classmethod
    def char_fatmulti2_litgoatssb_warlock_demon(cls):
        label = "w2"
        cls.SendLabelTo.all_demonic_warlock.append(label)

    @classmethod
    def char_fatmulti2_litgoatdkb_dk_tank(cls):
        label = "w2"
        cls.SendLabelTo.all_unholy_tank_dk.append(label)

    @classmethod
    def char_fatmulti2_litgoatdkb_dk_dps(cls):
        label = "w2"
        cls.SendLabelTo.all_unholy_dps_dk.append(label)

    # --- fatmulti 3
    @classmethod
    def char_fatmulti3_opiitou_druid_balance(cls):
        label = "w3"
        cls.SendLabelTo.all_boomkin_druid.append(label)

    @classmethod
    def char_fatmulti3_opiitou_druid_bear(cls):
        label = "w3"
        cls.SendLabelTo.all_bear_druid.append(label)

    @classmethod
    def char_fatmulti3_litgoatssc_warlock_demon(cls):
        label = "w3"
        cls.SendLabelTo.all_demonic_warlock.append(label)

    @classmethod
    def char_fatmulti3_litgoatdkc_dk_tank(cls):
        label = "w3"
        cls.SendLabelTo.all_unholy_tank_dk.append(label)

    @classmethod
    def char_fatmulti3_litgoatdkc_dk_dps(cls):
        label = "w3"
        cls.SendLabelTo.all_unholy_dps_dk.append(label)

    # --- fatmulti 4
    @classmethod
    def char_fatmulti4_swagsonic_mage_arcane(cls):
        label = "w4"
        cls.SendLabelTo.all_arcane_mage.append(label)

    @classmethod
    def char_fatmulti4_swagsonic_mage_fire(cls):
        label = "w4"
        cls.SendLabelTo.all_fire_mage.append(label)

    @classmethod
    def char_fatmulti4_litgoatssd_warlock_demon(cls):
        label = "w4"
        cls.SendLabelTo.all_demonic_warlock.append(label)

    @classmethod
    def char_fatmulti4_litgoatdkd_dk_tank(cls):
        label = "w4"
        cls.SendLabelTo.all_unholy_tank_dk.append(label)

    @classmethod
    def char_fatmulti4_litgoatdkd_dk_dps(cls):
        label = "w4"
        cls.SendLabelTo.all_unholy_dps_dk.append(label)

    # --- fatmulti 5
    @classmethod
    def char_fatmulti5_kangliu_priest_shadow(cls):
        label = "w5"
        cls.SendLabelTo.all_shadow_priest.append(label)

    @classmethod
    def char_fatmulti5_kangliu_priest_disco(cls):
        label = "w5"
        cls.SendLabelTo.all_disco_priest.append(label)

    @classmethod
    def char_fatmulti5_litgoatsse_warlock_demon(cls):
        label = "w5"
        cls.SendLabelTo.all_demonic_warlock.append(label)

    @classmethod
    def char_fatmulti5_litgoatdke_dk_tank(cls):
        label = "w5"
        cls.SendLabelTo.all_unholy_tank_dk.append(label)

    @classmethod
    def char_fatmulti5_litgoatdke_dk_dps(cls):
        label = "w5"
        cls.SendLabelTo.all_unholy_dps_dk.append(label)

    @classmethod
    def char_fitsheep_kindhearted_demon_warlock(cls):
        label = "w6"
        cls.SendLabelTo.all_demonic_warlock.append(label)

    @classmethod
    def char_fitsheep_kindhearted_destruction_warlock(cls):
        label = "w6"
        cls.SendLabelTo.all_destruction_warlock.append(label)

    @classmethod
    def char_fatmulti6_kapacuk_marksman_hunter(cls):
        label = "w7"
        cls.SendLabelTo.all_marksman_hunter.append(label)

    @classmethod
    def char_fatmulti6_kapacuk_survival_hunter(cls):
        label = "w7"
        cls.SendLabelTo.all_survival_hunter.append(label)

    @classmethod
    def char_fatmulti8_bunnysisters_resto_druid(cls):
        label = "w8"
        cls.SendLabelTo.all_resto_druid.append(label)

    @classmethod
    def char_fatmulti8_bunnysisters_balance_druid(cls):
        label = "w8"
        cls.SendLabelTo.all_boomkin_druid.append(label)

    @classmethod
    def char_fatmulti9_glowyy_holy_pala(cls):
        label = "w9"
        cls.SendLabelTo.all_holy_pala.append(label)

    @classmethod
    def char_fatmulti9_glowyy_protect_pala(cls):
        label = "w9"
        cls.SendLabelTo.all_protect_pala.append(label)

    @classmethod
    def char_feixue_flydps_tank_dk(cls):
        label = "w10"
        cls.SendLabelTo.all_unholy_tank_dk.append(label)

    @classmethod
    def char_makun7551_laoshou_protect_pala(cls):
        label = "w10"
        cls.SendLabelTo.all_protect_pala.append(label)

    @classmethod
    def char_makun7551_laoshou_holy_pala(cls):
        label = "w10"
        cls.SendLabelTo.all_holy_pala.append(label)

    @classmethod
    def char_makun7551_ganjj_tank_dk(cls):
        label = "w10"
        cls.SendLabelTo.all_unholy_tank_dk.append(label)

    @classmethod
    def char_makun7551_ganjj_dps_dk(cls):
        label = "w10"
        cls.SendLabelTo.all_unholy_dps_dk.append(label)

    @classmethod
    def char_fatmulti11_litgugua_balance_druid(cls):
        label = "w11"
        cls.SendLabelTo.all_boomkin_druid.append(label)

    @classmethod
    def char_fatmulti11_litgugua_resto_druid(cls):
        label = "w11"
        cls.SendLabelTo.all_resto_druid.append(label)

    @classmethod
    def char_fatmulti12_litgugub_balance_druid(cls):
        label = "w12"
        cls.SendLabelTo.all_boomkin_druid.append(label)

    @classmethod
    def char_fatmulti12_litgugub_resto_druid(cls):
        label = "w12"
        cls.SendLabelTo.all_resto_druid.append(label)

    @classmethod
    def char_fatmulti13_litguguc_balance_druid(cls):
        label = "w13"
        cls.SendLabelTo.all_boomkin_druid.append(label)

    @classmethod
    def char_fatmulti13_litguguc_resto_druid(cls):
        label = "w13"
        cls.SendLabelTo.all_resto_druid.append(label)

    @classmethod
    def char_fatmulti14_litgugud_balance_druid(cls):
        label = "w14"
        cls.SendLabelTo.all_boomkin_druid.append(label)

    @classmethod
    def char_fatmulti14_litgugud_resto_druid(cls):
        label = "w14"
        cls.SendLabelTo.all_resto_druid.append(label)

    @classmethod
    def char_fatmulti19_lgmsi_shadow_priest(cls):
        label = "w2"
        cls.SendLabelTo.all_holy_priest.append(label)

    @classmethod
    def char_fatmulti20_lgmsj_shadow_priest(cls):
        label = "w3"
        cls.SendLabelTo.all_holy_priest.append(label)

    @classmethod
    def char_fatmulti21_lgmsk_shadow_priest(cls):
        label = "w4"
        cls.SendLabelTo.all_holy_priest.append(label)

    @classmethod
    def char_fatmulti22_lgmsl_shadow_priest(cls):
        label = "w5"
        cls.SendLabelTo.all_holy_priest.append(label)

    @classmethod
    def char_fatmulti23_lgsmm_elemental_shaman(cls):
        label = "w7"
        cls.SendLabelTo.all_resto_shaman.append(label)

    @classmethod
    def char_fatmulti24_lgsmn_elemental_shaman(cls):
        label = "w8"
        cls.SendLabelTo.all_resto_shaman.append(label)

    @classmethod
    def char_fatmulti25_lgsmo_elemental_shaman(cls):
        label = "w9"
        cls.SendLabelTo.all_resto_shaman.append(label)

    @classmethod
    def char_fatmulti26_lgsmp_elemental_shaman(cls):
        label = "w10"
        cls.SendLabelTo.all_resto_shaman.append(label)
