# -*- coding: utf-8 -*-

import pytest

from hotkeynet.projects.warmane.constant.talent_category_association import (
    get_talent_by_category, Talent as T,
    TalentCategory as TC,
)


def test_get_talent_by_category():
    assert T.druid_pve_bear in get_talent_by_category(TC.tank)
    assert len(get_talent_by_category(TC.tank)) == 6

    assert T.paladin_pve_protect not in get_talent_by_category(TC.non_tank)

    assert T.druid_pve_balance in get_talent_by_category(TC.druid_balance)
    assert T.druid_pvp_balance in get_talent_by_category(TC.druid_balance)

    assert T.paladin_pvp_protect in get_talent_by_category(TC.paladin_dps)

    assert T.paladin_pve_protect in get_talent_by_category(TC.paladin_non_dps)
    assert T.paladin_pve_holy in get_talent_by_category(TC.paladin_non_dps)
    assert T.paladin_pvp_holy in get_talent_by_category(TC.paladin_non_dps)

    assert T.paladin_pvp_retri in get_talent_by_category(TC.dispeler)
    assert T.shaman_pve_enhancement in get_talent_by_category(TC.dispeler)
    assert T.druid_pve_bear not in get_talent_by_category(TC.dispeler)
    assert T.druid_pvp_cat not in get_talent_by_category(TC.dispeler)

    # 测试 TC.${class}_non_${spec}
    assert T.warrior_pve_fury not in get_talent_by_category(TC.shaman_non_resto)
    assert T.shaman_pve_resto not in get_talent_by_category(TC.shaman_non_resto)
    assert T.shaman_pve_elemental in get_talent_by_category(TC.shaman_non_resto)
    assert T.shaman_pvp_elemental in get_talent_by_category(TC.shaman_non_resto)



def test_get_category_by_talent():
    pass


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
