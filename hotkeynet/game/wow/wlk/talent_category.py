# -*- coding: utf-8 -*-

"""
枚举所有职业天赋的分类.
"""

from enum import IntEnum, auto


class TalentCategory(IntEnum):
    """
    对天赋的分类方式有很多. 比如有:

    - 按照 PvP / PvE
    - 按照副本角色, Tank, DPS, 近战, 远程, 施法者, 治疗
    """
    all = auto()

    # by pvp, pve
    pvp = auto()
    pve = auto()

    # by role
    tank = auto()
    dps = auto()
    healer = auto()
    non_tank = auto()
    non_dps = auto()
    non_healer = auto()

    # by melee, range
    melee = auto()
    ranger = auto()
    non_melee = auto()
    non_ranger = auto()

    # by physics, caster
    physics = auto()
    caster = auto()
    non_physics = auto()
    non_caster = auto()

    # 驱散
    dispeler = auto()
    non_dispeler = auto()

    # by class
    warrior = auto()
    warrior_fury = auto()
    warrior_non_fury = auto()
    warrior_arm = auto()
    warrior_non_arm = auto()
    warrior_protect = auto()
    warrior_non_protect = auto()

    warrior_tank = auto()
    warrior_dps = auto()
    non_warrior = auto()

    paladin = auto()
    paladin_retri = auto()
    paladin_non_retri = auto()
    paladin_holy = auto()
    paladin_non_holy = auto()
    paladin_protect = auto()
    paladin_non_protect = auto()

    paladin_tank = auto()
    paladin_non_tank = auto()
    paladin_dps = auto()
    paladin_non_dps = auto()
    paladin_healer = auto()
    paladin_non_healer = auto()
    non_paladin = auto()

    dk = auto()
    dk_blood = auto()
    dk_non_blood = auto()
    dk_unholy = auto()
    dk_non_unholy = auto()
    dk_frost = auto()
    dk_non_frost = auto()

    dk_tank = auto()
    dk_dps = auto()
    non_dk = auto()

    hunter = auto()
    hunter_marksman = auto()
    hunter_non_marksman = auto()
    hunter_survival = auto()
    hunter_non_survival = auto()
    hunter_beast = auto()
    hunter_non_beast = auto()

    non_hunter = auto()

    shaman = auto()
    shaman_resto = auto()
    shaman_non_resto = auto()
    shaman_elemental = auto()
    shaman_non_elemental = auto()
    shaman_enhancement = auto()
    shaman_non_enhancement = auto()

    shaman_dps = auto()
    shaman_healer = auto()
    non_shaman = auto()

    rogue = auto()
    rogue_combat = auto()
    rogue_non_combat = auto()
    rogue_assassin = auto()
    rogue_non_assassin = auto()
    rogue_subtlety = auto()
    rogue_non_subtlety = auto()

    non_rogue = auto()

    druid = auto()
    druid_balance = auto()
    druid_non_balance = auto()
    druid_resto = auto()
    druid_non_resto = auto()
    druid_cat = auto()
    druid_non_cat = auto()
    druid_bear = auto()
    druid_non_bear = auto()

    druid_tank = auto()
    druid_non_tank = auto()
    druid_dps = auto()
    druid_non_dps = auto()
    druid_healer = auto()
    druid_non_healer = auto()
    non_druid = auto()

    mage = auto()
    mage_fire = auto()
    mage_non_fire = auto()
    mage_arcane = auto()
    mage_non_arcane = auto()
    mage_frost = auto()
    mage_non_frost = auto()
    non_mage = auto()

    warlock = auto()
    warlock_demonology = auto()
    warlock_non_demonology = auto()
    warlock_affliction = auto()
    warlock_non_affliction = auto()
    warlock_destruction = auto()
    warlock_non_destruction = auto()

    non_warlock = auto()

    priest = auto()
    priest_shadow = auto()
    priest_non_shadow = auto()
    priest_disco = auto()
    priest_non_disco = auto()
    priest_holy = auto()
    priest_non_holy = auto()

    priest_dps = auto()
    priest_non_dps = auto()
    priest_healer = auto()
    priest_non_healer = auto()

    non_priest = auto()
