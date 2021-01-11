# Use Monkey Patch to replace this value

import json
import typing

from pathlib_mate import PathCls as Path

credentials_file = Path(__file__).parent.parent.parent.change(new_basename="credentials.json")
credentials = json.loads(credentials_file.read_text(encoding="utf-8"))


def indice_to_labels(indices):
    return ["w{}".format(ind) for ind in indices]


def different_labels(indices1, indices2):
    indices1, indices2 = list(indices1), list(indices2)
    l = list(set(indices1).difference(set(indices2)))
    l.sort()
    convertion_flag = False
    for ind in (indices1 + indices2):
        if isinstance(ind, int):
            convertion_flag = True
            break
    if convertion_flag:
        return indice_to_labels(l)
    else:
        return convertion_flag


class Config:
    wow_exe_path = r"D:\HSH\Games\WOW Private\Client\World of Warcraft 3.3.5 enUS (Warman wod models)\Wow.exe"
    combat_mode = None

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

    class Credential:
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

        fatmulti18_username = "fatmulti18"
        fatmulti18_password = credentials["fatmulti18"]

        all = [
            dict(username=fatmulti1_username, password=fatmulti1_password),
            dict(username=fatmulti3_username, password=fatmulti3_password),
            dict(username=fatmulti2_username, password=fatmulti2_password),
            dict(username=fatmulti4_username, password=fatmulti4_password),
            dict(username=fatmulti5_username, password=fatmulti5_password),
            dict(username=fitsheep_username, password=fitsheep_password),
            dict(username=fatmulti6_username, password=fatmulti6_password),
            dict(username=fatmulti8_username, password=fatmulti8_password),
            dict(username=fatmulti9_username, password=fatmulti9_password),
            dict(username=fatmulti10_username, password=fatmulti10_password),
            dict(username=fatmulti11_username, password=fatmulti11_password),
            dict(username=fatmulti12_username, password=fatmulti12_password),
            dict(username=fatmulti13_username, password=fatmulti13_password),
            dict(username=fatmulti14_username, password=fatmulti14_password),
            dict(username=fatmulti15_username, password=fatmulti15_password),
            dict(username=fatmulti16_username, password=fatmulti16_password),
            dict(username=fatmulti17_username, password=fatmulti17_password),
            dict(username=fatmulti18_username, password=fatmulti18_password),
        ]  # type: typing.List[typing.Dict[str, str]]

    class Windows:
        from_1_to_5 = list(range(1, 5 + 1))
        from_1_to_10 = list(range(1, 10 + 1))
        from_1_to_18 = list(range(1, 18 + 1))

        launch_and_rename_windows = None
        batch_login_windows = None
        batch_login_accounts = None
        toggle_round_robin_windows = None
        toggle_specific_windows = None

    class SendLabelTo:
        all = []  # type: typing.List[str]
        all_tank = []  # type: typing.List[str]
        non_tank = []  # type: typing.List[str]
        all_dps = []  # type: typing.List[str]
        non_dps = []  # type: typing.List[str]
        all_healer = []  # type: typing.List[str]
        non_healer = []  # type: typing.List[str]

        # 1. war
        all_protect_war = []  # type: typing.List[str]
        all_arms_war = []  # type: typing.List[str]
        all_fury_war = []  # type: typing.List[str]

        # 2. pala
        all_protect_pala = []  # type: typing.List[str]
        all_retri_pala = []  # type: typing.List[str]
        all_holy_pala = []  # type: typing.List[str]

        # 3. dk
        all_blood_tank_dk = []  # type: typing.List[str]
        all_unholy_tank_dk = []  # type: typing.List[str]
        all_frost_tank_dk = []  # type: typing.List[str]

        # 4. hunter
        all_marksman_hunter = []  # type: typing.List[str]
        all_survival_hunter = []  # type: typing.List[str]
        all_beast_hunter = []  # type: typing.List[str]

        # 5. shaman
        all_resto_shaman = []  # type: typing.List[str]
        all_elemental_shaman = []  # type: typing.List[str]
        all_enhancement_shaman = []  # type: typing.List[str]

        # 6. rogue
        all_combat_rogue = []  # type: typing.List[str]
        all_assass_rogue = []  # type: typing.List[str]
        all_subtlety_rogue = []  # type: typing.List[str]

        # 7. druid
        all_boomkin_druid = []  # type: typing.List[str]
        all_resto_druid = []  # type: typing.List[str]
        all_bear_druid = []  # type: typing.List[str]
        all_cat_druid = []  # type: typing.List[str]

        # 8. mage
        all_fire_mage = []  # type: typing.List[str]
        all_arcane_mage = []  # type: typing.List[str]
        all_frost_mage = []  # type: typing.List[str]

        # 9. warlock
        all_demonic_warlock = []  # type: typing.List[str]
        all_affiliate_warlock = []  # type: typing.List[str]
        all_destruction_warlock = []  # type: typing.List[str]

        # 10. priest
        all_shadow_priest = []  # type: typing.List[str]
        all_disco_priest = []  # type: typing.List[str]
        all_holy_priest = []  # type: typing.List[str]

        leader_1 = []  # type: typing.List[str]
        non_leader_1 = []  # type: typing.List[str]
        leader_2 = []  # type: typing.List[str]
        non_leader_2 = []  # type: typing.List[str]

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

    @classmethod
    def set_mode_10p_batlefury_luxiaofeng_high_gs_team_solo_raid(cls):
        cls.use_1920_1080_resolution()
        cls.Windows.launch_and_rename_windows = cls.Windows.from_1_to_10
        cls.Windows.batch_login_windows = list(range(1, 10 + 1))
        cls.Windows.batch_login_accounts = list(range(1, 10 + 1))
        cls.Windows.toggle_round_robin_windows = list(range(1, 10 + 1))
        cls.Windows.toggle_specific_windows = list(range(1, 10 + 1))

        cls.SendLabelTo.all = indice_to_labels(range(1, 10 + 1))
        cls.SendLabelTo.leader_1 = indice_to_labels([1, ])
        cls.SendLabelTo.non_leader_2 = different_labels(range(1, 10 + 1), [1, ])
        cls.SendLabelTo.leader_1 = indice_to_labels([10, ])
        cls.SendLabelTo.non_leader_2 = different_labels(range(1, 10 + 1), [10, ])

        cls.SendLabelTo.all_protect_pala = indice_to_labels([1, ])
        cls.SendLabelTo.all_holy_pala = indice_to_labels([9, ])

        cls.SendLabelTo.all_unholy_tank_dk = indice_to_labels([10, ])

        cls.SendLabelTo.all_marksman_hunter = indice_to_labels([7, ])

        cls.SendLabelTo.all_elemental_shaman = indice_to_labels([3, ])

        cls.SendLabelTo.all_boomkin_druid = indice_to_labels([2, ])
        cls.SendLabelTo.all_resto_druid = indice_to_labels([8, ])

        cls.SendLabelTo.all_arcane_mage = indice_to_labels([4, ])
        cls.SendLabelTo.all_demonic_warlock = indice_to_labels([6, ])
        cls.SendLabelTo.all_shadow_priest = indice_to_labels([5, ])

    @classmethod
    def set_mode_18p_luxiaofeng_litgoatss_litgugu_team_winter_graps(cls):
        cls.use_1600_900_resolution()
        cls.Windows.launch_and_rename_windows = cls.Windows.from_1_to_18
        cls.Windows.batch_login_windows = list(range(1, 18 + 1))
        cls.Windows.batch_login_accounts = list(range(1, 18 + 1))
        cls.Windows.toggle_round_robin_windows = list(range(1, 18 + 1))
        cls.Windows.toggle_specific_windows = list(range(1, 18 + 1))

        cls.SendLabelTo.all = ["w{}".format(i) for i in range(1, 18 + 1)]
        cls.SendLabelTo.leader_1 = indice_to_labels([6, ])
        cls.SendLabelTo.non_leader_2 = indice_to_labels(different_labels(range(1, 18 + 1), [6, ]))

        cls.SendLabelTo.all_holy_pala = indice_to_labels([9, ])

        cls.SendLabelTo.all_unholy_tank_dk = indice_to_labels([10, ])

        cls.SendLabelTo.all_marksman_hunter = indice_to_labels([7, ])

        cls.SendLabelTo.all_boomkin_druid = indice_to_labels([11, 12, 13, 14, 15, 16, 17, 18])
        cls.SendLabelTo.all_resto_druid = indice_to_labels([8, ])

        cls.SendLabelTo.all_demonic_warlock = indice_to_labels([1, 2, 3, 4, 5, 6])
