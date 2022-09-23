# -*- coding: utf-8 -*-

from ordered_set import OrderedSet
from hotkeynet.game.wow.wlk import Character, char_oset_helper
from ..character_factory import char_fact, char_group


class ActiveCharactersFactory:
    @property
    def x10p_r_abcde_fghij_core_team(self) -> OrderedSet[Character]:
        """
        主力 10 人组
        """
        return char_oset_helper.set_team_leader_and_tank(chars=OrderedSet([
            char_fact.ra_pve_protect_pala.set_leader_1_tank_1(),
            char_fact.rb_pve_elemental_shaman,
            char_fact.rc_pve_balance_druid,
            char_fact.rd_pve_arcane_mage,
            char_fact.re_pve_shadow_priest,
            char_fact.rf_pve_demon_warlock,
            char_fact.rg_pve_marksman_hunter,
            char_fact.rh_pve_resto_druid,
            char_fact.ri_pve_holy_paladin.set_dr_pala_2(),
            char_fact.rj_pve_blood_tank_dk.set_leader_2_tank_2()
        ]))


raid_active_char_fact = ActiveCharactersFactory()
