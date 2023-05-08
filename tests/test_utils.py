# -*- coding: utf-8 -*-

import os
from hotkeynet import utils


def test_render_template():
    content = "Hello {{ name }}"
    assert utils.render_template(content, data={"name": "Alice"}) == "Hello Alice"


def test_remove_empty_line():
    content = "<div>\n" "    \n" "    <strong></strong>\n" "    \n" "</div>\n"
    assert utils.remove_empty_line(content) == (
        "<div>\n" "    <strong></strong>\n" "</div>"
    )


def test_union_list():
    assert utils.union_list([3, 4, 1], [2, 3], [5, 3, 4]) == [1, 2, 3, 4, 5]


def test_intersection_list():
    assert utils.intersection_list([3, 2, 1], [4, 2, 3], [4, 5, 3]) == [3]


def test_difference_list():
    assert utils.difference_list([1, 2, 3, 4, 5], [1, 3], [5, 3]) == [2, 4]


def test_set_to_list():
    assert utils.set_to_list({3, 1, 2}) == [1, 2, 3]
    assert utils.set_to_list({3, 1, 2}, reverse=True) == [3, 2, 1]


def test_has_duplicate():
    assert utils.has_duplicate([1, 1, 2]) is True
    assert utils.has_duplicate([1, 2, 3]) is False


if __name__ == "__main__":
    from hotkeynet.tests import run_cov_test

    run_cov_test(__file__, "hotkeynet.utils", preview=False)
