# -*- coding: utf-8 -*-

from collections import OrderedDict

from ..config import Config
from ..constant.windows import window_list
from ....script import Script


def build_all(script: Script, config: Config):
    script.labels = OrderedDict([
        (window.label, window.title)
        for window in window_list[:config.game_client_config.n_windows]
    ])
