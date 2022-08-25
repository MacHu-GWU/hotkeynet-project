# -*- coding: utf-8 -*-

"""
此模块用于枚举所有的在 www.warmane.com 的账号密码, 避免将敏感信息写入代码,
并安全地在 HotkeyNet 脚本中引用这些信息.
"""

import os
from enum import Enum

from superjson import json

from hotkeynet.enumerate import EnumHelper
from hotkeynet.game.wow.model import Account

from .paths import path_tauri_accounts_json, path_tauri_test_accounts_json

if "CI" in os.environ:
    accounts_data = json.load(path_tauri_test_accounts_json.abspath, verbose=False)
else:
    accounts_data = json.load(path_tauri_accounts_json.abspath, verbose=False)


def load_account(username: str) -> Account:
    return Account(username=username, password=accounts_data[username])


class AccountEnum(Enum):
    """
    枚举出所有的用户名密码的数据对象, 以供之后引用.
    """
    account_fatmulti1 = load_account("fatmulti1")
    account_fatmulti2 = load_account("fatmulti2")
    account_fatmulti3 = load_account("fatmulti3")
    account_fatmulti4 = load_account("fatmulti4")
    account_fatmulti5 = load_account("fatmulti5")


class AccountHelper(EnumHelper[AccountEnum, Account]):
    enum_class = AccountEnum
