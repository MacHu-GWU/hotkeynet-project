# -*- coding: utf-8 -*-

"""
Remove all not used label defined in any SendLabel.to object.
"""

from ._config_and_script import config, script
from ....script import SendLabel

all_labels = set(config.lbs_all())

for hotkey in script.hotkeys.values():
    for action in hotkey.actions:
        if isinstance(action, SendLabel):
            labels1 = action.to
            labels2 = list(action.to)
            for label in labels2:
                if label not in all_labels:
                    labels1.remove(label)
            action.to = labels1
