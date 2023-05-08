# -*- coding: utf-8 -*-

import os
from hotkeynet import keyname
from hotkeynet.script import ClickMouse


class TestMouse:
    def test_set_attribute(self):
        _ = (
            ClickMouse()
            .set_left_click()
            .set_right_click()
            .set_middle_click()
            .set_click_button4()
            .set_click_button5()
            .set_stroke_down()
            .set_stroke_as_up()
            .set_stroke_as_both()
            .set_stroke_as_no_click()
            .set_target_as_window()
            .set_target_as_screen()
            .set_mode_as_no_move()
            .set_mode_as_dupe()
            .set_mode_as_scale()
            .set_mode_as_x_y(x=0, y=0)
            .set_restore_as_yes()
            .set_restore_as_no()
        )

    def test_render(self):
        assert (
            ClickMouse(button=keyname.MOUSE_LButton).render() == "<ClickMouse LButton>"
        )
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
