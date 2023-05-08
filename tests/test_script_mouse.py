# -*- coding: utf-8 -*-

import os
from hotkeynet import keyname
from hotkeynet.script import ClickMouse


class TestMouse:
    def test_render(self):
        assert ClickMouse(button=keyname.MOUSE_LButton).render() == "<ClickMouse LButton>"
        assert (
            ClickMouse(button=keyname.MOUSE_LButton)
            .set_mode_as_x_y(640, 480)
            .set_restore_as_no()
            .render()
            == "<ClickMouse LButton 640 480 NoRestore>"
        )


if __name__ == "__main__":
    from hotkeynet.tests import run_cov_test

    run_cov_test(__file__, "hotkeynet.script", preview=False)
