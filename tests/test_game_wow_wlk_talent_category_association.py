# -*- coding: utf-8 -*-

import os
from hotkeynet.game.wow.wlk.talent_category_association import (
    get_talent_by_category,
    get_category_by_talent,
    Talent as TL,
    TalentCategory as TC,
)


def test_get_talent_by_category():
    assert TL.druid_pve_bear in get_talent_by_category(TC.tank)
    assert len(get_talent_by_category(TC.tank)) == 6

    assert TL.paladin_pve_protect not in get_talent_by_category(TC.non_tank)

    assert TL.druid_pve_balance in get_talent_by_category(TC.druid_balance)
    assert TL.druid_pvp_balance in get_talent_by_category(TC.druid_balance)

    assert TL.paladin_pvp_protect in get_talent_by_category(TC.paladin_dps)

    assert TL.paladin_pve_protect in get_talent_by_category(TC.paladin_non_dps)
    assert TL.paladin_pve_holy in get_talent_by_category(TC.paladin_non_dps)
    assert TL.paladin_pvp_holy in get_talent_by_category(TC.paladin_non_dps)

    assert TL.paladin_pvp_retri in get_talent_by_category(TC.dispeler)
    assert TL.shaman_pve_enhancement in get_talent_by_category(TC.dispeler)
    assert TL.druid_pve_bear not in get_talent_by_category(TC.dispeler)
    assert TL.druid_pvp_cat not in get_talent_by_category(TC.dispeler)

    # 测试 TC.${class}_non_${spec}
    assert TL.warrior_pve_fury not in get_talent_by_category(TC.shaman_non_resto)
    assert TL.shaman_pve_resto not in get_talent_by_category(TC.shaman_non_resto)
    assert TL.shaman_pve_elemental in get_talent_by_category(TC.shaman_non_resto)
    assert TL.shaman_pvp_elemental in get_talent_by_category(TC.shaman_non_resto)


def test_get_category_by_talent():
    assert get_category_by_talent(TL.warrior_pvp_fury) == [
        TC.all,
        TC.pvp,
        TC.dps,
        TC.non_tank,
        TC.non_healer,
        TC.melee,
        TC.non_ranger,
        TC.physics,
        TC.non_caster,
        TC.non_dispeler,
        TC.warrior,
        TC.warrior_fury,
        TC.warrior_non_arm,
        TC.warrior_non_protect,
        TC.warrior_dps,
        TC.non_paladin,
        TC.non_dk,
        TC.non_hunter,
        TC.non_shaman,
        TC.non_rogue,
        TC.non_druid,
        TC.non_mage,
        TC.non_warlock,
        TC.non_priest,
    ]

    assert get_category_by_talent(TL.paladin_pve_holy) == [
        TC.all,
        TC.pve,
        TC.healer,
        TC.non_tank,
        TC.non_dps,
        TC.ranger,
        TC.non_melee,
        TC.caster,
        TC.non_physics,
        TC.dispeler,
        TC.non_warrior,
        TC.paladin,
        TC.paladin_non_retri,
        TC.paladin_holy,
        TC.paladin_non_protect,
        TC.paladin_non_tank,
        TC.paladin_non_dps,
        TC.paladin_healer,
        TC.non_dk,
        TC.non_hunter,
        TC.non_shaman,
        TC.non_rogue,
        TC.non_druid,
        TC.non_mage,
        TC.non_warlock,
        TC.non_priest,
    ]


if __name__ == "__main__":
    import sys
    import subprocess

    abspath = os.path.abspath(__file__)
    dir_project_root = os.path.dirname(abspath)
    for _ in range(10):
        if os.path.exists(os.path.join(dir_project_root, ".git")):
            break
        else:
            dir_project_root = os.path.dirname(dir_project_root)
    else:
        raise FileNotFoundError("cannot find project root dir!")
    dir_htmlcov = os.path.join(dir_project_root, "htmlcov")
    bin_pytest = os.path.join(os.path.dirname(sys.executable), "pytest")

    args = [
        bin_pytest,
        "-s", "--tb=native", "-vv",
        f"--rootdir={dir_project_root}",
        "--cov=hotkeynet.game.wow.wlk.talent_category_association",
        "--cov-report", "term-missing",
        "--cov-report", f"html:{dir_htmlcov}",
        abspath,
    ]
    subprocess.run(args)
