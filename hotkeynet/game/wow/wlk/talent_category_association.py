# -*- coding: utf-8 -*-

"""
将所有天赋以及其分类联系起来.
"""

import typing as TP
from .talent import Talent
from .talent_category import TalentCategory
from ....utils import union_list, intersection_list, difference_list

TL = Talent
TC = TalentCategory

# 用人类的判断定义 类别的 和 具体天赋 的对应关系
# 这里由于是 many to many 的关系, 我们不可能定义全部的关系, 只能定义一部分
# 然后用集合运算计算出其他的联系
association = [
    (TC.tank, TL.warrior_pve_protect),
    (TC.tank, TL.paladin_pve_protect),
    (TC.tank, TL.druid_pve_bear),
    (TC.tank, TL.dk_pve_blood_tank),
    (TC.tank, TL.dk_pve_unholy_tank),
    (TC.tank, TL.dk_pve_frost_tank),

    (TC.dps, TL.warrior_pvp_protect),
    (TC.dps, TL.paladin_pvp_protect),
    (TC.dps, TL.druid_pvp_bear),

    (TC.dps, TL.warrior_pve_fury),
    (TC.dps, TL.warrior_pve_arm),
    (TC.dps, TL.paladin_pve_retri),
    (TC.dps, TL.dk_pve_blood_dps),
    (TC.dps, TL.dk_pve_unholy_dps),
    (TC.dps, TL.dk_pve_frost_dps),
    (TC.dps, TL.hunter_pve_marksman),
    (TC.dps, TL.hunter_pve_survival),
    (TC.dps, TL.hunter_pve_beast),
    (TC.dps, TL.shaman_pve_elemental),
    (TC.dps, TL.shaman_pve_enhancement),
    (TC.dps, TL.rogue_pve_combat),
    (TC.dps, TL.rogue_pve_assassin),
    (TC.dps, TL.rogue_pve_subtlety),
    (TC.dps, TL.druid_pve_balance),
    (TC.dps, TL.druid_pve_cat),
    (TC.dps, TL.mage_pve_fire),
    (TC.dps, TL.mage_pve_arcane),
    (TC.dps, TL.mage_pve_frost),
    (TC.dps, TL.warlock_pve_demonology),
    (TC.dps, TL.warlock_pve_affliction),
    (TC.dps, TL.warlock_pve_destruction),
    (TC.dps, TL.priest_pve_shadow),

    (TC.dps, TL.warrior_pvp_fury),
    (TC.dps, TL.warrior_pvp_arm),
    (TC.dps, TL.paladin_pvp_retri),
    (TC.dps, TL.dk_pvp_blood),
    (TC.dps, TL.dk_pvp_unholy),
    (TC.dps, TL.dk_pvp_frost),
    (TC.dps, TL.hunter_pvp_marksman),
    (TC.dps, TL.hunter_pvp_survival),
    (TC.dps, TL.hunter_pvp_beast),
    (TC.dps, TL.shaman_pvp_elemental),
    (TC.dps, TL.shaman_pvp_enhancement),
    (TC.dps, TL.rogue_pvp_combat),
    (TC.dps, TL.rogue_pvp_assassin),
    (TC.dps, TL.rogue_pvp_subtlety),
    (TC.dps, TL.druid_pvp_balance),
    (TC.dps, TL.druid_pvp_cat),
    (TC.dps, TL.mage_pvp_fire),
    (TC.dps, TL.mage_pvp_arcane),
    (TC.dps, TL.mage_pvp_frost),
    (TC.dps, TL.warlock_pvp_demonology),
    (TC.dps, TL.warlock_pvp_affliction),
    (TC.dps, TL.warlock_pvp_destruction),
    (TC.dps, TL.priest_pvp_shadow),

    (TC.healer, TL.paladin_pve_holy),
    (TC.healer, TL.shaman_pve_resto),
    (TC.healer, TL.druid_pve_resto),
    (TC.healer, TL.priest_pve_disco),
    (TC.healer, TL.priest_pve_holy),

    (TC.healer, TL.paladin_pvp_holy),
    (TC.healer, TL.shaman_pvp_resto),
    (TC.healer, TL.druid_pvp_resto),
    (TC.healer, TL.priest_pvp_disco),
    (TC.healer, TL.priest_pvp_holy),

    (TC.melee, TL.warrior_pve_fury),
    (TC.melee, TL.warrior_pve_arm),
    (TC.melee, TL.warrior_pve_protect),
    (TC.melee, TL.paladin_pve_retri),
    (TC.melee, TL.paladin_pve_protect),
    (TC.melee, TL.dk_pve_blood_dps),
    (TC.melee, TL.dk_pve_unholy_dps),
    (TC.melee, TL.dk_pve_frost_dps),
    (TC.melee, TL.dk_pve_blood_tank),
    (TC.melee, TL.dk_pve_unholy_tank),
    (TC.melee, TL.dk_pve_frost_tank),
    (TC.melee, TL.shaman_pve_enhancement),
    (TC.melee, TL.rogue_pve_combat),
    (TC.melee, TL.rogue_pve_assassin),
    (TC.melee, TL.rogue_pve_subtlety),
    (TC.melee, TL.druid_pve_cat),
    (TC.melee, TL.druid_pve_bear),
    (TC.melee, TL.warrior_pvp_fury),
    (TC.melee, TL.warrior_pvp_arm),
    (TC.melee, TL.warrior_pvp_protect),
    (TC.melee, TL.paladin_pvp_retri),
    (TC.melee, TL.paladin_pvp_protect),
    (TC.melee, TL.dk_pvp_blood),
    (TC.melee, TL.dk_pvp_unholy),
    (TC.melee, TL.dk_pvp_frost),
    (TC.melee, TL.shaman_pvp_enhancement),
    (TC.melee, TL.rogue_pvp_combat),
    (TC.melee, TL.rogue_pvp_assassin),
    (TC.melee, TL.rogue_pvp_subtlety),
    (TC.melee, TL.druid_pvp_cat),
    (TC.melee, TL.druid_pvp_bear),

    (TC.ranger, TL.paladin_pve_holy),
    (TC.ranger, TL.hunter_pve_marksman),
    (TC.ranger, TL.hunter_pve_survival),
    (TC.ranger, TL.hunter_pve_beast),
    (TC.ranger, TL.shaman_pve_resto),
    (TC.ranger, TL.shaman_pve_elemental),
    (TC.ranger, TL.shaman_pve_enhancement),
    (TC.ranger, TL.druid_pve_balance),
    (TC.ranger, TL.druid_pve_resto),
    (TC.ranger, TL.mage_pve_fire),
    (TC.ranger, TL.mage_pve_arcane),
    (TC.ranger, TL.mage_pve_frost),
    (TC.ranger, TL.warlock_pve_demonology),
    (TC.ranger, TL.warlock_pve_affliction),
    (TC.ranger, TL.warlock_pve_destruction),
    (TC.ranger, TL.priest_pve_shadow),
    (TC.ranger, TL.priest_pve_disco),
    (TC.ranger, TL.priest_pve_holy),
    (TC.ranger, TL.paladin_pvp_holy),
    (TC.ranger, TL.hunter_pvp_marksman),
    (TC.ranger, TL.hunter_pvp_survival),
    (TC.ranger, TL.hunter_pvp_beast),
    (TC.ranger, TL.shaman_pvp_resto),
    (TC.ranger, TL.shaman_pvp_elemental),
    (TC.ranger, TL.druid_pvp_balance),
    (TC.ranger, TL.druid_pvp_resto),
    (TC.ranger, TL.mage_pvp_fire),
    (TC.ranger, TL.mage_pvp_arcane),
    (TC.ranger, TL.mage_pvp_frost),
    (TC.ranger, TL.warlock_pvp_demonology),
    (TC.ranger, TL.warlock_pvp_affliction),
    (TC.ranger, TL.warlock_pvp_destruction),
    (TC.ranger, TL.priest_pvp_shadow),
    (TC.ranger, TL.priest_pvp_disco),
    (TC.ranger, TL.priest_pvp_holy),

    (TC.physics, TL.warrior_pve_fury),
    (TC.physics, TL.warrior_pve_arm),
    (TC.physics, TL.warrior_pve_protect),
    (TC.physics, TL.paladin_pve_retri),
    (TC.physics, TL.paladin_pve_protect),
    (TC.physics, TL.dk_pve_blood_dps),
    (TC.physics, TL.dk_pve_unholy_dps),
    (TC.physics, TL.dk_pve_frost_dps),
    (TC.physics, TL.dk_pve_blood_tank),
    (TC.physics, TL.dk_pve_unholy_tank),
    (TC.physics, TL.dk_pve_frost_tank),
    (TC.physics, TL.hunter_pve_marksman),
    (TC.physics, TL.hunter_pve_survival),
    (TC.physics, TL.hunter_pve_beast),
    (TC.physics, TL.shaman_pve_enhancement),
    (TC.physics, TL.rogue_pve_combat),
    (TC.physics, TL.rogue_pve_assassin),
    (TC.physics, TL.rogue_pve_subtlety),
    (TC.physics, TL.druid_pve_cat),
    (TC.physics, TL.druid_pve_bear),
    (TC.physics, TL.warrior_pvp_fury),
    (TC.physics, TL.warrior_pvp_arm),
    (TC.physics, TL.warrior_pvp_protect),
    (TC.physics, TL.paladin_pvp_retri),
    (TC.physics, TL.paladin_pvp_protect),
    (TC.physics, TL.dk_pvp_blood),
    (TC.physics, TL.dk_pvp_unholy),
    (TC.physics, TL.dk_pvp_frost),
    (TC.physics, TL.hunter_pvp_marksman),
    (TC.physics, TL.hunter_pvp_survival),
    (TC.physics, TL.hunter_pvp_beast),
    (TC.physics, TL.shaman_pvp_enhancement),
    (TC.physics, TL.rogue_pvp_combat),
    (TC.physics, TL.rogue_pvp_assassin),
    (TC.physics, TL.rogue_pvp_subtlety),
    (TC.physics, TL.druid_pvp_cat),
    (TC.physics, TL.druid_pvp_bear),

    (TC.caster, TL.paladin_pve_holy),
    (TC.caster, TL.shaman_pve_resto),
    (TC.caster, TL.shaman_pve_elemental),
    (TC.caster, TL.druid_pve_balance),
    (TC.caster, TL.druid_pve_resto),
    (TC.caster, TL.mage_pve_fire),
    (TC.caster, TL.mage_pve_arcane),
    (TC.caster, TL.mage_pve_frost),
    (TC.caster, TL.warlock_pve_demonology),
    (TC.caster, TL.warlock_pve_affliction),
    (TC.caster, TL.warlock_pve_destruction),
    (TC.caster, TL.priest_pve_shadow),
    (TC.caster, TL.priest_pve_disco),
    (TC.caster, TL.priest_pve_holy),
    (TC.caster, TL.paladin_pvp_holy),
    (TC.caster, TL.shaman_pvp_resto),
    (TC.caster, TL.shaman_pvp_elemental),
    (TC.caster, TL.druid_pvp_balance),
    (TC.caster, TL.druid_pvp_resto),
    (TC.caster, TL.mage_pvp_fire),
    (TC.caster, TL.mage_pvp_arcane),
    (TC.caster, TL.mage_pvp_frost),
    (TC.caster, TL.warlock_pvp_demonology),
    (TC.caster, TL.warlock_pvp_affliction),
    (TC.caster, TL.warlock_pvp_destruction),
    (TC.caster, TL.priest_pvp_shadow),
    (TC.caster, TL.priest_pvp_disco),
    (TC.caster, TL.priest_pvp_holy),
]

