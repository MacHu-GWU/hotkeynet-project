# -*- coding: utf-8 -*-

from hotkeynet.projects.warmane.config import (
    Config, GameClientConfig, ActiveCharacterConfig,
)
from hotkeynet.projects.warmane.constant.characters import CharacterFactory
from hotkeynet.projects.warmane.constant.talent import Talent


class Mode:
    @classmethod
    def set_mode_solo_raid_10p_batlefury_flydps_core_team(cls, config: Config):
        config.game_client_config.use_1920_1080_resolution()
        config.game_client_config.use_n_windows(10)
        config.toggle_window_config.key1_to_25_window_index = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        config.toggle_window_config.round_robin_window_index = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        config.active_character_config = ActiveCharacterConfig(
            active_characters=[
                CharacterFactory.make_char_fatmulti1_batlefury_pve_protect_pala().evolve(window_index=1, is_tank1=True, is_dr_pala1=True),
                CharacterFactory.make_char_fatmulti2_quentin_pve_elemental_shaman().evolve(window_index=2),
                CharacterFactory.make_char_fatmulti3_opiitou_pve_balance_druid().evolve(window_index=3),
                CharacterFactory.make_char_fatmulti4_swagsonic_pve_arcane_mage().evolve(window_index=4),
                CharacterFactory.make_char_fatmulti5_kangliu_pve_shadow_priest().evolve(window_index=5),
                CharacterFactory.make_char_fitsheep_kindhearted_pve_demonology_warlock().evolve(window_index=6),
                CharacterFactory.make_char_fatmulti6_kapacuk_pve_marksman_hunter().evolve(window_index=7),
                CharacterFactory.make_char_fatmulti8_bunnysisters_pve_resto_druid().evolve(window_index=8),
                CharacterFactory.make_char_fatmulti9_glowyy_pve_holy_pala().evolve(window_index=9, is_dr_pala2=True),
                CharacterFactory.make_char_monkey130_flydps_pve_blood_tank_dk().evolve(window_index=10, is_tank2=True),
            ]
        )
        config.active_character_config.set_leader1_window_index(1)
        config.active_character_config.set_leader2_window_index(10)

    @classmethod
    def set_mode_questing_daily_gold_farm_(cls, config: Config):
        config.game_client_config.use_1920_1080_resolution()
        config.game_client_config.use_n_windows(10)