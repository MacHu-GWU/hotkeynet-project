# -*- coding: utf-8 -*-

import os
from hotkeynet.game.wow.wlk.talent import (
    TL,
    TC,
    OrderedSet,
)


class TestTalent:
    def test_name_is_string_value_is_int(self):
        assert TL.dk_pve_blood_tank.name == "dk_pve_blood_tank"
        assert isinstance(TL.dk_pve_blood_tank.value, int)

    def test_sortable(self):
        talent_list = [
            TL.druid_pve_balance,
            TL.dk_pve_blood_tank,
            TL.priest_pve_disco,
        ]
        talent_list.sort()

        talent_code_list = [t.value for t in talent_list]
        talent_code_list.sort()
        assert (
            talent_code_list[1] > talent_code_list[0]
            and talent_code_list[2] > talent_code_list[1]
        )


class TestTalentCategory:
    def test_name_is_string_value_is_int(self):
        assert TC.warrior_tank.name == "warrior_tank"
        assert isinstance(TC.warrior_tank.value, int)

    def test_sortable(self):
        talent_category_list = [
            TC.tank,
            TC.dps,
            TC.healer
        ]
        talent_category_list.sort()

        talent_category_code_list = [t.value for t in talent_category_list]
        talent_category_code_list.sort()
        assert (
            talent_category_code_list[1] > talent_category_code_list[0]
            and talent_category_code_list[2] > talent_category_code_list[1]
        )


def test_get_talent_by_category():
    assert TL.druid_pve_bear in TC.tank.talents
    assert len(TC.tank.talents) == 6

    assert TL.paladin_pve_protect not in TC.non_tank.talents

    assert TL.druid_pve_balance in TC.druid_balance.talents
    assert TL.druid_pvp_balance in TC.druid_balance.talents

    assert TL.paladin_pvp_protect in TC.paladin_dps.talents

    assert TL.paladin_pve_protect in TC.paladin_non_dps.talents
    assert TL.paladin_pve_holy in TC.paladin_non_dps.talents
    assert TL.paladin_pvp_holy in TC.paladin_non_dps.talents

    assert TL.paladin_pvp_retri in TC.dispeler.talents
    assert TL.shaman_pve_enhancement in TC.dispeler.talents
    assert TL.druid_pve_bear not in TC.dispeler.talents
    assert TL.druid_pvp_cat not in TC.dispeler.talents

    # 测试 TC.${class}_non_${spec}
    assert TL.warrior_pve_fury not in TC.shaman_non_resto.talents
    assert TL.shaman_pve_resto not in TC.shaman_non_resto.talents
    assert TL.shaman_pve_elemental in TC.shaman_non_resto.talents
    assert TL.shaman_pvp_elemental in TC.shaman_non_resto.talents


def test_get_category_by_talent():
    assert TL.warrior_pvp_fury.categories == OrderedSet([
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
    ])

    assert TL.paladin_pve_holy.categories == OrderedSet([
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
    ])

    assert TL.druid_pve_bear.is_tank() is True
    assert TL.druid_pvp_cat.is_tank() is False


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
        "--cov=hotkeynet.game.wow.wlk.talent",
        "--cov-report", "term-missing",
        "--cov-report", f"html:{dir_htmlcov}",
        abspath,
    ]
    subprocess.run(args)