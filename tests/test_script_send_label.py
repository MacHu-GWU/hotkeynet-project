# -*- coding: utf-8 -*-

import os
from hotkeynet.script import SendLabel, Label, Key
from hotkeynet import keyname as KN


class TestSendLabel:
    def test_render(self):
        sl = SendLabel(
            to=["w1", ],
            blocks=[
                Key.make(KN.KEY_1),
            ]
        )
        assert sl.render() == (
            "<SendLabel w1>\n"
            "    <Key 1>"
        )

    def test_render_edge_case_no_target(self):
        sl = SendLabel()
        assert sl.render() == ""

    def test_render_edge_case_no_sub_blocks(self):
        sl = SendLabel(
            to=["w1", "w2"],
        )
        assert sl.render() == ""


if __name__ == "__main__":
    from hotkeynet.tests import run_cov_test

    run_cov_test(__file__, "hotkeynet.script", preview=False)
