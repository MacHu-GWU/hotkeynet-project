# -*- coding: utf-8 -*-

"""
将所有天赋以及其分类联系起来.
"""

import typing
from .talent import Talent
from .talent_category import TalentCategory
from ....utils import union_list, intersection_list, difference_list

T = Talent
TC = TalentCategory

association = [
    (TC.tank, T.warrior_pve_protect),
    (TC.tank, T.paladin_pve_protect),
    (TC.tank, T.druid_pve_bear),
    (TC.tank, T.dk_pve_blood_tank),
    (TC.tank, T.dk_pve_unholy_tank),
    (TC.tank, T.dk_pve_frost_tank),

    (TC.dps, T.warrior_pvp_protect),
    (TC.dps, T.paladin_pvp_protect),
    (TC.dps, T.druid_pvp_bear),

    (TC.dps, T.warrior_pve_fury),
    (TC.dps, T.warrior_pve_arm),
    (TC.dps, T.paladin_pve_retri),
    (TC.dps, T.dk_pve_blood_dps),
    (TC.dps, T.dk_pve_unholy_dps),
    (TC.dps, T.dk_pve_frost_dps),
    (TC.dps, T.hunter_pve_marksman),
    (TC.dps, T.hunter_pve_survival),
    (TC.dps, T.hunter_pve_beast),
    (TC.dps, T.shaman_pve_elemental),
    (TC.dps, T.shaman_pve_enhancement),
    (TC.dps, T.rogue_pve_combat),
    (TC.dps, T.rogue_pve_assassin),
    (TC.dps, T.rogue_pve_subtlety),
    (TC.dps, T.druid_pve_balance),
    (TC.dps, T.druid_pve_cat),
    (TC.dps, T.mage_pve_fire),
    (TC.dps, T.mage_pve_arcane),
    (TC.dps, T.mage_pve_frost),
    (TC.dps, T.warlock_pve_demonology),
    (TC.dps, T.warlock_pve_affliction),
    (TC.dps, T.warlock_pve_destruction),
    (TC.dps, T.priest_pve_shadow),

    (TC.dps, T.warrior_pvp_fury),
    (TC.dps, T.warrior_pvp_arm),
    (TC.dps, T.paladin_pvp_retri),
    (TC.dps, T.dk_pvp_blood),
    (TC.dps, T.dk_pvp_unholy),
    (TC.dps, T.dk_pvp_frost),
    (TC.dps, T.hunter_pvp_marksman),
    (TC.dps, T.hunter_pvp_survival),
    (TC.dps, T.hunter_pvp_beast),
    (TC.dps, T.shaman_pvp_elemental),
    (TC.dps, T.shaman_pvp_enhancement),
    (TC.dps, T.rogue_pvp_combat),
    (TC.dps, T.rogue_pvp_assassin),
    (TC.dps, T.rogue_pvp_subtlety),
    (TC.dps, T.druid_pvp_balance),
    (TC.dps, T.druid_pvp_cat),
    (TC.dps, T.mage_pvp_fire),
    (TC.dps, T.mage_pvp_arcane),
    (TC.dps, T.mage_pvp_frost),
    (TC.dps, T.warlock_pvp_demonology),
    (TC.dps, T.warlock_pvp_affliction),
    (TC.dps, T.warlock_pvp_destruction),
    (TC.dps, T.priest_pvp_shadow),

    (TC.healer, T.paladin_pve_holy),
    (TC.healer, T.shaman_pve_resto),
    (TC.healer, T.druid_pve_resto),
    (TC.healer, T.priest_pve_disco),
    (TC.healer, T.priest_pve_holy),

    (TC.healer, T.paladin_pvp_holy),
    (TC.healer, T.shaman_pvp_resto),
    (TC.healer, T.druid_pvp_resto),
    (TC.healer, T.priest_pvp_disco),
    (TC.healer, T.priest_pvp_holy),

    (TC.melee, T.warrior_pve_fury),
    (TC.melee, T.warrior_pve_arm),
    (TC.melee, T.warrior_pve_protect),
    (TC.melee, T.paladin_pve_retri),
    (TC.melee, T.paladin_pve_protect),
    (TC.melee, T.dk_pve_blood_dps),
    (TC.melee, T.dk_pve_unholy_dps),
    (TC.melee, T.dk_pve_frost_dps),
    (TC.melee, T.dk_pve_blood_tank),
    (TC.melee, T.dk_pve_unholy_tank),
    (TC.melee, T.dk_pve_frost_tank),
    (TC.melee, T.shaman_pve_enhancement),
    (TC.melee, T.rogue_pve_combat),
    (TC.melee, T.rogue_pve_assassin),
    (TC.melee, T.rogue_pve_subtlety),
    (TC.melee, T.druid_pve_cat),
    (TC.melee, T.druid_pve_bear),
    (TC.melee, T.warrior_pvp_fury),
    (TC.melee, T.warrior_pvp_arm),
    (TC.melee, T.warrior_pvp_protect),
    (TC.melee, T.paladin_pvp_retri),
    (TC.melee, T.paladin_pvp_protect),
    (TC.melee, T.dk_pvp_blood),
    (TC.melee, T.dk_pvp_unholy),
    (TC.melee, T.dk_pvp_frost),
    (TC.melee, T.shaman_pvp_enhancement),
    (TC.melee, T.rogue_pvp_combat),
    (TC.melee, T.rogue_pvp_assassin),
    (TC.melee, T.rogue_pvp_subtlety),
    (TC.melee, T.druid_pvp_cat),
    (TC.melee, T.druid_pvp_bear),

    (TC.ranger, T.paladin_pve_holy),
    (TC.ranger, T.hunter_pve_marksman),
    (TC.ranger, T.hunter_pve_survival),
    (TC.ranger, T.hunter_pve_beast),
    (TC.ranger, T.shaman_pve_resto),
    (TC.ranger, T.shaman_pve_elemental),
    (TC.ranger, T.shaman_pve_enhancement),
    (TC.ranger, T.druid_pve_balance),
    (TC.ranger, T.druid_pve_resto),
    (TC.ranger, T.mage_pve_fire),
    (TC.ranger, T.mage_pve_arcane),
    (TC.ranger, T.mage_pve_frost),
    (TC.ranger, T.warlock_pve_demonology),
    (TC.ranger, T.warlock_pve_affliction),
    (TC.ranger, T.warlock_pve_destruction),
    (TC.ranger, T.priest_pve_shadow),
    (TC.ranger, T.priest_pve_disco),
    (TC.ranger, T.priest_pve_holy),
    (TC.ranger, T.paladin_pvp_holy),
    (TC.ranger, T.hunter_pvp_marksman),
    (TC.ranger, T.hunter_pvp_survival),
    (TC.ranger, T.hunter_pvp_beast),
    (TC.ranger, T.shaman_pvp_resto),
    (TC.ranger, T.shaman_pvp_elemental),
    (TC.ranger, T.druid_pvp_balance),
    (TC.ranger, T.druid_pvp_resto),
    (TC.ranger, T.mage_pvp_fire),
    (TC.ranger, T.mage_pvp_arcane),
    (TC.ranger, T.mage_pvp_frost),
    (TC.ranger, T.warlock_pvp_demonology),
    (TC.ranger, T.warlock_pvp_affliction),
    (TC.ranger, T.warlock_pvp_destruction),
    (TC.ranger, T.priest_pvp_shadow),
    (TC.ranger, T.priest_pvp_disco),
    (TC.ranger, T.priest_pvp_holy),

    (TC.physics, T.warrior_pve_fury),
    (TC.physics, T.warrior_pve_arm),
    (TC.physics, T.warrior_pve_protect),
    (TC.physics, T.paladin_pve_retri),
    (TC.physics, T.paladin_pve_protect),
    (TC.physics, T.dk_pve_blood_dps),
    (TC.physics, T.dk_pve_unholy_dps),
    (TC.physics, T.dk_pve_frost_dps),
    (TC.physics, T.dk_pve_blood_tank),
    (TC.physics, T.dk_pve_unholy_tank),
    (TC.physics, T.dk_pve_frost_tank),
    (TC.physics, T.hunter_pve_marksman),
    (TC.physics, T.hunter_pve_survival),
    (TC.physics, T.hunter_pve_beast),
    (TC.physics, T.shaman_pve_enhancement),
    (TC.physics, T.rogue_pve_combat),
    (TC.physics, T.rogue_pve_assassin),
    (TC.physics, T.rogue_pve_subtlety),
    (TC.physics, T.druid_pve_cat),
    (TC.physics, T.druid_pve_bear),
    (TC.physics, T.warrior_pvp_fury),
    (TC.physics, T.warrior_pvp_arm),
    (TC.physics, T.warrior_pvp_protect),
    (TC.physics, T.paladin_pvp_retri),
    (TC.physics, T.paladin_pvp_protect),
    (TC.physics, T.dk_pvp_blood),
    (TC.physics, T.dk_pvp_unholy),
    (TC.physics, T.dk_pvp_frost),
    (TC.physics, T.hunter_pvp_marksman),
    (TC.physics, T.hunter_pvp_survival),
    (TC.physics, T.hunter_pvp_beast),
    (TC.physics, T.shaman_pvp_enhancement),
    (TC.physics, T.rogue_pvp_combat),
    (TC.physics, T.rogue_pvp_assassin),
    (TC.physics, T.rogue_pvp_subtlety),
    (TC.physics, T.druid_pvp_cat),
    (TC.physics, T.druid_pvp_bear),

    (TC.caster, T.paladin_pve_holy),
    (TC.caster, T.shaman_pve_resto),
    (TC.caster, T.shaman_pve_elemental),
    (TC.caster, T.druid_pve_balance),
    (TC.caster, T.druid_pve_resto),
    (TC.caster, T.mage_pve_fire),
    (TC.caster, T.mage_pve_arcane),
    (TC.caster, T.mage_pve_frost),
    (TC.caster, T.warlock_pve_demonology),
    (TC.caster, T.warlock_pve_affliction),
    (TC.caster, T.warlock_pve_destruction),
    (TC.caster, T.priest_pve_shadow),
    (TC.caster, T.priest_pve_disco),
    (TC.caster, T.priest_pve_holy),
    (TC.caster, T.paladin_pvp_holy),
    (TC.caster, T.shaman_pvp_resto),
    (TC.caster, T.shaman_pvp_elemental),
    (TC.caster, T.druid_pvp_balance),
    (TC.caster, T.druid_pvp_resto),
    (TC.caster, T.mage_pvp_fire),
    (TC.caster, T.mage_pvp_arcane),
    (TC.caster, T.mage_pvp_frost),
    (TC.caster, T.warlock_pvp_demonology),
    (TC.caster, T.warlock_pvp_affliction),
    (TC.caster, T.warlock_pvp_destruction),
    (TC.caster, T.priest_pvp_shadow),
    (TC.caster, T.priest_pvp_disco),
    (TC.caster, T.priest_pvp_holy),
]

