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
    from hotkeynet.tests import run_cov_test

    run_cov_test(__file__, "hotkeynet.script", preview=False)
