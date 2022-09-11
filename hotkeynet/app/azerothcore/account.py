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

from .paths import path_azerothcore_accounts_json, path_azerothcore_test_accounts_json

if "CI" in os.environ:
    accounts_data = json.load(path_azerothcore_accounts_json.abspath, verbose=False)
else:
    accounts_data = json.load(path_azerothcore_test_accounts_json.abspath, verbose=False)


def load_account(username: str) -> Account:
    return Account(username=username, password=accounts_data[username])


class AccountEnum(Enum):
    """
    枚举出所有的用户名密码的数据对象, 以供之后引用.
    """
    account_fat01 = load_account("fat01")
    account_fat02 = load_account("fat02")
    account_fat03 = load_account("fat03")
    account_fat04 = load_account("fat04")
    account_fat05 = load_account("fat05")
    account_fat06 = load_account("fat06")
    account_fat07 = load_account("fat07")
    account_fat08 = load_account("fat08")
    account_fat09 = load_account("fat09")
    account_fat10 = load_account("fat10")


class AccountEnumHelper(EnumHelper[AccountEnum, Account]):
    enum_class = AccountEnum
