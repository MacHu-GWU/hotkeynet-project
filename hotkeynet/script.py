# -*- coding: utf-8 -*-

"""
该模块是对 HotkeyNet 脚本中的代码块 (我们这里叫 Block) 的抽象. 从而提供了
"在 Python 中写 HotkeyNet" 脚本的能力.
"""

import typing as T

import attr
from attrs_mate import AttrsClass

from . import keyname as KN
from . import tpl
from .vendor.better_enum import BetterStrEnum

from .utils import (
    remove_empty_line,
    has_duplicate,
)


class Context:
    """
    一个全局单例的上下文对象. 自动管理 HotkeyNet 代码块的从属关系.

    在该项目的早期版本中, 我们是用 类属性 来定义从属关系的. 如果代码块 SendLabel 属于
    代码块 Hotkey, 那么我们就要用下面这样的语法来写, 非常的繁琐::

        Hotkey(
            blocks = [
                SendLabel(
                    to=["w1", "w2"],
                    blocks = [
                        Key("1"),
                    ]
                ),
                SendLabel(
                    to=["w3", "w4"],
                    blocks = [
                        Key("2"),
                    ]
                ),
            ]
        )

    有了上下文机制, 我们可以用 Python 中的上下文管理器 ``with`` 语法来表达同样的逻辑,
    减少了缩进, 对人类读代码更加友好, 并且整体代码量也大幅减少::

        with Hotkey(...):
            with SendLabel(to=["w1", "w2"]):
                Key("1")
            with SendLabel(to=["w3", "w4"]):
                Key("2")

    具体实现的原理如下

    所有的 HotkeyNet 的代码块都是 :class:`Block` 的子类, 它们都有一个 ``blocks`` 属性.
    每当我们用

    :param stack: 储存当前的堆栈, 是一个后进先出的数据结构
    :param auto_id_index: 用于自动给每个 Block 加 ID 的数据结构. 每一类 Block 例如
        Command, Hotkey, SendLabel 都是从 1, 2, 3, ... 开始自动加序号.
    """

    def __init__(self):
        self.stack: list = list()
        self.auto_id_index: T.Dict[str, int] = dict()

    def push(self, obj):
        """
        将一个 Block 对象压入堆栈. 模拟进入 context manager 时候的行为.
        """
        self.stack.append(obj)

    def pop(self):
        """
        将一个 Block 对象从堆栈中弹出. 模拟退出 context manager 时候的行为.
        """
        return self.stack.pop()

    def reset(self):
        self.__init__()

    @property
    def current(self) -> "Block":
        """
        获取当前上下文中的最外层的 Block.
        """
        return self.stack[-1]

    def make_id(self, block_type: str = "Block") -> str:
        """
        自动给代码块加 ID. 所有的代码块都有一个 ID, 如果在创建代码块的时候不显示的定义 ID,
        则调用此函数自动生成. 详情请参考 :class:`Block`.
        """
        try:
            name = f"{block_type}{str(self.auto_id_index[block_type] + 1).zfill(4)}"
        except KeyError:
            self.auto_id_index[block_type] = 0
            name = f"{block_type}0001"
        self.auto_id_index[block_type] += 1
        return name


context = Context()  # 单例

BLOCK = T.TypeVar("BLOCK")