# 我们先专注于计算 类别 -> 天赋 的关系, 最后把它反过来就得到了 天赋 -> 类别 的关系
category_to_talent_mapper = {category: [] for category in TC}
for category, talent in association:
    category_to_talent_mapper[category].append(talent)

_c2t_map = category_to_talent_mapper
_all_talent = set(Talent)
_c2t_map[TC.all] = _all_talent

# 先处理 pve, pvp, 这个最简单
_pve_and_pvp = ["pve", "pvp"]
for pvn in _pve_and_pvp:
    _c2t_map[TC[pvn]] = [t for t in Talent if pvn in t.name]

# 然后处理各个职业
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
            if (class_ in t.name) and (spec in t.name)
        ]

    elif class_ in _all_class and len(tc_name_chunks) == 3:
        spec = tc.name.split("_")[-1]
        _c2t_map[TC[f"{class_}_non_{spec}"]] = difference_list(
            _c2t_map[TC[f"{class_}"]],
            _c2t_map[TC[f"{class_}_{spec}"]],
        )

    else:  # pragma: no cover
        pass

_all_role = ["tank", "dps", "healer"]
for role in _all_role:
    _c2t_map[TC[f"non_{role}"]] = difference_list(_all_talent, _c2t_map[TC[role]])

_all_detailed_role = ["melee", "ranger", "physics", "caster"]
for role in _all_detailed_role:
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


def get_talent_by_category(category: TC) -> TP.List[Talent]:
    return category_to_talent_mapper[category]


def get_category_by_talent(talent: TL) -> TP.List[TC]:
    return talent_to_category_mapper[talent]
