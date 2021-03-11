# -*- coding: utf-8 -*-

from pathlib_mate import PathCls as Path
from hotkeynet.script import Script
from hotkeynet.projects.warmane.config import (
    Config,
    GameClientConfig,
    ToggleWindowConfig,
    ActiveCharacterConfig,
)
from hotkeynet.projects.warmane.hkn_script.mode import Mode
from hotkeynet.projects.warmane.hkn_script.hkn import build_all


#=== Initialize config
script = Script()
game_client_config = GameClientConfig(
    wow_exe_path=r"D:\HSH\Games\WOW Private\Client\World of Warcraft 3.3.5 enUS (Warman wod models)\Wow.exe",
)
toggle_window_config = ToggleWindowConfig()
active_character_config = ActiveCharacterConfig()
config = Config(
    game_client_config=game_client_config,
    toggle_window_config=toggle_window_config,
    active_character_config=active_character_config,
)

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
build_all(script, config)

Path(__file__).change(new_basename="warmane.js").write_text(
    script.dump(),
    encoding="utf-8",
)