@attr.s
class Block(AttrsClass, T.Generic[BLOCK]):
    """
    所有 HotkeyNet 代码块的基类.

    :param id: 全局唯一的代码块 ID.
    :param blocks: 子 Block 的列表, 类似于 Tree 数据结构的叶子结点.
    """

    id: str = attr.ib(factory=context.make_id)
    blocks: T.List["Block"] = attr.ib(factory=list)

    def __call__(self) -> BLOCK:
        return self

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
        """
        创建 block 对象的时候, 上下文中的最外层的 (current) Block 会自动将自己添加到它的
        子 Block 列表中.
        """
        try:
            context.current.blocks.append(self)
        # 当且仅当这个 block 就是根节点时, 什么都不做.
        except IndexError as e:
            if str(e) == "list index out of range":
                pass
            else:
                raise e

    def _iter_by_type(self, type_: T.Type["Block"]) -> T.List:
        return [block for block in self.blocks if isinstance(block, type_)]

    def iter_label(self) -> T.List["Label"]:
        return self._iter_by_type(Label)

    def iter_command(self) -> T.List["Command"]:
        return self._iter_by_type(Command)

    def iter_hotkey(self) -> T.List["Hotkey"]:
        return self._iter_by_type(Hotkey)

    @property
    def title(self) -> str:
        """
        HotkeyNet 代码块是类似与 HTML tag 的标签, 只不过它不会 close. Title 就是每个代码块
        的第一行标签. 例如 ``<Hotkey ...>``.
        """
        raise NotImplementedError

    def is_sub_blocks_all_null(self) -> bool:
        return all([block.is_null() for block in self.blocks])

    def is_null(self) -> bool:
        """
        用于判断该代码块是否为空. 对于不同的代码块, 有不同的判空逻辑. 简单来说, 如果一个代码块
        是空的, 没有内容, 那么它就属于冗余, 不应该在 HotkeyNet 脚本中存在. 而之所以会产生
        空代码块是因为比如你写一些按下快捷键的 Action 的时候, 会触发几个按键, 但有的时候你
        不想触发它们, 但你又不得不在代码中定义它, 这时候就可以用 is_null() 做条件判断, 自动
        删除冗余的按键. 例如:

        - :meth:`Label.is_null`
        - :meth:`Command.is_null`
        - :meth:`Hotkey.is_null`
        """
        return False

    def render(self, verbose=False) -> str:
        """
        将 Python 对象渲染成 HotkeyNet 中的代码块. 本实现对于大多数的 Block 都使用,

        下面是对其不适用的 Block 的列表:

        - :meth:`Script.render`: 因为它是整个脚本, 并不是 HotkeyNet 语法中的代码块.
        """
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
class Script(Block["Script"]):
    """
    代表着整个 HotkeyNet 脚本.
    """

    @property
    def title(self) -> str:
        """
        没有 title.
        """
        return ""

    def check_duplicate_command_name(self):
        """
        确保没有重复定义的 :class:`Command` 对象.
        """
        cmd_name_list = [cmd.name for cmd in self.iter_command()]
        if has_duplicate(cmd_name_list):
            raise ValueError(f"Found duplicate command name: {cmd_name_list}")

    def validate(self):
        """
        检查 Script 的实现是否正确.
        """
        self.check_duplicate_command_name()

    def render(self, verbose: bool = False, no_empty_line: bool = True) -> str:
        if self.is_null():
            return ""
        else:
            self.validate()
            text = tpl.script_tpl.render(
                block=self,
                render=render,
                verbose=verbose,
            )
            if no_empty_line:
                return remove_empty_line(text)
            else:
                return text


class SendModeEnum(BetterStrEnum):
    SendWin = "SendWin"
    SendFocusWin = "SendFocusWin"
    SendWinM = "SendWinM"
    SendWinMF = "SendWinMF"
    SendWinS = "SendWinS"
    SendWinSF = "SendWinSF"


@attr.s
class Label(Block["Script"]):
    """
    用来给软件窗口加别名, 以便在 Command 获 Hotkey 中调用.

    Example::

        <Label name ip send_mode window>

    Reference:

    - https://hotkeynet.readthedocs.io/02-Reference/Label/index.html
    """

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
    ) -> "Label":
        return cls(name=name, window=window, ip=ip, send_mode=send_mode)

    @property
    def title(self):
        return f"<Label {self.name} {self.ip} {self.send_mode} {self.window}>"

    def is_null(self) -> bool:
        """
        如果标签没有名字, 那么就视为冗余, 应该删除.
        """
        return self.name is None


@attr.s
class Command(Block["Command"]):
    """
    代表着一个命令. 在 HotkeyNet 中相当于编程语言中的函数的概念.

    Example::

        <Command name>
            ...

    Reference:

    - https://hotkeynet.readthedocs.io/02-Reference/Command/index.html
    """

    name: str = attr.ib(default=None)

    @classmethod
    def make(cls, name: str) -> "Command":
        return cls(name=name)

    @property
    def title(self):
        return f"<Command {self.name}>"

    def is_null(self) -> bool:
        """
        如果一个命令没有具体的效果, 那么就视为冗余, 应该删除.
        """
        return self.is_sub_blocks_all_null()

    def call(self, args: T.List[str] = None) -> "CallCommand":
        """
        调用这个方法, 生成一个 :class:`CallCommand` 对象. 也就是在 HotkeyNet 中
        调用 Command 的代码块.
        """
        if args is None:
            return CallCommand(cmd=self)
        else:
            return CallCommand(cmd=self, args=args)


class CommandArgEnum:
    """
    注意, 这不是一个真正的 ``enum.Enum``. 但是为了兼容性考虑, 我们就不改这个类的名字了.
    """

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
            return f'"{arg}"'
        else:
            return arg


