# -*- coding: utf-8 -*-

import os
from hotkeynet.app.warmane.character import (
    LoginCharactersFactory,
    ActiveCharactersFactory,
    CharacterHelper,
    CharacterFactory,
    TL, TC,
)


class TestCharacterFactory:
    def test(self):
        for attr in CharacterFactory.__class__.__dict__:
            if attr.startswith("make_char"):
                getattr(CharacterFactory, attr)()


class TestLoginCharactersFactory:
    def test(self):
        for attr in LoginCharactersFactory.__class__.__dict__:
            if attr.startswith("make_chars"):
                getattr(LoginCharactersFactory, attr)()


class TestActiveCharactersFactory:
    def test(self):
        for attr in ActiveCharactersFactory.__class__.__dict__:
            if attr.startswith("make_team"):
                getattr(ActiveCharactersFactory, attr)()


class TestCharacterHelper:
    def test(self):
        chars = ActiveCharactersFactory.make_team_solo_dungeon_batlefury_quentin_opiitou_swagsonic_kangliu()
        CharacterHelper.sort_chars_by_window_label(chars)
        CharacterHelper.sort_chars_by_window_title(chars)
        CharacterHelper.filter_by_talent(chars, TL.paladin_pve_protect)
        CharacterHelper.filter_by_talent_category(chars, TC.tank)


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
        "--cov=hotkeynet.app.warmane.character",
        "--cov-report", "term-missing",
        "--cov-report", f"html:{dir_htmlcov}",
        abspath,
    ]
    subprocess.run(args)
