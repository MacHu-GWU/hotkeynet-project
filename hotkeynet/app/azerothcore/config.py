# -*- coding: utf-8 -*-

"""
对多开游戏的总体配置.
"""

from superjson import json

import attr
from attrs_mate import AttrsClass

from .paths import path_azerothcore_config_json


@attr.s
class Config(AttrsClass):
    """
    :param wow_exe_path: 魔兽世界客户端启动器的绝对路径.
    :param locale: 客户端的语言版本.
    """
    wow_exe_path: str = attr.ib(default=None)
    locale: str = attr.ib(default=None)


config_data = json.load(path_azerothcore_config_json.abspath, verbose=False)
config = Config(**config_data)
