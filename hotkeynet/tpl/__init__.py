# -*- coding: utf-8 -*-

"""
Jinja 2 template store.
"""

from jinja2 import Environment, PackageLoader

env = Environment(
    loader=PackageLoader(
        package_name="hotkeynet",
        package_path="tpl",
    )
)

command_tpl = env.get_template("Command.tpl")
hotkey_tpl = env.get_template("Hotkey.tpl")
send_label_tpl = env.get_template("SendLabel.tpl")
script_tpl = env.get_template("Script.tpl")
