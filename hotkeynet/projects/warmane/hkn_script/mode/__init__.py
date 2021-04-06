# -*- coding: utf-8 -*-

from . import (
    raid,
    dungeon,
    questing,
    leveling,
    pvp,
    temp,
)


class Mode(raid.Mode,
           dungeon.Mode,
           questing.Mode,
           leveling.Mode,
           pvp.Mode,
           temp.Mode):
    pass
