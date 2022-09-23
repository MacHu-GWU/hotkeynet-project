# -*- coding: utf-8 -*-

from ordered_set import OrderedSet
from hotkeynet.game.wow.wlk import Character, char_oset_helper
from ..character_factory import char_fact, char_group


class ActiveCharactersFactory:
    def x5p_r_abcde(self) -> OrderedSet[Character]:
        return char_oset_helper.set_team_leader_and_tank(chars=OrderedSet([
            char_fact.ra_pve_protect_pala.set_leader_12_and_tank_12(),
            char_fact.rb_pve_elemental_shaman,
            char_fact.rc_pve_balance_druid,
            char_fact.rd_pve_arcane_mage,
            char_fact.rh_pve_resto_druid,
        ]))

    def x5p_r_fghij(self) -> OrderedSet[Character]:
        return char_oset_helper.set_team_leader_and_tank(chars=OrderedSet([
            char_fact.re_pve_shadow_priest,
            char_fact.rf_pve_demon_warlock,
            char_fact.rg_pve_marksman_hunter,
            char_fact.ri_pve_holy_paladin.set_dr_pala_2(),
            char_fact.rj_pve_blood_tank_dk.set_leader_12_and_tank_12()
        ]))


dungeon_active_char_fact = ActiveCharactersFactory()
