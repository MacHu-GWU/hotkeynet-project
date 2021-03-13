# -*- coding: utf-8 -*-

from . import (
    raid,
    dungeon,
    questing,
)


class Mode(raid.Mode,
           dungeon.Mode,
           questing.Mode):
    pass
