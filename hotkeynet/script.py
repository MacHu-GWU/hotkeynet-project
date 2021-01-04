# -*- coding: utf-8 -*-

import typing
from collections import OrderedDict

import attr
from pathlib_mate import PathCls as Path

from .utils import render_template, remove_empty_line

TPL_DIR = Path(__file__).change(new_basename="templates")

_ScriptTemplate = Path(TPL_DIR, "Script.tpl").read_text(encoding="utf-8")


@attr.s
class Script:
    commands: OrderedDict = attr.ib(factory=OrderedDict)
    templates: OrderedDict = attr.ib(factory=OrderedDict)
    hotkeys: OrderedDict = attr.ib(factory=OrderedDict)

    def add_command(self, command: 'Command', ignore_duplicate=False):
        if command.name in self.commands:
            if not ignore_duplicate:
                raise ValueError(f"Duplicate command name found {command.name}")
        self.commands[command.name] = command

    def add_template(self, template: 'Template', ignore_duplicate=False):
        if template.name in self.templates:
            if not ignore_duplicate:
                raise ValueError(f"Duplicate template name found {template.name}")
        self.templates[template.name] = template

    def add_hotkey(self, hotkey: 'Hotkey', ignore_duplicate=False):
        if hotkey.key in self.hotkeys:
            if not ignore_duplicate:
                raise ValueError(f"Duplicate hotkey name found {hotkey.name}")
        self.hotkeys[hotkey.key] = hotkey

    def dump(self):
        return render_template(_ScriptTemplate, script=self)


_CommandTemplate = Path(TPL_DIR, "Command.tpl").read_text(encoding="utf-8")


@attr.s
class Command:
    name: str = attr.ib()
    actions = attr.ib(factory=list)  # type: typing.List[typing.Union[Action, str]]
    script: 'Script' = attr.ib(default=None)

    def __attrs_post_init__(self):
        if self.script is not None:
            self.script.add_command(self)

    def call(self, *args) -> str:
        """
        渲染 Command 被调用的代码块, 形如:

        <${CommandName} ${Arg1} ${Arg2} ...}

        :param args:
        :return:
        """
        return "<{}{}>".format(
            self.name,
            " " + " ".join(args) if len(args) else ""
        )

    def dump(self) -> str:
        """
        渲染整个 Command 代码块

        :return:
        """
        print(f"dump Command({self.name}) ...")
        return remove_empty_line(
            render_template(
                _CommandTemplate,
                command=self,
                render_action=render_action,
            )
        )


@attr.s
class Template:
    name: str = attr.ib()
    script: 'Script' = attr.ib(default=None)

    def __attrs_post_init__(self):
        if self.script is not None:
            self.script.add_template(self)


_HotkeyTemplate = Path(TPL_DIR, "Hotkey.tpl").read_text(encoding="utf-8")


@attr.s
class Hotkey:
    name: str = attr.ib()
    key: str = attr.ib()
    actions = attr.ib(factory=list)  # type: typing.List[typing.Union[Action, str]]
    script: 'Script' = attr.ib(default=None)

    def __attrs_post_init__(self):
        if self.script is not None:
            self.script.add_hotkey(self)

    @property
    def title(self) -> str:
        return f"<Hotkey {self.key}>"

    def dump(self) -> str:
        print(f"dump Hotkey(name='{self.name}', key='{self.key}') ...")
        return remove_empty_line(render_template(
            _HotkeyTemplate,
            hotkey=self,
            render_action=render_action,
        ))


# --- Action ---
@attr.s
class Action:
    def dump(self) -> str:
        raise NotImplementedError


@attr.s
class Key(Action):
    name = attr.ib()

    def dump(self) -> str:
        return "<Key {name}>".format(
            name=self.name,
        )


@attr.s
class KeyUp(Action):
    name = attr.ib()

    def dump(self) -> str:
        return "<KeyUp {name}>".format(
            name=self.name,
        )


@attr.s
class KeyDown(Action):
    name = attr.ib()

    def dump(self) -> str:
        return "<KeyDown {name}>".format(
            name=self.name,
        )


@attr.s
class Mouse(Action):
    """
    reference: http://hotkeynet.com/ref/clickmouse.html
    """
    button = attr.ib()  # type: str
    # Down, Up, Both, or NoClick
    stroke = attr.ib(default="")  # type: str
    # Window or Screen
    target = attr.ib(default="")  # type: str
    # NoMove, # #, Dupe, Scale, #% #%, ±# ±#
    mode = attr.ib(default="")  # type: str
    # Restore or NoRestore
    restore = attr.ib(default="")  # type: str

    def dump(self) -> str:
        return "<ClickMouse {}>".format(
            "{button}{stroke}{target}{mode}{restore}".format(
                button=(self.button + " ").lstrip(),
                stroke=(self.stroke + " ").lstrip(),
                target=(self.target + " ").lstrip(),
                mode=(self.mode + " ").lstrip(),
                restore=(self.restore + " ").lstrip(),
            ).strip()
        )


_SendLabelTemplate = Path(TPL_DIR, "SendLabel.tpl").read_text(encoding="utf-8")


@attr.s
class SendLabel(Action):
    to = attr.ib(factory=list)  # type: typing.List[str]
    actions = attr.ib(factory=list)  # type: typing.List[Action]

    @property
    def targets(self) -> str:
        return ", ".join(self.to)

    @property
    def title(self) -> str:
        return f"<SendLabel {self.targets}>"

    def dump(self) -> str:
        if len(self.to) and len(self.actions):
            return remove_empty_line(
                render_template(
                    _SendLabelTemplate,
                    send_label=self,
                    render_action=render_action,
                )
            )
        else:
            return ""


@attr.s
class CallCommand(Action):
    cmd = attr.ib(validator=attr.validators.instance_of(Command))  # type: Command
    args = attr.ib(factory=tuple)  # type: tuple

    def dump(self) -> str:
        return self.cmd.call(*self.args)


def render_action(action: typing.Union[Action, str]):
    if isinstance(action, Action):
        return action.dump()
    elif isinstance(action, str):
        return action
    else:
        raise TypeError
