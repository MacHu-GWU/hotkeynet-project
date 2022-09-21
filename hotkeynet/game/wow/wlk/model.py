# -*- coding: utf-8 -*-

import attr

from .. import model
from .talent import Talent


@attr.s
class Character(model.Character):
    """
    :param talent: 角色天赋
    """
    talent: Talent = attr.ib(default=None)

    is_tank_1: bool = attr.ib(default=False)
    is_tank_2: bool = attr.ib(default=False)
    tank_1_window: model.Window = attr.ib(default=None)
    tank_2_window: model.Window = attr.ib(default=None)

    is_dr_pala_1: bool = attr.ib(default=False)
    is_dr_pala_2: bool = attr.ib(default=False)

    def set_tank_1(self) -> 'Character':
        self.is_tank_1 = True
        return self

    def set_not_tank_1(self) -> 'Character':
        self.is_tank_1 = False
        return self

    def set_tank_2(self) -> 'Character':
        self.is_tank_2 = True
        return self

    def set_not_tank_2(self) -> 'Character':
        self.is_tank_2 = False
        return self

    def set_tank_1_window(self, window: model.Window) -> 'Character':
        self.tank_1_window = window
        return self

    def set_tank_2_window(self, window: model.Window) -> 'Character':
        self.tank_2_window = window
        return self

    def set_dr_pala_1(self) -> 'Character':
        self.is_dr_pala_1 = True
        return self

    def set_dr_pala_2(self) -> 'Character':
        self.is_dr_pala_2 = True
        return self

    def set_tank_12_and_leader_12(self) -> 'Character':
        self.set_tank_1()
        self.set_is_leader_1()
        self.set_tank_2()
        self.set_is_leader_2()
        return self