# -*- coding: utf-8 -*-

import os

from rich import print

from hotkeynet.script import (
    Script,
    Label,
)


class TestScript:
    def test_render(self):
        with Script() as script:
            Label(name="w1", window="WoW1")
            Label(name="w2", window="WoW2")

        # print("=" * 80)
        # print(script.render())
        # print("=" * 80)


if __name__ == "__main__":
    from hotkeynet.tests import run_cov_test

    run_cov_test(__file__, "hotkeynet.script", preview=False)
