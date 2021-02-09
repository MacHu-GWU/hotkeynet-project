# -*- coding: utf-8 -*-

from .script import script
from .config import Config
from ...script import SendLabel

for hotkey in script.hotkeys.values():
    for action in hotkey.actions:
        if isinstance(action, SendLabel):
            labels1 = action.to
            labels2 = list(action.to)
            for label in labels2:
                if label not in Config.SendLabelTo.all():
                    labels1.remove(label)
            action.to = labels1
