# -*- coding: utf-8 -*-

import os

from hotkeynet.script import SendLabel, Label, ModifiedClickMouse


class TestModifiedMouseClick:
    def test_dump_minimal(self):
        with SendLabel(
            to=["w1", "w2"],
        ) as send_label:
            ModifiedClickMouse.shift_left_click()

        assert send_label.render() == (
            "<SendLabel w1, w2>\n"
            "    <KeyDown Shift>\n"
            "    <ClickMouse LButton Down>\n"
            "    <ClickMouse LButton Up>\n"
            "    <KeyUp Shift>"
        )


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
        "-s", "--tb=native", "-vv",
        f"--rootdir={dir_project_root}",
        "--cov=hotkeynet.script",
        "--cov-report", "term-missing",
        "--cov-report", f"html:{dir_htmlcov}",
        abspath,
    ]
    subprocess.run(args)
