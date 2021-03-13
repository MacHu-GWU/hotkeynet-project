# -*- coding: utf-8 -*-

from collections import OrderedDict

from ._config_and_script import config, script
from ..config import Config
from ..constant.windows import window_list
from ....script import Script


def build_all_labels(script: Script, config: Config):
    script.labels = OrderedDict([
        (window.label, window.title)
        for window in window_list[:config.game_client_config.n_windows]
    ])


build_all_labels(script, config)