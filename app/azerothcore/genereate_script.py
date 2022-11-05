# -*- coding: utf-8 -*-

from hotkeynet.app.azerothcore.mode import (
    dungeon_mode_fact,
    raid_mode_fact,
)

# -----------------------------------------------------------------------------
# Azerothcore - Alliance - Raid
# -----------------------------------------------------------------------------
# mode = raid_mode_fact.x10p_core_team
# mode = raid_mode_fact.x10p_naxx_abomination_4th_boss
mode = raid_mode_fact.x25p_core_team


# -----------------------------------------------------------------------------
# Horde
# -----------------------------------------------------------------------------
# mode = dungeon_mode_fact.solo_dungeon_5p_horde_s_abcde

# -----------------------------------------------------------------------------
# Don't Touch
# -----------------------------------------------------------------------------
# mode.dump(verbose=True)
mode.dump(verbose=False)
