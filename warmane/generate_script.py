# -*- coding: utf-8 -*-

"""
创建一个 Hotkeynet Script 的流程如下:

1. 初始化 Config, 里面主要是一些变量的值的定义, 比如 各个职业所对应的 label.
    用 Config.set_mode_xxx() 方法来对其进行修改. 这个 xxx 要反映出该模式是做什么的.
2. 然后 import script 对象, script 是一个基础模板, 定义了 99% 的情况下各个职业需要做什么
3. 最后 对 script 对象中的 command hotkey 等进行一些动态的修改.
4. 于是就可以将 script dump 到文件了.
"""
from hotkeynet.projects.warmane.config import Config

# Config.set_mode_temp()

#--- 团队副本单刷
# Config.set_mode_10w_10p_batlefury_luxiaofeng_high_gs_team_solo_raid()
# Config.set_mode_10w_10p_batlefury_luxiaofeng_high_gs_team_solo_raid_onyxia()
# Config.set_mode_18p_batlefury_luxiaofeng_litgugu_team_solo_raid()

#--- 5人随机副本单刷 ---
# Config.set_mode_18w_5p_elite_team_batlefury_quentin_opiitou_swagsonic_kangliu()
Config.set_mode_18w_5p_glowyy_litgugu_abcd()
# Config.set_mode_18w_5p_glowyy_litgoatss_abc_bunnysisters()
# Config.set_mode_18w_5p_glowyy_litgoatss_de_laoshou_bunnysisters()
# Config.set_mode_18w_5p_glowyy_litgoatdk_abc_bunnysisters()
# Config.set_mode_18w_5p_glowyy_litgoatdk_de_ganjj_bunnysisters()

# Config.set_mode_18p_luxiaofeng_litgoatss_litgugu_team_winter_graps()

# Config.set_mode_18w_5p_batlefury_bunnysister_kangliu_kindhearted_kapacuk()


# Config.set_mode_18p_batlefury_kangliu_litgugu_team_solo_voa()

#--- 10人周常任务单刷 ---
# Config.set_mode_18w_10p_batlefury_litgoatssb_opiitou_swagsonic_litgoatsse_ganjj_litgugu_a_to_d_solo_weekly()
# Config.set_mode_18w_10p_luxiaofeng_glowyy_bunny_kindhearted_kapacuk_litgoatss_a_to_e_quentin_kangliu_solo_weekly()
# Config.set_mode_18w_5p_litgoatdk_abcde_solo_weekly()

#--- 冬拥湖周常任务单刷 ---
# Config.set_mode_18w_18p_luxiaofeng_litgoatss_litgugu_team_winter_graps()

# Config.set_mode_18w_18p_boomy_wild()

#--- 10开分两组日常任务刷钱 ---
# Config.set_mode_10w_10p_batle_to_kangliu_and_bunny_litgugu_a_to_d_daily_quest_gold_farm()

#--- 5人1带4升级
# Config.set_mode_18w_14p_opiitou_and_batlefury_carry_leveling()


from hotkeynet.projects.warmane.hkn import script
from pathlib_mate import PathCls as Path

Path(__file__).change(new_basename="warmane.js").write_text(
    script.dump(),
    encoding="utf-8",
)