@attr.s
class CallCommand(Block["Command"]):
    """
    代表着在 HotkeyNet 中调用 Command 的代码块.

    Example::

        <cmd_name arg1 arg2 ...>

    Reference:

    - https://hotkeynet.readthedocs.io/02-Reference/Command/index.html
    """

    cmd: T.Union[str, Command] = attr.ib(default=None)
    args: T.List[str] = attr.ib(factory=list)

    @property
    def cmd_name(self) -> str:
        """
        获取命令的名字.
        """
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
class SendPC(Block["SendPC.tpl"]):
    """
    将命令获 Hotkey 发送到本机或是网络上的另一台电脑上.

    Example::

        <SendPC ip>
            ...

    Reference:

    - https://hotkeynet.readthedocs.io/02-Reference/SendPC/index.html
    """

    ip: T.Optional[str] = attr.ib(default="local")

    @classmethod
    def make(cls, ip: str) -> "SendPC":
        return cls(ip=ip)

    @property
    def title(self):
        return f"<SendPC {self.ip}>"

    def is_null(self) -> bool:
        """
        如果 IP 地址为给定, 则为冗余, 应该删除.
        """
        return self.ip is None


@attr.s
class Run(Block["Run"]):
    """
    运行一个 Windows 程序.

    Reference:

    - https://hotkeynet.readthedocs.io/02-Reference/Run/index.html
    """

    path: T.Optional[str] = attr.ib(default=None)

    @classmethod
    def make(cls, path: str) -> "Run":
        return cls(path=path)

    @property
    def title(self):
        return f"<Run {CommandArgEnum.encode_arg(self.path)}>"

    def is_null(self) -> bool:
        """
        如果路径没给定, 那么也就没有具体的效果, 应该删除.
        """
        return self.path is None


@attr.s
class Hotkey(Block["Hotkey"]):
    """
    代表着一个快捷键的具体效果. 也是 HotkeyNet 中最关键, 最常用的代码块.

    Example::

        <Hotkey 1>
            ...

    Reference:

    - https://hotkeynet.readthedocs.io/02-Reference/Hotkey/index.html
    """

    key: str = attr.ib(default=None)

    @property
    def title(self):
        return f"<Hotkey {self.key}>"

    def is_null(self) -> bool:
        """
        如果快捷键没有给定, 或是没有定义快捷键的效果, 那么就视为冗余, 应该删除.
        """
        return (self.key is None) or self.is_sub_blocks_all_null()

    @property
    def ref(self) -> str:
        """
        用于在其他地方引用这个快捷键的名字. 通常是被 :class:`SetButtonHotkey` 所引用.
        """
        return self.title[1:-1]


@attr.s
class MovementHotkey(Block["MovementHotkey"]):
    """
    代表着一个用于保持按下状态的快捷键的具体效果. 常用于游戏中的人物移动.

    Example::

        <MovementHotkey Up>
            ...

    Reference:

    - https://hotkeynet.readthedocs.io/02-Reference/MovementHotkey/index.html
    """

    key: str = attr.ib(default=None)

    @property
    def title(self) -> str:
        return f"<MovementHotkey {self.key}>"

    def is_null(self) -> bool:
        """
        如果快捷键没有给定, 或是没有定义快捷键的效果, 那么就视为冗余, 应该删除.
        """
        return (self.key is None) or self.is_sub_blocks_all_null()


@attr.s
class Key(Block["Key"]):
    """
    代表单个键盘按键的效果.

    Example::

        <Key 1>

    Reference:

    - https://hotkeynet.readthedocs.io/02-Reference/Key/index.html
    """

    key: str = attr.ib(default=None)

    @property
    def title(self):
        return f"<Key {self.key}>"

    @classmethod
    def make(cls, key: str) -> "Key":
        return cls(key=key)

    @classmethod
    def trigger(cls) -> "Key":
        return cls(key=KN.TRIGGER)

    def is_null(self) -> bool:
        """
        如果按键未被定义, 那么就视为冗余, 应该删除.
        """
        return self.key is None


@attr.s
class KeyUp(Block["KeyUp"]):
    """
    代表松开键盘按键的效果. 常用于模拟组合按键, 例如 Ctrl + C.

    Example::

        <KeyDown Ctrl>
        <Key C>
        <KeyUp Ctrl>

    Reference:

    - https://hotkeynet.readthedocs.io/02-Reference/Key/index.html
    """

    key: str = attr.ib(default=None)

    @property
    def title(self):
        return f"<KeyUp {self.key}>"

    def is_null(self) -> bool:
        """
        如果按键未被定义, 那么就视为冗余, 应该删除.
        """
        return self.key is None


@attr.s
class KeyDown(Block["KeyDown"]):
    """
    代表按下键盘按键的效果. 常用于模拟组合按键, 例如 Ctrl + C.

    Example::

        <KeyDown Ctrl>
        <Key C>
        <KeyUp Ctrl>

    Reference:

    - https://hotkeynet.readthedocs.io/02-Reference/Key/index.html
    """

    key: str = attr.ib(default=None)

    @property
    def title(self):
        return f"<KeyDown {self.key}>"

    def is_null(self) -> bool:
        """
        如果按键未被定义, 那么就视为冗余, 应该删除.
        """
        return self.key is None


