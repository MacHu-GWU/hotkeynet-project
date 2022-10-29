# -*- coding: utf-8 -*-

from ordered_set import OrderedSet
from hotkeynet.game.wow.wlk import Character, char_oset_helper
from ..character_factory import char_fact


class ActiveCharactersFactory:
    # --------------------------------------------------------------------------
    # Icecrown
    # --------------------------------------------------------------------------
    def x5p_batlefury_quentin_opiitou_swagsonic_kangliu(self) -> OrderedSet[Character]:
        """
        主力 5 人组
        """
        return char_oset_helper.set_team_leader_and_tank(chars=OrderedSet([
            char_fact.fatmulti1_batlefury_pve_protect_pala.set_is_leader_1().set_tank_1().set_dr_pala_1(),
            char_fact.fatmulti2_quentin_pve_elemental_shaman,
            char_fact.fatmulti3_opiitou_pve_balance_druid,
            char_fact.fatmulti4_swagsonic_pve_arcane_mage,
            char_fact.fatmulti5_kangliu_pve_shadow_priest,
        ]))

    def x5p_flexible(self) -> OrderedSet[Character]:
        """
        该模式用于 1 个坦克 带着 3 个 DPS, 1 个治疗 打 5 人小副本.
        """
        return char_oset_helper.set_team_leader_and_tank(chars=OrderedSet([
            # =================================================================
            # === Tank 部分 ===
            # --- Paladin
            # char_fact.fatmulti1_batlefury_pve_retri_pala.set_is_leader_1(),
            char_fact.fatmulti1_batlefury_pve_protect_pala.set_is_leader_1().set_tank_1().set_dr_pala_1(),
            # char_fact.fatmulti9_glowyy_pve_protect_pala.set_is_leader_1().set_tank_1().set_dr_pala_1(),
            # char_fact.makun7551_laoshou_retri_paladin.set_is_leader_1(),

            # --- DK
            # char_fact.fatmulti10_luxiaofeng_pve_unholy_tank_dk.set_is_leader_1().set_tank_1(),
            # char_fact.fatmulti1_litgoatdka_pve_blood_dk.set_is_leader_1().set_tank_1(),
            # char_fact.makun7551_ganjj_pve_blood_tank_dk.set_is_leader_1().set_tank_1(),

            # --- Druid
            # char_fact.fatmulti3_opiitou_pve_bear_druid.set_is_leader_1().set_tank_1(),

            # === DPS 部分 ===
            char_fact.fatmulti11_litgugua_pve_balance_druid,
            char_fact.fatmulti12_litgugub_pve_balance_druid,
            char_fact.fatmulti13_litguguc_pve_balance_druid,

            # char_fact.fatmulti15_litgugue_pvp_balance_druid,
            # char_fact.fatmulti16_litguguf_pvp_balance_druid,
            # char_fact.fatmulti17_litgugug_pvp_balance_druid,

            # === 治疗部分 ===
            # char_fact.fatmulti8_bunnysisters_pve_resto_druid,

            char_fact.fatmulti14_litgugud_pvp_resto_druid,

            # char_fact.fatmulti18_litguguh_pvp_resto_druid,
        ]))

    # === 情人节 2 月中, 美酒节 9 月中, 万圣节 10 月中, 节日刷牌子 ===
    # 把 DK 5 人组 和 术士 5 人组 加上 Ganjj 和 Laoshou 分成 3 队 分别刷节日任务
    @property
    def x5p_festival_team_1_dk(self) -> OrderedSet[Character]:
        return char_oset_helper.set_team_leader_and_tank(chars=OrderedSet([
            char_fact.fatmulti1_litgoatdka_pve_blood_dk.set_leader_12_and_tank_12(),
            char_fact.fatmulti2_litgoatdkb_pve_unholy_dk,
            char_fact.fatmulti3_litgoatdkc_pve_unholy_dk,
            char_fact.fatmulti4_litgoatdkd_pve_unholy_dk,
            char_fact.fatmulti8_bunnysisters_pve_resto_druid,
        ]))

    @property
    def x5p_festival_team_2_ss(self) -> OrderedSet[Character]:
        return char_oset_helper.set_team_leader_and_tank(chars=OrderedSet([
            char_fact.fatmulti3_litgoatssc_pve_demo_warlock,
            char_fact.fatmulti4_litgoatssd_pve_demo_warlock,
            char_fact.fatmulti5_litgoatsse_pve_demo_warlock,
            char_fact.fatmulti1_batlefury_pve_protect_pala.set_leader_12_and_tank_12(),
            char_fact.fatmulti13_litguguc_pvp_resto_druid,
        ]))

    @property
    def x5p_festival_team_3_mix(self) -> OrderedSet[Character]:
        return char_oset_helper.set_team_leader_and_tank(chars=OrderedSet([
            char_fact.fatmulti1_litgoatssa_pve_demo_warlock,
            char_fact.fatmulti2_litgoatssb_pve_demo_warlock,
            char_fact.fatmulti5_litgoatdke_pve_unholy_dk,
            char_fact.fatmulti9_glowyy_pve_protect_pala.set_leader_12_and_tank_12(),
            char_fact.fatmulti14_litgugud_pvp_resto_druid,
        ]))

    # 把 牧师 4 人组 和 萨满 4 人组 加上 Ganjj 和 Laoshou 分成 2 队分别刷节日任务
    @property
    def x5p_festival_team_4_ms_sm(self) -> OrderedSet[Character]:
        return char_oset_helper.set_team_leader_and_tank(chars=OrderedSet([
            char_fact.makun7551_ganjj_pve_blood_tank_dk.set_leader_12_and_tank_12(),
            char_fact.fatmulti19_lgmsi_pve_shadow_priest,
            char_fact.fatmulti20_lgmsj_pve_shadow_priest,
            char_fact.fatmulti23_lgsmm_pve_elemental_shaman,
            char_fact.fatmulti24_lgsmn_pve_resto_shaman,
        ]))

    @property
    def x5p_festival_team_5_ms_sm(self) -> OrderedSet[Character]:
        return char_oset_helper.set_team_leader_and_tank(chars=OrderedSet([
            char_fact.makun7551_laoshou_protect_paladin.set_leader_12_and_tank_12(),
            char_fact.fatmulti21_lgmsk_pve_shadow_priest,
            char_fact.fatmulti22_lgmsl_pve_shadow_priest,
            char_fact.fatmulti25_lgsmo_pve_elemental_shaman,
            char_fact.fatmulti26_lgsmp_pve_resto_shaman,
        ]))

    @property
    def x5p_festival_team_6_litgugu_efgh(self) -> OrderedSet[Character]:
        return char_oset_helper.set_team_leader_and_tank(chars=OrderedSet([
            char_fact.fatmulti10_luxiaofeng_pve_blood_tank_dk.set_leader_12_and_tank_12(),
            char_fact.fatmulti15_litgugue_pvp_balance_druid,
            char_fact.fatmulti16_litguguf_pvp_balance_druid,
            char_fact.fatmulti17_litgugug_pvp_balance_druid,
            char_fact.fatmulti18_litguguh_pvp_resto_druid,
        ]))

    # --------------------------------------------------------------------------
    # Lordaeron
    # --------------------------------------------------------------------------
    @property
    def x5p_lgqs_abcde(self) -> OrderedSet[Character]:
        return char_oset_helper.set_team_leader_and_tank(chars=OrderedSet([
            (
                char_fact.fatmulti1_lgqsa_pve_protect_pala
                    .set_is_leader_1().set_tank_1().set_dr_pala_1()
                    .set_is_leader_2().set_tank_2().set_dr_pala_2()
            ),
            char_fact.fatmulti2_lgqsb_pve_retri_pala(),
            char_fact.fatmulti3_lgqsc_pve_retri_pala(),
            char_fact.fatmulti4_lgqsd_pve_retri_pala(),
            char_fact.fatmulti5_lgqse_pve_holy_pala(),
        ]))


dungeon_active_char_fact = ActiveCharactersFactory()
