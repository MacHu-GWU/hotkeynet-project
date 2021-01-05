# -*- coding: utf-8 -*-

from hotkeynet.projects.warmane.config import Config

Config.set_mode_10p_batlefury_luxiaofeng_high_gs_team_solo_raid()
# Config.set_mode_18p_luxiaofeng_litgoatss_litgugu_team_winter_graps()

from hotkeynet.projects.warmane.hkn import script
from pathlib_mate import PathCls as Path

Path(__file__).change(new_basename="warmane.js").write_text(
    script.dump(),
    encoding="utf-8",
)
