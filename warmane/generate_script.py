# -*- coding: utf-8 -*-

from hotkeynet.templates import warmane_5p_rdf as warmane
from pathlib_mate import PathCls as Path

Path(__file__).change(new_basename="warmane.js").write_text(
    warmane.script.dump(),
    encoding="utf-8"
)
