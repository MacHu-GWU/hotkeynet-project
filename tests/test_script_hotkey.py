# -*- coding: utf-8 -*-

import os
from hotkeynet import keyname
from hotkeynet.script import Command, Hotkey, Key, SendLabel


class TestHotkey:
    def test_render_edge_case_no_sub_blocks(self):
        # just no sub block
        hk = Hotkey(
            key=keyname.KEY_1,
        )
        assert hk.render() == ""

        # has sub block, but all element in sub block is also empty
        hk = Hotkey(
            key=keyname.KEY_1,
            blocks=[
                SendLabel(
                    to=[],
                    blocks=[
                        Key(key=keyname.KEY_1)
                    ]
                )
            ]
        )
        assert hk.render() == ""


if __name__ == "__main__":
    from hotkeynet.tests import run_cov_test

    run_cov_test(__file__, "hotkeynet.script", preview=False)
