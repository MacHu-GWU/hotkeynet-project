# -*- coding: utf-8 -*-

import os
from hotkeynet import keyname
from hotkeynet.script import Key


class TestSendKey:
    def test_render(self):
        assert Key(key=keyname.ALT_(keyname.KEY_1)).render() == "<Key Alt 1>"


if __name__ == "__main__":
    from hotkeynet.tests import run_cov_test

    run_cov_test(__file__, "hotkeynet.script", preview=False)
