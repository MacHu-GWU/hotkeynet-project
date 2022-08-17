# -*- coding: utf-8 -*-

import os
from hotkeynet.game.wow.wlk.talent import Talent


class TestTalent:
    def test_name_is_string_value_is_int(self):
        assert Talent.dk_pve_blood_tank.name == "dk_pve_blood_tank"
        assert isinstance(Talent.dk_pve_blood_tank.value, int)

    def test_sortable(self):
        talent_list = [
            Talent.druid_pve_balance,
            Talent.dk_pve_blood_tank,
            Talent.priest_pve_disco,
        ]
        talent_list.sort()

        talent_code_list = [t.value for t in talent_list]
        talent_code_list.sort()
        assert (
            talent_code_list[1] > talent_code_list[0]
            and talent_code_list[2] > talent_code_list[1]
        )


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
        "-s", "--tb=native",
        f"--rootdir={dir_project_root}",
        "--cov=hotkeynet.game.warmane.wlk.talent",
        "--cov-report", "term-missing",
        "--cov-report", f"html:{dir_htmlcov}",
        abspath,
    ]
    subprocess.run(args)
