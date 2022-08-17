# -*- coding: utf-8 -*-

import typing as T

import attr
from attrs_mate import AttrsClass
from jinja2 import Template

from . import tpl


class Context:
    def __init__(self):
        self.stack: list = list()

    def push(self, obj):
        self.stack.append(obj)

    def pop(self):
        return self.stack.pop()

    @property
    def current(self) -> 'Block':
        return self.stack[-1]


_context = Context()

BLOCK = T.TypeVar("BLOCK")


@attr.s
class Block(AttrsClass, T.Generic[BLOCK]):
    blocks: T.List['Block'] = attr.ib(factory=list)

    def __call__(self) -> BLOCK:
        return self.__enter__()

    def __enter__(self) -> BLOCK:
        _context.push(self)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        _context.pop()

    def __attrs_post_init__(self):
        try:
            _context.current.blocks.append(self)
        except IndexError as e:
            if str(e) == "list index out of range":
                pass
            else:
                raise e

    def _iter_by_type(self, type: T.Type['Block']) -> T.List:
        return [
            block
            for block in self.blocks
            if isinstance(block, type)
        ]

    def iter_label(self) -> T.List['Label']:
        return self._iter_by_type(Label)

    def iter_command(self) -> T.List['Command']:
        return self._iter_by_type(Command)

    def iter_hotkey(self) -> T.List['Hotkey']:
        return self._iter_by_type(Hotkey)

    @property
    def template(self) -> Template:
        raise NotImplementedError

    def render(self) -> str:
        raise NotImplementedError


@attr.s
class Script(Block['Script']):
    pass


@attr.s
class Label(Block['Script']):
    name: str = attr.ib(default=None)
    ip: str = attr.ib(default="local")
    send_mode: str = attr.ib(default="SendWinM")
    window: str = attr.ib(default=None)


@attr.s
class Command(Block['Command']):
    _tpl = tpl.command_tpl

    name: str = attr.ib(default=None)


@attr.s
class SendPC(Block['SendPC']):
    name: str = attr.ib(default=None)


@attr.s
class Hotkey(Block['Hotkey']):
    name: str = attr.ib(default=None)
    key: str = attr.ib(default=None)


@attr.s
class Key(Block['Key']):
    name: str = attr.ib(default=None)


@attr.s
class SendLabel(Block['SendLabel']):
    name: str = attr.ib(default=None)
    to: T.List[Label] = attr.ib(factory=list)
