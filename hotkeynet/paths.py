# -*- coding: utf-8 -*-

from pathlib_mate import Path

dir_project_root = Path.dir_here(__file__).parent

assert dir_project_root.basename == "hotkeynet-project"

dir_app = dir_project_root / "app"
dir_app_warmane = dir_app / "warmane"
path_accounts_json = dir_app_warmane / "accounts.json"

