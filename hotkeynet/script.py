# -*- coding: utf-8 -*-

import typing as T
import enum
from functools import cached_property

import attr
from attrs_mate import AttrsClass
from jinja2 import Template

from . import keyname as KN
from . import tpl
from .enumerate import EnumHelper
from .utils import remove_empty_line


class Context:
    def __init__(self):
        self.stack: list = list()
        self.auto_name_index: T.Dict[str, int] = {
            "Command": 0,
            "Hotkey": 0,
        }

    def push(self, obj):
        self.stack.append(obj)

    def pop(self):
        return self.stack.pop()

    @property
    def current(self) -> 'Block':
        return self.stack[-1]

    def _auto_name(self, block_type: str) -> str:
        name = f"{block_type}{str(self.auto_name_index[block_type] + 1).zfill(3)}"
        self.auto_name_index[block_type] += 1
        return name

    def auto_command_name(self) -> str:
        return self._auto_name("Command")

    def auto_hotkey_name(self) -> str:
        return self._auto_name("Hotkey")

    def auto_movement_hotkey_name(self) -> str:
        return self._auto_name("MovementHotkey")


context = Context()

BLOCK = T.TypeVar("BLOCK")


@attr.s
class Block(AttrsClass, T.Generic[BLOCK]):
    blocks: T.List['Block'] = attr.ib(factory=list)

    def __call__(self) -> BLOCK:
        return self.__enter__()

    def __enter__(self) -> BLOCK:
        context.push(self)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        context.pop()

    def __attrs_post_init__(self):
        try:
            context.current.blocks.append(self)
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

    def _are_sub_blocks_all_null(self) -> bool:
        return all([block.is_null() for block in self.blocks])

    def is_null(self) -> bool:
        return False

    def render(self, verbose=False) -> str:
        if verbose:
            print(f"render {self.title} ...")
        if self.is_null():
            return ""
        else:
            return tpl.block_tpl.render(
                block=self,
                render=render,
                verbose=verbose,
            )


@attr.s
class Script(Block['Script']):
    @property
    def title(self) -> str:
        return ""

    def render(self, verbose=False) -> str:
        if self.is_null():
            return ""
        else:
            return remove_empty_line(
                tpl.script_tpl.render(
                    block=self,
                    render=render,
                    verbose=verbose,
                )
            )


class SendModeEnum(enum.Enum):
    SendWin = "SendWin"
    SendFocusWin = "SendFocusWin"
    SendWinM = "SendWinM"
    SendWinMF = "SendWinMF"
    SendWinS = "SendWinS"
    SendWinSF = "SendWinSF"


@attr.s
class Label(Block['Script']):
    name: str = attr.ib(default=None)
    window: str = attr.ib(default=None)
    ip: str = attr.ib(default="local")
    send_mode: str = attr.ib(default=SendModeEnum.SendWinM.value)

    @classmethod
    def make(
        cls,
        name: str,
        window: str,
        ip: str = "local",
        send_mode: str = SendModeEnum.SendWinM.value,
    ) -> 'Label':
        return cls(name=name, window=window, ip=ip, send_mode=send_mode)

    @property
    def title(self):
        return f"<Label {self.name} {self.ip} {self.send_mode} {self.window}>"

    def is_null(self) -> bool:
        return self.name is None


@attr.s
class Command(Block['Command']):
    name: str = attr.ib(factory=context.auto_command_name)

    @classmethod
    def make(cls, name: str) -> 'Command':
        return cls(name=name)

    @property
    def title(self):
        return f"<Command {self.name}>"

    def is_null(self) -> bool:
        return self._are_sub_blocks_all_null()

    def call(self, args: T.List[str]) -> 'CallCommand':
        return CallCommand(cmd=self, args=args)


class CommandArgEnum:
    Arg1 = "%1%"
    Arg2 = "%2%"
    Arg3 = "%3%"
    Arg4 = "%4%"
    Arg5 = "%5%"
    Arg6 = "%6%"
    Arg7 = "%7%"
    Arg8 = "%8%"
    Arg9 = "%9%"
    Arg10 = "%10%"

    @classmethod
    def is_arg(cls, arg: str) -> bool:
        return (arg.startswith("%") and arg.endswith("%"))

    @classmethod
    def encode_arg(cls, arg: str) -> str:
        if cls.is_arg(arg):
            return arg
        else:
            return f"\"{arg}\""


