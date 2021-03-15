# -*- coding: utf-8 -*-

from ...config import Config, ActiveCharacterConfig
from ...constant.characters import CharacterFactory


class Mode:
    @classmethod
    def set_mode_leveling_two_team_carry_in_dungeon(cls, config: Config):
        """
        Batlefury Retri paladin + 4 alts
        Opiitou Bear druid + 4 alts
        """
        config.game_client_config.use_1600_900_resolution()
        config.game_client_config.use_n_windows(22)
        config.toggle_window_config.key1_to_25_window_index = [
            1, 15, 16, 17, 18,
            3, 19, 20, 21, 22,
        ]
        config.toggle_window_config.round_robin_window_index = list(range(1, 22 + 1))
        config.active_character_config = ActiveCharacterConfig(
            active_characters=[
                # team 1
                CharacterFactory.make_char_fatmulti1_batlefury_pve_retri_pala().evolve(),
                CharacterFactory.make_char_fatmulti19_lgmsi_pve_shadow_priest().evolve(leader1_window_index=1),
                CharacterFactory.make_char_fatmulti20_lgmsj_pve_shadow_priest().evolve(leader1_window_index=1),
                CharacterFactory.make_char_fatmulti21_lgmsk_pve_shadow_priest().evolve(leader1_window_index=1),
                CharacterFactory.make_char_fatmulti22_lgmsl_pve_shadow_priest().evolve(leader1_window_index=1),

                # team 2
                CharacterFactory.make_char_fatmulti3_opiitou_pve_bear_druid().evolve(),
                CharacterFactory.make_char_fatmulti23_lgsmm_pve_elemental_shaman().evolve(leader1_window_index=3),
                CharacterFactory.make_char_fatmulti24_lgsmn_pve_elemental_shaman().evolve(leader1_window_index=3),
                CharacterFactory.make_char_fatmulti25_lgsmo_pve_elemental_shaman().evolve(leader1_window_index=3),
                CharacterFactory.make_char_fatmulti26_lgsmp_pve_elemental_shaman().evolve(leader1_window_index=3),
            ]
        )
        config.active_character_config.set_leader1_window_index(1)
