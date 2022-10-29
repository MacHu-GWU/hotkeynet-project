# -*- coding: utf-8 -*-

from hotkeynet.app.warmane.mode import (
    trade_mode_fact,
    dungeon_mode_fact,
    raid_mode_fact,
)

# -----------------------------------------------------------------------------
# Warmane
# -----------------------------------------------------------------------------

# --- Dungeon
# mode = dungeon_mode_fact.use_solo_dungeon_batlefury_quentin_opiitou_swagsonic_kangliu()

# --- Raid
# mode = raid_mode_fact.use_solo_raid_10p_batlefury_luxiaofeng_core_team()

# --- Montly Login ---
# mode = trade_mode_fact.use_22p_monthly_login_1()
# mode = trade_mode_fact.use_22p_monthly_login_2()
mode = trade_mode_fact.use_5p_daily_alchemy_transmute()

# --- Festival daily ---
# mode = dungeon_mode_fact.use_5p_team_solo_dungeon_festival_team_1_dk()
# mode = dungeon_mode_fact.use_5p_team_solo_dungeon_festival_team_2_ss()
# mode = dungeon_mode_fact.use_5p_team_solo_dungeon_festival_team_3_mix()

# mode = dungeon_mode_fact.use_5p_team_solo_festival_team_4_ms_sm()
# mode = dungeon_mode_fact.use_5p_team_solo_festival_team_5_ms_sm()
# mode = dungeon_mode_fact.use_5p_team_solo_festival_team_6_litgugu_efgh()

# -----------------------------------------------------------------------------
# Lordaeron
# -----------------------------------------------------------------------------
# mode = dungeon_mode_fact.use_5p_lgqs_abcde_leveling()

# -----------------------------------------------------------------------------
# Don't Touch
# -----------------------------------------------------------------------------
mode.dump(verbose=True)
