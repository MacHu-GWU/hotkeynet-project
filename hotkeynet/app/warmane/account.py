# -*- coding: utf-8 -*-

"""
此模块用于枚举所有的在 www.warmane.com 的账号密码, 避免将敏感信息写入代码,
并安全地在 HotkeyNet 脚本中引用这些信息.
"""

import typing as T

from superjson import json
from hotkeynet.game.wow.model import (
    Account,
    Window,
    Character,
)
from hotkeynet.game.wow.wlk.talent_category_association import (
    Talent as TL,
    TalentCategory as TC,
    get_talent_by_category,
    get_category_by_talent,
)
from hotkeynet.game.wow.wlk.talent import Talent
from hotkeynet.paths import path_accounts_json

from enum import Enum

accounts_data = json.load(path_accounts_json.abspath, verbose=False)


def load_account(username: str) -> Account:
    return Account(username=username, password=accounts_data[username])


# Enumerate all username password data object
# 枚举出所有的用户名密码的数据对象, 以供之后引用
class AccountEnum(Enum):
    account_fatmulti1 = load_account("fatmulti1")
    account_fatmulti2 = load_account("fatmulti2")
    account_fatmulti3 = load_account("fatmulti3")
    account_fatmulti4 = load_account("fatmulti4")
    account_fatmulti5 = load_account("fatmulti5")
    account_fitsheep = load_account("fitsheep")
    account_fatmulti6 = load_account("fatmulti6")
    account_fatmulti8 = load_account("fatmulti8")
    account_fatmulti9 = load_account("fatmulti9")
    account_fatmulti10 = load_account("fatmulti10")
    account_makun7551 = load_account("makun7551")
    account_monkey130 = load_account("monkey130")
    account_freiliheng = load_account("freiliheng")
    account_fatmulti11 = load_account("fatmulti11")
    account_fatmulti12 = load_account("fatmulti12")
    account_fatmulti13 = load_account("fatmulti13")
    account_fatmulti14 = load_account("fatmulti14")
    account_fatmulti15 = load_account("fatmulti15")
    account_fatmulti16 = load_account("fatmulti16")
    account_fatmulti17 = load_account("fatmulti17")
    account_fatmulti18 = load_account("fatmulti18")
    account_fatmulti19 = load_account("fatmulti19")
    account_fatmulti20 = load_account("fatmulti20")
    account_fatmulti21 = load_account("fatmulti21")
    account_fatmulti22 = load_account("fatmulti22")
    account_fatmulti23 = load_account("fatmulti23")
    account_fatmulti24 = load_account("fatmulti24")
    account_fatmulti25 = load_account("fatmulti25")
    account_fatmulti26 = load_account("fatmulti26")
    account_fatmulti27 = load_account("fatmulti27")
    account_fatmulti28 = load_account("fatmulti28")
    account_fatmulti29 = load_account("fatmulti29")


all_window = TP

window_list = [
    Window(title="WoW{}".format(ind + 1), label="w{}".format( str(ind + 1).zfill(2)))
    for ind in range(25)
]  # type: T.List[Window]

window_index = {
    ind + 1: window
    for ind, window in enumerate(window_list)
}  # type: typing.Dict[int, Window]
