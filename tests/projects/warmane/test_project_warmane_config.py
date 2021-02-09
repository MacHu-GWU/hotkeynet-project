# -*- coding: utf-8 -*-

import pytest
from pytest import raises, approx
from hotkeynet.projects.warmane.config import (
    ensure_labels,
    different_labels,
    union_list,
    difference_list,
)

def test_ensure_labels():
    assert ensure_labels([1, 2, 3]) == ["w1", "w2", "w3"]
    assert ensure_labels(["w1", "w2", "w3"]) == ["w1", "w2", "w3"]


def test_union_list():
    assert union_list([3, 2], [1, 5], [6, 4], [1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]


def test_difference_list():
    assert difference_list([3, 2, 1, 4, 5, 6], [5, 2]) == [1, 3, 4, 6]
    assert difference_list([3, 2, 1, 4, 5, 6], [2,], [5, 2,]) == [1, 3, 4, 6]


def test_different_labels():
    assert different_labels([3, 2, 1, 4, 5, 6], [2,], ["w6", "w4",]) == ["w1", "w3", "w5"]


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
