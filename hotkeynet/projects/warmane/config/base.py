# -*- coding: utf-8 -*-

import attr


@attr.s
class BaseConfig:
    def validate(self):
        raise NotImplementedError
