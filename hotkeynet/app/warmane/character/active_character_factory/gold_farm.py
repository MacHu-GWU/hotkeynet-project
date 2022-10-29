# -*- coding: utf-8 -*-

from ordered_set import OrderedSet
from hotkeynet.game.wow.wlk import Character, char_oset_helper
from ..character_factory import char_fact


class ActiveCharactersFactory:
    # === 灰熊丘陵日常刷金 ===
    @property
    def x5p_daily_team_1_druid(self) -> OrderedSet[Character]:
        """
        灰熊秋林日常刷金 - 防骑 + 3 鸟德 + 1 奶德
        """
        return char_oset_helper.set_team_leader_and_tank(chars=OrderedSet([
            char_fact.fatmulti9_glowyy_pve_protect_pala.set_is_leader_1().set_tank_1().set_dr_pala_1(),
            char_fact.fatmulti15_litgugue_pvp_balance_druid,
            char_fact.fatmulti16_litguguf_pvp_balance_druid,
            char_fact.fatmulti17_litgugug_pvp_balance_druid,
            char_fact.fatmulti18_litguguh_pvp_resto_druid,
        ]))

    @property
    def x5p_daily_team_2_druid(self) -> OrderedSet[Character]:
        """
        灰熊秋林日常刷金 - 4 鸟德 + 1 奶德
        """
        return char_oset_helper.set_team_leader_and_tank(chars=OrderedSet([
            char_fact.fatmulti8_bunnysisters_pve_balance_druid.set_is_leader_1(),
            char_fact.fatmulti11_litgugua_pve_balance_druid,
            char_fact.fatmulti12_litgugub_pve_balance_druid,
            char_fact.fatmulti13_litguguc_pve_balance_druid,
            char_fact.fatmulti14_litgugud_pvp_resto_druid,
        ]))

    @property
    def x5p_daily_team_3_dk(self) -> OrderedSet[Character]:
        """
        灰熊秋林日常刷金 - 5 DK
        """
        return char_oset_helper.set_team_leader_and_tank(chars=OrderedSet([
            char_fact.fatmulti1_litgoatdka_pvp_frost_dk.set_is_leader_1(),
            char_fact.fatmulti2_litgoatdkb_pvp_frost_dk,
            char_fact.fatmulti3_litgoatdkc_pvp_frost_dk,
            char_fact.fatmulti4_litgoatdkd_pvp_frost_dk,
            char_fact.fatmulti5_litgoatdke_pvp_frost_dk,
        ]))

    @property
    def x5p_daily_team_4_ss(self) -> OrderedSet[Character]:
        """
        灰熊秋林日常刷金 - 5 SS
        """
        return char_oset_helper.set_team_leader_and_tank(chars=OrderedSet([
            char_fact.fatmulti1_litgoatssa_pve_demo_warlock.set_is_leader_1(),
            char_fact.fatmulti2_litgoatssb_pve_demo_warlock,
            char_fact.fatmulti3_litgoatssc_pve_demo_warlock,
            char_fact.fatmulti4_litgoatssd_pve_demo_warlock,
            char_fact.fatmulti5_litgoatsse_pve_demo_warlock,
        ]))

    @property
    def x5p_daily_team_5_ms(self) -> OrderedSet[Character]:
        """
        灰熊秋林日常刷金 - DK + 4 暗牧
        """
        return char_oset_helper.set_team_leader_and_tank(chars=OrderedSet([
            char_fact.makun7551_ganjj_pve_unholy_dps_dk.set_is_leader_1(),
            char_fact.fatmulti19_lgmsi_pve_shadow_priest,
            char_fact.fatmulti20_lgmsj_pve_shadow_priest,
            char_fact.fatmulti21_lgmsk_pve_shadow_priest,
            char_fact.fatmulti22_lgmsl_pve_shadow_priest,
        ]))

    @property
    def x5p_daily_team_6_sm(self) -> OrderedSet[Character]:
        """
        灰熊秋林日常刷金 - DK + 4 萨满
        """
        return char_oset_helper.set_team_leader_and_tank(chars=OrderedSet([
            char_fact.makun7551_laoshou_retri_paladin.set_is_leader_1(),
            char_fact.fatmulti23_lgsmm_pve_elemental_shaman,
            char_fact.fatmulti24_lgsmn_pve_elemental_shaman,
            char_fact.fatmulti25_lgsmo_pve_elemental_shaman,
            char_fact.fatmulti26_lgsmp_pve_elemental_shaman,
        ]))

    @property
    def x5p_daily_team_7_batlefury(self) -> OrderedSet[Character]:
        """
        灰熊秋林日常刷金 - Batlefury 黄金组合
        """
        return char_oset_helper.set_team_leader_and_tank(chars=OrderedSet([
            char_fact.fatmulti1_batlefury_pve_retri_pala.set_is_leader_1(),
            char_fact.fatmulti2_quentin_pve_elemental_shaman,
            char_fact.fatmulti3_opiitou_pve_balance_druid,
            char_fact.fatmulti4_swagsonic_pve_arcane_mage,
            char_fact.fatmulti5_kangliu_pve_shadow_priest,
        ]))


gold_farm_active_char_fact = ActiveCharactersFactory()
