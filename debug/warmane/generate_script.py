# -*- coding: utf-8 -*-

from pathlib_mate import PathCls as Path
from hotkeynet.projects.warmane.hkn_script._config_and_script import config, script
from hotkeynet.projects.warmane.hkn_script.mode import Mode

#=== Set Combat Mode
#--- Temp

#--- Solo Raid

# General
Mode.set_mode_solo_raid_10p_batlefury_flydps_core_team(config)

# Naxx

# VOA

# Onyxia

# ICC

#--- Leveling


#=== Build Script
from hotkeynet.projects.warmane.hkn_script import hkn
_ = hkn


#=== Dump Script
Path(__file__).change(new_basename="warmane.js").write_text(
    script.dump(),
    encoding="utf-8",
)
