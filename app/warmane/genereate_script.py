# -*- coding: utf-8 -*-

from hotkeynet.app.warmane.mode import Mode

# -----------------------------------------------------------------------------
# Warmane
# -----------------------------------------------------------------------------

# mode = Mode.use_solo_dungeon_batlefury_quentin_opiitou_swagsonic_kangliu()
# mode = Mode.use_solo_raid_10p_batlefury_luxiaofeng_core_team()

# --- Montly Login ---
mode = Mode.use_22p_monthly_login_1()
# mode = Mode.use_22p_monthly_login_2()

# -----------------------------------------------------------------------------
# Lordaeron
# -----------------------------------------------------------------------------
# mode = Mode.use_solo_dungeon_5p_lgqs_abcde()

# -----------------------------------------------------------------------------
# Don't Touch
# -----------------------------------------------------------------------------
mode.dump(verbose=True)
