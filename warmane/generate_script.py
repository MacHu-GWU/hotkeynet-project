# -*- coding: utf-8 -*-

from pathlib_mate import PathCls as Path
from hotkeynet.projects.warmane.hkn_script._config_and_script import config, script
from hotkeynet.projects.warmane.hkn_script.mode import Mode

#=== Set Combat Mode
#--- Temp

#--- Solo Raid

### General
# Mode.set_mode_solo_raid_10p_batlefury_flydps_core_team(config)
# Mode.set_mode_solo_raid_22p_batlefury_flydps_4_druid_4_priest_4_shaman_core_team(config)

### Naxx

### VOA

### Onyxia

### ICC

#--- Solo RDF
# Mode.set_mode_solo_dungeon_batlefury_quentin_opiitou_swagsonic_kangliu(config)

#--- Leveling


#--- Questing

#--- 灰熊丘陵日常
# Mode.set_mode_questing_grizzly_hill_daily_gold_farm_team0_fatmulti_1_to_5(config)
# Mode.set_mode_questing_grizzly_hill_daily_gold_farm_team1_litgugu_druid(config)
# Mode.set_mode_questing_grizzly_hill_daily_gold_farm_team2_litgoat_priest(config)
Mode.set_mode_questing_grizzly_hill_daily_gold_farm_team3_litgoat_shaman(config)

#--- 小队一起做杂七杂八的任务, 冲声望等
Mode.set_mode_questing_5_ppl_litgoat_warlock_team(config)
Mode.set_mode_questing_5_ppl_litgoat_dk_team(config)
Mode.set_mode_questing_4_ppl_litgugu_druid_team(config)
Mode.set_mode_questing_5_ppl_lgms_priest_glowyy_team(config)
Mode.set_mode_questing_5_ppl_lgsm_shaman_laoshou_team(config)


#--- 冬拥湖周常
# Mode.set_mode_questing_wintergraps_team1(config)

#=== Build Script
from hotkeynet.projects.warmane.hkn_script import hkn
_ = hkn

config.post_hook(config, script)


#=== Dump Script
Path(__file__).change(new_basename="warmane.js").write_text(
    script.dump(),
    encoding="utf-8",
)
