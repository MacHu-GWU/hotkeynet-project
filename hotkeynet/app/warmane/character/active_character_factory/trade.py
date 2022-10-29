# -*- coding: utf-8 -*-

from ordered_set import OrderedSet
from hotkeynet.game.wow.wlk import Character, char_oset_helper
from ..character_factory import char_fact


class ActiveCharactersFactory:
    @property
    def x22p_monthly_login_team_1(self) -> OrderedSet[Character]:
        """
        由于 Warmane 角色很久不登录的话, 名字就要被收回. 所以隔 1 - 2 个月就要登录一次.

        这是第 1 批次.
        """
        return char_oset_helper.set_team_leader_and_tank(chars=OrderedSet([
            (
                char_fact.fatmulti1_batlefury_pve_protect_pala
                    .set_is_leader_1().set_tank_1().set_dr_pala_1()
                    .set_is_leader_2().set_tank_2().set_dr_pala_2()
            ),
            char_fact.fatmulti2_quentin_pve_elemental_shaman,
            char_fact.fatmulti3_opiitou_pve_balance_druid,
            char_fact.fatmulti4_swagsonic_pve_arcane_mage,
            char_fact.fatmulti5_kangliu_pve_shadow_priest,
            char_fact.fitsheep_kindhearted_pve_demonology_warlock,
            char_fact.fatmulti6_kapacuk_pve_marksman_hunter,
            char_fact.fatmulti8_bunnysisters_pve_resto_druid,
            char_fact.fatmulti9_glowyy_pve_holy_pala,
            char_fact.fatmulti10_luxiaofeng_pve_unholy_tank_dk,
            char_fact.fatmulti11_litgugua_pve_balance_druid,
            char_fact.fatmulti16_litguguf_pvp_balance_druid,
            char_fact.fatmulti13_litguguc_pve_balance_druid,
            char_fact.fatmulti14_litgugud_pve_balance_druid,
            char_fact.fatmulti19_lgmsi_pve_shadow_priest,
            char_fact.fatmulti20_lgmsj_pve_shadow_priest,
            char_fact.fatmulti21_lgmsk_pve_shadow_priest,
            char_fact.fatmulti22_lgmsl_pve_shadow_priest,
            char_fact.fatmulti23_lgsmm_pve_elemental_shaman,
            char_fact.fatmulti24_lgsmn_pve_elemental_shaman,
            char_fact.fatmulti25_lgsmo_pve_elemental_shaman,
            char_fact.fatmulti26_lgsmp_pve_elemental_shaman,
        ]))

    @property
    def x22p_monthly_login_team_2(self) -> OrderedSet[Character]:
        """
        由于 Warmane 角色很久不登录的话, 名字就要被收回. 所以隔 1 - 2 个月就要登录一次.

        这是第 2 批次.
        """
        return char_oset_helper.set_team_leader_and_tank(chars=OrderedSet([
            (
                char_fact.makun7551_ganjj_pve_blood_tank_dk
                    .set_is_leader_1().set_tank_1().set_dr_pala_1()
                    .set_is_leader_2().set_tank_2().set_dr_pala_2()
            ),
            char_fact.fatmulti15_litgugue_pvp_balance_druid,
            char_fact.fatmulti16_litguguf_pvp_balance_druid,
            char_fact.fatmulti17_litgugug_pvp_balance_druid,
            char_fact.fatmulti18_litguguh_pvp_balance_druid,
        ]))

    @property
    def x5p_alchemy_transmute(self) -> OrderedSet[Character]:
        """
        """
        return char_oset_helper.set_team_leader_and_tank(chars=OrderedSet([
            (
                char_fact.fatmulti1_litgoatdka_pve_blood_dk
                    .set_is_leader_1().set_tank_1()
                    .set_is_leader_2().set_tank_2()
            ),
            char_fact.fatmulti2_litgoatdkb_pve_unholy_dk,
            char_fact.fatmulti3_litgoatdkc_pve_unholy_dk,
            char_fact.fatmulti4_litgoatdkd_pve_unholy_dk,
            char_fact.fatmulti5_litgoatdke_pve_unholy_dk,
            char_fact.fitsheep_bordercollie_pve_disco_priest,
        ]))


trade_active_char_fact = ActiveCharactersFactory()