@attr.s
class CallCommand(Block['Command']):
    cmd: T.Union[str, Command] = attr.ib(default=None)
    args: T.List[str] = attr.ib(factory=list)

    @property
    def cmd_name(self) -> str:
        if isinstance(self.cmd, Command):
            return self.cmd.name
        else:
            return self.cmd

    @property
    def title(self):
        if len(self.args) == 0:
            return f"<{self.cmd_name}"
        else:
            return "<{cmd_name} {args}>".format(
                cmd_name=self.cmd_name,
                args=" ".join(self.args),
            )


@attr.s
class SendPC(Block['SendPC.tpl']):
    ip: str = attr.ib(default="local")

    @classmethod
    def make(cls, ip: str) -> 'SendPC':
        return cls(ip=ip)

    @property
    def title(self):
        return f"<SendPC {self.ip}>"

    def is_null(self) -> bool:
        return self.ip is None


@attr.s
class Run(Block['Run']):
    path: str = attr.ib(default=None)

    @classmethod
    def make(cls, path: str) -> 'Run':
        return cls(path=path)

    @property
    def title(self):
        return f"<Run {CommandArgEnum.encode_arg(self.path)}>"

    def is_null(self) -> bool:
        return self.path is None


@attr.s
class Hotkey(Block['Hotkey']):
    name: str = attr.ib(factory=context.auto_hotkey_name)
    key: str = attr.ib(default=None)

    @property
    def title(self):
        return f"<Hotkey {self.key}>"

    def is_null(self) -> bool:
        return (self.key is None) or self._are_sub_blocks_all_null()


@attr.s
class MovementHotkey(Block['MovementHotkey']):
    name: str = attr.ib(factory=context.auto_movement_hotkey_name)
    key: str = attr.ib(default=None)

    @property
    def title(self) -> str:
        return f"<MovementHotkey {self.key}>"

    def is_null(self) -> bool:
        return (self.key is None) or self._are_sub_blocks_all_null()


@attr.s
class Key(Block['Key']):
    key: str = attr.ib(default=None)

    @property
    def title(self):
        return f"<Key {self.key}>"

    @classmethod
    def make(cls, key: str) -> 'Key':
        return cls(key=key)

    @classmethod
    def trigger(cls) -> 'Key':
        return cls(key="%Trigger%")


@attr.s
class KeyUp(Block['KeyUp']):
    key: str = attr.ib(default=None)

    @property
    def title(self):
        return f"<KeyUp {self.key}>"


@attr.s
class KeyDown(Block['KeyDown']):
    key: str = attr.ib(default=None)

    @property
    def title(self):
        return f"<KeyDown {self.key}>"


@attr.s
class SendLabel(Block['SendLabel']):
    name: str = attr.ib(default=None)
    to: T.List[Label] = attr.ib(factory=list)

    @property
    def targets(self) -> str:
        return ", ".join([label.name for label in self.to])

    @property
    def title(self) -> str:
        return f"<SendLabel {self.targets}>"

    def is_null(self) -> bool:
        return (len(self.to) == 0) or self._are_sub_blocks_all_null()


class MouseButtonEnum(enum.Enum):
    LButton = "LButton"
    MButton = "MButton"
    RButton = "RButton"
    Button4 = "Button4"
    Button5 = "Button5"


