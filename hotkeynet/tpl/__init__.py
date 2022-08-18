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

block_tpl = env.get_template("Block.tpl")
script_tpl = env.get_template("Script.tpl")