@attr.s
class SendLabel(Block["SendLabel"]):
    """
    将一堆按键发送到指定的窗口.

    Example::

        <SendLabel w1>
            ...

    Reference:

    - https://hotkeynet.readthedocs.io/02-Reference/SendLabel/index.html
    """

    name: str = attr.ib(default=None)
    to: T.List[str] = attr.ib(factory=list)

    @property
    def targets(self) -> str:
        return ", ".join(self.to)

    @property
    def title(self) -> str:
        return f"<SendLabel {self.targets}>"

    def is_null(self) -> bool:
        return (len(self.to) == 0) or self.is_sub_blocks_all_null()


class MouseButtonEnum(BetterStrEnum):
    LButton = "LButton"
    MButton = "MButton"
    RButton = "RButton"
    Button4 = "Button4"
    Button5 = "Button5"


class MouseStrokeEnum(BetterStrEnum):
    Down = "Down"
    Up = "Up"
    Both = "Both"
    NoClick = "NoClick"


class MouseTargetEnum(BetterStrEnum):
    Window = "Window"
    Screen = "Screen"


class MouseModeEnum(BetterStrEnum):
    NoMove = "NoMove"
    Dupe = "Dupe"
    Scale = "Scale"


@attr.s
class ClickMouse(Block["Mouse"]):
    """
    Click Mouse.

    Example::

        <ClickMouse button stroke target mode restore>

    Reference:

    - https://hotkeynet.readthedocs.io/02-Reference/ClickMouse/index.html
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
    def make_left_click_on_window(cls) -> "ClickMouse":
        return cls(
            button=MouseButtonEnum.LButton.value,
            stroke=MouseStrokeEnum.Both.value,
            target=MouseTargetEnum.Window.value,
            mode=MouseModeEnum.NoMove.value,
        )

    @classmethod
    def make_left_click_on_window_at(cls, x: int, y: int) -> "ClickMouse":
        return cls(
            button=MouseButtonEnum.LButton.value,
            stroke=MouseStrokeEnum.Both.value,
            target=MouseTargetEnum.Window.value,
        ).set_mode_as_x_y(x, y)

    @classmethod
    def make_right_click_on_window(cls) -> "ClickMouse":
        return cls(
            button=MouseButtonEnum.RButton.value,
            stroke=MouseStrokeEnum.Both.value,
            target=MouseTargetEnum.Window.value,
            mode=MouseModeEnum.NoMove.value,
        )

    @classmethod
    def make_right_click_on_window_at(cls, x: int, y: int) -> "ClickMouse":
        return cls(
            button=MouseButtonEnum.RButton.value,
            stroke=MouseStrokeEnum.Both.value,
            target=MouseTargetEnum.Window.value,
        ).set_mode_as_x_y(x, y)

    def set_left_click(self) -> "ClickMouse":
        self.button = MouseButtonEnum.LButton.value
        return self

    def set_right_click(self) -> "ClickMouse":
        self.button = MouseButtonEnum.RButton.value
        return self

    def set_middle_click(self) -> "ClickMouse":
        self.button = MouseButtonEnum.MButton.value
        return self

    def set_click_button4(self) -> "ClickMouse":
        self.button = MouseButtonEnum.Button4.value
        return self

    def set_click_button5(self) -> "ClickMouse":
        self.button = MouseButtonEnum.Button5.value
        return self

    def set_stroke_down(self) -> "ClickMouse":
        self.stroke = MouseStrokeEnum.Down.value
        return self

    def set_stroke_as_up(self) -> "ClickMouse":
        self.stroke = MouseStrokeEnum.Up.value
        return self

    def set_stroke_as_both(self) -> "ClickMouse":
        self.stroke = MouseStrokeEnum.Both.value
        return self

    def set_stroke_as_no_click(self) -> "ClickMouse":
        self.stroke = MouseStrokeEnum.NoClick.value
        return self

    def set_target_as_window(self) -> "ClickMouse":
        self.target = MouseTargetEnum.Window.value
        return self

    def set_target_as_screen(self) -> "ClickMouse":
        self.target = MouseTargetEnum.Screen.value
        return self

    def set_mode_as_no_move(self) -> "ClickMouse":
        self.mode = MouseModeEnum.NoMove.value
        return self

    def set_mode_as_dupe(self) -> "ClickMouse":
        self.mode = MouseModeEnum.Dupe.value
        return self

    def set_mode_as_scale(self) -> "ClickMouse":
        self.mode = MouseModeEnum.Scale.value
        return self

    def set_mode_as_x_y(self, x: int, y: int) -> "ClickMouse":
        self.mode = f"{x} {y}"
        return self

    def set_restore_as_yes(self) -> "ClickMouse":
        self.restore = "Restore"
        return self

    def set_restore_as_no(self) -> "ClickMouse":
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


@attr.s
class MoveMouse(Block["MoveMouse"]):
    """
    将鼠标移动到窗口中的指定位置.

    Example::

        <MoveMouse x y>

    Reference:

    - https://hotkeynet.readthedocs.io/02-Reference/MoveMouse/index.html
    """

    x: int = attr.ib(default=None)
    y: int = attr.ib(default=None)
    target: T.Optional[str] = attr.ib(default=None)

    def set_target_as_window(self) -> "MoveMouse":
        self.target = "window"
        return self

    def set_target_as_screen(self) -> "MoveMouse":
        self.target = "screen"
        return self

    @property
    def title(self) -> str:
        if self.target is None:
            return f"<MoveMouse {self.x} {self.y}>"
        else:
            return f"<MoveMouse {self.target} {self.x} {self.y}>"

    def is_null(self) -> bool:
        return (self.x is None) or (self.y is None)


@attr.s
class RenameWin(Block["RenameWin"]):
    """
    重名窗口.

    Example::

        <RenameWin old new>

    Reference:

    - https://hotkeynet.readthedocs.io/02-Reference/RenameWin/index.html
    """

    old: str = attr.ib(default=None)
    new: str = attr.ib(default=None)

    @classmethod
    def make(cls, old: str, new: str) -> "RenameWin":
        return cls(old=old, new=new)

    @property
    def title(self) -> str:
        return "<RenameWin {old} {new}>".format(
            old=CommandArgEnum.encode_arg(self.old),
            new=CommandArgEnum.encode_arg(self.new),
        )

    def is_null(self) -> bool:
        """
        如果新旧窗口名有一个没有定义, 则视为冗余, 应该删除.
        """
        return (self.old is None) or (self.new is None)


@attr.s
class TargetWin(Block["TargetWin"]):
    """
    Reference:

    - https://hotkeynet.readthedocs.io/02-Reference/TargetWin/index.html
    """

    window: str = attr.ib(default=None)

    @classmethod
    def make(cls, window: str) -> "TargetWin":
        return cls(window=window)

    @property
    def title(self) -> str:
        return f"<TargetWin {CommandArgEnum.encode_arg(self.window)}>"

    def is_null(self) -> bool:
        return self.window is None


@attr.s
class Wait(Block["Wait"]):
    """
    Example::

        <wait milliseconds>

    Reference:

    - https://hotkeynet.readthedocs.io/02-Reference/Wait/index.html
    """

    milli: T.Optional[int] = attr.ib(default=None)

    @classmethod
    def make(cls, milli: int) -> "Wait":
        return cls(milli=milli)

    @property
    def title(self) -> str:
        return f"<Wait {self.milli}>"

    def is_null(self) -> bool:
        return not bool(self.milli)


@attr.s
class WaitForWin(Block["WaitForWin"]):
    """
    等待一个窗口被完全打开.

    Example::

        <WaitForWin window timeout>

    Reference:

    - https://hotkeynet.readthedocs.io/02-Reference/WaitForWin/index.html
    """

    window: T.Optional[str] = attr.ib(default=None)
    timeout: T.Optional[int] = attr.ib(default=None)

    @classmethod
    def make(cls, window: str, timeout: int) -> "WaitForWin":
        return cls(window=window, timeout=timeout)

    @property
    def title(self) -> str:
        return f"<WaitForWin {self.window} {self.timeout}>"

    def is_null(self) -> bool:
        return (self.window is None) or (self.timeout is None)


@attr.s
class WaitForWinEnabled(Block["WaitForWinEnabled"]):
    """
    等待当前窗口被完全打开.

    Example::

        <WaitForWinEnabled timeout>

    Reference:

    - https://hotkeynet.readthedocs.io/02-Reference/WaitForWinEnabled/index.html
    """

    timeout: int = attr.ib(default=None)

    @classmethod
    def make(cls, timeout: int) -> "WaitForWinEnabled":
        return cls(timeout=timeout)

    @property
    def title(self) -> str:
        return f"<WaitForWinEnabled {self.timeout}>"

    def is_null(self) -> bool:
        return self.timeout is None


@attr.s
class SetForegroundWin(Block["SetForegroundWin"]):
    """
    Reference:

    - https://hotkeynet.readthedocs.io/02-Reference/SetForegroundWin/index.html
    """

    @property
    def title(self) -> str:
        return "<SetForegroundWin>"


@attr.s
class SetActiveWin(Block["SetActiveWin"]):
    """
    Reference:

    - https://hotkeynet.readthedocs.io/02-Reference/SetActiveWin/index.html
    """

    @property
    def title(self) -> str:
        return "<SetActiveWin>"


@attr.s
class Toggle(Block["Toggle"]):
    """
    用 Round robin 的方式, 让你在按下同一个 Hotkey 的时候, 自动改变行为.

    Example::

        <Hotkey F1>
           <Toggle>
              <Key 1>
           <Toggle>
              <Key 2>
           <Toggle>
              <Key 3>

    Reference:

    - https://hotkeynet.readthedocs.io/02-Reference/Toggle/index.html
    """

    @property
    def title(self) -> str:
        return "<Toggle>"


@attr.s
class ToggleHotkeys(Block["ToggleHotkeys"]):
    """
    Reference:

    - https://hotkeynet.readthedocs.io/02-Reference/ToggleHotkeys/index.html
    """

    @property
    def title(self) -> str:
        return "<ToggleHotkeys>"


@attr.s
class ToggleWin(Block["ToggleWin"]):
    """
    用 Round robin 的方式, 让你在按下同一个 Hotkey 的时候, 自动切换到队列中的下一个窗口.

    Reference:

    - https://hotkeynet.readthedocs.io/02-Reference/ToggleWin/index.html
    """

    windows: T.List[str] = attr.ib(factory=list)

    @classmethod
    def make(cls, windows: T.List[str]) -> "ToggleWin":
        return cls(windows=windows)

    @property
    def title(self) -> str:
        return "<ToggleWin {windows}>".format(windows=" ".join(self.windows))

    def is_null(self) -> bool:
        return len(self.windows) == 0


@attr.s
class SendWin(Block["SendWin"]):
    """
    将按键动作发送到指定窗口.  它会自动将该窗口设为当前活动窗口.

    Reference:

    - https://hotkeynet.readthedocs.io/02-Reference/SendWin/index.html
    """

    window: str = attr.ib(default=None)

    @classmethod
    def make(cls, window: str) -> "SendWin":
        return cls(window=window)

    @property
    def title(self) -> str:
        return f"<SendWin {CommandArgEnum.encode_arg(self.window)}>"

    def is_null(self) -> bool:
        return self.window is None


@attr.s
class SendWinM(Block["SendWinM"]):
    """
    将按键动作发送到指定后台窗口. 该窗口可以是后台窗口.

    Reference:

    - https://hotkeynet.readthedocs.io/02-Reference/SendWinM/index.html
    """

    window: str = attr.ib(default=None)

    @classmethod
    def make(cls, window: str) -> "SendWinM":
        return cls(window=window)

    @property
    def title(self) -> str:
        return f"<SendWinM {CommandArgEnum.encode_arg(self.window)}>"

    def is_null(self) -> bool:
        return self.window is None


@attr.s
class SendWinMF(Block["SendWinMF"]):
    """
    Reference:

    - https://hotkeynet.readthedocs.io/02-Reference/SendWinMF/index.html
    """

    window: str = attr.ib(default=None)

    @classmethod
    def make(cls, window: str) -> "SendWinMF":
        return cls(window=window)

    @property
    def title(self) -> str:
        return f"<SendWinMF {CommandArgEnum.encode_arg(self.window)}>"

    def is_null(self) -> bool:
        return self.window is None


@attr.s
class SendWinS(Block["SendWinS"]):
    """
    Reference:

    - https://hotkeynet.readthedocs.io/02-Reference/SendWinS/index.html
    """

    window: str = attr.ib(default=None)

    @classmethod
    def make(cls, window: str) -> "SendWinS":
        return cls(window=window)

    @property
    def title(self) -> str:
        return f"<SendWinS {CommandArgEnum.encode_arg(self.window)}>"

    def is_null(self) -> bool:
        return self.window is None


@attr.s
class SendWinSF(Block["SendWinSF"]):
    """
    Reference:

    - https://hotkeynet.readthedocs.io/02-Reference/SendWinSF/index.html
    """

    window: str = attr.ib(default=None)

    @classmethod
    def make(cls, window: str) -> "SendWinSF":
        return cls(window=window)

    @property
    def title(self) -> str:
        return f"<SendWinSF {CommandArgEnum.encode_arg(self.window)}>"

    def is_null(self) -> bool:
        return self.window is None


@attr.s
class SendFocusWin(Block["SendFocusWin"]):
    """
    将按键动作发送到当前活动窗口.

    Reference:

    - https://hotkeynet.readthedocs.io/02-Reference/SendFocusWin/index.html
    """

    @property
    def title(self) -> str:
        return f"<SendFocusWin>"


@attr.s
class SetWinPos(Block["SetWinPos"]):
    """
    设置窗口在桌面的位置..

    Reference:

    - https://hotkeynet.readthedocs.io/02-Reference/SetWinPos/index.html
    """

    x: int = attr.ib(default=None)
    y: int = attr.ib(default=None)

    @classmethod
    def make(cls, x: int, y: int) -> "SetWinPos":
        return cls(x=x, y=y)

    @property
    def title(self) -> str:
        return f"<SetWinPos {self.x} {self.y}>"

    def is_null(self) -> bool:
        return (self.x is None) or (self.y is None)


@attr.s
class SetWinSize(Block["SetWinSize"]):
    """
    设置窗口大小.

    Reference:

    - https://hotkeynet.readthedocs.io/02-Reference/SetWinSize/index.html
    """

    x: int = attr.ib(default=None)
    y: int = attr.ib(default=None)

    @classmethod
    def make(cls, x: int, y: int) -> "SetWinSize":
        return cls(x=x, y=y)

    @property
    def title(self) -> str:
        return f"<SetWinSize {self.x} {self.y}>"

    def is_null(self) -> bool:
        return (self.x is None) or (self.y is None)


@attr.s
class SetWinRect(Block["SetWinRect"]):
    """
    设置窗口的位置以及大小.

    Reference:

    - https://hotkeynet.readthedocs.io/02-Reference/SetWinRect/index.html
    """

    x: int = attr.ib(default=None)
    y: int = attr.ib(default=None)
    width: int = attr.ib(default=None)
    height: int = attr.ib(default=None)

    @classmethod
    def make(cls, x: int, y: int, width: int, height: int) -> "SetWinRect":
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
class Text(Block["Text"]):
    """
    用键盘输入文本.

    Reference:

    - https://hotkeynet.readthedocs.io/02-Reference/Text/index.html
    """

    text: str = attr.ib(default=None)

    @classmethod
    def make(cls, text: str) -> "Text":
        return cls(text=text)

    @property
    def title(self) -> str:
        return f"<Text {self.text}>"

    def is_null(self) -> bool:
        return self.text is None


@attr.s
class CreatePanel(Block["CreatePanel"]):
    """
    创建一个 Panel 按钮面板 widget.

    Reference:

    - https://hotkeynet.readthedocs.io/02-Reference/CreatePanel/index.html
    """

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
    ) -> "CreatePanel":
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
class CreateButton(Block["CreateButton"]):
    """
    创建 Panel 按钮面板上的按钮.

    Reference:

    - https://hotkeynet.readthedocs.io/02-Reference/CreateButton/index.html
    """

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
        text: T.Optional[str] = None,
    ) -> "CreateButton":
        return cls(name=name, x=x, y=y, width=width, height=height, text=text)

    @property
    def title(self) -> str:
        non_null_args = [
            i
            for i in [
                self.name,
                str(self.x),
                str(self.x),
                str(self.width),
                str(self.height),
                f'"{self.text}"' if self.text else None,
            ]
            if i
        ]
        return "<CreateButton {}>".format(" ".join(non_null_args))

    def is_null(self) -> bool:
        return (
            (self.name is None)
            or (self.x is None)
            or (self.y is None)
            or (self.width is None)
            or (self.height is None)
        )


@attr.s
class CreatePictureButton(Block["CreatePictureButton"]):
    """
    创建 Panel 按钮面板上的带图标的按钮.

    Reference:

    - https://hotkeynet.readthedocs.io/02-Reference/CreatePictureButton/index.html
    """

    name: str = attr.ib(default=None)
    x: int = attr.ib(default=None)
    y: int = attr.ib(default=None)
    file: str = attr.ib(default=None)
    text: T.Optional[str] = attr.ib(default=None)

    @classmethod
    def make(
        cls, name: str, x: int, y: int, file: str, text: T.Optional[str] = None
    ) -> "CreatePictureButton":
        return cls(name=name, x=x, y=y, file=file, text=text)

    @property
    def title(self) -> str:
        non_null_args = [
            i
            for i in [
                self.name,
                str(self.x),
                str(self.y),
                f'"{self.file}"',
                self.text,
            ]
            if i is not None
        ]
        return "<CreatePictureButton {}>".format(" ".join(non_null_args))

    def is_null(self) -> bool:
        return (
            (self.name is None)
            or (self.x is None)
            or (self.y is None)
            or (self.file is None)
        )


@attr.s
class CreateColoredButton(Block["CreateColoredButton"]):
    """
    创建 Panel 按钮面板上的色块的按钮.

    Reference:

    - https://hotkeynet.readthedocs.io/02-Reference/CreateColoredButton/index.html
    """

    name: str = attr.ib(default=None)
    x: int = attr.ib(default=None)
    y: int = attr.ib(default=None)
    width: int = attr.ib(default=None)
    height: int = attr.ib(default=None)
    bkcolor: str = attr.ib(default=None)
    textcolor: str = attr.ib(default=None)
    text: T.Optional[str] = attr.ib(default=None)

    @classmethod
    def make(
        cls,
        name: str,
        x: int,
        y: int,
        width: int,
        height: int,
        bkcolor: str,
        textcolor: str,
        text: T.Optional[str] = None,
    ) -> "CreateColoredButton":
        return cls(
            name=name,
            x=x,
            y=y,
            width=width,
            height=height,
            bkcolor=bkcolor,
            textcolor=textcolor,
            text=text,
        )

    @property
    def title(self) -> str:
        non_null_args = [
            i
            for i in [
                self.name,
                str(self.x),
                str(self.y),
                str(self.width),
                str(self.height),
                self.bkcolor,
                self.textcolor,
                self.text,
            ]
            if i is not None
        ]
        return "<CreateColoredButton {}>".format(" ".join(non_null_args))

    def is_null(self) -> bool:
        return (
            (self.name is None)
            or (self.x is None)
            or (self.y is None)
            or (self.width is None)
            or (self.height is None)
            or (self.bkcolor is None)
            or (self.textcolor is None)
        )


@attr.s
class AddButtonToPanel(Block["AddButtonToPanel"]):
    """
    将按钮添加到 Panel 按钮面板中.

    Reference:

    - https://hotkeynet.readthedocs.io/02-Reference/AddButtonToPanel/index.html
    """

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
    ) -> "AddButtonToPanel":
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
        return "<AddButtonToPanel {}>".format(" ".join(non_null_args))

    def is_null(self) -> bool:
        return (self.button is None) or (self.panel is None)


@attr.s
class SetButtonHotkey(Block["SetButtonHotkey"]):
    """
    将按钮和 :class:`Hotkey` 绑定.

    Reference:

    - https://hotkeynet.readthedocs.io/02-Reference/SetButtonHotkey/index.html
    """

    button: str = attr.ib(default=None)
    hotkey: "Hotkey" = attr.ib(default=None)

    @classmethod
    def make(
        cls,
        button: str,
        hotkey: Hotkey,
    ) -> "SetButtonHotkey":
        return cls(button=button, hotkey=hotkey)

    @property
    def title(self) -> str:
        return f"<SetButtonHotkey {self.button} {self.hotkey.ref}>"

    def is_null(self) -> bool:
        return (self.button is None) or (self.hotkey is None)


@attr.s
class SetButtonCommand(Block["SetButtonCommand"]):
    """
    将按钮和 :class:`Command` 绑定.

    Reference:

    - https://hotkeynet.readthedocs.io/02-Reference/SetButtonCommand/index.html
    """

    button: str = attr.ib(default=None)
    command: "Command" = attr.ib(default=None)
    args: tuple = attr.ib(default=None)

    @classmethod
    def make(
        cls,
        button: str,
        command: Command,
        args: tuple = None,
    ) -> "SetButtonCommand":
        return cls(button=button, command=command, args=args)

    @property
    def title(self) -> str:
        if self.args:
            args_part = " {}".format(" ".join(self.args))
        else:
            args_part = ""
        return f"<SetButtonCommand {self.button} {self.command.name}{args_part}>"

    def is_null(self) -> bool:
        return (self.button is None) or (self.command is None)


@attr.s
class AlwaysOnTop(Block["AlwaysOnTop"]):
    """
    将当前窗口设为桌面最上端的窗口

    Reference:

    - https://hotkeynet.readthedocs.io/02-Reference/AlwaysOnTop/index.html
    """

    on: bool = attr.ib(default=True)

    @classmethod
    def make(cls, on: bool = True) -> "AlwaysOnTop":
        return cls(on=on)

    @property
    def title(self) -> str:
        if self.on:
            return f"<AlwaysOnTop on>"
        else:
            return f"<AlwaysOnTop off>"


@attr.s
class SetPanelLayout(Block["SetPanelLayout"]):
    """
    设置 Panel 按钮面板的布局.

    Reference:

    - https://hotkeynet.readthedocs.io/02-Reference/SetPanelLayout/index.html
    """

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
    ) -> "SetPanelLayout":
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
        return "<SetPanelLayout {}>".format(" ".join(non_null_args))

    def is_null(self) -> bool:
        return (
            (self.panel is None) or (self.row_length is None) or (self.margin is None)
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
