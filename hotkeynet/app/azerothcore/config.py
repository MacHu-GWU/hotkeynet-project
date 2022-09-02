# -*- coding: utf-8 -*-

from superjson import json

import attr
from attrs_mate import AttrsClass

from .paths import path_azerothcore_config_json


@attr.s
class Config(AttrsClass):
    wow_exe_path: str = attr.ib(default=None)


config_data = json.load(path_azerothcore_config_json.abspath, verbose=False)
config = Config(**config_data)
