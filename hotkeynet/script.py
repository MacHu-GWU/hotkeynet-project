# -*- coding: utf-8 -*-

import typing
from collections import OrderedDict

import attr
from pathlib_mate import PathCls as Path

from . import keyname
from .utils import render_template, remove_empty_line

TPL_DIR = Path(__file__).change(new_basename="templates")

_ScriptTemplate = Path(TPL_DIR, "Script.tpl").read_text(encoding="utf-8")


@attr.s
class Script:
    """

    :param labels: OrderedDict([(label_name, window_name), ...])
    """
    commands: OrderedDict = attr.ib(factory=OrderedDict)
    templates: OrderedDict = attr.ib(factory=OrderedDict)
    hotkeys: OrderedDict = attr.ib(factory=OrderedDict)
    labels: OrderedDict = attr.ib(factory=OrderedDict)

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
                existing_hotkey = self.hotkeys[hotkey.key]
                msg = (
                    f"Hotkey(name={hotkey.name},key={hotkey.key}) cannot defined. "
                    f"Another hotkey Hotkey(name={existing_hotkey.name},key={existing_hotkey.key}) already exists. "
                )
                raise ValueError(msg)
        self.hotkeys[hotkey.key] = hotkey

    def dump(self):
        return render_template(_ScriptTemplate, script=self)


@attr.s
class Command:
    name: str = attr.ib(validator=attr.validators.instance_of(str))
    actions = attr.ib(factory=list)  # type: typing.List[typing.Union[Action, str]]
    script: 'Script' = attr.ib(default=None, validator=attr.validators.optional(attr.validators.instance_of(Script)))

    _template = Path(TPL_DIR, "Command.tpl").read_text(encoding="utf-8")

    def __attrs_post_init__(self):
        if self.script is not None:
            self.script.add_command(self)

    @property
    def title(self):
        return f"<Command {self.name}>"

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
                self._template,
                command=self,
                render_action=render_action,
            )
        )


@attr.s
class Template:
    name: str = attr.ib()
    script: 'Script' = attr.ib(default=None, validator=attr.validators.optional(attr.validators.instance_of(Script)))

    def __attrs_post_init__(self):
        if self.script is not None:
            self.script.add_template(self)


@attr.s
class Hotkey:
    name: str = attr.ib()
    key: str = attr.ib()
    actions = attr.ib(factory=list)  # type: typing.List[typing.Union[Action, str]]
    script: 'Script' = attr.ib(default=None, validator=attr.validators.optional(attr.validators.instance_of(Script)))

    _template = Path(TPL_DIR, "Hotkey.tpl").read_text(encoding="utf-8")

    def __attrs_post_init__(self):
        if self.script is not None:
            self.script.add_hotkey(self)

    @property
    def title(self) -> str:
        return f"<Hotkey {self.key}>"

    _send_labels = None # type: typing.Dict[str, SendLabel]

    def get_send_label_by_name(self, name) -> 'SendLabel':
        if self._send_labels is None:
            self._send_labels = dict()
            for action in self.actions:
                if isinstance(action, SendLabel):
                    self._send_labels[action.name] = action
        return self._send_labels[name]

    def validate(self):
        # don't allow duplicate label in SendLabel actions.
        for action in self.actions :
            if isinstance(action, SendLabel):
                for label in action.to:
                    for _action in self.actions:
                        if isinstance(_action, SendLabel) \
                            and (action.name != _action.name) \
                            and (label in _action.to):
                            raise ValueError(f"label {label} in {action} conflicts with {_action}")

    def dump(self) -> str:
        print(f"dump Hotkey(name='{self.name}', key='{self.key}') ...")
        self.validate()
        if len(self.actions):
            content = remove_empty_line(render_template(
                self._template,
                hotkey=self,
                render_action=render_action,
            ))
            if content.count("\n") == 0:
                print("    no action, skip")
                return ""
            else:
                return content
        else:
            print("    no action, skip")
            return ""

@attr.s
class MovementHotkey(Hotkey):
    name: str = attr.ib()
    key: str = attr.ib()
    actions = attr.ib(factory=list)  # type: typing.List[typing.Union[Action, str]]
    script: 'Script' = attr.ib(default=None, validator=attr.validators.optional(attr.validators.instance_of(Script)))

    @property
    def title(self) -> str:
        return f"<MovementHotkey {self.key}>"


# --- Action ---
@attr.s
class Action:
    def dump(self) -> str:
        raise NotImplementedError


@attr.s
class Key(Action):
    name = attr.ib(validator=attr.validators.instance_of(str))

    def dump(self) -> str:
        return "<Key {name}>".format(
            name=self.name,
        )

    @classmethod
    def trigger(cls):
        return cls(name="%Trigger%")


