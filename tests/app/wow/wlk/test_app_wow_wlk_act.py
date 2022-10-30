# -*- coding: utf-8 -*-

import os
import pytest
from hotkeynet.app.wow.wlk import act


class TestPaladin:
    def test(self):
        _ = act.paladin_protection.Hammer_of_the_Righteous()
        _ = act.paladin_retribution.Divine_Storm()
        _ = act.paladin_holy.Holy_Shock()

        with pytest.raises(ValueError):
            act.paladin_holy.Blessing_of_Sanctuary()


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
        "--cov=hotkeynet.app.wow.wlk.act",
        "--cov-report", "term-missing",
        "--cov-report", f"html:{dir_htmlcov}",
        abspath,
    ]
    subprocess.run(args)
