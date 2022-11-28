# -*- coding: utf-8 -*-

import os
from rich import print
import hotkeynet as hk
from hotkeynet.app.azerothcore.mode import (
    dungeon_mode_fact,
    raid_mode_fact,
)
from hotkeynet.tests import run_cov_test


class TestMode:
    def test_launched_windows(self):
        # hk.context.reset()
        # dungeon_mode_fact.x5p_horde_s_abcde.render(verbose=False)
        #
        # hk.context.reset()
        # raid_mode_fact.x10p_core_team.render(verbose=False)

        # hk.context.reset()
        # raid_mode_fact.x10p_naxx_abomination_4th_boss.render(verbose=False)
        #
        hk.context.reset()
        raid_mode_fact.x25p_core_team.render(verbose=True)


if __name__ == "__main__":
    run_cov_test(__file__, "hotkeynet.app.azerothcore.mode")
