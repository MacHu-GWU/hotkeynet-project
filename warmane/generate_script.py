# -*- coding: utf-8 -*-

# from hotkeynet.projects.warmane import hkn_5p_rdf as hkn
from hotkeynet.projects.warmane import hkn_10p_raid as hkn
from pathlib_mate import PathCls as Path

Path(__file__).change(new_basename="warmane.js").write_text(
    hkn.script.dump(),
    encoding="utf-8"
)
