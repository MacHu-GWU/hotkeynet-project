# -*- coding: utf-8 -*-

"""
此模块用于枚举所有的账号密码, 避免将敏感信息写入代码, 并安全地在 HotkeyNet 脚本中
引用这些信息.
"""

import attr
from attrs_mate import AttrsClass


@attr.s
class Credential(AttrsClass):
    username: str = attr.ib()
    password: str = attr.ib()
