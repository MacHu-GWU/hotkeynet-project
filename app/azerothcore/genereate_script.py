# -*- coding: utf-8 -*-

from hotkeynet.app.azerothcore.mode import mode_fact

# -----------------------------------------------------------------------------
# Azerothcore
# -----------------------------------------------------------------------------
mode = mode_fact.solo_raid_10p_core_team()
# mode = mode_fact.solo_raid_10p_naxx_abomination_4th_boss()

# -----------------------------------------------------------------------------
# Don't Touch
# -----------------------------------------------------------------------------
mode.dump(verbose=True)
