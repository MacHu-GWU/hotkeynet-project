# -*- coding: utf-8 -*-

"""

"""


class ActFactoryMeta(type):
    """
    meta class of ActFactory
    """

    def __new__(cls, name, bases, attrs):
        for k, v in attrs.items():
            if not k.startswith("_"):
                @property
                def func(self) -> str:
                    return v

                attrs[k] = func
        klass = super(ActFactoryMeta, cls).__new__(cls, name, bases, attrs)
        return klass


class ActFactory(metaclass=ActFactoryMeta):
    pass
