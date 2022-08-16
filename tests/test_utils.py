# -*- coding: utf-8 -*-

import os
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
    assert utils.union_list([3, 4, 1], [2, 3], [5, 3, 4]) == [1, 2, 3, 4, 5]


def test_intersection_list():
    assert utils.intersection_list([3, 2, 1], [4, 2, 3], [4, 5, 3]) == [3]


def test_difference_list():
    assert utils.difference_list([1, 2, 3, 4, 5], [1, 3], [5, 3]) == [2, 4]


if __name__ == "__main__":
    import sys
    import subprocess

    abspath = os.path.abspath(__file__)
    dir_project_root = os.path.dirname(abspath)
    for _ in range(10):
        if os.path.exists(os.path.join(dir_project_root, ".git")):
            break
        else:
            dir_project_root = os.path.dirname(dir_project_root)
    else:
        raise FileNotFoundError("cannot find project root dir!")
    dir_htmlcov = os.path.join(dir_project_root, "htmlcov")
    bin_pytest = os.path.join(os.path.dirname(sys.executable), "pytest")

    args = [
        bin_pytest,
        "-s", "--tb=native",
        f"--rootdir={dir_project_root}",
        "--cov=hotkeynet.utils",
        "--cov-report", "term-missing",
        "--cov-report", f"html:{dir_htmlcov}",
        abspath,
    ]
    subprocess.run(args, check=True)
