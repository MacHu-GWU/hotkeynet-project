# -*- coding: utf-8 -*-

import attr

from .. import model
from .talent import Talent


@attr.s
class Character(model.Character):
    talent: Talent = attr.ib(default=None)

    is_tank1: bool = attr.ib(default=False)
    is_tank2: bool = attr.ib(default=False)
    is_dr_pala1: bool = attr.ib(default=False)
    is_dr_pala2: bool = attr.ib(default=False)

    def set_tank1(self) -> 'Character':
        self.is_tank1 = True
        return self

    def set_tank2(self) -> 'Character':
        self.is_tank2 = True
        return self

    def set_dr_pala1(self) -> 'Character':
        self.is_dr_pala1 = True
        return self

    def set_dr_pala2(self) -> 'Character':
        self.is_dr_pala2 = True
        return self
