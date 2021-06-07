# -*- coding: utf-8 -*-

from ... import act
from ...config import Config, ActiveCharacterConfig
from ...constant.windows import window_index
from ...constant.characters import CharacterFactory
from ...constant.talent_category_association import T, TC
from .....script import Script, SendLabel
from . import post_hooks


class Mode:
    @classmethod
    def set_mode_solo_dungeon_batlefury_quentin_opiitou_swagsonic_kangliu(cls, config: Config):
        config.game_client_config.use_1600_900_resolution()
        # config.game_client_config.use_1176_664_resolution()
        config.game_client_config.use_n_windows(22)
        config.game_client_config.use_credential_list_default()
        config.toggle_window_config.key1_to_25_window_index = list(range(1, 22 + 1))
        config.toggle_window_config.round_robin_window_index = list(range(1, 5 + 1))
        config.active_character_config = ActiveCharacterConfig(
            active_characters=[
                CharacterFactory.make_char_fatmulti1_batlefury_pve_protect_pala().evolve(is_tank1=True,
                                                                                         is_dr_pala1=True),
                CharacterFactory.make_char_fatmulti2_quentin_pve_elemental_shaman().evolve(),
                CharacterFactory.make_char_fatmulti3_opiitou_pve_balance_druid().evolve(),
                CharacterFactory.make_char_fatmulti4_swagsonic_pve_arcane_mage().evolve(),
                CharacterFactory.make_char_fatmulti5_kangliu_pve_shadow_priest().evolve(),
            ]
        )
        config.active_character_config.set_leader1_window_index(1)
        config.active_character_config.set_leader2_window_index(1)

    @classmethod
    def set_mode_solo_dungeon_batlefury_litgugu_abcd(cls, config: Config):
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
                CharacterFactory.make_char_fatmulti11_litgugua_pve_balance_druid().evolve(),
                CharacterFactory.make_char_fatmulti12_litgugub_pve_balance_druid().evolve(),
                CharacterFactory.make_char_fatmulti13_litguguc_pve_balance_druid().evolve(),
                CharacterFactory.make_char_fatmulti14_litgugud_pvp_resto_druid().evolve(),
            ]
        )
        config.active_character_config.set_leader1_window_index(1)
        config.active_character_config.set_leader2_window_index(1)
        config.post_hook = [
            post_hooks.boomkin_round_robin_starfall
        ]

    @classmethod
    def set_mode_solo_dungeon_litgoatdk_abcd_bunnysisters(cls, config: Config):
        config.game_client_config.use_1600_900_resolution()
        config.game_client_config.use_n_windows(22)
        config.game_client_config.use_credential_list_default()
        config.toggle_window_config.key1_to_25_window_index = list(range(1, 22 + 1))
        config.toggle_window_config.round_robin_window_index = list(range(1, 22 + 1))
        config.active_character_config = ActiveCharacterConfig(
            active_characters=[
                CharacterFactory.make_char_fatmulti1_litgoatdka_pve_blood_dk().evolve(),
                CharacterFactory.make_char_fatmulti2_litgoatdkb_pve_unholy_dk().evolve(),
                CharacterFactory.make_char_fatmulti3_litgoatdkc_pve_unholy_dk().evolve(),
                CharacterFactory.make_char_fatmulti4_litgoatdkd_pve_unholy_dk().evolve(),
                CharacterFactory.make_char_fatmulti8_bunnysisters_pve_resto_druid().evolve(),
            ]
        )
        config.active_character_config.set_leader1_window_index(1)
        config.active_character_config.set_leader2_window_index(1)
        config.post_hook = post_hooks.litgoatdk_abcde_team_death_grip

    @classmethod
    def set_mode_solo_dungeon_litgoatdk_abcd_glowyy(cls, config: Config):
        config.game_client_config.use_1600_900_resolution()
        config.game_client_config.use_n_windows(22)
        config.game_client_config.use_credential_list_default()
        config.toggle_window_config.key1_to_25_window_index = list(range(1, 22 + 1))
        config.toggle_window_config.round_robin_window_index = list(range(1, 22 + 1))
        config.active_character_config = ActiveCharacterConfig(
            active_characters=[
                CharacterFactory.make_char_fatmulti1_litgoatdka_pve_blood_dk().evolve(),
                CharacterFactory.make_char_fatmulti2_litgoatdkb_pve_unholy_dk().evolve(),
                CharacterFactory.make_char_fatmulti3_litgoatdkc_pve_unholy_dk().evolve(),
                CharacterFactory.make_char_fatmulti4_litgoatdkd_pve_unholy_dk().evolve(),
                CharacterFactory.make_char_fatmulti9_glowyy_pve_holy_pala().evolve(),
            ]
        )
        config.active_character_config.set_leader1_window_index(1)
        config.active_character_config.set_leader2_window_index(1)

    @classmethod
    def set_mode_solo_dungeon_glowyy_and_litgugu_abcd(cls, config: Config):
        config.game_client_config.use_1600_900_resolution()
        config.game_client_config.use_n_windows(22)
        config.game_client_config.use_credential_list_default()
        config.toggle_window_config.key1_to_25_window_index = list(range(1, 22 + 1))
        config.toggle_window_config.round_robin_window_index = list(range(1, 22 + 1))
        config.active_character_config = ActiveCharacterConfig(
            active_characters=[
                CharacterFactory.make_char_fatmulti9_glowyy_pve_protect_pala().evolve(),
                CharacterFactory.make_char_fatmulti11_litgugua_pve_balance_druid().evolve(),
                CharacterFactory.make_char_fatmulti12_litgugub_pve_balance_druid().evolve(),
                CharacterFactory.make_char_fatmulti13_litguguc_pve_balance_druid().evolve(),
                CharacterFactory.make_char_fatmulti14_litgugud_pvp_resto_druid().evolve(),
            ]
        )
        config.active_character_config.set_leader1_window_index(9)
        config.active_character_config.set_leader2_window_index(9)
        config.post_hook = [
            post_hooks.boomkin_round_robin_starfall
        ]

    @classmethod
    def set_mode_solo_dungeon_batlefury_carry_4_priest(cls, config: Config):
        config.game_client_config.use_1600_900_resolution()
        config.game_client_config.use_n_windows(22)
        config.game_client_config.use_credential_list_default()
        config.toggle_window_config.key1_to_25_window_index = list(range(1, 22 + 1))
        config.toggle_window_config.round_robin_window_index = list(range(1, 22 + 1))
        config.active_character_config = ActiveCharacterConfig(
            active_characters=[
                CharacterFactory.make_char_fatmulti1_batlefury_pve_protect_pala().evolve(),
                CharacterFactory.make_char_fatmulti19_lgmsi_pve_shadow_priest().evolve(),
                CharacterFactory.make_char_fatmulti20_lgmsj_pve_shadow_priest().evolve(),
                # CharacterFactory.make_char_fatmulti21_lgmsk_pve_shadow_priest().evolve(),
                CharacterFactory.make_char_fatmulti21_lgmsk_pve_holy_priest().evolve(),
                # CharacterFactory.make_char_fatmulti22_lgmsl_pve_shadow_priest().evolve(),
                CharacterFactory.make_char_fatmulti22_lgmsl_pve_holy_priest().evolve(),
            ]
        )
        config.active_character_config.set_leader1_window_index(1)
        config.active_character_config.set_leader2_window_index(15) # priest
        # config.active_character_config.set_leader2_window_index(19) # shaman

        config.post_hook = post_hooks.lgms_ijkl_shadow_priest_group


    @classmethod
    def set_mode_solo_dungeon_batlefury_carry_4_shaman(cls, config: Config):
        config.game_client_config.use_1600_900_resolution()
        config.game_client_config.use_n_windows(22)
        config.game_client_config.use_credential_list_default()
        config.toggle_window_config.key1_to_25_window_index = list(range(1, 22 + 1))
        config.toggle_window_config.round_robin_window_index = list(range(1, 22 + 1))
        config.active_character_config = ActiveCharacterConfig(
            active_characters=[
                CharacterFactory.make_char_fatmulti1_batlefury_pve_protect_pala().evolve(),

                CharacterFactory.make_char_fatmulti23_lgsmm_pve_elemental_shaman().evolve(),
                # CharacterFactory.make_char_fatmulti23_lgsmm_pve_resto_shaman().evolve(),

                CharacterFactory.make_char_fatmulti24_lgsmn_pve_elemental_shaman().evolve(),
                # CharacterFactory.make_char_fatmulti24_lgsmn_pve_resto_shaman().evolve(),

                CharacterFactory.make_char_fatmulti25_lgsmo_pve_elemental_shaman().evolve(),
                # CharacterFactory.make_char_fatmulti25_lgsmo_pve_resto_shaman().evolve(),

                # CharacterFactory.make_char_fatmulti26_lgsmp_pve_elemental_shaman().evolve(),
                CharacterFactory.make_char_fatmulti26_lgsmp_pve_resto_shaman().evolve(),
            ]
        )
        config.active_character_config.set_leader1_window_index(1)
        # config.active_character_config.set_leader2_window_index(15) # priest
        config.active_character_config.set_leader2_window_index(19) # shaman

        def post_hook(config: 'Config', script: Script):
            from ..hk_g07_skills import hk_g

            hk_g.actions = [
                SendLabel(
                    name=TC.paladin_protect.name,
                    to=config.lbs_by_tc(tc=TC.paladin_protect),
                    actions=[
                        act.General.TRIGGER
                    ]
                )
            ]

            if len(list(config.active_character_config.iter_by_talent_category(tc=TC.priest_healer))):
                hk_g.actions.append(
                    SendLabel(
                        name=TC.priest_healer.name,
                        to=config.lbs_by_tc(tc=TC.priest_healer)[:1],
                        actions=[
                            act.Target.TARGET_FOCUS,
                            act.Priest.HOLY_SPEC_PRAYER_OF_MENDING_KEY_1,
                        ]
                    )
                )

            if len(list(config.active_character_config.iter_by_talent_category(tc=TC.shaman_resto))):
                hk_g.actions.append(
                    SendLabel(
                        name=TC.shaman_resto.name,
                        to=config.lbs_by_tc(tc=TC.shaman_resto)[:1],
                        actions=[
                            act.Target.TARGET_FOCUS,
                            act.Shaman.RESTO_SPEC_EARTH_SHIELD,
                        ]
                    )
                )

        config.post_hook = post_hook

    @classmethod
    def set_mode_solo_dungeon_ganjj_2_priest_2_shaman_team1(cls, config: Config):
        config.game_client_config.use_1600_900_resolution()
        config.game_client_config.use_n_windows(22)
        config.game_client_config.use_credential_list_default()
        config.toggle_window_config.key1_to_25_window_index = list(range(1, 22 + 1))
        config.toggle_window_config.round_robin_window_index = list(range(1, 22 + 1))
        config.active_character_config = ActiveCharacterConfig(
            active_characters=[
                CharacterFactory.make_char_makun7551_ganjj_pve_blood_tank_dk().evolve(is_tank1=True),

                CharacterFactory.make_char_fatmulti19_lgmsi_pve_shadow_priest().evolve(),
                CharacterFactory.make_char_fatmulti20_lgmsj_pve_shadow_priest().evolve(),
                # CharacterFactory.make_char_fatmulti21_lgmsk_pve_shadow_priest().evolve(),
                # CharacterFactory.make_char_fatmulti22_lgmsl_pve_shadow_priest().evolve(),

                CharacterFactory.make_char_fatmulti23_lgsmm_pve_elemental_shaman().evolve(),
                CharacterFactory.make_char_fatmulti24_lgsmn_pve_resto_shaman().evolve(),
                # CharacterFactory.make_char_fatmulti25_lgsmo_pve_elemental_shaman().evolve(),
                # CharacterFactory.make_char_fatmulti26_lgsmp_pve_resto_shaman().evolve(),
            ]
        )
        config.active_character_config.set_leader1_window_index(10)
        config.active_character_config.set_leader2_window_index(10)

        config.post_hook = [
            # post_hooks.lgms_ijkl_shadow_priest_group
            post_hooks.resto_shaman_earth_shield,
        ]

    @classmethod
    def set_mode_solo_dungeon_laoshou_2_priest_2_shaman_team2(cls, config: Config):
        config.game_client_config.use_1600_900_resolution()
        config.game_client_config.use_n_windows(22)
        config.game_client_config.use_credential_list_default()
        config.toggle_window_config.key1_to_25_window_index = list(range(1, 22 + 1))
        config.toggle_window_config.round_robin_window_index = list(range(1, 22 + 1))
        config.active_character_config = ActiveCharacterConfig(
            active_characters=[
                CharacterFactory.make_char_makun7551_laoshou_protect_paladin().evolve(is_tank1=True),
                # CharacterFactory.make_char_fatmulti19_lgmsi_pve_shadow_priest().evolve(),
                # CharacterFactory.make_char_fatmulti20_lgmsj_pve_shadow_priest().evolve(),
                CharacterFactory.make_char_fatmulti21_lgmsk_pve_shadow_priest().evolve(),
                CharacterFactory.make_char_fatmulti22_lgmsl_pve_shadow_priest().evolve(),

                # CharacterFactory.make_char_fatmulti23_lgsmm_pve_elemental_shaman().evolve(),
                # CharacterFactory.make_char_fatmulti24_lgsmn_pve_resto_shaman().evolve(),
                CharacterFactory.make_char_fatmulti25_lgsmo_pve_elemental_shaman().evolve(),
                CharacterFactory.make_char_fatmulti26_lgsmp_pve_resto_shaman().evolve(),
            ]
        )
        config.active_character_config.set_leader1_window_index(10)
        config.active_character_config.set_leader2_window_index(10)

        config.post_hook = [
            post_hooks.lgms_ijkl_shadow_priest_group,
            post_hooks.resto_shaman_earth_shield,
        ]
