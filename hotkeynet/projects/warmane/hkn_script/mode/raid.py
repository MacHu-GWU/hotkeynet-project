# -*- coding: utf-8 -*-

from ...config import Config, ActiveCharacterConfig
from ...constant.characters import CharacterFactory
from .....script import Script


class Mode:
    @classmethod
    def set_mode_solo_raid_10p_batlefury_flydps_core_team(cls, config: Config):
        config.game_client_config.use_1920_1080_resolution()
        config.game_client_config.use_n_windows(10)
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
                CharacterFactory.make_char_monkey130_flydps_pve_blood_tank_dk().evolve(is_tank2=True),
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
        config.game_client_config.use_1600_900_resolution()
        # config.game_client_config.use_1176_664_resolution()

        config.game_client_config.use_n_windows(22)
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
                CharacterFactory.make_char_fatmulti9_glowyy_pve_holy_pala().evolve(is_dr_pala2=True),
                CharacterFactory.make_char_monkey130_flydps_pve_blood_tank_dk().evolve(is_tank2=True),
                CharacterFactory.make_char_fatmulti11_litgugua_pve_balance_druid(),
                CharacterFactory.make_char_fatmulti12_litgugub_pve_balance_druid(),
                CharacterFactory.make_char_fatmulti13_litguguc_pve_balance_druid(),
                CharacterFactory.make_char_fatmulti14_litgugud_pve_resto_druid(),
                CharacterFactory.make_char_fatmulti19_lgmsi_pve_shadow_priest(),
                CharacterFactory.make_char_fatmulti20_lgmsj_pve_shadow_priest(),
                CharacterFactory.make_char_fatmulti21_lgmsk_pve_shadow_priest(),
                CharacterFactory.make_char_fatmulti22_lgmsl_pve_shadow_priest(),
                CharacterFactory.make_char_fatmulti23_lgsmm_pve_elemental_shaman(),
                CharacterFactory.make_char_fatmulti24_lgsmn_pve_elemental_shaman(),
                CharacterFactory.make_char_fatmulti25_lgsmo_pve_elemental_shaman(),
                CharacterFactory.make_char_fatmulti26_lgsmp_pve_elemental_shaman(),
            ]
        )
        config.active_character_config.set_leader1_window_index(1)
        config.active_character_config.set_leader2_window_index(10)


