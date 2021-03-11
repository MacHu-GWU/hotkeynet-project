# -*- coding: utf-8 -*-

from .script import script
from .config_ import Config
from collections import OrderedDict

script.labels = OrderedDict([
    ("w{}".format(index+1), "WoW{}".format(index+1))
    for index, _ in enumerate(Config.Windows.launch_and_rename_windows)
])