@attr.s
class KeyUp(Action):
    name = attr.ib(validator=attr.validators.instance_of(str))

    def dump(self) -> str:
        return "<KeyUp {name}>".format(
            name=self.name,
        )


@attr.s
class KeyDown(Action):
    name = attr.ib(validator=attr.validators.instance_of(str))

    def dump(self) -> str:
        return "<KeyDown {name}>".format(
            name=self.name,
        )


@attr.s
class Mouse(Action):
    """
    reference: http://hotkeynet.com/ref/clickmouse.html
    """
    button = attr.ib(validator=attr.validators.instance_of(str))  # type: str
    # Down, Up, Both, or NoClick
    stroke = attr.ib(default="", validator=attr.validators.instance_of(str))  # type: str
    # Window or Screen
    target = attr.ib(default="", validator=attr.validators.instance_of(str))  # type: str
    # NoMove, # #, Dupe, Scale, #% #%, ±# ±#
    mode = attr.ib(default="", validator=attr.validators.instance_of(str))  # type: str
    # Restore or NoRestore
    restore = attr.ib(default="", validator=attr.validators.instance_of(str))  # type: str

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


def _build_modified_mouse_click(modifier, button):
    return "\n".join([
        action.dump()
        for action in [
            KeyDown(name=modifier),
            Mouse(button=button, stroke="Down"),
            Mouse(button=button, stroke="Up"),
            KeyUp(name=modifier),
        ]
    ])


@attr.s
class ModifiedMouseClick(Action):
    modifier = attr.ib()
    button = attr.ib()

    def dump(self) -> str:
        return _build_modified_mouse_click(modifier=self.modifier, button=self.button)

    @classmethod
    def shift_left_click(cls):
        return cls(modifier=keyname.SHIFT, button=keyname.MOUSE_LButton)

    @classmethod
    def shift_right_click(cls):
        return cls(modifier=keyname.SHIFT, button=keyname.MOUSE_LButton)

    @classmethod
    def shift_middle_click(cls):
        return cls(modifier=keyname.SHIFT, button=keyname.MOUSE_MButton)

    @classmethod
    def alt_left_click(cls):
        return cls(modifier=keyname.ALT, button=keyname.MOUSE_LButton)

    @classmethod
    def alt_right_click(cls):
        return cls(modifier=keyname.ALT, button=keyname.MOUSE_LButton)

    @classmethod
    def alt_middle_click(cls):
        return cls(modifier=keyname.ALT, button=keyname.MOUSE_MButton)

    @classmethod
    def ctrl_left_click(cls):
        return cls(modifier=keyname.CTRL, button=keyname.MOUSE_LButton)

    @classmethod
    def ctrl_right_click(cls):
        return cls(modifier=keyname.CTRL, button=keyname.MOUSE_LButton)

    @classmethod
    def ctrl_middle_click(cls):
        return cls(modifier=keyname.CTRL, button=keyname.MOUSE_MButton)


@attr.s
class SendLabel(Action):
    name = attr.ib(validator=attr.validators.instance_of(str))
    to = attr.ib(factory=list)  # type: typing.List[str]
    actions = attr.ib(factory=list)  # type: typing.List[typing.Union[Action, str]]
    _template = Path(TPL_DIR, "SendLabel.tpl").read_text(encoding="utf-8")

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
                    self._template,
                    send_label=self,
                    render_action=render_action,
                )
            )
        else:
            return ""


@attr.s
class SendFocusWindow(Action):
    name = attr.ib(validator=attr.validators.instance_of(str))
    actions = attr.ib(factory=list)  # type: typing.List[typing.Union[Action, str]]
    _template = Path(TPL_DIR, "SendLabel.tpl").read_text(encoding="utf-8")

    @property
    def title(self) -> str:
        return f"<SendFocusWin>"

    def dump(self) -> str:
        if len(self.actions):
            return remove_empty_line(
                render_template(
                    self._template,
                    send_label=self,
                    render_action=render_action,
                )
            )
        else:
            return ""


@attr.s
class CallCommand(Action):
    cmd = attr.ib()  # type: typing.Union[Command, str]
    args = attr.ib(factory=tuple)  # type: tuple

    @cmd.validator
    def check_cmd(self, attribute, value):
        if not isinstance(value, (Command, str)):
            raise TypeError

    def dump(self) -> str:
        return self.cmd.call(*self.args)


def render_action(action: typing.Union[Action, str]):
    if isinstance(action, Action):
        return action.dump()
    elif isinstance(action, str):
        return action
    else:
        raise TypeError
