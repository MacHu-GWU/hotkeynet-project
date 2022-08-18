# -*- coding: utf-8 -*-

import os
import typing as T

from rich import print

from hotkeynet.script import (
    Script,
    Label,
    Hotkey,
    SendLabel,
    Key,
)
from hotkeynet import keyname


class MyScript:
    def __init__(self):
        self.script = Script()

        self.make_labels()
        self.make_hotkeys()

    def make_labels(self):
        with self.script():
            self.labels: T.List[Label] = list()
            for i in range(1, 1 + 5):
                self.labels.append(
                    Label(name=f"w{i}", window=f"WoW{i}")
                )

    def make_hotkeys(self):
        with self.script():
            with Hotkey(
                name="Key1",
                key=keyname.SCROLOCK_ON(keyname.KEY_1),
            ) as self.hk_1:
                with SendLabel(
                    name="",
                    to=self.labels,
                ):
                    Key(key=keyname.KEY_1)


def test_context():
    my_script = MyScript()
    # print(my_script.script)

    assert len(my_script.script.blocks) == 5 + 1
    assert len(my_script.script.iter_label()) == 5
    assert len(my_script.script.iter_hotkey()) == 1

    assert isinstance(my_script.hk_1, Hotkey)
    assert len(my_script.hk_1.blocks) == 1

    assert isinstance(my_script.hk_1.blocks[0], SendLabel)
    assert len(my_script.hk_1.blocks[0].to) == 5
    assert len(my_script.hk_1.blocks[0].blocks) == 1

    assert isinstance(my_script.hk_1.blocks[0].blocks[0], Key)


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
