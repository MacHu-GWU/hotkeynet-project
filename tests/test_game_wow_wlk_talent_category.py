# -*- coding: utf-8 -*-

import os

from hotkeynet.game.wow.wlk.talent_category import TalentCategory


class TestTalentCategory:
    def test_name_is_string_value_is_int(self):
        assert TalentCategory.warrior_tank.name == "warrior_tank"
        assert isinstance(TalentCategory.warrior_tank.value, int)

    def test_sortable(self):
        talent_category_list = [
            TalentCategory.tank,
            TalentCategory.dps,
            TalentCategory.healer
        ]
        talent_category_list.sort()

        talent_category_code_list = [t.value for t in talent_category_list]
        talent_category_code_list.sort()
        assert (
            talent_category_code_list[1] > talent_category_code_list[0]
            and talent_category_code_list[2] > talent_category_code_list[1]
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
        "-s", "--tb=native", "-vv",
        f"--rootdir={dir_project_root}",
        "--cov=hotkeynet.game.wow.wlk.talent_category",
        "--cov-report", "term-missing",
        "--cov-report", f"html:{dir_htmlcov}",
        abspath,
    ]
    subprocess.run(args)