@attr.s
class Mouse(Block['Mouse']):
    """
    Click Mouse action
    """
    button: str = attr.ib(default=None)
    # Down, Up, Both, or NoClick
    stroke: str = attr.ib(default="")
    # Window or Screen
    target: str = attr.ib(default="")
    # NoMove, # #, Dupe, Scale, #% #%, ±# ±#
    mode: str = attr.ib(default="")
    # Restore or NoRestore
    restore: str = attr.ib(default="")

    def set_stroke_down(self) -> 'Mouse':
        self.stroke = "Down"
        return self

    def set_stroke_as_up(self) -> 'Mouse':
        self.stroke = "Up"
        return self

    def set_stroke_as_both(self) -> 'Mouse':
        self.stroke = "Both"
        return self

    def set_stroke_as_no_click(self) -> 'Mouse':
        self.stroke = "NoClick"
        return self

    def set_target_as_window(self) -> 'Mouse':
        self.target = "Window"
        return self

    def set_target_as_screen(self) -> 'Mouse':
        self.target = "Screen"
        return self

    def set_mode_as_no_move(self) -> 'Mouse':
        self.mode = "NoMove"
        return self

    def set_mode_as_dupe(self) -> 'Mouse':
        self.mode = "Dupe"
        return self

    def set_mode_as_scale(self) -> 'Mouse':
        self.mode = "Scale"
        return self

    def set_mode_as_x_y(self, x: int, y: int) -> 'Mouse':
        self.mode = f"{x} {y}"
        return self

    def set_restore_as_yes(self) -> 'Mouse':
        self.restore = "Restore"
        return self

    def set_restore_as_no(self) -> 'Mouse':
        self.restore = "NoRestore"
        return self

    @property
    def title(self):
        return "<ClickMouse {}>".format(
            "{button}{stroke}{target}{mode}{restore}".format(
                button=(self.button + " ").lstrip(),
                stroke=(self.stroke + " ").lstrip(),
                target=(self.target + " ").lstrip(),
                mode=(self.mode + " ").lstrip(),
                restore=(self.restore + " ").lstrip(),
            ).strip()
        )


def _build_modified_mouse_click(modifier, button):
    return "\n".join([
        action.dump()
        for action in [
            KeyDown(key=modifier),
            Mouse(button=button, stroke="Down"),
            Mouse(button=button, stroke="Up"),
            KeyUp(key=modifier),
        ]
    ])


class ModifiedMouseClick:
    """
    This is not a Block object, it is just a factory class.
    """

    @classmethod
    def _make(cls, modifier: str, button: str) -> T.List[T.Union[KeyDown, KeyUp, Mouse]]:
        return [
            KeyDown(key=modifier),
            Mouse(button=button, stroke="Down"),
            Mouse(button=button, stroke="Up"),
            KeyUp(key=modifier),
        ]

    @classmethod
    def shift_left_click(cls):
        return cls._make(modifier=KN.SHIFT, button=KN.MOUSE_LButton)

    @classmethod
    def shift_right_click(cls):
        return cls._make(modifier=KN.SHIFT, button=KN.MOUSE_LButton)

    @classmethod
    def shift_middle_click(cls):
        return cls._make(modifier=KN.SHIFT, button=KN.MOUSE_MButton)

    @classmethod
    def alt_left_click(cls):
        return cls._make(modifier=KN.ALT, button=KN.MOUSE_LButton)

    @classmethod
    def alt_right_click(cls):
        return cls._make(modifier=KN.ALT, button=KN.MOUSE_LButton)

    @classmethod
    def alt_middle_click(cls):
        return cls._make(modifier=KN.ALT, button=KN.MOUSE_MButton)

    @classmethod
    def ctrl_left_click(cls):
        return cls._make(modifier=KN.CTRL, button=KN.MOUSE_LButton)

    @classmethod
    def ctrl_right_click(cls):
        return cls._make(modifier=KN.CTRL, button=KN.MOUSE_LButton)

    @classmethod
    def ctrl_middle_click(cls):
        return cls._make(modifier=KN.CTRL, button=KN.MOUSE_MButton)


@attr.s
class RenameWin(Block['RenameWin']):
    old: str = attr.ib(default=None)
    new: str = attr.ib(default=None)

    @classmethod
    def make(cls, old: str, new: str) -> 'RenameWin':
        return cls(old=old, new=new)

    @property
    def title(self) -> str:
        return "<RenameWin {old} {new}>".format(
            old=CommandArgEnum.encode_arg(self.old),
            new=CommandArgEnum.encode_arg(self.new),
        )

    def is_null(self) -> bool:
        return (self.old is None) or (self.new is None)


def render(
    obj: T.Union[Block, str],
    verbose: bool = False,
    **kwargs
) -> str:
    """
    A global function that take any object as argument and render it.
    """
    if isinstance(obj, Block):
        return obj.render(verbose=verbose)
    elif isinstance(obj, str):
        return obj
    else:  # pragma: no cover
        raise TypeError