category_to_talent_mapper = {category: [] for category in TC}
for category, talent in association:
    category_to_talent_mapper[category].append(talent)

_c2t_map = category_to_talent_mapper
_all_talent = set(Talent)
_c2t_map[TC.all] = _all_talent

_pve_and_pvp = ["pve", "pvp"]
for pvn in _pve_and_pvp:
    _c2t_map[TC[pvn]] = [t for t in Talent if pvn in t.name]

_all_class = [
    "warrior", "paladin", "dk",
    "hunter", "shaman",
    "rogue", "druid",
    "mage", "warlock", "priest"
]
for class_ in _all_class:
    _c2t_map[TC[class_]] = [t for t in Talent if t.name.startswith(class_)]
    _c2t_map[TC[f"non_{class_}"]] = difference_list(_all_talent, _c2t_map[TC[class_]])

for tc in TC:
    tc_name_chunks = tc.name.split("_")
    class_ = tc_name_chunks[0]
    if class_ in _all_class and len(tc_name_chunks) == 2:
        spec = tc.name.split("_")[-1]
        _c2t_map[TC[f"{class_}_{spec}"]] = [
            t
            for t in Talent
            if class_ in t.name and spec in t.name
        ]

for tc in TC:
    tc_name_chunks = tc.name.split("_")
    class_ = tc_name_chunks[0]
    if class_ in _all_class and len(tc_name_chunks) == 3:
        spec = tc.name.split("_")[-1]
        _c2t_map[TC[f"{class_}_non_{spec}"]] = difference_list(
            _all_talent,
            _c2t_map[TC[f"{class_}_{spec}"]],
        )

