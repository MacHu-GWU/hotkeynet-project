# -*- coding: utf-8 -*-

from . import (
    raid,
    dungeon,
    questing,
    leveling,
    temp,
)


class Mode(raid.Mode,
           dungeon.Mode,
           questing.Mode,
           leveling.Mode,
           temp.Mode):
    pass
