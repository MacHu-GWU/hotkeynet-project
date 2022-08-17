# -*- coding: utf-8 -*-

import typing as T
import enum

import attr
from attrs_mate import AttrsClass
from jinja2 import Template

from . import tpl
from .enumerate import EnumGetter
from .utils import remove_empty_line


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

    @property
    def title(self) -> str:
        raise NotImplementedError

    def render(self, verbose=False) -> str:
        if verbose:
            print(f"render {self.title} ...")
        return tpl.block_tpl.render(block=self, render=render)


@attr.s
class Script(Block['Script']):
    pass


class SendModeEnum(enum.Enum):
    """
    SendWin, SendFocusWin, SendWinM, SendWinMF, SendWinS, or SendWinSF
    """
    SendWin = "SendWin"
    SendFocusWin = "SendFocusWin"
    SendWinM = "SendWinM"
    SendWinMF = "SendWinMF"
    SendWinS = "SendWinS"
    SendWinSF = "SendWinSF"


@attr.s
class Label(Block['Script']):
    name: str = attr.ib(default=None)
    ip: str = attr.ib(default="local")
    send_mode: str = attr.ib(default=SendModeEnum.SendWinM.value)
    window: str = attr.ib(default=None)

    @property
    def title(self):
        return f"<Label {self.name} {self.ip} {self.send_mode} {self.window}>"


@attr.s
class Command(Block['Command']):
    name: str = attr.ib(default=None)

    @property
    def title(self):
        return f"<Command {self.name}>"


@attr.s
class SendPC(Block['SendPC.tpl']):
    ip: str = attr.ib(default="local")

    @property
    def title(self):
        return f"<SendPC {self.ip}>"


@attr.s
class Run(Block['Run']):
    path: str = attr.ib(default=None)

    @property
    def title(self):
        return f"<Run \"{self.path}\">"


@attr.s
class Hotkey(Block['Hotkey']):
    name: str = attr.ib(default=None)
    key: str = attr.ib(default=None)

    @property
    def title(self):
        return f"<Hotkey {self.key}>"


@attr.s
class Key(Block['Key']):
    key: str = attr.ib(default=None)

    @property
    def title(self):
        return f"<Key {self.key}>"

    @classmethod
    def trigger(cls) -> 'Key':
        return cls(key="%Trigger%")


@attr.s
class SendLabel(Block['SendLabel']):
    name: str = attr.ib(default=None)
    to: T.List[Label] = attr.ib(factory=list)

    @property
    def targets(self) -> str:
        return ", ".join([label.title for label in self.to])

    @property
    def title(self) -> str:
        return f"<SendLabel {self.targets}>"


def render(
    obj: T.Union[Block, str],
    **kwargs
) -> str:
    """
    A global function that take any object as argument and render it.
    """
    if isinstance(obj, Block):
        return obj.render()
    elif isinstance(obj, str):
        return obj
    else:  # pragma: no cover
        raise TypeError
