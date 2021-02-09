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
# Config.set_mode_10p_batlefury_luxiaofeng_high_gs_team_solo_raid()
Config.set_mode_10p_batlefury_luxiaofeng_high_gs_team_solo_raid_onyxia()

# Config.set_mode_18p_luxiaofeng_litgoatss_litgugu_team_winter_graps()
# Config.set_mode_18p_batlefury_luxiaofeng_litgugu_team_solo_raid()
# Config.set_mode_18p_batlefury_kangliu_litgugu_team_solo_voa()

from hotkeynet.projects.warmane.hkn import script
from pathlib_mate import PathCls as Path

Path(__file__).change(new_basename="warmane.js").write_text(
    script.dump(),
    encoding="utf-8",
)
