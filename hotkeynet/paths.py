# -*- coding: utf-8 -*-

from pathlib_mate import Path

dir_project_root = Path.dir_here(__file__).parent

assert dir_project_root.basename == "hotkeynet-project"

dir_app = dir_project_root / "app"