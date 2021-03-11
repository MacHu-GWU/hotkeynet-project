# -*- coding: utf-8 -*-

"""
枚举所有职业天赋的分类.
"""

from enum import Enum, auto


class TalentCategory(Enum):
    pvp = auto()
    pve = auto()

    tank = auto()
    dps = auto()
    healer = auto()

    melee = auto()
    ranger = auto()

    physics = auto()
    caster = auto()

    warrior = auto()
    paladin = auto()
    dk = auto()
    hunter = auto()
    shaman = auto()
    rogue = auto()
    druid = auto()
    mage = auto()
    warlock = auto()
    priest = auto()
