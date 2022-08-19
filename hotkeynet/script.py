# -*- coding: utf-8 -*-

import typing as T
import enum
# from functools import cached_property

import attr
from attrs_mate import AttrsClass
from jinja2 import Template

from . import keyname as KN
from . import tpl


# from .enumerate import EnumHelper
# from .utils import remove_empty_line


class Context:
    def __init__(self):
        self.stack: list = list()
        self.auto_id_index: T.Dict[str, int] = dict()

    def push(self, obj):
        self.stack.append(obj)

    def pop(self):
        return self.stack.pop()

    @property
    def current(self) -> 'Block':
        return self.stack[-1]

    def make_id(self, block_type: str = "Block") -> str:
        try:
            name = f"{block_type}{str(self.auto_id_index[block_type] + 1).zfill(4)}"
        except KeyError:
            self.auto_id_index[block_type] = 0
            name = f"{block_type}0001"
        self.auto_id_index[block_type] += 1
        return name


context = Context()

BLOCK = T.TypeVar("BLOCK")


@attr.s
class Block(AttrsClass, T.Generic[BLOCK]):
    id: str = attr.ib(factory=context.make_id)
    blocks: T.List['Block'] = attr.ib(factory=list)

    def __call__(self) -> BLOCK:
        return self.__enter__()

    def __enter__(self) -> BLOCK:
        """
        __enter__ 是为 ``with Block() as block:`` 这样的上下文管理器语法服务的. 这个
        语法能自动将被上下文包括起来的 子 Block, 添加到 上下文所在的 Block 中去. 从而让
        这些 Block 的关系人类可读, 机器也可解析. 这些上下文解析的逻辑是在 Block 实例被创建
        的时候执行的. 但是这样做就要求所有的 Block 只能在它 "该被创建" 的时候, 被创建.

        如果你提前在没有上下文的时候创建 Block 的实例, 而在需要它的时候直接引用它, 这样会
        导致父 Block 无法感知到被引用的 Block 的存在. 所以如果你需要定义一些常用的 Block
        然后直接引用, 期望这样做可以减少代码重复, 这时你需要确保这些引用的定义是一个函数,
        而不是一个具体的实例.
        """
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

    def _iter_by_type(self, type_: T.Type['Block']) -> T.List:
        return [
            block
            for block in self.blocks
            if isinstance(block, type_)
        ]

    def iter_label(self) -> T.List['Label']:
        return self._iter_by_type(Label)

    def iter_command(self) -> T.List['Command']:
        return self._iter_by_type(Command)

    def iter_hotkey(self) -> T.List['Hotkey']:
        return self._iter_by_type(Hotkey)

    @property
    def title(self) -> str:
        raise NotImplementedError

    def _are_sub_blocks_all_null(self) -> bool:
        return all([block.is_null() for block in self.blocks])

    def is_null(self) -> bool:
        return False

    def render(self, verbose=False) -> str:
        if verbose:
            try:
                print(f"render {self.title} ...")
            except Exception:
                print(f"render <{self.__class__.__name__}>")
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

    def check_duplicate_command_name(self):
        cmd_name_list = list()
        for block in self.blocks:
            if isinstance(block, Command):
                cmd_name_list.append(block.name)
        if len(cmd_name_list) != len(set(cmd_name_list)):
            raise ValueError(f"Found duplicate command name: {cmd_name_list}")

    def validate(self):
        self.check_duplicate_command_name()

    def render(self, verbose=False) -> str:
        if self.is_null():
            return ""
        else:
            # return remove_empty_line(
            #     tpl.script_tpl.render(
            #         block=self,
            #         render=render,
            #         verbose=verbose,
            #     )
            # )
            self.validate()
            return tpl.script_tpl.render(
                block=self,
                render=render,
                verbose=verbose,
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
    name: str = attr.ib(default=None)

    @classmethod
    def make(cls, name: str) -> 'Command':
        return cls(name=name)

    @property
    def title(self):
        return f"<Command {self.name}>"

    def is_null(self) -> bool:
        return self._are_sub_blocks_all_null()

    def call(self, args: T.List[str] = None) -> 'CallCommand':
        if args is None:
            return CallCommand(cmd=self)
        else:
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
        return arg.startswith("%") and arg.endswith("%")

    @classmethod
    def encode_arg(cls, arg: str) -> str:
        if cls.is_arg(arg):
            return arg
        elif " " in arg:
            return f"\"{arg}\""
        else:
            return arg


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
            return f"<{self.cmd_name}>"
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
    key: str = attr.ib(default=None)

    @property
    def title(self):
        return f"<Hotkey {self.key}>"

    def is_null(self) -> bool:
        return (self.key is None) or self._are_sub_blocks_all_null()

    @property
    def ref(self) -> str:
        """
        used by SetButtonHotkey
        """
        return self.title[1:-1]


@attr.s
class MovementHotkey(Block['MovementHotkey']):
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
        return cls(key=KN.TRIGGER)


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
    to: T.List[str] = attr.ib(factory=list)

    @property
    def targets(self) -> str:
        return ", ".join(self.to)

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


class MouseStrokeEnum(enum.Enum):
    Down = "Down"
    Up = "Up"
    Both = "Both"
    NoClick = "NoClick"


class MouseTargetEnum(enum.Enum):
    Window = "Window"
    Screen = "Screen"


class MouseModeEnum(enum.Enum):
    NoMove = "NoMove"
    Dupe = "Dupe"
    Scale = "Scale"


@attr.s
class ClickMouse(Block['Mouse']):
    """
    Click Mouse
    """
    # LButton, MButton, RButton, Button4, or Button5
    button: str = attr.ib(default=None)
    # Down, Up, Both, or NoClick
    stroke: str = attr.ib(default="")
    # Window or Screen
    target: str = attr.ib(default="")
    # NoMove, # #, Dupe, Scale, #% #%, ±# ±#
    mode: str = attr.ib(default="")
    # Restore or NoRestore
    restore: str = attr.ib(default="")

    @classmethod
    def make_left_click_on_window(cls) -> 'ClickMouse':
        return cls(
            button=MouseButtonEnum.LButton.value,
            stroke=MouseStrokeEnum.Both.value,
            target=MouseTargetEnum.Window.value,
            mode=MouseModeEnum.NoMove.value,
        )

    @classmethod
    def make_left_click_on_window_at(cls, x: int, y: int) -> 'ClickMouse':
        return cls(
            button=MouseButtonEnum.LButton.value,
            stroke=MouseStrokeEnum.Both.value,
            target=MouseTargetEnum.Window.value,
        ).set_mode_as_x_y(x, y)

    @classmethod
    def make_right_click_on_window(cls) -> 'ClickMouse':
        return cls(
            button=MouseButtonEnum.RButton.value,
            stroke=MouseStrokeEnum.Both.value,
            target=MouseTargetEnum.Window.value,
            mode=MouseModeEnum.NoMove.value,
        )

    @classmethod
    def make_right_click_on_window_at(cls, x: int, y: int) -> 'ClickMouse':
        return cls(
            button=MouseButtonEnum.RButton.value,
            stroke=MouseStrokeEnum.Both.value,
            target=MouseTargetEnum.Window.value,
        ).set_mode_as_x_y(x, y)

    def set_left_click(self) -> 'ClickMouse':
        self.button = MouseButtonEnum.LButton.value
        return self

    def set_right_click(self) -> 'ClickMouse':
        self.button = MouseButtonEnum.RButton.value
        return self

    def set_middle_click(self) -> 'ClickMouse':
        self.button = MouseButtonEnum.MButton.value
        return self

    def set_click_button4(self) -> 'ClickMouse':
        self.button = MouseButtonEnum.Button4.value
        return self

    def set_click_button5(self) -> 'ClickMouse':
        self.button = MouseButtonEnum.Button5.value
        return self

    def set_stroke_down(self) -> 'ClickMouse':
        self.stroke = MouseStrokeEnum.Down.value
        return self

    def set_stroke_as_up(self) -> 'ClickMouse':
        self.stroke = MouseStrokeEnum.Up.value
        return self

    def set_stroke_as_both(self) -> 'ClickMouse':
        self.stroke = MouseStrokeEnum.Both.value
        return self

    def set_stroke_as_no_click(self) -> 'ClickMouse':
        self.stroke = MouseStrokeEnum.NoClick.value
        return self

    def set_target_as_window(self) -> 'ClickMouse':
        self.target = MouseTargetEnum.Window.value
        return self

    def set_target_as_screen(self) -> 'ClickMouse':
        self.target = MouseTargetEnum.Screen.value
        return self

    def set_mode_as_no_move(self) -> 'ClickMouse':
        self.mode = MouseModeEnum.NoMove.value
        return self

    def set_mode_as_dupe(self) -> 'ClickMouse':
        self.mode = MouseModeEnum.Dupe.value
        return self

    def set_mode_as_scale(self) -> 'ClickMouse':
        self.mode = MouseModeEnum.Scale.value
        return self

    def set_mode_as_x_y(self, x: int, y: int) -> 'ClickMouse':
        self.mode = f"{x} {y}"
        return self

    def set_restore_as_yes(self) -> 'ClickMouse':
        self.restore = "Restore"
        return self

    def set_restore_as_no(self) -> 'ClickMouse':
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

    def is_null(self) -> bool:
        return self.button is None


def _build_modified_mouse_click(modifier, button):
    return "\n".join([
        action.dump()
        for action in [
            KeyDown(key=modifier),
            ClickMouse(button=button, stroke="Down"),
            ClickMouse(button=button, stroke="Up"),
            KeyUp(key=modifier),
        ]
    ])


class ModifiedClickMouse:
    """
    This is not a Block object, it is just a factory class.
    """

    @classmethod
    def _make(cls, modifier: str, button: str) -> T.List[T.Union[KeyDown, KeyUp, ClickMouse]]:
        return [
            KeyDown(key=modifier),
            ClickMouse(button=button, stroke="Down"),
            ClickMouse(button=button, stroke="Up"),
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
class MoveMouse(Block['MoveMouse']):
    x: int = attr.ib(default=None)
    y: int = attr.ib(default=None)
    target: T.Optional[str] = attr.ib(default=None)

    def set_target_as_window(self) -> 'MoveMouse':
        self.target = "window"
        return self

    def set_target_as_screen(self) -> 'MoveMouse':
        self.target = "screen"
        return self

    @property
    def title(self) -> str:
        if self.target is None:
            return f"<MoveMouse {self.x} {self.y}>"
        else:
            return f"<MoveMouse {self.target} {self.x} {self.y}>"

    def is_null(self) -> bool:
        return (
            (self.x is None)
            or (self.y is None)
        )


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


@attr.s
class TargetWin(Block['TargetWin']):
    window: str = attr.ib(default=None)

    @classmethod
    def make(cls, window: str) -> 'TargetWin':
        return cls(window=window)

    @property
    def title(self) -> str:
        return f"<TargetWin {CommandArgEnum.encode_arg(self.window)}>"

    def is_null(self) -> bool:
        return self.window is None


@attr.s
class Wait(Block['Wait']):
    milli: int = attr.ib(default=None)

    @classmethod
    def make(cls, milli: int) -> 'Wait':
        return cls(milli=milli)

    @property
    def title(self) -> str:
        return f"<Wait {self.milli}>"

    def is_null(self) -> bool:
        return not bool(self.milli)


@attr.s
class WaitForWin(Block['WaitForWin']):
    window: str = attr.ib(default=None)
    timeout: int = attr.ib(default=None)

    @classmethod
    def make(cls, window: str, timeout: int) -> 'WaitForWin':
        return cls(window=window, timeout=timeout)

    @property
    def title(self) -> str:
        return f"<WaitForWin {self.window} {self.timeout}>"

    def is_null(self) -> bool:
        return (
            (self.window is None)
            or (self.timeout is None)
        )


@attr.s
class WaitForWinEnabled(Block['WaitForWinEnabled']):
    timeout: int = attr.ib(default=None)

    @classmethod
    def make(cls, timeout: int) -> 'WaitForWinEnabled':
        return cls(timeout=timeout)

    @property
    def title(self) -> str:
        return f"<WaitForWinEnabled {self.timeout}>"

    def is_null(self) -> bool:
        return self.timeout is None


@attr.s
class SetForegroundWin(Block['SetForegroundWin']):
    @property
    def title(self) -> str:
        return "<SetForegroundWin>"


@attr.s
class SetActiveWin(Block['SetActiveWin']):
    @property
    def title(self) -> str:
        return "<SetActiveWin>"


@attr.s
class Toggle(Block['Toggle']):
    @property
    def title(self) -> str:
        return "<Toggle>"


@attr.s
class ToggleHotkeys(Block['ToggleHotkeys']):
    @property
    def title(self) -> str:
        return "<ToggleHotkeys>"


@attr.s
class ToggleWin(Block['ToggleWin']):
    windows: T.List[str] = attr.ib(factory=list)

    @classmethod
    def make(cls, windows: T.List[str]) -> 'ToggleWin':
        return cls(windows=windows)

    @property
    def title(self) -> str:
        return "<ToggleWin {windows}>".format(
            windows=" ".join(self.windows)
        )

    def is_null(self) -> bool:
        return len(self.windows) == 0


@attr.s
class SendWin(Block['SendWin']):
    window: str = attr.ib(default=None)

    @classmethod
    def make(cls, window: str) -> 'SendWin':
        return cls(window=window)

    @property
    def title(self) -> str:
        return f"<SendWin {CommandArgEnum.encode_arg(self.window)}>"

    def is_null(self) -> bool:
        return self.window is None


@attr.s
class SendWinM(Block['SendWinM']):
    window: str = attr.ib(default=None)

    @classmethod
    def make(cls, window: str) -> 'SendWinM':
        return cls(window=window)

    @property
    def title(self) -> str:
        return f"<SendWinM {CommandArgEnum.encode_arg(self.window)}>"

    def is_null(self) -> bool:
        return self.window is None


@attr.s
class SendWinMF(Block['SendWinMF']):
    window: str = attr.ib(default=None)

    @classmethod
    def make(cls, window: str) -> 'SendWinMF':
        return cls(window=window)

    @property
    def title(self) -> str:
        return f"<SendWinMF {CommandArgEnum.encode_arg(self.window)}>"

    def is_null(self) -> bool:
        return self.window is None


@attr.s
class SendWinS(Block['SendWinS']):
    window: str = attr.ib(default=None)

    @classmethod
    def make(cls, window: str) -> 'SendWinS':
        return cls(window=window)

    @property
    def title(self) -> str:
        return f"<SendWinS {CommandArgEnum.encode_arg(self.window)}>"

    def is_null(self) -> bool:
        return self.window is None


@attr.s
class SendWinSF(Block['SendWinSF']):
    window: str = attr.ib(default=None)

    @classmethod
    def make(cls, window: str) -> 'SendWinSF':
        return cls(window=window)

    @property
    def title(self) -> str:
        return f"<SendWinSF {CommandArgEnum.encode_arg(self.window)}>"

    def is_null(self) -> bool:
        return self.window is None


@attr.s
class SendFocusWin(Block['SendFocusWin']):
    @property
    def title(self) -> str:
        return f"<SendFocusWin>"


@attr.s
class SetWinPos(Block['SetWinPos']):
    x: int = attr.ib(default=None)
    y: int = attr.ib(default=None)

    @classmethod
    def make(cls, x: int, y: int) -> 'SetWinPos':
        return cls(x=x, y=y)

    @property
    def title(self) -> str:
        return f"<SetWinPos {self.x} {self.y}>"

    def is_null(self) -> bool:
        return (self.x is None) or (self.y is None)


@attr.s
class SetWinSize(Block['SetWinSize']):
    x: int = attr.ib(default=None)
    y: int = attr.ib(default=None)

    @classmethod
    def make(cls, x: int, y: int) -> 'SetWinSize':
        return cls(x=x, y=y)

    @property
    def title(self) -> str:
        return f"<SetWinSize {self.x} {self.y}>"

    def is_null(self) -> bool:
        return (self.x is None) or (self.y is None)


@attr.s
class SetWinRect(Block['SetWinRect']):
    x: int = attr.ib(default=None)
    y: int = attr.ib(default=None)
    width: int = attr.ib(default=None)
    height: int = attr.ib(default=None)

    @classmethod
    def make(cls, x: int, y: int, width: int, height: int) -> 'SetWinRect':
        return cls(x=x, y=y, width=width, height=height)

    @property
    def title(self) -> str:
        return f"<SetWinRect {self.x} {self.y} {self.width} {self.height}>"

    def is_null(self) -> bool:
        return (
            (self.x is None)
            or (self.y is None)
            or (self.width is None)
            or (self.height is None)
        )


@attr.s
class Text(Block['Text']):
    text: str = attr.ib(default=None)

    @classmethod
    def make(cls, text: str) -> 'Text':
        return cls(text=text)

    @property
    def title(self) -> str:
        return f"<Text {self.text}>"

    def is_null(self) -> bool:
        return self.text is None


@attr.s
class CreatePanel(Block['CreatePanel']):
    name: str = attr.ib(default=None)
    x: int = attr.ib(default=None)
    y: int = attr.ib(default=None)
    width: int = attr.ib(default=None)
    height: int = attr.ib(default=None)

    @classmethod
    def make(
        cls,
        name: str,
        x: int,
        y: int,
        width: int,
        height: int,
    ) -> 'CreatePanel':
        return cls(name=name, x=x, y=y, width=width, height=height)

    @property
    def title(self) -> str:
        return f"<CreatePanel {self.name} {self.x} {self.y} {self.width} {self.height}>"

    def is_null(self) -> bool:
        return (
            (self.name is None)
            or (self.x is None)
            or (self.y is None)
            or (self.width is None)
            or (self.height is None)
        )


@attr.s
class CreateButton(Block['CreateButton']):
    name: str = attr.ib(default=None)
    x: int = attr.ib(default=None)
    y: int = attr.ib(default=None)
    width: int = attr.ib(default=None)
    height: int = attr.ib(default=None)
    text: T.Optional[str] = attr.ib(default=None)

    @classmethod
    def make(
        cls,
        name: str,
        x: int,
        y: int,
        width: int,
        height: int,
        text: T.Optional[str] = None
    ) -> 'CreateButton':
        return cls(name=name, x=x, y=y, width=width, height=height, text=text)

    @property
    def title(self) -> str:
        non_null_args = [
            i
            for i in [
                self.name,
                None if self.x is None else str(self.x),
                None if self.y is None else str(self.x),
                None if self.width is None else str(self.x),
                None if self.height is None else str(self.x),
                f"\"{self.text}\"" if self.text else None,
            ]
            if i
        ]
        return "<CreateButton {}>".format(
            " ".join(non_null_args)
        )

    def is_null(self) -> bool:
        return (
            (self.name is None)
            or (self.x is None)
            or (self.y is None)
            or (self.width is None)
            or (self.height is None)
        )


@attr.s
class CreatePictureButton(Block['CreatePictureButton']):
    name: str = attr.ib(default=None)
    x: int = attr.ib(default=None)
    y: int = attr.ib(default=None)
    file: str = attr.ib(default=None)
    text: T.Optional[str] = attr.ib(default=None)

    @classmethod
    def make(
        cls,
        name: str,
        x: int,
        y: int,
        file: str,
        text: T.Optional[str] = None
    ) -> 'CreatePictureButton':
        return cls(name=name, x=x, y=y, file=file, text=text)

    @property
    def title(self) -> str:
        non_null_args = [
            i
            for i in [
                self.name,
                self.x,
                self.y,
                f"\"{self.file}\"",
                self.text,
            ]
            if i is not None
        ]
        return "<CreatePictureButton {}>".format(
            " ".join(non_null_args)
        )

    def is_null(self) -> bool:
        return (
            (self.name is None)
            or (self.x is None)
            or (self.y is None)
            or (self.file is None)
        )


@attr.s
class AddButtonToPanel(Block['AddButtonToPanel']):
    button: str = attr.ib(default=None)
    panel: str = attr.ib(default=None)
    x: T.Optional[int] = attr.ib(default=0)
    y: T.Optional[int] = attr.ib(default=0)
    width: T.Optional[int] = attr.ib(default=None)
    height: T.Optional[int] = attr.ib(default=None)

    @classmethod
    def make(
        cls,
        button: str,
        panel: str,
        x: int = 0,
        y: int = 0,
        width: int = None,
        height: int = None,
    ) -> 'AddButtonToPanel':
        return cls(button=button, panel=panel, x=x, y=y, width=width, height=height)

    @property
    def title(self) -> str:
        non_null_args = [
            str(i)
            for i in [
                self.button,
                self.panel,
                self.x,
                self.y,
                self.width,
                self.height,
            ]
            if i is not None
        ]
        return "<AddButtonToPanel {}>".format(
            " ".join(non_null_args)
        )

    def is_null(self) -> bool:
        return (
            (self.button is None)
            or (self.panel is None)
        )


@attr.s
class SetButtonHotkey(Block['SetButtonHotkey']):
    button: str = attr.ib(default=None)
    hotkey: 'Hotkey' = attr.ib(default=None)

    @classmethod
    def make(
        cls,
        button: str,
        hotkey: Hotkey,
    ) -> 'SetButtonHotkey':
        return cls(button=button, hotkey=hotkey)

    @property
    def title(self) -> str:
        return f"<SetButtonHotkey {self.button} {self.hotkey.ref}>"

    def is_null(self) -> bool:
        return (
            (self.button is None)
            or (self.hotkey is None)
        )


@attr.s
class SetButtonCommand(Block['SetButtonCommand']):
    button: str = attr.ib(default=None)
    command: 'Command' = attr.ib(default=None)
    args: tuple = attr.ib(default=None)

    @classmethod
    def make(
        cls,
        button: str,
        command: Command,
        args: tuple = None,
    ) -> 'SetButtonCommand':
        return cls(button=button, command=command, args=args)

    @property
    def title(self) -> str:
        if self.args:
            args_part = " {}".format(" ".join(self.args))
        else:
            args_part = ""
        return f"<SetButtonCommand {self.button} {self.command.name}{args_part}>"

    def is_null(self) -> bool:
        return (
            (self.button is None)
            or (self.command is None)
        )


@attr.s
class AlwaysOnTop(Block['AlwaysOnTop']):
    on: bool = attr.ib(default=True)

    @classmethod
    def make(cls, on: bool = True) -> 'AlwaysOnTop':
        return cls(on=on)

    @property
    def title(self) -> str:
        if self.on:
            return f"<AlwaysOnTop on>"
        else:
            return f"<AlwaysOnTop off>"


@attr.s
class SetPanelLayout(Block['SetPanelLayout']):
    panel: str = attr.ib(default=None)
    row_length: int = attr.ib(default=None)
    margin: int = attr.ib(default=None)
    button_width: T.Optional[int] = attr.ib(default=None)
    button_height: T.Optional[int] = attr.ib(default=None)

    @classmethod
    def make(
        cls,
        panel: str,
        row_length: int,
        margin: int,
        button_width: int = None,
        button_height: int = None,
    ) -> 'SetPanelLayout':
        return cls(
            panel=panel,
            row_length=row_length,
            margin=margin,
            button_width=button_width,
            button_height=button_height,
        )

    @property
    def title(self) -> str:
        non_null_args = [
            i
            for i in [
                self.panel,
                str(self.row_length) if self.row_length else None,
                str(self.margin) if self.margin else None,
                str(self.button_width) if self.button_width else None,
                str(self.button_height) if self.button_height else None,
            ]
            if i is not None
        ]
        return "<SetPanelLayout {}>".format(
            " ".join(non_null_args)
        )

    def is_null(self) -> bool:
        return (
            (self.panel is None)
            or (self.row_length is None)
            or (self.margin is None)
        )


def render(
    obj: T.Union[Block, str],
    verbose: bool = False,
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
