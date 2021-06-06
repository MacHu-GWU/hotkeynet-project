# -*- coding: utf-8 -*-

from ...config import Config, ActiveCharacterConfig
from ...constant.characters import CharacterFactory
from ...constant.talent_category_association import T, TC
from .....script import Script, Hotkey, SendLabel, Key
from ... import act
from ..... import keyname, utils
from .._config_and_script import script


class Mode:
    @classmethod
    def set_mode_solo_raid_10p_batlefury_luxiaofeng_core_team(cls, config: Config):
        config.game_client_config.use_1600_900_resolution()
        config.game_client_config.use_n_windows(10)
        config.game_client_config.use_credential_list_luxiaofeng()
        config.toggle_window_config.key1_to_25_window_index = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        config.toggle_window_config.round_robin_window_index = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        config.active_character_config = ActiveCharacterConfig(
            active_characters=[
                CharacterFactory.make_char_fatmulti1_batlefury_pve_protect_pala().evolve(is_tank1=True,
                                                                                         is_dr_pala1=True),
                CharacterFactory.make_char_fatmulti2_quentin_pve_elemental_shaman().evolve(),
                CharacterFactory.make_char_fatmulti3_opiitou_pve_balance_druid().evolve(),
                CharacterFactory.make_char_fatmulti4_swagsonic_pve_arcane_mage().evolve(),
                CharacterFactory.make_char_fatmulti5_kangliu_pve_shadow_priest().evolve(),
                CharacterFactory.make_char_fitsheep_kindhearted_pve_demonology_warlock().evolve(),
                CharacterFactory.make_char_fatmulti6_kapacuk_pve_marksman_hunter().evolve(),
                CharacterFactory.make_char_fatmulti8_bunnysisters_pve_resto_druid().evolve(),
                CharacterFactory.make_char_fatmulti9_glowyy_pve_holy_pala().evolve(is_dr_pala2=True),
                CharacterFactory.make_char_fatmulti10_luxiaofeng_pve_blood_tank_dk().evolve(is_tank2=True),
            ]
        )
        config.active_character_config.set_leader1_window_index(1)
        config.active_character_config.set_leader2_window_index(10)

        def post_hook(config: Config, script: Script):
            print("set_mode_solo_raid_10p_batlefury_flydps_core_team")

        config.post_hook = post_hook

    @classmethod
    def post_hook_set_mode_solo_raid_10p_batlefury_flydps_core_team(cls, config: Config, script: Script):
        pass

    @classmethod
    def set_mode_solo_raid_22p_batlefury_flydps_4_druid_4_priest_4_shaman_core_team(cls, config: Config):
        # config.game_client_config.use_1600_900_resolution()
        config.game_client_config.use_1176_664_resolution()
        config.game_client_config.use_n_windows(22)
        config.game_client_config.use_credential_list_default()
        config.toggle_window_config.key1_to_25_window_index = list(range(1, 22 + 1))
        config.toggle_window_config.round_robin_window_index = list(range(1, 22 + 1))
        config.active_character_config = ActiveCharacterConfig(
            active_characters=[
                CharacterFactory.make_char_fatmulti1_batlefury_pve_protect_pala().evolve(is_tank1=True,
                                                                                         is_dr_pala1=True),
                CharacterFactory.make_char_fatmulti2_quentin_pve_elemental_shaman().evolve(),
                CharacterFactory.make_char_fatmulti3_opiitou_pve_balance_druid().evolve(),
                CharacterFactory.make_char_fatmulti4_swagsonic_pve_arcane_mage().evolve(),
                CharacterFactory.make_char_fatmulti5_kangliu_pve_shadow_priest().evolve(),
                CharacterFactory.make_char_fitsheep_kindhearted_pve_demonology_warlock().evolve(),
                CharacterFactory.make_char_fatmulti6_kapacuk_pve_marksman_hunter().evolve(),
                CharacterFactory.make_char_fatmulti8_bunnysisters_pve_resto_druid().evolve(),
                # CharacterFactory.make_char_fatmulti9_glowyy_pve_holy_pala().evolve(is_dr_pala2=True),
                CharacterFactory.make_char_fatmulti9_glowyy_pve_protect_pala().evolve(is_dr_pala2=True),

                # CharacterFactory.make_char_monkey130_flydps_pve_blood_tank_dk().evolve(is_tank2=True),
                # CharacterFactory.make_char_makun7551_laoshou_retri_paladin().evolve(),
                CharacterFactory.make_char_makun7551_ganjj_pve_blood_tank_dk().evolve(),

                CharacterFactory.make_char_fatmulti11_litgugua_pve_balance_druid(),
                CharacterFactory.make_char_fatmulti12_litgugub_pve_balance_druid(),
                CharacterFactory.make_char_fatmulti13_litguguc_pve_balance_druid(),
                CharacterFactory.make_char_fatmulti14_litgugud_pvp_resto_druid(),

                CharacterFactory.make_char_fatmulti19_lgmsi_pve_shadow_priest(),
                CharacterFactory.make_char_fatmulti20_lgmsj_pve_shadow_priest(),
                CharacterFactory.make_char_fatmulti21_lgmsk_pve_shadow_priest(),
                CharacterFactory.make_char_fatmulti22_lgmsl_pve_shadow_priest(),

                # CharacterFactory.make_char_fatmulti23_lgsmm_pve_elemental_shaman(),
                # CharacterFactory.make_char_fatmulti24_lgsmn_pve_elemental_shaman(),
                # CharacterFactory.make_char_fatmulti25_lgsmo_pve_elemental_shaman(),
                # CharacterFactory.make_char_fatmulti26_lgsmp_pve_elemental_shaman(),

                CharacterFactory.make_char_fatmulti23_lgsmm_pve_resto_shaman(),
                CharacterFactory.make_char_fatmulti24_lgsmn_pve_resto_shaman(),
                CharacterFactory.make_char_fatmulti25_lgsmo_pve_resto_shaman(),
                CharacterFactory.make_char_fatmulti26_lgsmp_pve_resto_shaman(),
            ]
        )
        config.active_character_config.set_leader1_window_index(1)
        config.active_character_config.set_leader2_window_index(10)

    @classmethod
    def set_mode_solo_raid_10p_naxx10_team2_batlefury_litgugu_abcd(cls, config: Config):
        config.game_client_config.use_1600_900_resolution()
        # config.game_client_config.use_1176_664_resolution()

        config.game_client_config.use_n_windows(22)
        config.game_client_config.use_credential_list_default()
        config.toggle_window_config.key1_to_25_window_index = list(range(1, 22 + 1))
        config.toggle_window_config.round_robin_window_index = list(range(1, 22 + 1))
        config.active_character_config = ActiveCharacterConfig(
            active_characters=[
                CharacterFactory.make_char_fatmulti1_batlefury_pve_protect_pala().evolve(is_tank1=True,
                                                                                         is_dr_pala1=True),
                CharacterFactory.make_char_fatmulti2_litgoatssb_pve_demo_warlock().evolve(),
                CharacterFactory.make_char_fatmulti3_opiitou_pve_balance_druid().evolve(),
                CharacterFactory.make_char_fatmulti4_swagsonic_pve_arcane_mage().evolve(),
                CharacterFactory.make_char_fatmulti5_litgoatsse_pve_demo_warlock().evolve(),
                CharacterFactory.make_char_fatmulti11_litgugua_pve_balance_druid().evolve(),
                CharacterFactory.make_char_fatmulti12_litgugub_pve_balance_druid().evolve(),
                CharacterFactory.make_char_fatmulti13_litguguc_pve_balance_druid().evolve(),
                CharacterFactory.make_char_fatmulti14_litgugud_pvp_resto_druid().evolve(is_tank2=True),
                CharacterFactory.make_char_makun7551_ganjj_pve_blood_tank_dk(),
            ]
        )
        config.active_character_config.set_leader1_window_index(1)
        config.active_character_config.set_leader2_window_index(10)

    @classmethod
    def set_mode_solo_raid_10p_naxx10_team3_glowyy_litgoatss_abcd(cls, config: Config):
        config.game_client_config.use_1600_900_resolution()
        # config.game_client_config.use_1176_664_resolution()

        config.game_client_config.use_n_windows(22)
        config.game_client_config.use_credential_list_default()
        config.toggle_window_config.key1_to_25_window_index = list(range(1, 22 + 1))
        config.active_character_config = ActiveCharacterConfig(
            active_characters=[
                CharacterFactory.make_char_fatmulti1_litgoatssa_pve_demo_warlock().evolve(),
                CharacterFactory.make_char_fatmulti2_quentin_pve_elemental_shaman().evolve(),
                CharacterFactory.make_char_fatmulti3_litgoatssc_pve_demo_warlock().evolve(),
                CharacterFactory.make_char_fatmulti4_litgoatssd_pve_demo_warlock().evolve(),
                CharacterFactory.make_char_fatmulti5_kangliu_pve_shadow_priest().evolve(),
                CharacterFactory.make_char_fitsheep_kindhearted_pve_demonology_warlock().evolve(),
                CharacterFactory.make_char_fatmulti6_kapacuk_pve_marksman_hunter().evolve(),
                CharacterFactory.make_char_fatmulti8_bunnysisters_pve_resto_druid().evolve(),
                CharacterFactory.make_char_fatmulti9_glowyy_pve_protect_pala().evolve(is_tank1=True,
                                                                                      is_dr_pala1=True),
                CharacterFactory.make_char_makun7551_laoshou_retri_paladin().evolve(),
            ]
        )
        config.toggle_window_config.round_robin_window_index = list(range(1, 22 + 1))
        config.active_character_config.set_leader1_window_index(9)
        config.active_character_config.set_leader2_window_index(9)


    @classmethod
    def set_mode_solo_raid_10p_naxx10_team4_lgms(cls, config: Config):
        config.game_client_config.use_1600_900_resolution()
        # config.game_client_config.use_1176_664_resolution()

        config.game_client_config.use_n_windows(22)
        config.game_client_config.use_credential_list_default()
        config.toggle_window_config.key1_to_25_window_index = list(range(1, 22 + 1))
        config.active_character_config = ActiveCharacterConfig(
            active_characters=[
                CharacterFactory.make_char_monkey130_flydps_pve_blood_tank_dk().evolve(),
                CharacterFactory.make_char_fatmulti19_lgmsi_pve_shadow_priest().evolve(),
                CharacterFactory.make_char_fatmulti20_lgmsj_pve_shadow_priest().evolve(),
                CharacterFactory.make_char_fatmulti21_lgmsk_pve_shadow_priest().evolve(),
                CharacterFactory.make_char_fatmulti22_lgmsl_pve_shadow_priest().evolve(),
            ]
        )
        config.toggle_window_config.round_robin_window_index = list(range(1, 22 + 1))
        config.active_character_config.set_leader1_window_index(10)
        config.active_character_config.set_leader2_window_index(10)

    @classmethod
    def set_mode_solo_raid_10p_naxx10_team5_lgsm(cls, config: Config):
        config.game_client_config.use_1600_900_resolution()
        # config.game_client_config.use_1176_664_resolution()

        config.game_client_config.use_n_windows(22)
        config.game_client_config.use_credential_list_default()
        config.toggle_window_config.key1_to_25_window_index = list(range(1, 22 + 1))
        config.active_character_config = ActiveCharacterConfig(
            active_characters=[
                CharacterFactory.make_char_monkey130_flydps_pve_blood_tank_dk().evolve(),
                CharacterFactory.make_char_fatmulti23_lgsmm_pve_elemental_shaman().evolve(),
                CharacterFactory.make_char_fatmulti24_lgsmn_pve_elemental_shaman().evolve(),
                CharacterFactory.make_char_fatmulti25_lgsmo_pve_elemental_shaman().evolve(),
                CharacterFactory.make_char_fatmulti26_lgsmp_pve_elemental_shaman().evolve(),
            ]
        )
        config.toggle_window_config.round_robin_window_index = list(range(1, 22 + 1))
        config.active_character_config.set_leader1_window_index(10)
        config.active_character_config.set_leader2_window_index(10)

    @classmethod
    def set_mode_solo_raid_10p_naxx10_team6_temp(cls, config: Config):
        config.game_client_config.use_1600_900_resolution()
        # config.game_client_config.use_1176_664_resolution()

        config.game_client_config.use_n_windows(22)
        config.game_client_config.use_credential_list_default()
        config.toggle_window_config.key1_to_25_window_index = list(range(1, 22 + 1))
        config.active_character_config = ActiveCharacterConfig(
            active_characters=[
                # 1 - 5
                # CharacterFactory.make_char_fatmulti1_batlefury_pve_protect_pala().evolve(),
                # CharacterFactory.make_char_fatmulti1_batlefury_pve_retri_pala().evolve(),
                # CharacterFactory.make_char_fatmulti1_litgoatssa_pve_demo_warlock().evolve(),
                CharacterFactory.make_char_fatmulti1_litgoatdka_pve_blood_dk().evolve(),
                # CharacterFactory.make_char_fatmulti1_litgoatdka_pvp_frost_dk().evolve(),
                #
                # CharacterFactory.make_char_fatmulti2_quentin_pve_elemental_shaman().evolve(),
                # CharacterFactory.make_char_fatmulti2_quentin_pve_resto_shaman().evolve(),
                # CharacterFactory.make_char_fatmulti2_litgoatssb_pve_demo_warlock().evolve(),
                CharacterFactory.make_char_fatmulti2_litgoatdkb_pve_unholy_dk().evolve(),
                # CharacterFactory.make_char_fatmulti2_litgoatdkb_pvp_frost_dk().evolve(),
                #
                # CharacterFactory.make_char_fatmulti3_opiitou_pve_balance_druid().evolve(),
                # CharacterFactory.make_char_fatmulti3_opiitou_pve_bear_druid().evolve(),
                # CharacterFactory.make_char_fatmulti3_litgoatssc_pve_demo_warlock().evolve(),
                CharacterFactory.make_char_fatmulti3_litgoatdkc_pve_unholy_dk().evolve(),
                # CharacterFactory.make_char_fatmulti3_litgoatdkc_pvp_frost_dk().evolve(),
                #
                # CharacterFactory.make_char_fatmulti4_swagsonic_pve_arcane_mage().evolve(),
                # CharacterFactory.make_char_fatmulti4_swagsonic_pve_fire_mage().evolve(),
                # CharacterFactory.make_char_fatmulti4_litgoatssd_pve_demo_warlock().evolve(),
                CharacterFactory.make_char_fatmulti4_litgoatdkd_pve_unholy_dk().evolve(),
                # CharacterFactory.make_char_fatmulti4_litgoatdkd_pvp_frost_dk().evolve(),
                #
                # CharacterFactory.make_char_fatmulti5_kangliu_pve_shadow_priest().evolve(),
                # CharacterFactory.make_char_fatmulti5_kangliu_pve_disco_priest().evolve(),
                # CharacterFactory.make_char_fatmulti5_litgoatsse_pve_demo_warlock().evolve(),
                CharacterFactory.make_char_fatmulti5_litgoatdke_pve_unholy_dk().evolve(),
                # CharacterFactory.make_char_fatmulti5_litgoatdke_pvp_frost_dk().evolve(),

                # 6 - 10
                # CharacterFactory.make_char_fitsheep_kindhearted_pve_demonology_warlock().evolve(),
                # CharacterFactory.make_char_fitsheep_kindhearted_pvp_destruction_warlock().evolve(),
                # CharacterFactory.make_char_fitsheep_bordercollie_pve_shadow_priest().evolve(),
                # CharacterFactory.make_char_fitsheep_bordercollie_pve_disco_priest().evolve(),
                #
                # CharacterFactory.make_char_fatmulti6_kapacuk_pve_marksman_hunter().evolve(),
                # CharacterFactory.make_char_fatmulti6_kapacuk_pvp_beast_hunter().evolve(),
                #
                # CharacterFactory.make_char_fatmulti8_bunnysisters_pve_resto_druid().evolve(),
                # CharacterFactory.make_char_fatmulti8_bunnysisters_pve_balance_druid().evolve(),
                #
                # CharacterFactory.make_char_fatmulti9_glowyy_pve_holy_pala().evolve(),
                # CharacterFactory.make_char_fatmulti9_glowyy_pve_protect_pala().evolve(),
                #
                CharacterFactory.make_char_monkey130_flydps_pve_blood_tank_dk().evolve(),
                #
                # CharacterFactory.make_char_makun7551_ganjj_pve_blood_tank_dk().evolve(),
                # CharacterFactory.make_char_makun7551_laoshou_retri_paladin().evolve(),

                # 11 - 14
                # CharacterFactory.make_char_fatmulti11_litgugua_pve_balance_druid().evolve(),
                # CharacterFactory.make_char_fatmulti11_litgugua_pvp_resto_druid().evolve(),
                #
                # CharacterFactory.make_char_fatmulti12_litgugub_pve_balance_druid().evolve(),
                # CharacterFactory.make_char_fatmulti12_litgugub_pvp_resto_druid().evolve(),
                #
                # CharacterFactory.make_char_fatmulti13_litguguc_pve_balance_druid().evolve(),
                # CharacterFactory.make_char_fatmulti13_litguguc_pvp_resto_druid().evolve(),
                #
                # CharacterFactory.make_char_fatmulti14_litgugud_pve_balance_druid().evolve(),
                # CharacterFactory.make_char_fatmulti14_litgugud_pvp_resto_druid().evolve(),

                # 15 - 18
                # CharacterFactory.make_char_fatmulti19_lgmsi_pve_shadow_priest().evolve(),
                # CharacterFactory.make_char_fatmulti20_lgmsj_pve_shadow_priest().evolve(),
                # CharacterFactory.make_char_fatmulti21_lgmsk_pve_shadow_priest().evolve(),
                # CharacterFactory.make_char_fatmulti22_lgmsl_pve_shadow_priest().evolve(),

                # 19 - 22
                # CharacterFactory.make_char_fatmulti23_lgsmm_pve_elemental_shaman().evolve(),
                # CharacterFactory.make_char_fatmulti24_lgsmn_pve_elemental_shaman().evolve(),
                # CharacterFactory.make_char_fatmulti25_lgsmo_pve_elemental_shaman().evolve(),
                # CharacterFactory.make_char_fatmulti26_lgsmp_pve_elemental_shaman().evolve(),
            ]
        )
        config.toggle_window_config.round_robin_window_index = list(range(1, 22 + 1))
        config.active_character_config.set_leader1_window_index(10)
        config.active_character_config.set_leader2_window_index(10)


    @classmethod
    def set_mode_solo_raid_25p_naxx25_full_run(cls, config: Config):
        # config.game_client_config.use_1600_900_resolution()
        config.game_client_config.use_1176_664_resolution()

        config.game_client_config.use_n_windows(22)
        config.game_client_config.use_credential_list_default()
        config.toggle_window_config.key1_to_25_window_index = list(range(1, 22 + 1))
        config.active_character_config = ActiveCharacterConfig(
            active_characters=[
                # 1 - 5
                CharacterFactory.make_char_fatmulti1_batlefury_pve_protect_pala().evolve(is_tank1=True),
                # CharacterFactory.make_char_fatmulti1_batlefury_pve_retri_pala().evolve(),
                # CharacterFactory.make_char_fatmulti1_litgoatssa_pve_demo_warlock().evolve(),
                # CharacterFactory.make_char_fatmulti1_litgoatdka_pve_blood_dk().evolve(),
                # CharacterFactory.make_char_fatmulti1_litgoatdka_pvp_frost_dk().evolve(),
                #
                CharacterFactory.make_char_fatmulti2_quentin_pve_elemental_shaman().evolve(),
                # CharacterFactory.make_char_fatmulti2_quentin_pve_resto_shaman().evolve(),
                # CharacterFactory.make_char_fatmulti2_litgoatssb_pve_demo_warlock().evolve(),
                # CharacterFactory.make_char_fatmulti2_litgoatdkb_pve_unholy_dk().evolve(),
                # CharacterFactory.make_char_fatmulti2_litgoatdkb_pvp_frost_dk().evolve(),
                #
                CharacterFactory.make_char_fatmulti3_opiitou_pve_balance_druid().evolve(),
                # CharacterFactory.make_char_fatmulti3_opiitou_pve_bear_druid().evolve(),
                # CharacterFactory.make_char_fatmulti3_litgoatssc_pve_demo_warlock().evolve(),
                # CharacterFactory.make_char_fatmulti3_litgoatdkc_pve_unholy_dk().evolve(),
                # CharacterFactory.make_char_fatmulti3_litgoatdkc_pvp_frost_dk().evolve(),
                #
                CharacterFactory.make_char_fatmulti4_swagsonic_pve_arcane_mage().evolve(),
                # CharacterFactory.make_char_fatmulti4_swagsonic_pve_fire_mage().evolve(),
                # CharacterFactory.make_char_fatmulti4_litgoatssd_pve_demo_warlock().evolve(),
                # CharacterFactory.make_char_fatmulti4_litgoatdkd_pve_unholy_dk().evolve(),
                # CharacterFactory.make_char_fatmulti4_litgoatdkd_pvp_frost_dk().evolve(),
                #
                CharacterFactory.make_char_fatmulti5_kangliu_pve_shadow_priest().evolve(),
                # CharacterFactory.make_char_fatmulti5_kangliu_pve_disco_priest().evolve(),
                # CharacterFactory.make_char_fatmulti5_litgoatsse_pve_demo_warlock().evolve(),
                # CharacterFactory.make_char_fatmulti5_litgoatdke_pve_unholy_dk().evolve(),
                # CharacterFactory.make_char_fatmulti5_litgoatdke_pvp_frost_dk().evolve(),

                # 6 - 10
                CharacterFactory.make_char_fitsheep_kindhearted_pve_demonology_warlock().evolve(),
                # CharacterFactory.make_char_fitsheep_kindhearted_pvp_destruction_warlock().evolve(),
                # CharacterFactory.make_char_fitsheep_bordercollie_pve_shadow_priest().evolve(),
                # CharacterFactory.make_char_fitsheep_bordercollie_pve_disco_priest().evolve(),
                #
                CharacterFactory.make_char_fatmulti6_kapacuk_pve_marksman_hunter().evolve(),
                # CharacterFactory.make_char_fatmulti6_kapacuk_pvp_beast_hunter().evolve(),
                #
                CharacterFactory.make_char_fatmulti8_bunnysisters_pve_resto_druid().evolve(),
                # CharacterFactory.make_char_fatmulti8_bunnysisters_pve_balance_druid().evolve(),
                #
                CharacterFactory.make_char_fatmulti9_glowyy_pve_holy_pala().evolve(),
                # CharacterFactory.make_char_fatmulti9_glowyy_pve_protect_pala().evolve(),
                #
                # CharacterFactory.make_char_monkey130_flydps_pve_blood_tank_dk().evolve(),
                CharacterFactory.make_char_fatmulti10_luxiaofeng_pve_blood_tank_dk().evolve(is_tank2=True),
                #
                # CharacterFactory.make_char_makun7551_ganjj_pve_blood_tank_dk().evolve(),
                # CharacterFactory.make_char_makun7551_laoshou_retri_paladin().evolve(),

                # 11 - 14
                # CharacterFactory.make_char_fatmulti11_litgugua_pve_balance_druid().evolve(),
                # CharacterFactory.make_char_fatmulti11_litgugua_pvp_resto_druid().evolve(),
                #
                # CharacterFactory.make_char_fatmulti12_litgugub_pve_balance_druid().evolve(),
                # CharacterFactory.make_char_fatmulti12_litgugub_pvp_resto_druid().evolve(),
                #
                # CharacterFactory.make_char_fatmulti13_litguguc_pve_balance_druid().evolve(),
                # CharacterFactory.make_char_fatmulti13_litguguc_pvp_resto_druid().evolve(),
                #
                # CharacterFactory.make_char_fatmulti14_litgugud_pve_balance_druid().evolve(),
                # CharacterFactory.make_char_fatmulti14_litgugud_pvp_resto_druid().evolve(),

                CharacterFactory.make_char_fatmulti15_litgugue_pvp_balance_druid().evolve(),
                CharacterFactory.make_char_fatmulti16_litguguf_pvp_balance_druid().evolve(),
                CharacterFactory.make_char_fatmulti17_litgugug_pvp_balance_druid().evolve(),
                CharacterFactory.make_char_fatmulti18_litguguh_pvp_resto_druid().evolve(),  # Healer

                # 15 - 18
                CharacterFactory.make_char_fatmulti19_lgmsi_pve_shadow_priest().evolve(),
                CharacterFactory.make_char_fatmulti20_lgmsj_pve_shadow_priest().evolve(),
                CharacterFactory.make_char_fatmulti21_lgmsk_pve_shadow_priest().evolve(),
                CharacterFactory.make_char_fatmulti22_lgmsl_pve_shadow_priest().evolve(),

                # 19 - 22
                CharacterFactory.make_char_fatmulti23_lgsmm_pve_elemental_shaman().evolve(),
                CharacterFactory.make_char_fatmulti24_lgsmn_pve_elemental_shaman().evolve(),
                # CharacterFactory.make_char_fatmulti25_lgsmo_pve_elemental_shaman().evolve(),
                CharacterFactory.make_char_fatmulti25_lgsmo_pve_resto_shaman().evolve(),
                # CharacterFactory.make_char_fatmulti26_lgsmp_pve_elemental_shaman().evolve(),
                CharacterFactory.make_char_fatmulti26_lgsmp_pve_resto_shaman().evolve(),
            ]
        )
        config.toggle_window_config.round_robin_window_index = list(range(1, 22 + 1))
        config.active_character_config.set_leader1_window_index(1)
        config.active_character_config.set_leader2_window_index(10)

    #--- UDR
    @classmethod
    def set_mode_solo_raid_10p_udr10_team1_kindhearted_litgoatdk_lgsm(cls, config: Config):
        config.game_client_config.use_1600_900_resolution()
        # config.game_client_config.use_1176_664_resolution()

        config.game_client_config.use_n_windows(22)
        config.game_client_config.use_credential_list_default()
        config.toggle_window_config.key1_to_25_window_index = list(range(1, 22 + 1))
        config.active_character_config = ActiveCharacterConfig(
            active_characters=[
                CharacterFactory.make_char_fatmulti1_litgoatdka_pvp_frost_dk().evolve(),
                CharacterFactory.make_char_fatmulti3_litgoatdkc_pvp_frost_dk().evolve(),
                CharacterFactory.make_char_fatmulti2_litgoatdkb_pvp_frost_dk().evolve(),
                CharacterFactory.make_char_fatmulti4_litgoatdkd_pvp_frost_dk().evolve(),
                CharacterFactory.make_char_fatmulti5_litgoatdke_pvp_frost_dk().evolve(),

                CharacterFactory.make_char_fitsheep_kindhearted_pve_demonology_warlock().evolve(),

                CharacterFactory.make_char_fatmulti23_lgsmm_pve_elemental_shaman().evolve(),
                CharacterFactory.make_char_fatmulti24_lgsmn_pve_elemental_shaman().evolve(),
                CharacterFactory.make_char_fatmulti25_lgsmo_pve_elemental_shaman().evolve(),
                CharacterFactory.make_char_fatmulti26_lgsmp_pve_elemental_shaman().evolve(),
            ]
        )
        config.toggle_window_config.round_robin_window_index = list(range(1, 22 + 1))
        config.active_character_config.set_leader1_window_index(6)
        config.active_character_config.set_leader2_window_index(6)

    @classmethod
    def set_mode_solo_raid_25p_udr25_team2_litgoatss_litgugua_lgms(cls, config: Config):
        config.game_client_config.use_1600_900_resolution()
        # config.game_client_config.use_1176_664_resolution()

        config.game_client_config.use_n_windows(22)
        config.game_client_config.use_credential_list_default()
        config.toggle_window_config.key1_to_25_window_index = list(range(1, 22 + 1))
        config.active_character_config = ActiveCharacterConfig(
            active_characters=[
                CharacterFactory.make_char_fatmulti1_litgoatssa_pve_demo_warlock().evolve(),
                CharacterFactory.make_char_fatmulti2_litgoatssb_pve_demo_warlock().evolve(),
                CharacterFactory.make_char_fatmulti3_litgoatssc_pve_demo_warlock().evolve(),
                CharacterFactory.make_char_fatmulti4_litgoatssd_pve_demo_warlock().evolve(),
                CharacterFactory.make_char_fatmulti5_litgoatsse_pve_demo_warlock().evolve(),

                CharacterFactory.make_char_fatmulti6_kapacuk_pve_marksman_hunter().evolve(),
                CharacterFactory.make_char_fatmulti8_bunnysisters_pve_resto_druid().evolve(),
                CharacterFactory.make_char_fatmulti9_glowyy_pve_protect_pala().evolve(),
                CharacterFactory.make_char_makun7551_laoshou_retri_paladin().evolve(),

                CharacterFactory.make_char_fatmulti11_litgugua_pve_balance_druid().evolve(),
                CharacterFactory.make_char_fatmulti12_litgugub_pve_balance_druid().evolve(),
                CharacterFactory.make_char_fatmulti13_litguguc_pve_balance_druid().evolve(),
                CharacterFactory.make_char_fatmulti14_litgugud_pve_balance_druid().evolve(),

                CharacterFactory.make_char_fatmulti19_lgmsi_pve_shadow_priest().evolve(),
                CharacterFactory.make_char_fatmulti20_lgmsj_pve_shadow_priest().evolve(),
                CharacterFactory.make_char_fatmulti21_lgmsk_pve_shadow_priest().evolve(),
                CharacterFactory.make_char_fatmulti22_lgmsl_pve_shadow_priest().evolve(),
            ]
        )
        config.toggle_window_config.round_robin_window_index = list(range(1, 22 + 1))
        config.active_character_config.set_leader1_window_index(7)
        config.active_character_config.set_leader2_window_index(7)

    #--- VOA
    @classmethod
    def set_mode_solo_raid_10p_voa10_team1_batlefury_team(cls, config: Config):
        config.game_client_config.use_1600_900_resolution()

        config.game_client_config.use_n_windows(22)
        config.game_client_config.use_credential_list_default()
        config.toggle_window_config.key1_to_25_window_index = list(range(1, 22 + 1))
        config.toggle_window_config.round_robin_window_index = list(range(1, 22 + 1))
        config.active_character_config = ActiveCharacterConfig(
            active_characters=[
                CharacterFactory.make_char_fatmulti1_batlefury_pve_protect_pala().evolve(is_tank1=True),

                CharacterFactory.make_char_fatmulti2_litgoatssb_pve_demo_warlock().evolve(),
                CharacterFactory.make_char_fatmulti3_opiitou_pve_balance_druid().evolve(),
                CharacterFactory.make_char_fatmulti4_swagsonic_pve_arcane_mage().evolve(),
                CharacterFactory.make_char_fatmulti5_litgoatsse_pve_demo_warlock().evolve(),

                CharacterFactory.make_char_fitsheep_bordercollie_pve_shadow_priest().evolve(),
                CharacterFactory.make_char_fatmulti6_kapacuk_pve_marksman_hunter().evolve(),
                CharacterFactory.make_char_makun7551_laoshou_retri_paladin().evolve(is_tank2=True),

                CharacterFactory.make_char_fatmulti13_litguguc_pve_balance_druid().evolve(),
                CharacterFactory.make_char_fatmulti14_litgugud_pvp_resto_druid().evolve(),
            ]
        )
        config.active_character_config.set_leader1_window_index(1)
        config.active_character_config.set_leader2_window_index(10)

    @classmethod
    def set_mode_solo_raid_10p_voa10_team2_glowyy_team(cls, config: Config):
        config.game_client_config.use_1600_900_resolution()

        config.game_client_config.use_n_windows(22)
        config.game_client_config.use_credential_list_default()
        config.toggle_window_config.key1_to_25_window_index = list(range(1, 22 + 1))
        config.active_character_config = ActiveCharacterConfig(
            active_characters=[
                CharacterFactory.make_char_fatmulti1_litgoatssa_pve_demo_warlock().evolve(),
                CharacterFactory.make_char_fatmulti2_quentin_pve_elemental_shaman().evolve(),
                CharacterFactory.make_char_fatmulti3_litgoatssc_pve_demo_warlock().evolve(),
                CharacterFactory.make_char_fatmulti4_litgoatssd_pve_demo_warlock().evolve(),
                CharacterFactory.make_char_fatmulti5_kangliu_pve_shadow_priest().evolve(),

                CharacterFactory.make_char_fatmulti8_bunnysisters_pve_resto_druid().evolve(),
                CharacterFactory.make_char_fatmulti9_glowyy_pve_protect_pala().evolve(is_tank1=True),
                CharacterFactory.make_char_makun7551_ganjj_pve_blood_tank_dk().evolve(is_tank2=True),

                CharacterFactory.make_char_fatmulti11_litgugua_pve_balance_druid().evolve(),
                CharacterFactory.make_char_fatmulti12_litgugub_pve_balance_druid().evolve(),
            ]
        )
        config.toggle_window_config.round_robin_window_index = list(range(1, 22 + 1))
        config.active_character_config.set_leader1_window_index(9)
        config.active_character_config.set_leader2_window_index(10)

    @classmethod
    def set_mode_solo_raid_10p_voa10_team4_luxiaofeng_2_priest_2_shaman_team(cls, config: Config):
        config.game_client_config.use_1600_900_resolution()

        config.game_client_config.use_n_windows(22)
        config.game_client_config.use_credential_list_luxiaofeng()
        config.toggle_window_config.key1_to_25_window_index = list(range(1, 22 + 1))
        config.active_character_config = ActiveCharacterConfig(
            active_characters=[
                CharacterFactory.make_char_fatmulti2_litgoatdkb_pve_unholy_dk().evolve(),
                CharacterFactory.make_char_fatmulti3_litgoatdkc_pve_unholy_dk().evolve(),

                CharacterFactory.make_char_fitsheep_kindhearted_pve_demonology_warlock(),

                CharacterFactory.make_char_fatmulti10_luxiaofeng_pve_blood_tank_dk().evolve(is_tank1=True),

                # CharacterFactory.make_char_fatmulti15_litgugue_pvp_balance_druid().evolve(),
                # CharacterFactory.make_char_fatmulti16_litguguf_pvp_balance_druid().evolve(),

                CharacterFactory.make_char_fatmulti19_lgmsi_pve_shadow_priest().evolve(),
                CharacterFactory.make_char_fatmulti20_lgmsj_pve_shadow_priest().evolve(),

                # CharacterFactory.make_char_fatmulti23_lgsmm_pve_elemental_shaman().evolve(),
                CharacterFactory.make_char_fatmulti23_lgsmm_pve_resto_shaman().evolve(),
                # CharacterFactory.make_char_fatmulti24_lgsmn_pve_elemental_shaman().evolve(),
                CharacterFactory.make_char_fatmulti24_lgsmn_pve_resto_shaman().evolve(),
            ]
        )
        config.toggle_window_config.round_robin_window_index = list(range(1, 22 + 1))
        config.active_character_config.set_leader1_window_index(10)
        config.active_character_config.set_leader2_window_index(10)

    @classmethod
    def set_mode_solo_raid_10p_voa10_team5_flydps_2_priest_2_shaman_team(cls, config: Config):
        config.game_client_config.use_1600_900_resolution()

        config.game_client_config.use_n_windows(22)
        config.game_client_config.use_credential_list_flydps()
        config.toggle_window_config.key1_to_25_window_index = list(range(1, 22 + 1))
        config.active_character_config = ActiveCharacterConfig(
            active_characters=[
                CharacterFactory.make_char_monkey130_flydps_pve_blood_tank_dk().evolve(is_tank1=True),
                CharacterFactory.make_char_fatmulti1_litgoatdka_pve_blood_dk().evolve(is_tank2=True),
                CharacterFactory.make_char_fatmulti4_litgoatdkd_pve_unholy_dk().evolve(),
                CharacterFactory.make_char_fatmulti5_litgoatdke_pve_unholy_dk().evolve(),

                CharacterFactory.make_char_fatmulti21_lgmsk_pve_shadow_priest().evolve(),
                CharacterFactory.make_char_fatmulti22_lgmsl_pve_shadow_priest().evolve(),

                CharacterFactory.make_char_fatmulti25_lgsmo_pve_elemental_shaman().evolve(),
                # CharacterFactory.make_char_fatmulti25_lgsmo_pve_resto_shaman().evolve(),
                # CharacterFactory.make_char_fatmulti26_lgsmp_pve_elemental_shaman().evolve(),
                CharacterFactory.make_char_fatmulti26_lgsmp_pve_resto_shaman().evolve(),
            ]
        )
        config.toggle_window_config.round_robin_window_index = list(range(1, 22 + 1))
        config.active_character_config.set_leader1_window_index(10)
        config.active_character_config.set_leader2_window_index(1)


    # VOA 10 four team.
    # batlefury team = 10 p
    # litgoatss x 5, litgoatdk x 5 = 10p
    # litgugu x 8, lgms x 4, lgsm x 4 = 16 p
    # bordercollie, laoshou, ganjj, flydps = 4p

    @classmethod
    def set_mode_solo_raid_10p_voa10_team5(cls, config: Config):
        config.game_client_config.use_1600_900_resolution()

        config.game_client_config.use_n_windows(22)
        config.game_client_config.use_credential_list_default()
        config.toggle_window_config.key1_to_25_window_index = list(range(1, 22 + 1))
        config.toggle_window_config.round_robin_window_index = list(range(1, 22 + 1))
        config.active_character_config = ActiveCharacterConfig(
            active_characters=[
                CharacterFactory.make_char_fatmulti1_batlefury_pve_protect_pala().evolve(is_tank1=True),
                CharacterFactory.make_char_fatmulti2_litgoatssb_pve_demo_warlock().evolve(),
                CharacterFactory.make_char_fatmulti3_litgoatdkc_pve_unholy_dk().evolve(),

                CharacterFactory.make_char_fatmulti4_swagsonic_pve_arcane_mage().evolve(),
                CharacterFactory.make_char_fitsheep_bordercollie_pve_shadow_priest().evolve(),
                CharacterFactory.make_char_makun7551_ganjj_pve_unholy_dps_dk().evolve(),

                CharacterFactory.make_char_fatmulti11_litgugua_pvp_resto_druid().evolve(),
                CharacterFactory.make_char_fatmulti16_litguguf_pvp_balance_druid().evolve(),

                CharacterFactory.make_char_fatmulti19_lgmsi_pve_shadow_priest().evolve(),
                CharacterFactory.make_char_fatmulti23_lgsmm_pve_elemental_shaman().evolve(),
            ]
        )
        config.active_character_config.set_leader1_window_index(1)
        config.active_character_config.set_leader2_window_index(10)

    @classmethod
    def set_mode_solo_raid_10p_voa10_team6(cls, config: Config):
        config.game_client_config.use_1600_900_resolution()

        config.game_client_config.use_n_windows(22)
        config.game_client_config.use_credential_list_default()
        config.toggle_window_config.key1_to_25_window_index = list(range(1, 22 + 1))
        config.active_character_config = ActiveCharacterConfig(
            active_characters=[
                CharacterFactory.make_char_fatmulti9_glowyy_pve_protect_pala().evolve(is_tank1=True),

                CharacterFactory.make_char_fatmulti1_litgoatssa_pve_demo_warlock().evolve(),
                CharacterFactory.make_char_fatmulti3_litgoatssc_pve_demo_warlock().evolve(),
                CharacterFactory.make_char_fatmulti2_litgoatdkb_pve_unholy_dk().evolve(),

                CharacterFactory.make_char_fatmulti5_kangliu_pve_shadow_priest().evolve(),
                CharacterFactory.make_char_fatmulti8_bunnysisters_pve_balance_druid().evolve(),

                CharacterFactory.make_char_fatmulti13_litguguc_pvp_resto_druid().evolve(),
                CharacterFactory.make_char_fatmulti18_litguguh_pvp_balance_druid().evolve(),
                CharacterFactory.make_char_fatmulti20_lgmsj_pve_shadow_priest().evolve(),
                CharacterFactory.make_char_fatmulti24_lgsmn_pve_elemental_shaman().evolve(),
            ]
        )
        config.toggle_window_config.round_robin_window_index = list(range(1, 22 + 1))
        config.active_character_config.set_leader1_window_index(9)
        config.active_character_config.set_leader2_window_index(9)

    @classmethod
    def set_mode_solo_raid_10p_voa10_team7(cls, config: Config):
        config.game_client_config.use_1600_900_resolution()

        config.game_client_config.use_n_windows(22)
        config.game_client_config.use_credential_list_luxiaofeng()
        config.toggle_window_config.key1_to_25_window_index = list(range(1, 22 + 1))
        config.active_character_config = ActiveCharacterConfig(
            active_characters=[
                CharacterFactory.make_char_fatmulti10_luxiaofeng_pve_blood_tank_dk().evolve(is_tank1=True),
                CharacterFactory.make_char_makun7551_laoshou_protect_paladin_at_window_9().evolve(is_tank2=True),

                CharacterFactory.make_char_fatmulti4_litgoatssd_pve_demo_warlock().evolve(),
                CharacterFactory.make_char_fatmulti5_litgoatdke_pve_unholy_dk().evolve(),

                CharacterFactory.make_char_fatmulti2_quentin_pve_elemental_shaman().evolve(),
                CharacterFactory.make_char_fitsheep_kindhearted_pve_demonology_warlock().evolve(),

                CharacterFactory.make_char_fatmulti15_litgugue_pvp_balance_druid().evolve(),
                CharacterFactory.make_char_fatmulti12_litgugub_pvp_resto_druid().evolve(),

                CharacterFactory.make_char_fatmulti21_lgmsk_pve_shadow_priest().evolve(),
                CharacterFactory.make_char_fatmulti25_lgsmo_pve_elemental_shaman().evolve(),
            ]
        )
        config.toggle_window_config.round_robin_window_index = list(range(1, 22 + 1))
        config.active_character_config.set_leader1_window_index(10)
        config.active_character_config.set_leader2_window_index(9)

    @classmethod
    def set_mode_solo_raid_10p_voa10_team8(cls, config: Config):
        config.game_client_config.use_1600_900_resolution()

        config.game_client_config.use_n_windows(22)
        config.game_client_config.use_credential_list_flydps()
        config.toggle_window_config.key1_to_25_window_index = list(range(1, 22 + 1))
        config.active_character_config = ActiveCharacterConfig(
            active_characters=[
                CharacterFactory.make_char_monkey130_flydps_pve_blood_tank_dk().evolve(is_tank1=True),
                CharacterFactory.make_char_fatmulti1_litgoatdka_pve_blood_dk().evolve(is_tank2=True),

                CharacterFactory.make_char_fatmulti3_opiitou_pve_balance_druid().evolve(),

                CharacterFactory.make_char_fatmulti5_litgoatsse_pve_demo_warlock().evolve(),
                CharacterFactory.make_char_fatmulti4_litgoatdkd_pve_unholy_dk().evolve(),

                CharacterFactory.make_char_fatmulti6_kapacuk_pve_marksman_hunter().evolve(),

                CharacterFactory.make_char_fatmulti17_litgugug_pvp_balance_druid().evolve(),
                CharacterFactory.make_char_fatmulti14_litgugud_pvp_resto_druid().evolve(),

                CharacterFactory.make_char_fatmulti22_lgmsl_pve_shadow_priest().evolve(),
                CharacterFactory.make_char_fatmulti26_lgsmp_pve_elemental_shaman().evolve(),
            ]
        )
        config.toggle_window_config.round_robin_window_index = list(range(1, 22 + 1))
        config.active_character_config.set_leader1_window_index(10)
        config.active_character_config.set_leader2_window_index(1)

    @classmethod
    def set_mode_solo_raid_22p_voa25_batlefury_2_priest_2_shaman_team1(cls, config: Config):
        # config.game_client_config.use_1600_900_resolution()
        config.game_client_config.use_1176_664_resolution()
        config.game_client_config.use_n_windows(22)
        config.game_client_config.use_credential_list_default()
        config.toggle_window_config.key1_to_25_window_index = list(range(1, 22 + 1))
        config.toggle_window_config.round_robin_window_index = list(range(1, 22 + 1))

        config.active_character_config = ActiveCharacterConfig(
            active_characters=[
                # 1 - 5
                CharacterFactory.make_char_fatmulti1_batlefury_pve_protect_pala().evolve(is_tank2=True),
                CharacterFactory.make_char_fatmulti2_quentin_pve_elemental_shaman().evolve(),
                CharacterFactory.make_char_fatmulti3_opiitou_pve_balance_druid().evolve(),
                CharacterFactory.make_char_fatmulti4_litgoatdkd_pve_unholy_dk().evolve(),
                CharacterFactory.make_char_fatmulti5_litgoatdke_pve_unholy_dk().evolve(),

                # 6 - 10
                CharacterFactory.make_char_fitsheep_bordercollie_pve_disco_priest().evolve(), # Healer
                CharacterFactory.make_char_fatmulti9_glowyy_pve_holy_pala().evolve(), # Healer
                CharacterFactory.make_char_fatmulti10_luxiaofeng_pve_blood_tank_dk().evolve(is_tank1=True),

                # 11 - 14
                CharacterFactory.make_char_fatmulti15_litgugue_pvp_balance_druid().evolve(),
                CharacterFactory.make_char_fatmulti16_litguguf_pvp_balance_druid().evolve(),
                CharacterFactory.make_char_fatmulti17_litgugug_pvp_balance_druid().evolve(),
                CharacterFactory.make_char_fatmulti18_litguguh_pvp_resto_druid().evolve(),  # Healer

                # 15 - 18
                CharacterFactory.make_char_fatmulti19_lgmsi_pve_shadow_priest().evolve(),
                CharacterFactory.make_char_fatmulti20_lgmsj_pve_shadow_priest().evolve(),

                # 19 - 22
                CharacterFactory.make_char_fatmulti23_lgsmm_pve_elemental_shaman().evolve(),
                CharacterFactory.make_char_fatmulti24_lgsmn_pve_elemental_shaman().evolve(),

                CharacterFactory.make_char_makun7551_ganjj_pve_unholy_dps_dk_at_window_22().evolve(),
            ]
        )
        config.active_character_config.set_leader1_window_index(1)
        config.active_character_config.set_leader2_window_index(10)

    @classmethod
    def set_mode_solo_raid_22p_voa25_litgoatdk_2_priest_2_shaman_team2(cls, config: Config):
        # config.game_client_config.use_1600_900_resolution()
        config.game_client_config.use_1176_664_resolution()
        config.game_client_config.use_n_windows(22)
        config.game_client_config.use_credential_list_default()
        config.toggle_window_config.key1_to_25_window_index = list(range(1, 22 + 1))
        config.toggle_window_config.round_robin_window_index = list(range(1, 22 + 1))

        config.active_character_config = ActiveCharacterConfig(
            active_characters=[
                # 1 - 5
                CharacterFactory.make_char_fatmulti1_litgoatdka_pve_blood_dk().evolve(is_tank2=True),
                CharacterFactory.make_char_fatmulti3_litgoatdkc_pve_unholy_dk().evolve(),
                CharacterFactory.make_char_fatmulti2_litgoatdkb_pve_unholy_dk().evolve(),
                CharacterFactory.make_char_fatmulti4_swagsonic_pve_arcane_mage().evolve(),
                CharacterFactory.make_char_fatmulti5_kangliu_pve_shadow_priest().evolve(),

                # 6 - 10
                CharacterFactory.make_char_fitsheep_kindhearted_pve_demonology_warlock().evolve(),
                CharacterFactory.make_char_fatmulti6_kapacuk_pve_marksman_hunter().evolve(),
                CharacterFactory.make_char_fatmulti8_bunnysisters_pve_resto_druid().evolve(), # Healer
                CharacterFactory.make_char_monkey130_flydps_pve_blood_tank_dk().evolve(is_tank1=True),

                # 11 - 14
                CharacterFactory.make_char_fatmulti11_litgugua_pve_balance_druid().evolve(),
                CharacterFactory.make_char_fatmulti12_litgugub_pve_balance_druid().evolve(),
                # CharacterFactory.make_char_fatmulti11_litgugua_pvp_resto_druid().evolve(),
                # CharacterFactory.make_char_fatmulti12_litgugub_pvp_resto_druid().evolve(),
                CharacterFactory.make_char_fatmulti13_litguguc_pvp_resto_druid().evolve(), # Healer
                CharacterFactory.make_char_fatmulti14_litgugud_pve_balance_druid().evolve(),

                # 15 - 18
                CharacterFactory.make_char_fatmulti21_lgmsk_pve_shadow_priest().evolve(),
                CharacterFactory.make_char_fatmulti22_lgmsl_pve_shadow_priest().evolve(),

                # 19 - 22
                CharacterFactory.make_char_makun7551_laoshou_retri_paladin_at_window_19().evolve(),
                CharacterFactory.make_char_fatmulti25_lgsmo_pve_elemental_shaman().evolve(),
                CharacterFactory.make_char_fatmulti26_lgsmp_pve_elemental_shaman().evolve(),
            ]
        )
        config.active_character_config.set_leader1_window_index(1)
        config.active_character_config.set_leader2_window_index(10)

    @classmethod
    def set_mode_solo_raid_22p_voa25_team3(cls, config: Config):
        config.game_client_config.use_1600_900_resolution()
        # config.game_client_config.use_1176_664_resolution()
        config.game_client_config.use_n_windows(22)
        config.game_client_config.use_credential_list_default()
        config.toggle_window_config.key1_to_25_window_index = list(range(1, 22 + 1))
        config.toggle_window_config.round_robin_window_index = list(range(1, 22 + 1))

        config.active_character_config = ActiveCharacterConfig(
            active_characters=[
                # 1 - 5
                CharacterFactory.make_char_fatmulti1_litgoatssa_pve_demo_warlock().evolve(),
                CharacterFactory.make_char_fatmulti2_litgoatssb_pve_demo_warlock().evolve(),
                CharacterFactory.make_char_fatmulti3_litgoatssc_pve_demo_warlock().evolve(),
                CharacterFactory.make_char_fatmulti4_litgoatssd_pve_demo_warlock().evolve(),
                CharacterFactory.make_char_fatmulti5_litgoatsse_pve_demo_warlock().evolve(),

                CharacterFactory.make_char_freiliheng_stophealing_pve_blood_tank_dk().evolve(is_tank1=True),
            ]
        )
        config.active_character_config.set_leader2_window_index(10)


    #--- ICC
    @classmethod
    def set_mode_solo_raid_10p_icc10_lich_king_team(cls, config: Config):
        """

        :param config:
        :return:
        """
        config.game_client_config.use_1600_900_resolution()
        # config.game_client_config.use_1176_664_resolution()

        config.game_client_config.use_n_windows(22)
        config.game_client_config.use_credential_list_default()
        config.toggle_window_config.key1_to_25_window_index = list(range(1, 22 + 1))
        config.active_character_config = ActiveCharacterConfig(
            active_characters=[
                # 1 - 5
                CharacterFactory.make_char_fatmulti1_batlefury_pve_protect_pala().evolve(),

                CharacterFactory.make_char_fatmulti2_quentin_pve_elemental_shaman().evolve(),
                # CharacterFactory.make_char_fatmulti2_quentin_pve_resto_shaman().evolve(),

                CharacterFactory.make_char_fatmulti3_opiitou_pve_balance_druid().evolve(),

                CharacterFactory.make_char_fatmulti4_swagsonic_pve_arcane_mage().evolve(),

                CharacterFactory.make_char_fatmulti5_kangliu_pve_shadow_priest().evolve(),

                # 6 - 10
                CharacterFactory.make_char_fitsheep_kindhearted_pve_demonology_warlock().evolve(),

                CharacterFactory.make_char_fatmulti6_kapacuk_pve_marksman_hunter().evolve(),

                CharacterFactory.make_char_fatmulti8_bunnysisters_pve_resto_druid().evolve(),

                CharacterFactory.make_char_fatmulti9_glowyy_pve_holy_pala().evolve(),

                CharacterFactory.make_char_monkey130_flydps_pve_blood_tank_dk().evolve(),
            ]
        )
        config.toggle_window_config.round_robin_window_index = list(range(1, 22 + 1))
        config.active_character_config.set_leader1_window_index(1)
        config.active_character_config.set_leader2_window_index(10)


    @classmethod
    def set_mode_solo_raid_10p_onyxia(cls, config: Config):
        """

        :param config:
        :return:
        """
        config.game_client_config.use_1600_900_resolution()

        config.game_client_config.use_n_windows(22)
        config.game_client_config.use_credential_list_default()
        config.toggle_window_config.key1_to_25_window_index = list(range(1, 22 + 1))
        config.active_character_config = ActiveCharacterConfig(
            active_characters=[
                # 1 - 5
                CharacterFactory.make_char_fatmulti1_batlefury_pve_protect_pala().evolve(leader2_window_index=10),

                CharacterFactory.make_char_fatmulti2_quentin_pve_elemental_shaman().evolve(leader1_window_index=10, leader2_window_index=10),

                CharacterFactory.make_char_fatmulti3_opiitou_pve_balance_druid().evolve(leader1_window_index=10, leader2_window_index=10),

                CharacterFactory.make_char_fatmulti4_swagsonic_pve_arcane_mage().evolve(leader1_window_index=10, leader2_window_index=10),

                CharacterFactory.make_char_fatmulti5_kangliu_pve_shadow_priest().evolve(leader1_window_index=10, leader2_window_index=10),

                # 6 - 10
                CharacterFactory.make_char_fitsheep_kindhearted_pve_demonology_warlock().evolve(leader1_window_index=10, leader2_window_index=10),

                CharacterFactory.make_char_fatmulti6_kapacuk_pve_marksman_hunter().evolve(leader1_window_index=10, leader2_window_index=10),

                CharacterFactory.make_char_fatmulti8_bunnysisters_pve_resto_druid().evolve(leader1_window_index=10, leader2_window_index=10),

                CharacterFactory.make_char_fatmulti9_glowyy_pve_holy_pala().evolve(leader1_window_index=1, leader2_window_index=10),

                CharacterFactory.make_char_fatmulti10_luxiaofeng_pve_blood_tank_dk().evolve(),
            ]
        )
        config.toggle_window_config.round_robin_window_index = list(range(1, 22 + 1))

        from .. import hk_g03_1_to_12
        from .. import hk_g07_skills

        send_label = hk_g03_1_to_12.hk_1.get_send_label_by_name(T.paladin_pve_holy.name)
        send_label.actions = [
            act.Target.TARGET_FOCUS,
            Key(name=keyname.KEY_1),
        ]

        send_label = hk_g03_1_to_12.hk_2.get_send_label_by_name(T.paladin_pve_holy.name)
        send_label.actions = [
            act.Target.TARGET_FOCUS,
            Key(name=keyname.KEY_2),
        ]

        send_label = hk_g03_1_to_12.hk_0_short_term_buff.get_send_label_by_name(TC.paladin_healer.name)
        send_label.actions = [
            act.Target.TARGET_W10_LUXIAOFENG,
            act.Paladin.HOLY_SPEC_KEY_0_BEACON_OF_LIGHT,
        ]

        hk_c = Hotkey(
            name="C",
            key=keyname.SCROLOCK_ON(keyname.C),
            actions=[
                SendLabel(
                    name=TC.priest.name,
                    to=config.lbs_by_tc(tc=TC.priest),
                    actions=[
                        act.Target.TARGET_W10_LUXIAOFENG,
                        act.Priest.ALL_SPEC_FEAR_WARD,
                    ]
                ),
            ],
            script=script,
        )

        hk_v = Hotkey(
            name="V",
            key=keyname.SCROLOCK_ON(keyname.V),
            actions=[
                SendLabel(
                    name=TC.paladin_protect.name,
                    to=config.lbs_by_tc(tc=TC.paladin_protect),
                    actions=[
                        act.Paladin.ALL_SPEC_DIVINE_PROTECTION,
                    ]
                ),
            ],
            script=script,
        )

        hk_b = Hotkey(
            name="B",
            key=keyname.SCROLOCK_ON(keyname.B),
            actions=[
                SendLabel(
                    name=TC.paladin_protect.name,
                    to=config.lbs_by_tc(tc=TC.paladin_protect),
                    actions=[
                        act.Paladin.ALL_SPEC_DIVINE_SACRIFICE,
                    ]
                ),
                SendLabel(
                    name=TC.paladin_non_protect.name,
                    to=config.lbs_by_tc(tc=TC.paladin_non_protect),
                    actions=[
                        act.Paladin.ALL_SPEC_AURA_MASTERY,
                    ]
                ),
            ],
            script=script,
        )

