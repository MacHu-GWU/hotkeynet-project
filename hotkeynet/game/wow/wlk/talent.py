# -*- coding: utf-8 -*-

"""
枚举所有职业天赋.
"""

from enum import auto
from ..model import Talent


class Talent(Talent):
    warrior_pve_fury = auto()
    warrior_pve_arm = auto()
    warrior_pve_protect = auto()

    warrior_pvp_fury = auto()
    warrior_pvp_arm = auto()
    warrior_pvp_protect = auto()

    paladin_pve_retri = auto()
    paladin_pve_holy = auto()
    paladin_pve_protect = auto()

    paladin_pvp_retri = auto()
    paladin_pvp_holy = auto()
    paladin_pvp_protect = auto()

    dk_pve_blood_dps = auto()
    dk_pve_unholy_dps = auto()
    dk_pve_frost_dps = auto()
    dk_pve_blood_tank = auto()
    dk_pve_unholy_tank = auto()
    dk_pve_frost_tank = auto()

    dk_pvp_blood = auto()
    dk_pvp_unholy = auto()
    dk_pvp_frost = auto()

    hunter_pve_marksman = auto()
    hunter_pve_survival = auto()
    hunter_pve_beast = auto()

    hunter_pvp_marksman = auto()
    hunter_pvp_survival = auto()
    hunter_pvp_beast = auto()

    shaman_pve_resto = auto()
    shaman_pve_elemental = auto()
    shaman_pve_enhancement = auto()

    shaman_pvp_resto = auto()
    shaman_pvp_elemental = auto()
    shaman_pvp_enhancement = auto()

    rogue_pve_combat = auto()
    rogue_pve_assassin = auto()
    rogue_pve_subtlety = auto()

    rogue_pvp_combat = auto()
    rogue_pvp_assassin = auto()
    rogue_pvp_subtlety = auto()

    druid_pve_balance = auto()
    druid_pve_resto = auto()
    druid_pve_cat = auto()
    druid_pve_bear = auto()

    druid_pvp_balance = auto()
    druid_pvp_resto = auto()
    druid_pvp_cat = auto()
    druid_pvp_bear = auto()

    mage_pve_fire = auto()
    mage_pve_arcane = auto()
    mage_pve_frost = auto()

    mage_pvp_fire = auto()
    mage_pvp_arcane = auto()
    mage_pvp_frost = auto()

    warlock_pve_demonology = auto()
    warlock_pve_affliction = auto()
    warlock_pve_destruction = auto()

    warlock_pvp_demonology = auto()
    warlock_pvp_affliction = auto()
    warlock_pvp_destruction = auto()

    priest_pve_shadow = auto()
    priest_pve_disco = auto()
    priest_pve_holy = auto()

    priest_pvp_shadow = auto()
    priest_pvp_disco = auto()
    priest_pvp_holy = auto()
