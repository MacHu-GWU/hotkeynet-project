# -*- coding: utf-8 -*-

from hotkeynet.app.tauri.mode import Mode

# -----------------------------------------------------------------------------
# Evermoon
# -----------------------------------------------------------------------------
mode = Mode.use_solo_dungeon_carrot_flower_team()

# -----------------------------------------------------------------------------
# Don't Touch
# -----------------------------------------------------------------------------
mode.dump(verbose=True)
