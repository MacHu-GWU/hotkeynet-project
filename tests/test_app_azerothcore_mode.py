# -*- coding: utf-8 -*-

import os
from rich import print
import hotkeynet as hk
from hotkeynet.app.azerothcore.mode import Mode


class TestMode:
    def test_launched_windows(self):
        hk.context.reset()
        mode = Mode.use_solo_dungeon_qs_abcde()
        mode.hkn_script.script.render(verbose=False),
        print(mode.launched_windows)


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
        "--cov=hotkeynet.app.azerothcore.mode",
        "--cov-report", "term-missing",
        "--cov-report", f"html:{dir_htmlcov}",
        abspath,
    ]
    subprocess.run(args)
