# -*- coding: utf-8 -*-

from . import (
    raid,
    icc,
    dungeon,
    questing,
    leveling,
    pvp,
    temp,
)


class Mode(raid.Mode,
           icc.Mode,
           dungeon.Mode,
           questing.Mode,
           leveling.Mode,
           pvp.Mode,
           temp.Mode):
    pass
