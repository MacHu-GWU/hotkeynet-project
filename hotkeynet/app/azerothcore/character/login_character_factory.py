# -*- coding: utf-8 -*-


from ordered_set import OrderedSet
from hotkeynet.game.wow.wlk import (
    Character,
)

from .character_factory import char_fact


class LoginCharactersFactory:
    @property
    def r_abcde(self) -> OrderedSet[Character]:
        return OrderedSet([
            char_fact.ra_pve_protect_pala.set_inactive(),
            char_fact.rb_pve_elemental_shaman.set_inactive(),
            char_fact.rc_pve_balance_druid.set_inactive(),
            char_fact.rd_pve_arcane_mage.set_inactive(),
            char_fact.re_pve_shadow_priest.set_inactive(),
        ])

    @property
    def r_abcde_fghij(self) -> OrderedSet[Character]:
        return OrderedSet([
            char_fact.ra_pve_protect_pala.set_inactive(),
            char_fact.rb_pve_elemental_shaman.set_inactive(),
            char_fact.rc_pve_balance_druid.set_inactive(),
            char_fact.rd_pve_arcane_mage.set_inactive(),
            char_fact.re_pve_shadow_priest.set_inactive(),
            char_fact.rf_pve_demon_warlock.set_inactive(),
            char_fact.rg_pve_marksman_hunter.set_inactive(),
            char_fact.rh_pve_resto_druid.set_inactive(),
            char_fact.ri_pve_holy_paladin.set_inactive(),
            char_fact.rj_pve_blood_tank_dk.set_inactive(),
        ])

    @property
    def r_a_to_y(self) -> OrderedSet[Character]:
        return OrderedSet([
            char_fact.ra_pve_protect_pala.set_inactive(),
            char_fact.rb_pve_elemental_shaman.set_inactive(),
            char_fact.rc_pve_balance_druid.set_inactive(),
            char_fact.rd_pve_arcane_mage.set_inactive(),
            char_fact.re_pve_shadow_priest.set_inactive(),

            char_fact.rf_pve_demon_warlock.set_inactive(),
            char_fact.rg_pve_marksman_hunter.set_inactive(),
            char_fact.rh_pve_resto_druid.set_inactive(),
            char_fact.ri_pve_holy_paladin.set_inactive(),
            char_fact.rj_pve_blood_tank_dk.set_inactive(),

            char_fact.rk_pve_balance_druid.set_inactive(),
            char_fact.rl_pve_balance_druid.set_inactive(),
            char_fact.rm_pve_balance_druid.set_inactive(),
            char_fact.rn_pve_shadow_priest.set_inactive(),
            char_fact.ro_pve_shadow_priest.set_inactive(),

            char_fact.rp_pve_shadow_priest.set_inactive(),
            char_fact.rq_pve_shadow_priest.set_inactive(),
            char_fact.rr_pve_shadow_priest.set_inactive(),
            char_fact.rs_pve_shadow_priest.set_inactive(),
            char_fact.rt_pve_shadow_priest.set_inactive(),

            char_fact.ru_pve_shadow_priest.set_inactive(),
            char_fact.rv_pve_shadow_priest.set_inactive(),
            char_fact.rw_pve_resto_shaman.set_inactive(),
            char_fact.rx_pve_holy_paladin.set_inactive(),
            char_fact.ry_pve_disco_priest.set_inactive(),
        ])

    @property
    def s_abcde(self) -> OrderedSet[Character]:
        return OrderedSet([
            char_fact.sa_pve_protect_paladin.set_inactive(),
            char_fact.sb_pve_elemental_shaman.set_inactive(),
            char_fact.sc_pve_elemental_shaman.set_inactive(),
            char_fact.sd_pve_elemental_shaman.set_inactive(),
            char_fact.se_pve_resto_shaman.set_inactive(),
        ])


login_char_fact = LoginCharactersFactory()
