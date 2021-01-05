# -*- coding: utf-8 -*-

import pytest
from hotkeynet import utils


def test_remove_indent():
    content = """
    <div>
        <strong></strong>
    </div>
    """
    assert utils.remove_indent(content) == "\n".join([
        "<div>",
        "    <strong></strong>",
        "</div>",
    ])


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
