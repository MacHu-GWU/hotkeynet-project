# -*- coding: utf-8 -*-

import os
from hotkeynet.game.wow.wlk.model import (
    Account,
    Character,
    Window,
    TL, TC,
    OrderedSet,
    char_oset_helper,
)


class TestCharacterOrderedSetHelper:
    def test_set_team_leader_and_tank(self):
        a = Character(
            account=Account(username="multi1", password=""),
            name="a",
            window=Window.make(1),
        ).set_leader_12_and_tank_12()
        b = Character(
            account=Account(username="multi2", password=""),
            name="b",
            window=Window.make(2),
        )
        chars = OrderedSet([a, b])
        assert b.leader_1_window is None
        assert b.leader_2_window is None
        assert b.tank_1_window is None
        assert b.tank_2_window is None

        char_oset_helper.set_team_leader_and_tank(chars)
        assert b.leader_1_window.label == "w01"
        assert b.leader_2_window.label == "w01"
        assert b.tank_1_window.label == "w01"
        assert b.tank_2_window.label == "w01"

    def test_sort_and_filter(self):
        a = Character(
            account=Account(username="multi1", password=""),
            name="a",
            window=Window.make(1),
            talent=TL.warrior_pve_protect,
        )
        b = Character(
            account=Account(username="multi2", password=""),
            name="b",
            window=Window.make(2),
            talent=TL.mage_pve_frost,
        )
        c = Character(
            account=Account(username="multi3", password=""),
            name="c",
            window=Window.make(3),
            talent=TL.priest_pve_holy,
        )
        chars = OrderedSet([b, c, a])

        chars = char_oset_helper.sort_chars_by_window_label(chars)
        assert chars[0].window.label == "w01"

        chars = char_oset_helper.sort_chars_by_window_title(chars)
        assert chars[0].window.label == "w01"

        chars = char_oset_helper.filter_by_talent(chars, tl=TL.warrior_pve_protect)
        assert len(chars) == 1
        assert chars[0].talent == TL.warrior_pve_protect

        chars = char_oset_helper.filter_by_talent_category(chars, tc=TC.tank)
        assert len(chars) == 1
        assert chars[0].talent == TL.warrior_pve_protect


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
