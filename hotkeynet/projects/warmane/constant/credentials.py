# -*- coding: utf-8 -*-

"""
此模块用于枚举所有的账号密码, 避免将敏感信息写入代码, 并安全地在 Hotkeynet 脚本中引用这些
信息.
"""

import json
import typing

import attr
from pathlib_mate import PathCls as Path
from enum import Enum

# put credentials.json file in the git repo root folder
credentials_file = Path(__file__).parent.parent.parent.parent.change(new_basename="credentials.json")
assert credentials_file.parent.basename == "hotkeynet-project"
credentials_data = json.loads(credentials_file.read_text(encoding="utf-8"))


@attr.s
class Credential:
    username = attr.ib()
    password = attr.ib()


# Enumerate all username password data object
# 枚举出所有的用户名密码的数据对象, 以供之后引用
class Credentials(Enum):
    cred_fatmulti1 = Credential(username="fatmulti1", password=credentials_data["fatmulti1"])
    cred_fatmulti2 = Credential(username="fatmulti2", password=credentials_data["fatmulti2"])
    cred_fatmulti3 = Credential(username="fatmulti3", password=credentials_data["fatmulti3"])
    cred_fatmulti4 = Credential(username="fatmulti4", password=credentials_data["fatmulti4"])
    cred_fatmulti5 = Credential(username="fatmulti5", password=credentials_data["fatmulti5"])
    cred_fitsheep = Credential(username="fitsheep", password=credentials_data["fitsheep"])
    cred_fatmulti6 = Credential(username="fatmulti6", password=credentials_data["fatmulti6"])
    cred_fatmulti8 = Credential(username="fatmulti8", password=credentials_data["fatmulti8"])
    cred_fatmulti9 = Credential(username="fatmulti9", password=credentials_data["fatmulti9"])
    cred_fatmulti10 = Credential(username="fatmulti10", password=credentials_data["fatmulti10"])
    cred_makun7551 = Credential(username="makun7551", password=credentials_data["makun7551"])
    cred_monkey130 = Credential(username="monkey130", password=credentials_data["monkey130"])
    cred_freiliheng = Credential(username="freiliheng", password=credentials_data["freiliheng"])
    cred_fatmulti11 = Credential(username="fatmulti11", password=credentials_data["fatmulti11"])
    cred_fatmulti12 = Credential(username="fatmulti12", password=credentials_data["fatmulti12"])
    cred_fatmulti13 = Credential(username="fatmulti13", password=credentials_data["fatmulti13"])
    cred_fatmulti14 = Credential(username="fatmulti14", password=credentials_data["fatmulti14"])
    cred_fatmulti15 = Credential(username="fatmulti15", password=credentials_data["fatmulti15"])
    cred_fatmulti16 = Credential(username="fatmulti16", password=credentials_data["fatmulti16"])
    cred_fatmulti17 = Credential(username="fatmulti17", password=credentials_data["fatmulti17"])
    cred_fatmulti18 = Credential(username="fatmulti18", password=credentials_data["fatmulti18"])
    cred_fatmulti19 = Credential(username="fatmulti19", password=credentials_data["fatmulti19"])
    cred_fatmulti20 = Credential(username="fatmulti20", password=credentials_data["fatmulti20"])
    cred_fatmulti21 = Credential(username="fatmulti21", password=credentials_data["fatmulti21"])
    cred_fatmulti22 = Credential(username="fatmulti22", password=credentials_data["fatmulti22"])
    cred_fatmulti23 = Credential(username="fatmulti23", password=credentials_data["fatmulti23"])
    cred_fatmulti24 = Credential(username="fatmulti24", password=credentials_data["fatmulti24"])
    cred_fatmulti25 = Credential(username="fatmulti25", password=credentials_data["fatmulti25"])
    cred_fatmulti26 = Credential(username="fatmulti26", password=credentials_data["fatmulti26"])
    cred_fatmulti27 = Credential(username="fatmulti27", password=credentials_data["fatmulti27"])
    cred_fatmulti28 = Credential(username="fatmulti28", password=credentials_data["fatmulti28"])
    cred_fatmulti29 = Credential(username="fatmulti29", password=credentials_data["fatmulti29"])
