# -*- coding: utf-8 -*-

import os
from hotkeynet.app.warmane.character import (
    CharacterFactory,
    ActiveCharactersFactory,
)


class TestCharacterFactory:
    def test(self):
        for attr in CharacterFactory.__dict__:
            if attr.startswith("make_char"):
                getattr(CharacterFactory, attr)()


class TestActiveCharactersFactory:
    def test(self):
        ActiveCharactersFactory.make_team_solo_dungeon_1_tank_3_dps_1_healer()
        ActiveCharactersFactory.make_team_solo_dungeon_festival_team_1_dk()
        ActiveCharactersFactory.make_team_solo_dungeon_festival_team_2_ss()
        ActiveCharactersFactory.make_team_solo_dungeon_festival_team_3_mix()
        ActiveCharactersFactory.make_team_solo_dungeon_festival_team_4_ms_sm()
        ActiveCharactersFactory.make_team_solo_dungeon_festival_team_5_ms_sm()

        ActiveCharactersFactory.make_team_daily_gold_farm_team_1_druid()
        ActiveCharactersFactory.make_team_daily_gold_farm_team_2_druid()
        ActiveCharactersFactory.make_team_daily_gold_farm_team_3_dk()
        ActiveCharactersFactory.make_team_daily_gold_farm_team_4_ss()
        ActiveCharactersFactory.make_team_daily_gold_farm_team_5_ms()
        ActiveCharactersFactory.make_team_daily_gold_farm_team_6_sm()
        ActiveCharactersFactory.make_team_daily_gold_farm_team_7()


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
