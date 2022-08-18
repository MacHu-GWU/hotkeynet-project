# -*- coding: utf-8 -*-

"""
该模块定义了在 WOTLK 版本中所有职业的天赋, 以及围绕着天赋进行的各种计算. 这里有 3 个重要概念:

1. Talent: 是一个枚举类型, 枚举了所有魔兽世界 WLK 中的角色天赋.
2. TalentCategory: 是一个枚举类型, 对所有的天赋进行归类. 归类的方式有很多, 例如按照
    PvE, PvP 分类, 按照 Tank, DPS, Healer, 按照 近战, 远程, 物理, 魔法等.
3. talent association: 是一个双向字典, 可以根据 Talent 找到它所属于哪些分类, 也可以
    根据 TalentCategory 找到里面包含了哪些天赋.
"""

import typing as TP
from enum import auto

from .. import model
from ....utils import union_list, intersection_list, difference_list


class Talent(model.Talent):
    """
    角色天赋.
    """
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


class TalentCategory(model.TalentCategory):
    """
    天赋的类别.

    对天赋的分类方式有很多. 比如有:

    - 按照 PvP / PvE
    - 按照副本角色, Tank, DPS, 近战, 远程, 施法者, 治疗
    - 按照职业, 比如 战士, 骑士, 盗贼
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


TL = Talent
TC = TalentCategory

# 用人类的判断定义 类别的 和 具体天赋 的对应关系
# 这里由于天赋与分类是 many to many 的关系, 我们不可能定义全部的关系, 只能定义一部分
# 然后用集合运算计算出其他的联系. 换言之我们这里定义 什么天赋 "是" 什么分类
# 至于什么 "不是", 则用集合运算求补集即可
_association = [
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
for category, talent in _association:
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

# 处理各个职业的各系天赋
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

# 处理 tank, dps, healer
_all_role = ["tank", "dps", "healer"]
for role in _all_role:
    _c2t_map[TC[f"non_{role}"]] = difference_list(_all_talent, _c2t_map[TC[role]])

# 处理 近战, 远程, 物理, 魔法
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
