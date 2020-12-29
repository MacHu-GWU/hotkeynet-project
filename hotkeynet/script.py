# -*- coding: utf-8 -*-

import attr
from collections import OrderedDict
import jinja2
from . import keyname


@attr.s
class Script:
    commands: OrderedDict = attr.ib()
    templates: OrderedDict = attr.ib()
    hotkeys: OrderedDict = attr.ib()

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


@attr.s
class Command:
    name: str = attr.ib()
    content: str = attr.ib()
    script: 'Script' = attr.ib(default=None)

    def __attrs_post_init__(self):
        if self.script is not None:
            self.script.add_command(self)

    def call(self, *args):
        return "<{}{}>".format(
            self.name,
            " " + " ".join(args) if len(args) else ""
        )

    def dump(self):
        return """
        <Command {self.name}>
        {self.content}
        """.format(self=self)


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
    script: 'Script' = attr.ib(default=None)

    def __attrs_post_init__(self):
        if self.script is not None:
            self.script.add_hotkey(self)


@attr.s
class Key:
    name = attr.ib()
    mod1 = attr.ib(default=None)
    mod2 = attr.ib(default=None)
    mod3 = attr.ib(default=None)

    def dump(self):
        return "<Key {name}>".format(
            name=self.name,
            mod1=self.mod1 if self.mod1 else "",
            mod2=self.mod2 if self.mod2 else "",
            mod3=self.mod3 if self.mod3 else "",
        )


@attr.s
class MouseClick:
    name = attr.ib()
    mod1 = attr.ib(default=None)


def render_template(content, **kwargs):
    return jinja2.Template(content).render(**kwargs)




class SendLabel