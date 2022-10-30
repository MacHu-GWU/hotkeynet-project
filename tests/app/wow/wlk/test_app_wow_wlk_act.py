# -*- coding: utf-8 -*-

import os
from hotkeynet.app.wow.wlk import act
from hotkeynet.app.wow.wlk.act.paladin import Paladin

class TestPaladin:
    def test(self):
        # print("")
        # print(type(Paladin().Holy_Light))
        # print(Paladin().Holy_Light)
        print(act.paladin.Holy_Light())
        print(act.paladin_protection.Hammer_of_the_Righteous())
        print(act.paladin_holy.HB_Holy_Light())

        print(act.paladin_holy.Blessing_of_Sanctuary())
        pass



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
