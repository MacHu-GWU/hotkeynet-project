# -*- coding: utf-8 -*-

from hotkeynet.projects.warmane.config import (
    Config,
    GameClientConfig,
    ToggleWindowConfig,
    ActiveCharacterConfig,
)
from hotkeynet.script import Script

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
