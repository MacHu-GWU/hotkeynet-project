# -*- coding: utf-8 -*-

from pathlib_mate import PathCls as Path
from hotkeynet.projects.warmane.hkn_script._config_and_script import config, script
from hotkeynet.projects.warmane.hkn_script.mode import Mode

#=== Set Combat Mode
#--- Temp
# Mode.set_mode_temp(config)

#------------------------------------------------------------------------------
#                                   Solo RAID
#------------------------------------------------------------------------------

### General
# Mode.set_mode_solo_raid_10p_batlefury_luxiaofeng_core_team(config)
# Mode.set_mode_solo_raid_22p_batlefury_flydps_4_druid_4_priest_4_shaman_core_team(config)

### Naxx
# Mode.set_mode_solo_raid_10p_naxx10_team2_batlefury_litgugu_abcd(config)
# Mode.set_mode_solo_raid_10p_naxx10_team3_glowyy_litgoatss_abcd(config)
# Mode.set_mode_solo_raid_25p_naxx25_full_run(config)

### UDR

# Mode.set_mode_solo_raid_10p_udr10_team1_kindhearted_litgoatdk_lgsm(config)
# Mode.set_mode_solo_raid_25p_udr25_team2_litgoatss_litgugua_lgms(config)

### VOA 10 宝库摸奖
# Mode.set_mode_solo_raid_10p_voa10_team1_batlefury_team(config)
# Mode.set_mode_solo_raid_10p_voa10_team2_glowyy_team(config)
# Mode.set_mode_solo_raid_10p_voa10_team4_luxiaofeng_2_priest_2_shaman_team(config)
# Mode.set_mode_solo_raid_10p_voa10_team5_flydps_2_priest_2_shaman_team(config)

### VOA 25 宝库摸奖
# Mode.set_mode_solo_raid_22p_voa25_batlefury_2_priest_2_shaman_team1(config)
# Mode.set_mode_solo_raid_22p_voa25_litgoatdk_2_priest_2_shaman_team2(config)
# Mode.set_mode_solo_raid_22p_voa25_team3(config)

### Onyxia

### ICC

# Mode.set_mode_solo_raid_10p_icc10_lich_king_team(config)

#------------------------------------------------------------------------------
#                                   Solo RDF
#------------------------------------------------------------------------------
# Mode.set_mode_solo_dungeon_batlefury_quentin_opiitou_swagsonic_kangliu(config)
# Mode.set_mode_solo_dungeon_batlefury_litgugu_abcd(config)

# Mode.set_mode_solo_dungeon_litgoatdk_abcd_bunnysisters(config)
# Mode.set_mode_solo_dungeon_litgoatdk_abcd_glowyy(config)

# Mode.set_mode_solo_dungeon_glowyy_and_litgugu_abcd(config)
# Mode.set_mode_solo_dungeon_batlefury_carry_4_priest(config)
Mode.set_mode_solo_dungeon_batlefury_carry_4_shaman(config)

# Naxx

# Mode.set_mode_solo_raid_10p_naxx10_team4_lgms(config)
# Mode.set_mode_solo_raid_10p_naxx10_team5_lgsm(config)
# Mode.set_mode_solo_raid_10p_naxx10_team6_temp(config)

#---

#--- Leveling
# Mode.set_mode_leveling_two_team_carry_in_dungeon(config)

#------------------------------------------------------------------------------
#                                   Questing
#------------------------------------------------------------------------------

#--- 灰熊丘陵日常 Grizzily Hill Daily Quest
# Mode.set_mode_questing_grizzly_hill_daily_gold_farm_team0_fatmulti_1_to_5(config)
#
# Mode.set_mode_questing_grizzly_hill_daily_gold_farm_team1_litgugu_druid(config)
# Mode.set_mode_questing_grizzly_hill_daily_gold_farm_team2_litgoat_ss_and_ganjj_priest(config)
# Mode.set_mode_questing_grizzly_hill_daily_gold_farm_team3_litgoat_dk_and_laoshou_shaman(config)
#
# Mode.set_mode_questing_4_ppl_litgugu_efgh_luxiaofeng_druid_team(config)


#--- 冬拥湖周常 Wintergraps Weekly Quest
# Mode.set_mode_questing_5_ppl_batlefury_team(config)              # Paladin Main Team
# Mode.set_mode_questing_5_ppl_litgoat_warlock_team(config)         # Warlock
# Mode.set_mode_questing_5_ppl_litgoat_dk_team(config)              # DK
#
# Mode.set_mode_questing_4_ppl_litgugu_abcd_bunnysisters_druid_team(config) # 5 Druid PK
# # Mode.set_mode_pvp_wintergrasp_wg_5_ppl_lgms_priest_ganjj_team(config) # Priest
# Mode.set_mode_pvp_wintergrasp_wg_5_ppl_lgsm_shaman_laoshou_team(config) # Shaman
#
# Mode.set_mode_questing_4_ppl_litgugu_efgh_luxiaofeng_druid_team(config)

#------------------------------------------------------------------------------
#                                   PvP
#------------------------------------------------------------------------------
# Mode.set_mode_questing_4_ppl_litgugu_abcd_bunnysisters_druid_team(config) # 5 Druid PK

# Mode.set_mode_questing_4_ppl_litgugu_efgh_bunnysisters_druid_team(config) # 5 Druid PK

# Mode.set_mode_pvp_wintergraps_team1(config)

# Mode.set_mode_pvp_wintergrasp_wg_5_ppl_lgms_priest_ganjj_team(config) # Priest
# Mode.set_mode_pvp_wintergrasp_wg_5_ppl_lgsm_shaman_laoshou_team(config) # Shaman


#=== Build Script
from hotkeynet.projects.warmane.hkn_script import hkn
_ = hkn

if isinstance(config.post_hook, list):
    for post_hook in config.post_hook:
        post_hook(config, script)
else:
    config.post_hook(config, script)


#=== Dump Script
Path(__file__).change(new_basename="warmane.js").write_text(
    script.dump(),
    encoding="utf-8",
)