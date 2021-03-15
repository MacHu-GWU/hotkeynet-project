# -*- coding: utf-8 -*-

from ...config import Config, ActiveCharacterConfig
from ...constant.characters import CharacterFactory


class Mode:
    @classmethod
    def set_mode_temp(cls, config: Config):
        # ------------------------------
        # config.game_client_config.use_1176_664_resolution()
        config.game_client_config.use_1600_900_resolution()
        # config.game_client_config.use_1920_1080_resolution()
        #------------------------------
        config.game_client_config.use_n_windows(22)
        config.toggle_window_config.key1_to_25_window_index = list(range(1, 22 + 1))
        config.toggle_window_config.round_robin_window_index = list(range(1, 22 + 1))
        # ------------------------------
        config.active_character_config = ActiveCharacterConfig(
            active_characters=[
                # 1 - 5
                # CharacterFactory.make_char_fatmulti1_batlefury_pve_protect_pala().evolve(),
                # CharacterFactory.make_char_fatmulti1_batlefury_pve_retri_pala().evolve(),
                # CharacterFactory.make_char_fatmulti1_litgoatssa_pve_demo_warlock().evolve(),
                # CharacterFactory.make_char_fatmulti1_litgoatdka_pve_blood_dk().evolve(),
                # CharacterFactory.make_char_fatmulti1_litgoatdka_pvp_frost_dk().evolve(),
                #
                # CharacterFactory.make_char_fatmulti3_opiitou_pve_balance_druid().evolve(),
                # CharacterFactory.make_char_fatmulti3_opiitou_pve_bear_druid().evolve(),
                # CharacterFactory.make_char_fatmulti3_litgoatssc_pve_demo_warlock().evolve(),
                # CharacterFactory.make_char_fatmulti3_litgoatdkc_pve_unholy_dk().evolve(),
                # CharacterFactory.make_char_fatmulti3_litgoatdkc_pvp_frost_dk().evolve(),
                #
                # CharacterFactory.make_char_fatmulti2_quentin_pve_elemental_shaman().evolve(),
                # CharacterFactory.make_char_fatmulti2_quentin_pve_resto_shaman().evolve(),
                # CharacterFactory.make_char_fatmulti2_litgoatssb_pve_demo_warlock().evolve(),
                # CharacterFactory.make_char_fatmulti3_litgoatdkc_pve_unholy_dk().evolve(),
                # CharacterFactory.make_char_fatmulti3_litgoatdkc_pvp_frost_dk().evolve(),
                #
                # CharacterFactory.make_char_fatmulti4_swagsonic_pve_arcane_mage().evolve(),
                # CharacterFactory.make_char_fatmulti4_swagsonic_pve_fire_mage().evolve(),
                # CharacterFactory.make_char_fatmulti4_litgoatssd_pve_demo_warlock().evolve(),
                # CharacterFactory.make_char_fatmulti4_litgoatdkd_pve_unholy_dk().evolve(),
                # CharacterFactory.make_char_fatmulti4_litgoatdkd_pvp_frost_dk().evolve(),
                #
                # CharacterFactory.make_char_fatmulti5_kangliu_pve_shadow_priest().evolve(),
                # CharacterFactory.make_char_fatmulti5_kangliu_pve_disco_priest().evolve(),
                # CharacterFactory.make_char_fatmulti5_litgoatsse_pve_demo_warlock().evolve(),
                # CharacterFactory.make_char_fatmulti5_litgoatdke_pve_unholy_dk().evolve(),
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
                # CharacterFactory.make_char_monkey130_flydps_pve_blood_tank_dk().evolve(),
                #
                # CharacterFactory.make_char_makun7551_ganjj_pve_blood_tank_dk().evolve(),
                # CharacterFactory.make_char_makun7551_laoshou_retri_paladin().evolve(),

                # 11 - 14
                # CharacterFactory.make_char_fatmulti11_litgugua_pve_balance_druid().evolve(),
                # CharacterFactory.make_char_fatmulti11_litgugua_pvp_resto_druid().evolve(),
                #
                # CharacterFactory.make_char_fatmulti12_litgugub_pve_balance_druid().evolve(),
                # CharacterFactory.make_char_fatmulti12_litgugub_pvp_resto_drudi().evolve(),
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
        config.active_character_config.set_leader1_window_index(1)
