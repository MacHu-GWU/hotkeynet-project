# -*- coding: utf-8 -*-

import os
import typing as T

from rich import print

from hotkeynet.script import (
    Label,
)


class TestLabel:
    def test(self):
        lb = Label(name="w1", window="wow1")
        assert lb.render() == "<Label w1 local SendWinM wow1>"


if __name__ == "__main__":
    from hotkeynet.tests import run_cov_test

    run_cov_test(__file__, "hotkeynet.script", preview=False)
