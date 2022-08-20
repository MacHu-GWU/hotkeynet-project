# -*- coding: utf-8 -*-

import os
from hotkeynet.game.wow.model import (
    Account,
    Character,
    Talent,
    TalentCategory,
    Window,
)


class TestWindow:
    def test_make(self):
        window = Window.make(1)
        assert window.label == "w01"
        assert window.title == "WoW01"


class TestCharacter:
    def test_set_method(self):
        window = Window.make(3)
        leader_1_window = Window.make(1)
        leader_2_window = Window.make(2)

        char1 = Character()
        assert char1.is_leader_1 is False
        assert char1.is_leader_2 is False

        char2 = (
            char1
            .set_window(window)
            .set_active()
            .set_inactive()
            .set_is_leader_1()
            .set_not_leader_1()
            .set_is_leader_2()
            .set_not_leader_2()
            .set_leader_1_window(leader_1_window)
            .set_leader_2_window(leader_2_window)
        )
        assert char1 is char2


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
        "--cov=hotkeynet.game.wow.model",
        "--cov-report", "term-missing",
        "--cov-report", f"html:{dir_htmlcov}",
        abspath,
    ]
    subprocess.run(args)
