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


def test_union_list():
    assert utils.union_list([3,4,1], [2,3], [5,3,4]) == [1,2,3,4,5]


def test_difference_list():
    assert utils.difference_list([1,2,3,4,5], [1,3], [5,3]) == [2,4]


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
