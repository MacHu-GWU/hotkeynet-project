# -*- coding: utf-8 -*-

import attr
from collections import OrderedDict
import jinja2
from pathlib_mate import PathCls as Path

from . import keyname
from .utils import render_template, remove_comments


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
        if hotkey.name in self.commands:
            if not ignore_duplicate:
                raise ValueError(f"Duplicate hotkey name found {hotkey.name}")
        self.hotkeys[hotkey.name] = hotkey

    def dump(self):
        return render_template(_ScriptTemplate, script=self)


_CommandTemplate = Path(TPL_DIR, "Command.tpl").read_text(encoding="utf-8")


@attr.s
class Command:
    name: str = attr.ib()
    content: str = attr.ib()
    script: 'Script' = attr.ib(default=None)

    def __attrs_post_init__(self):
        if self.script is not None:
            self.script.add_command(self)

    def call(self, *args):
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

    def dump(self):
        """
        渲染整个 Command 代码块

        :return:
        """
        return render_template(_CommandTemplate, command=self)


@attr.s
class Template:
    name: str = attr.ib()
    script: 'Script' = attr.ib(default=None)

    def __attrs_post_init__(self):
        if self.script is not None:
            self.script.add_template(self)


@attr.s
class Hotkey:
    name: str = attr.ib()
    key: str = attr.ib()
    script: 'Script' = attr.ib(default=None)

    def __attrs_post_init__(self):
        if self.script is not None:
            self.script.add_hotkey(self)

    @property
    def title(self):
        return f"<Hotkey {self.key}>"

    def dump(self):
        return "<Hotkey>"


@attr.s
class KeyboardMouseAction:
    pass


@attr.s
class Key(KeyboardMouseAction):
    name = attr.ib()

    def dump(self):
        return "<Key {name}>".format(
            name=self.name,
        )

@attr.s
class KeyUp(KeyboardMouseAction):
    name = attr.ib()

    def dump(self):
        return "<KeyUp {name}>".format(
            name=self.name,
        )

@attr.s
class KeyDown(KeyboardMouseAction):
    name = attr.ib()

    def dump(self):
        return "<KeyDown {name}>".format(
            name=self.name,
        )

@attr.s
class Mouse(KeyboardMouseAction):
    """
    reference: http://hotkeynet.com/ref/clickmouse.html
    """
    button = attr.ib()
    stroke = attr.ib(default="") # Down, Up, Both, or NoClick
    target = attr.ib(default="") # Window or Screen
    mode = attr.ib(default="") # NoMove, # #, Dupe, Scale, #% #%, ±# ±#
    restore = attr.ib(default="") # Restore or NoRestore

    def dump(self):
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
class SendLabel:
    to = attr.ib(factory=list)
    actions = attr.ib(factory=list)

    @property
    def targets(self):
        return ", ".join(self.to)

    def dump(self):
        return render_template(_SendLabelTemplate, send_label=self)