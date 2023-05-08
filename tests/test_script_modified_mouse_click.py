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
    from hotkeynet.tests import run_cov_test

    run_cov_test(__file__, "hotkeynet.script", preview=False)
