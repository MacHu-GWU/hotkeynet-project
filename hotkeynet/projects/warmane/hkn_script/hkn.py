# -*- coding: utf-8 -*-

from ..config import Config
from ....script import Script
from . import (
    cmd_g01_window_and_login,
    labels,
)


def build_all(script: Script, config: Config):
    cmd_g01_window_and_login.build_all(script, config)
    labels.build_all(script, config)
