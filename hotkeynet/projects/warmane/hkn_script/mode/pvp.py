# -*- coding: utf-8 -*-

from ...config import Config, ActiveCharacterConfig
from ...constant.characters import CharacterFactory
from .....script import Script, SendLabel
from ...constant.talent_category_association import TC
from ... import act
from . import post_hooks


def post_hook_druid(config: 'Config', script: Script):
    from .. import hk_g07_skills

    hk_g07_skills.hk_alt_f1.actions = [
        SendLabel(
            name=TC.druid.name,
            to=config.lbs_by_tc(tc=TC.druid),
            actions=[
                act.Druid.ALL_SPEC_CAT_STEALTH_MACRO,
            ]
        )
    ]



class Mode:
    @classmethod
    def set_mode_pvp_grizzly_hill(cls, config: Config):
        config.game_client_config.use_1600_900_resolution()
        config.game_client_config.use_n_windows(22)
        config.game_client_config.use_credential_list_default()
        config.toggle_window_config.key1_to_25_window_index = list(range(1, 22 + 1))
        config.active_character_config = ActiveCharacterConfig(
            active_characters=[
                # CharacterFactory.make_char_fatmulti1_litgoatdka_pvp_frost_dk().evolve(),
                # CharacterFactory.make_char_fatmulti2_litgoatdkb_pvp_frost_dk().evolve(),
                # CharacterFactory.make_char_fatmulti3_litgoatdkc_pvp_frost_dk().evolve(),
                # CharacterFactory.make_char_fatmulti4_litgoatdkd_pvp_frost_dk().evolve(),
                # CharacterFactory.make_char_fatmulti5_litgoatdke_pvp_frost_dk().evolve(),

                CharacterFactory.make_char_fatmulti8_bunnysisters_pve_resto_druid().evolve(),
                CharacterFactory.make_char_fatmulti11_litgugua_pve_balance_druid().evolve(),
                CharacterFactory.make_char_fatmulti12_litgugub_pve_balance_druid().evolve(),
                CharacterFactory.make_char_fatmulti13_litguguc_pve_balance_druid().evolve(),
                CharacterFactory.make_char_fatmulti14_litgugud_pve_balance_druid().evolve(),
            ]
        )
        config.toggle_window_config.round_robin_window_index = list(range(1, 22 + 1))
        config.active_character_config.set_leader1_window_index(11)

        config.post_hook = post_hook_druid

    @classmethod
    def set_mode_pvp_wintergraps_team1(cls, config: Config):
        config.game_client_config.use_1176_664_resolution()
        config.game_client_config.use_n_windows(22)
        config.game_client_config.use_credential_list_default()
        config.toggle_window_config.key1_to_25_window_index = list(range(1, 22 + 1))
        config.toggle_window_config.round_robin_window_index = list(range(1, 22 + 1))
        config.active_character_config = ActiveCharacterConfig(
            active_characters=[
                CharacterFactory.make_char_fatmulti1_litgoatdka_pvp_frost_dk().evolve(),
                CharacterFactory.make_char_fatmulti2_litgoatdkb_pvp_frost_dk().evolve(),
                CharacterFactory.make_char_fatmulti3_litgoatdkc_pvp_frost_dk().evolve(),
                CharacterFactory.make_char_fatmulti4_litgoatdkd_pvp_frost_dk().evolve(),
                CharacterFactory.make_char_fatmulti5_litgoatdke_pvp_frost_dk().evolve(),

                CharacterFactory.make_char_fatmulti11_litgugua_pve_balance_druid().evolve(),
                CharacterFactory.make_char_fatmulti12_litgugub_pve_balance_druid().evolve(),
                CharacterFactory.make_char_fatmulti13_litguguc_pve_balance_druid().evolve(),
                CharacterFactory.make_char_fatmulti14_litgugud_pvp_resto_druid().evolve(),

                CharacterFactory.make_char_fatmulti19_lgmsi_pve_shadow_priest().evolve(),
                CharacterFactory.make_char_fatmulti20_lgmsj_pve_shadow_priest().evolve(),
                CharacterFactory.make_char_fatmulti21_lgmsk_pve_shadow_priest().evolve(),
                CharacterFactory.make_char_fatmulti22_lgmsl_pve_shadow_priest().evolve(),

                CharacterFactory.make_char_fitsheep_kindhearted_pvp_destruction_warlock().evolve(),
                CharacterFactory.make_char_fatmulti8_bunnysisters_pve_resto_druid().evolve(),
                CharacterFactory.make_char_fatmulti9_glowyy_pve_holy_pala().evolve(),
                CharacterFactory.make_char_makun7551_laoshou_retri_paladin().evolve(),

                CharacterFactory.make_char_fatmulti23_lgsmm_pve_elemental_shaman().evolve(),
                CharacterFactory.make_char_fatmulti24_lgsmn_pve_elemental_shaman().evolve(),
                CharacterFactory.make_char_fatmulti25_lgsmo_pve_elemental_shaman().evolve(),
                CharacterFactory.make_char_fatmulti26_lgsmp_pve_elemental_shaman().evolve(),
            ]
        )
        config.active_character_config.set_leader1_window_index(1)
        config.active_character_config.set_leader2_window_index(6)

        def post_hook(config: 'Config', script: Script):
            print("set_mode_questing_wintergraps_team1")

            from .. import hk_g07_skills

            hk_g07_skills.hk_g.actions = [
                SendLabel(
                    name=TC.dk.name,
                    to=config.lbs_by_tc(tc=TC.dk),
                    actions=[
                        act.Target.TARGET_FOCUS_TARGET,
                        act.DK.ALL_SPEC_DEATH_GRIP_KEY_G,
                    ]
                )
            ]

        config.post_hook = post_hook

    @classmethod
    def set_mode_pvp_wintergrasp_wg_5_ppl_lgms_priest_ganjj_team(cls, config: Config):
        config.game_client_config.use_1600_900_resolution()
        config.game_client_config.use_n_windows(22)
        config.game_client_config.use_credential_list_default()
        config.toggle_window_config.key1_to_25_window_index = list(range(1, 22 + 1))
        config.toggle_window_config.round_robin_window_index = list(range(1, 22 + 1))
        config.active_character_config = ActiveCharacterConfig(
            active_characters=[
                CharacterFactory.make_char_makun7551_ganjj_pve_unholy_dps_dk().evolve(),
                CharacterFactory.make_char_fatmulti19_lgmsi_pve_shadow_priest().evolve(),
                CharacterFactory.make_char_fatmulti20_lgmsj_pve_shadow_priest().evolve(),
                CharacterFactory.make_char_fatmulti21_lgmsk_pve_shadow_priest().evolve(),
                CharacterFactory.make_char_fatmulti22_lgmsl_pve_shadow_priest().evolve(),
            ]
        )
        config.active_character_config.set_leader1_window_index(ind=10)
        config.active_character_config.set_leader2_window_index(ind=15)

        config.post_hook = [
            post_hooks.litgoatdk_abcde_team_death_grip,
            post_hooks.lgms_ijkl_shadow_priest_group,
        ]

    @classmethod
    def set_mode_pvp_wintergrasp_wg_5_ppl_lgsm_shaman_laoshou_team(cls, config: Config):
        config.game_client_config.use_1600_900_resolution()
        config.game_client_config.use_n_windows(22)
        config.game_client_config.use_credential_list_default()
        config.toggle_window_config.key1_to_25_window_index = list(range(1, 22 + 1))
        config.toggle_window_config.round_robin_window_index = list(range(1, 22 + 1))
        config.active_character_config = ActiveCharacterConfig(
            active_characters=[
                CharacterFactory.make_char_makun7551_laoshou_protect_paladin().evolve(),
                # CharacterFactory.make_char_makun7551_ganjj_pve_blood_tank_dk().evolve(),
                CharacterFactory.make_char_fatmulti23_lgsmm_pve_elemental_shaman().evolve(),
                CharacterFactory.make_char_fatmulti24_lgsmn_pve_elemental_shaman().evolve(),
                CharacterFactory.make_char_fatmulti25_lgsmo_pve_elemental_shaman().evolve(),
                CharacterFactory.make_char_fatmulti26_lgsmp_pve_elemental_shaman().evolve(),
            ]
        )
        config.active_character_config.set_leader1_window_index(ind=10)
        config.active_character_config.set_leader2_window_index(ind=19)
