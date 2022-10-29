# -*- coding: utf-8 -*-

from ordered_set import OrderedSet
from hotkeynet.game.wow.wlk import Character, char_oset_helper
from ..character_factory import char_fact


class ActiveCharactersFactory:
    @property
    def x10p_batlefury_luxiaofeng_core_team(self) -> OrderedSet[Character]:
        """
        主力 10 人组
        """
        return char_oset_helper.set_team_leader_and_tank(chars=OrderedSet([
            char_fact.fatmulti1_batlefury_pve_protect_pala.set_is_leader_1().set_tank_1().set_dr_pala_1(),
            char_fact.fatmulti2_quentin_pve_elemental_shaman,
            char_fact.fatmulti3_opiitou_pve_balance_druid,
            char_fact.fatmulti4_swagsonic_pve_arcane_mage,
            char_fact.fatmulti5_kangliu_pve_shadow_priest,
            char_fact.fitsheep_kindhearted_pve_demonology_warlock,
            char_fact.fatmulti6_kapacuk_pve_marksman_hunter,
            char_fact.fatmulti8_bunnysisters_pve_resto_druid,
            char_fact.fatmulti9_glowyy_pve_holy_pala.set_dr_pala_2(),
            char_fact.fatmulti10_luxiaofeng_pve_unholy_tank_dk.set_is_leader_2().set_tank_2(),
        ]))


raid_active_char_fact = ActiveCharactersFactory()
