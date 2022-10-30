# -*- coding: utf-8 -*-

import os
from hotkeynet.act_factory import ActFactory, click_name as CN
from hotkeynet import KN


class Paladin(ActFactory):
    holy_light = KN.KEY_1
    flash_of_light = KN.KEY_2
    beacon_of_light = CN.left
    holy_shock = CN.shift_left_click


paladin = Paladin()


def test():
    k11 = paladin.holy_light()
    k12 = paladin.holy_light()
    k21 = paladin.flash_of_light()
    k22 = paladin.flash_of_light()
    k31 = paladin.beacon_of_light()
    k32 = paladin.beacon_of_light()
    k4 = paladin.holy_shock()

    assert id(k11) != id(k12)
    assert id(k21) != id(k22)
    assert id(k31) != id(k32)

    assert k11.key == KN.KEY_1
    assert k21.key == KN.KEY_2

    assert k31.button == KN.MOUSE_LButton
    assert len(k4) == 4


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
        "--cov=hotkeynet.act_factory",
        "--cov-report", "term-missing",
        "--cov-report", f"html:{dir_htmlcov}",
        abspath,
    ]
    subprocess.run(args)
