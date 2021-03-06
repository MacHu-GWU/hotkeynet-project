# -*- coding: utf-8 -*-

from ...config import Config, ActiveCharacterConfig
from ...constant.characters import CharacterFactory
from . import post_hooks


class Mode:

    #--- 没有明确的地点, 仅仅是5个一组一起做任务 ---
    @classmethod
    def set_mode_questing_5_ppl_batlefury_team(cls, config: Config):
        """
        Batlefury + Quentin + Opiitou + Swagsonic + Kangliu 黄金五人组
        """
        config.game_client_config.use_1600_900_resolution()
        config.game_client_config.use_n_windows(22)
        config.game_client_config.use_credential_list_default()
        config.toggle_window_config.key1_to_25_window_index = list(range(1, 22 + 1))
        config.toggle_window_config.round_robin_window_index = list(range(1, 22 + 1))
        config.active_character_config = ActiveCharacterConfig(
            active_characters=[
                # CharacterFactory.make_char_().evolve(), # 同时多开一个打团队副本
                CharacterFactory.make_char_fatmulti1_batlefury_pve_retri_pala().evolve(),
                CharacterFactory.make_char_fatmulti2_quentin_pve_elemental_shaman().evolve(),
                CharacterFactory.make_char_fatmulti3_opiitou_pve_balance_druid().evolve(),
                CharacterFactory.make_char_fatmulti4_swagsonic_pve_arcane_mage().evolve(),
                CharacterFactory.make_char_fatmulti5_kangliu_pve_shadow_priest().evolve(),
            ]
        )
        config.active_character_config.set_leader1_window_index(1)

    @classmethod
    def set_mode_questing_5_ppl_litgoat_warlock_team(cls, config: Config):
        """
        5 个 术士 一起做小队任务.
        """
        config.game_client_config.use_1600_900_resolution()
        config.game_client_config.use_n_windows(22)
        config.game_client_config.use_credential_list_default()
        config.toggle_window_config.key1_to_25_window_index = list(range(1, 22 + 1))
        config.toggle_window_config.round_robin_window_index = list(range(1, 22 + 1))
        config.active_character_config = ActiveCharacterConfig(
            active_characters=[
                # CharacterFactory.make_char_().evolve(), # 同时多开一个打团队副本
                CharacterFactory.make_char_fatmulti1_litgoatssa_pve_demo_warlock().evolve(),
                CharacterFactory.make_char_fatmulti2_litgoatssb_pve_demo_warlock().evolve(),
                CharacterFactory.make_char_fatmulti3_litgoatssc_pve_demo_warlock().evolve(),
                CharacterFactory.make_char_fatmulti4_litgoatssd_pve_demo_warlock().evolve(),
                CharacterFactory.make_char_fatmulti5_litgoatsse_pve_demo_warlock().evolve(),
            ]
        )
        config.active_character_config.set_leader1_window_index(1)

    @classmethod
    def set_mode_questing_5_ppl_litgoat_dk_team(cls, config: Config):
        """
        5 个 DK 一起做小队任务.
        """
        config.game_client_config.use_1600_900_resolution()
        config.game_client_config.use_n_windows(22)
        config.game_client_config.use_credential_list_default()
        config.toggle_window_config.key1_to_25_window_index = list(range(1, 22 + 1))
        config.toggle_window_config.round_robin_window_index = list(range(1, 22 + 1))
        config.active_character_config = ActiveCharacterConfig(
            active_characters=[
                # CharacterFactory.make_char_().evolve(), # 同时多开一个打团队副本
                CharacterFactory.make_char_fatmulti1_litgoatdka_pvp_frost_dk().evolve(),
                CharacterFactory.make_char_fatmulti2_litgoatdkb_pvp_frost_dk().evolve(),
                CharacterFactory.make_char_fatmulti3_litgoatdkc_pvp_frost_dk().evolve(),
                CharacterFactory.make_char_fatmulti4_litgoatdkd_pvp_frost_dk().evolve(),
                CharacterFactory.make_char_fatmulti5_litgoatdke_pvp_frost_dk().evolve(),
            ]
        )
        config.active_character_config.set_leader1_window_index(1)

        config.post_hook = post_hooks.litgoatdk_abcde_team_death_grip

    @classmethod
    def set_mode_questing_5_ppl_litgugu_abcd_bunnysisters_druid_team(cls, config: Config):
        config.game_client_config.use_1600_900_resolution()
        config.game_client_config.use_n_windows(22)
        config.game_client_config.use_credential_list_default()
        config.toggle_window_config.key1_to_25_window_index = list(range(1, 22 + 1))
        config.toggle_window_config.round_robin_window_index = list(range(1, 22 + 1))
        config.active_character_config = ActiveCharacterConfig(
            active_characters=[
                CharacterFactory.make_char_fatmulti8_bunnysisters_pve_resto_druid().evolve(),

                CharacterFactory.make_char_fatmulti11_litgugua_pve_balance_druid().evolve(),
                CharacterFactory.make_char_fatmulti12_litgugub_pve_balance_druid().evolve(),
                CharacterFactory.make_char_fatmulti13_litguguc_pve_balance_druid().evolve(),
                CharacterFactory.make_char_fatmulti14_litgugud_pve_balance_druid().evolve(),
            ]
        )
        config.active_character_config.set_leader1_window_index(ind=11)
        config.active_character_config.set_leader2_window_index(ind=11)
        config.post_hook = [
            post_hooks.boomkin_round_robin_starfall,
            post_hooks.druid_all_stealth,
        ]

    @classmethod
    def set_mode_questing_5_ppl_litgugu_efgh_luxiaofeng_druid_team(cls, config: Config):
        config.game_client_config.use_1600_900_resolution()
        config.game_client_config.use_n_windows(22)
        config.game_client_config.use_credential_list_default()
        config.toggle_window_config.key1_to_25_window_index = list(range(1, 22 + 1))
        config.toggle_window_config.round_robin_window_index = list(range(1, 22 + 1))
        config.active_character_config = ActiveCharacterConfig(
            active_characters=[
                CharacterFactory.make_char_fatmulti10_luxiaofeng_pve_blood_tank_dk().evolve(),

                CharacterFactory.make_char_fatmulti15_litgugue_pvp_balance_druid().evolve(),
                CharacterFactory.make_char_fatmulti16_litguguf_pvp_balance_druid().evolve(),
                CharacterFactory.make_char_fatmulti17_litgugug_pvp_balance_druid().evolve(),
                CharacterFactory.make_char_fatmulti18_litguguh_pvp_resto_druid().evolve(),
            ]
        )
        config.active_character_config.set_leader1_window_index(ind=10)
        config.active_character_config.set_leader2_window_index(ind=11)
        config.post_hook = [
            post_hooks.boomkin_round_robin_starfall
        ]

    @classmethod
    def set_mode_questing_5_ppl_lgms_priest_ganjj_team(cls, config: Config):
        config.game_client_config.use_1600_900_resolution()
        config.game_client_config.use_n_windows(22)
        config.game_client_config.use_credential_list_default()
        config.toggle_window_config.key1_to_25_window_index = list(range(1, 22 + 1))
        config.toggle_window_config.round_robin_window_index = list(range(1, 22 + 1))
        config.active_character_config = ActiveCharacterConfig(
            active_characters=[
                CharacterFactory.make_char_makun7551_ganjj_pve_blood_tank_dk().evolve(),
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
    def set_mode_questing_5_ppl_lgsm_shaman_laoshou_team(cls, config: Config):
        config.game_client_config.use_1600_900_resolution()
        config.game_client_config.use_n_windows(22)
        config.game_client_config.use_credential_list_default()
        config.toggle_window_config.key1_to_25_window_index = list(range(1, 22 + 1))
        config.toggle_window_config.round_robin_window_index = list(range(1, 22 + 1))
        config.active_character_config = ActiveCharacterConfig(
            active_characters=[
                CharacterFactory.make_char_makun7551_laoshou_protect_paladin().evolve(),
                CharacterFactory.make_char_fatmulti23_lgsmm_pve_elemental_shaman().evolve(),
                CharacterFactory.make_char_fatmulti24_lgsmn_pve_elemental_shaman().evolve(),
                CharacterFactory.make_char_fatmulti25_lgsmo_pve_elemental_shaman().evolve(),
                CharacterFactory.make_char_fatmulti26_lgsmp_pve_elemental_shaman().evolve(),
            ]
        )
        config.active_character_config.set_leader1_window_index(ind=10)
        config.active_character_config.set_leader2_window_index(ind=19)


    @classmethod
    def set_mode_questing_grizzly_hill_daily_gold_farm_team0_fatmulti_1_to_5(cls, config: Config):
        config.game_client_config.use_1600_900_resolution()
        config.game_client_config.use_n_windows(22)
        config.game_client_config.use_credential_list_default()
        config.toggle_window_config.key1_to_25_window_index = list(range(1, 22 + 1))
        config.toggle_window_config.round_robin_window_index = list(range(1, 22 + 1))
        config.active_character_config = ActiveCharacterConfig(
            active_characters=[
                # CharacterFactory.make_char_fatmulti9_glowyy_pve_protect_pala().evolve(),

                CharacterFactory.make_char_fatmulti1_batlefury_pve_retri_pala().evolve(),
                CharacterFactory.make_char_fatmulti2_quentin_pve_elemental_shaman().evolve(),
                CharacterFactory.make_char_fatmulti3_opiitou_pve_balance_druid().evolve(),
                CharacterFactory.make_char_fatmulti4_swagsonic_pve_arcane_mage().evolve(),
                CharacterFactory.make_char_fatmulti5_kangliu_pve_shadow_priest().evolve(),

                # CharacterFactory.make_char_fatmulti1_litgoatssa_pve_demo_warlock().evolve(),
                # CharacterFactory.make_char_fatmulti2_litgoatssb_pve_demo_warlock().evolve(),
                # CharacterFactory.make_char_fatmulti3_litgoatssc_pve_demo_warlock().evolve(),
                # CharacterFactory.make_char_fatmulti4_litgoatssd_pve_demo_warlock().evolve(),
                # CharacterFactory.make_char_fatmulti5_litgoatsse_pve_demo_warlock().evolve(),
            ]
        )
        config.active_character_config.set_leader1_window_index(1)

    @classmethod
    def set_mode_questing_grizzly_hill_daily_gold_farm_team1_litgugu_druid(cls, config: Config):
        config.game_client_config.use_1600_900_resolution()
        config.game_client_config.use_n_windows(22)
        config.game_client_config.use_credential_list_default()
        config.toggle_window_config.key1_to_25_window_index = list(range(1, 22 + 1))
        config.active_character_config = ActiveCharacterConfig(
            active_characters=[
                CharacterFactory.make_char_fatmulti1_batlefury_pve_protect_pala().evolve(),
                CharacterFactory.make_char_fatmulti2_quentin_pve_elemental_shaman().evolve(leader1_window_index=1),
                CharacterFactory.make_char_fatmulti3_opiitou_pve_balance_druid().evolve(leader1_window_index=1),
                CharacterFactory.make_char_fatmulti4_swagsonic_pve_arcane_mage().evolve(leader1_window_index=1),
                CharacterFactory.make_char_fatmulti5_kangliu_pve_shadow_priest().evolve(leader1_window_index=1),

                CharacterFactory.make_char_fatmulti8_bunnysisters_pve_resto_druid().evolve(leader1_window_index=11),
                CharacterFactory.make_char_fatmulti11_litgugua_pve_balance_druid().evolve(),
                CharacterFactory.make_char_fatmulti12_litgugub_pve_balance_druid().evolve(leader1_window_index=11),
                CharacterFactory.make_char_fatmulti13_litguguc_pve_balance_druid().evolve(leader1_window_index=11),
                CharacterFactory.make_char_fatmulti14_litgugud_pvp_resto_druid().evolve(leader1_window_index=11),
            ]
        )
        config.toggle_window_config.round_robin_window_index = list(range(1, 22 + 1))

    @classmethod
    def set_mode_questing_grizzly_hill_daily_gold_farm_team2_litgoat_ss_and_ganjj_priest(cls, config: Config):
        config.game_client_config.use_1600_900_resolution()
        config.game_client_config.use_n_windows(22)
        config.game_client_config.use_credential_list_default()
        config.toggle_window_config.key1_to_25_window_index = list(range(1, 22 + 1))
        config.toggle_window_config.round_robin_window_index = list(range(1, 22 + 1))
        config.active_character_config = ActiveCharacterConfig(
            active_characters=[
                CharacterFactory.make_char_fatmulti1_litgoatssa_pve_demo_warlock().evolve(),
                CharacterFactory.make_char_fatmulti2_litgoatssb_pve_demo_warlock().evolve(leader1_window_index=1),
                CharacterFactory.make_char_fatmulti3_litgoatssc_pve_demo_warlock().evolve(leader1_window_index=1),
                CharacterFactory.make_char_fatmulti4_litgoatssd_pve_demo_warlock().evolve(leader1_window_index=1),
                CharacterFactory.make_char_fatmulti5_litgoatsse_pve_demo_warlock().evolve(leader1_window_index=1),

                CharacterFactory.make_char_makun7551_ganjj_pve_unholy_dps_dk().evolve(),
                CharacterFactory.make_char_fatmulti19_lgmsi_pve_shadow_priest().evolve(leader1_window_index=10),
                CharacterFactory.make_char_fatmulti20_lgmsj_pve_shadow_priest().evolve(leader1_window_index=10),
                CharacterFactory.make_char_fatmulti21_lgmsk_pve_shadow_priest().evolve(leader1_window_index=10),
                CharacterFactory.make_char_fatmulti22_lgmsl_pve_shadow_priest().evolve(leader1_window_index=10),
            ]
        )

    @classmethod
    def set_mode_questing_grizzly_hill_daily_gold_farm_team3_litgoat_dk_and_laoshou_shaman(cls, config: Config):
        config.game_client_config.use_1600_900_resolution()
        config.game_client_config.use_n_windows(22)
        config.game_client_config.use_credential_list_default()
        config.toggle_window_config.key1_to_25_window_index = list(range(1, 22 + 1))
        config.toggle_window_config.round_robin_window_index = list(range(1, 22 + 1))
        config.active_character_config = ActiveCharacterConfig(
            active_characters=[
                CharacterFactory.make_char_fatmulti1_litgoatdka_pvp_frost_dk().evolve(),
                CharacterFactory.make_char_fatmulti2_litgoatdkb_pvp_frost_dk().evolve(leader1_window_index=1),
                CharacterFactory.make_char_fatmulti3_litgoatdkc_pvp_frost_dk().evolve(leader1_window_index=1),
                CharacterFactory.make_char_fatmulti4_litgoatdkd_pvp_frost_dk().evolve(leader1_window_index=1),
                CharacterFactory.make_char_fatmulti5_litgoatdke_pvp_frost_dk().evolve(leader1_window_index=1),

                CharacterFactory.make_char_makun7551_laoshou_retri_paladin().evolve(),
                CharacterFactory.make_char_fatmulti23_lgsmm_pve_elemental_shaman().evolve(leader1_window_index=10),
                CharacterFactory.make_char_fatmulti24_lgsmn_pve_elemental_shaman().evolve(leader1_window_index=10),
                CharacterFactory.make_char_fatmulti25_lgsmo_pve_elemental_shaman().evolve(leader1_window_index=10),
                CharacterFactory.make_char_fatmulti26_lgsmp_pve_elemental_shaman().evolve(leader1_window_index=10),
            ]
        )