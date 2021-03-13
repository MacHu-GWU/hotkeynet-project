# -*- coding: utf-8 -*-

from ...config import Config, ActiveCharacterConfig
from ...constant.characters import CharacterFactory


class Mode:
    @classmethod
    def set_mode_questing_grizzly_hill_daily_gold_farm_team1(cls, config: Config):
        config.game_client_config.use_1600_900_resolution()
        config.game_client_config.use_n_windows(22)
        config.toggle_window_config.key1_to_25_window_index = list(range(1, 22 + 1))
        config.toggle_window_config.round_robin_window_index = list(range(1, 22 + 1))
        config.active_character_config = ActiveCharacterConfig(
            active_characters=[
                CharacterFactory.make_char_fatmulti1_litgoatssa_pve_demo_warlock().evolve(),
                CharacterFactory.make_char_fatmulti2_litgoatssb_pve_demo_warlock().evolve(leader1_window_index=1),
                CharacterFactory.make_char_fatmulti3_litgoatssc_pve_demo_warlock().evolve(leader1_window_index=1),
                CharacterFactory.make_char_fatmulti4_litgoatssd_pve_demo_warlock().evolve(leader1_window_index=1),
                CharacterFactory.make_char_fatmulti5_litgoatsse_pve_demo_warlock().evolve(leader1_window_index=1),

                CharacterFactory.make_char_fatmulti8_bunnysisters_pve_resto_druid().evolve(leader1_window_index=11),
                CharacterFactory.make_char_fatmulti11_litgugua_pve_balance_druid().evolve(),
                CharacterFactory.make_char_fatmulti12_litgugub_pve_balance_druid().evolve(leader1_window_index=11),
                CharacterFactory.make_char_fatmulti13_litguguc_pve_balance_druid().evolve(leader1_window_index=11),
                CharacterFactory.make_char_fatmulti14_litgugud_pve_resto_druid().evolve(leader1_window_index=11),

                CharacterFactory.make_char_fatmulti9_glowyy_pve_protect_pala().evolve(),
                CharacterFactory.make_char_fatmulti19_lgmsi_pve_shadow_priest().evolve(leader1_window_index=9),
                CharacterFactory.make_char_fatmulti20_lgmsj_pve_shadow_priest().evolve(leader1_window_index=9),
                CharacterFactory.make_char_fatmulti21_lgmsk_pve_shadow_priest().evolve(leader1_window_index=9),
                CharacterFactory.make_char_fatmulti22_lgmsl_pve_shadow_priest().evolve(leader1_window_index=9),

                CharacterFactory.make_char_makun7551_laoshou_retri_paladin().evolve(),
                CharacterFactory.make_char_fatmulti23_lgsmm_pve_elemental_shaman().evolve(leader1_window_index=10),
                CharacterFactory.make_char_fatmulti24_lgsmn_pve_elemental_shaman().evolve(leader1_window_index=10),
                CharacterFactory.make_char_fatmulti25_lgsmo_pve_elemental_shaman().evolve(leader1_window_index=10),
                CharacterFactory.make_char_fatmulti26_lgsmp_pve_elemental_shaman().evolve(leader1_window_index=10),
            ]
        )

    @classmethod
    def set_mode_questing_wintergraps(cls, config: Config):
        config.game_client_config.use_1600_900_resolution()
        config.game_client_config.use_n_windows(22)
        config.toggle_window_config.key1_to_25_window_index = list(range(1, 22 + 1))
        config.toggle_window_config.round_robin_window_index = list(range(1, 22 + 1))
        config.active_character_config = ActiveCharacterConfig(
            active_characters=[
                CharacterFactory.make_char_fatmulti1_litgoatssa_pve_demo_warlock().evolve(),
                CharacterFactory.make_char_fatmulti2_litgoatssb_pve_demo_warlock().evolve(),
                CharacterFactory.make_char_fatmulti3_litgoatssc_pve_demo_warlock().evolve(),
                CharacterFactory.make_char_fatmulti4_litgoatssd_pve_demo_warlock().evolve(),
                CharacterFactory.make_char_fatmulti5_litgoatsse_pve_demo_warlock().evolve(),

                CharacterFactory.make_char_fatmulti11_litgugua_pve_balance_druid().evolve(),
                CharacterFactory.make_char_fatmulti12_litgugub_pve_balance_druid().evolve(),
                CharacterFactory.make_char_fatmulti13_litguguc_pve_balance_druid().evolve(),
                CharacterFactory.make_char_fatmulti14_litgugud_pve_resto_druid().evolve(),

                CharacterFactory.make_char_fatmulti19_lgmsi_pve_shadow_priest().evolve(),
                CharacterFactory.make_char_fatmulti20_lgmsj_pve_shadow_priest().evolve(),
                CharacterFactory.make_char_fatmulti21_lgmsk_pve_shadow_priest().evolve(),
                CharacterFactory.make_char_fatmulti22_lgmsl_pve_shadow_priest().evolve(),

                CharacterFactory.make_char_makun7551_ganjj_pve_blood_tank_dk().evolve(),
                CharacterFactory.make_char_fatmulti23_lgsmm_pve_elemental_shaman().evolve(),
                CharacterFactory.make_char_fatmulti24_lgsmn_pve_elemental_shaman().evolve(),
                CharacterFactory.make_char_fatmulti25_lgsmo_pve_elemental_shaman().evolve(),
                CharacterFactory.make_char_fatmulti26_lgsmp_pve_elemental_shaman().evolve(),
            ]
        )
        config.active_character_config.set_leader1_window_index(1)
