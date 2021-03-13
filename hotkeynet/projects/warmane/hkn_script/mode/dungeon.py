# -*- coding: utf-8 -*-

from ...config import Config, ActiveCharacterConfig
from ...constant.characters import CharacterFactory
from .....script import Script


class Mode:
    @classmethod
    def set_mode_solo_dungeon_batlefury_quentin_opiitou_swagsonic_kangliu(cls, config: Config):
        # config.game_client_config.use_1600_900_resolution()
        config.game_client_config.use_1176_664_resolution()
        config.game_client_config.use_n_windows(5)
        config.toggle_window_config.key1_to_25_window_index = list(range(1, 5+1))
        config.toggle_window_config.round_robin_window_index = list(range(1, 5+1))
        config.active_character_config = ActiveCharacterConfig(
            active_characters=[
                CharacterFactory.make_char_fatmulti1_batlefury_pve_protect_pala().evolve(is_tank1=True, is_dr_pala1=True),
                CharacterFactory.make_char_fatmulti2_quentin_pve_elemental_shaman().evolve(),
                CharacterFactory.make_char_fatmulti3_opiitou_pve_balance_druid().evolve(),
                CharacterFactory.make_char_fatmulti4_swagsonic_pve_arcane_mage().evolve(),
                CharacterFactory.make_char_fatmulti5_kangliu_pve_shadow_priest().evolve(),
            ]
        )
        config.active_character_config.set_leader1_window_index(1)
        config.active_character_config.set_leader2_window_index(1)
