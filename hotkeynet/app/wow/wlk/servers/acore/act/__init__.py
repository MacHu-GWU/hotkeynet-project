# -*- coding: utf-8 -*-

# 通用
from .common import (
    movement,
    pet_action,
    target,
    target_leader_key_mapper,
    camera,
    system,
    general,
)

# 板甲
# from .warrior import warrior, warrior_arm, warrior_fury, warrior_protection
from .paladin import paladin, paladin_retribution, paladin_protection, paladin_holy
from .dk import dk, dk_blood, dk_frost, dk_unholy

# 锁甲
from .shaman import (
    shaman,
    shaman_elemental_combat,
    shaman_enhancement,
    shaman_restoration,
)
from .hunter import hunter, hunter_beastMastery, hunter_marksmanship, hunter_survival

# 皮甲
# from .rogue import ...
from .druid import druid, druid_balance, druid_restoration, druid_feral

# 布甲
from .warlock import (
    warlock,
    warlock_affliction,
    warlock_demonology,
    warlock_destruction,
)
from .mage import mage, mage_arcane, mage_fire, mage_frost
from .priest import priest, priest_discipline, priest_holy, priest_shadow