_all_role = ["tank", "dps", "healer"]
for role in _all_role:
    _c2t_map[TC[f"non_{role}"]] = difference_list(_all_talent, _c2t_map[TC[role]])

for class_ in _all_class:
    for role in _all_role:
        tc_name_1 = f"{class_}_{role}"
        try:
            _c2t_map[TC[tc_name_1]] = intersection_list(
                _c2t_map[TC[class_]],
                _c2t_map[TC[role]],
            )
        except KeyError:
            pass

        tc_name_2 = f"{class_}_non_{role}"
        try:
            _c2t_map[TC[tc_name_2]] = difference_list(
                _c2t_map[TC[class_]],
                _c2t_map[TC[tc_name_1]],
            )
        except KeyError:
            pass

_c2t_map[TC.dispeler] = difference_list(
    union_list(
        _c2t_map[TC.paladin],
        _c2t_map[TC.druid],
        _c2t_map[TC.shaman],
        _c2t_map[TC.mage],
        _c2t_map[TC.priest],
    ),
    _c2t_map[TC.druid_bear],
    _c2t_map[TC.druid_cat],
)
_c2t_map[TC.non_dispeler] = difference_list(_all_talent, _c2t_map[TC.dispeler])


talent_to_category_mapper = {talent: [] for talent in Talent}
_t2c_map = talent_to_category_mapper
for category, talent_list in _c2t_map.items():
    for talent in talent_list:
        _t2c_map[talent].append(category)


def get_talent_by_category(category: TC) -> typing.Set[Talent]:
    return category_to_talent_mapper[category]


def get_category_by_talent(talent: Talent) -> typing.Set[TC]:
    return talent_to_category_mapper[talent]
