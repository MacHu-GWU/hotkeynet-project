# -*- coding: utf-8 -*-

import os

from rich import print

from hotkeynet.script import (
    Command,
    CommandArgEnum,
    SendPC,
    Run,
    RenameWin,
)


class TestCommand:
    def test_render(self):
        with Command(name="RunWow") as cmd:
            with SendPC():
                Run(path=r"C:\Games\World of Warcraft\Wow.exe")
                RenameWin(old="World of Warcraft", new=CommandArgEnum.Arg1)

        assert cmd.render() == (
            "<Command RunWow>\n"
            "    <SendPC local>\n"
            "        <Run \"C:\\Games\\World of Warcraft\\Wow.exe\">\n"
            "        <RenameWin \"World of Warcraft\" %1%>"
        )

        assert cmd.call(args=["WoW1", ]).render() == "<RunWow WoW1>"


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
