# -*- coding: utf-8 -*-

import typing as T
import attr
from attrs_mate import AttrsClass
from hotkeynet.game.wow.wlk import coordinator


@attr.s
class GameClient(AttrsClass):
    """
    Number of windows.
    """
    wow_exe_path = attr.ib(default=None)  # type: str

    window_left_top_x = attr.ib(default=None)  # type: int
    window_left_top_y = attr.ib(default=None)  # type: int
    window_width = attr.ib(default=None)  # type: int
    window_height = attr.ib(default=None)  # type: int
    wrong_password_pop_up_x = attr.ib(default=None)  # type: int
    wrong_password_pop_up_y = attr.ib(default=None)  # type: int
    username_input_box_x = attr.ib(default=None)  # type: int
    username_input_box_y = attr.ib(default=None)  # type: int
    log_out_button_x = attr.ib(default=None)  # type: int
    log_out_button_y = attr.ib(default=None)  # type: int
    return_to_game_button_x = attr.ib(default=None)  # type: int
    return_to_game_button_y = attr.ib(default=None)  # type: int
    pass_item_button_x = attr.ib(default=None)  # type: int
    pass_item_button_1_y = attr.ib(default=None)  # type: int
    pass_item_button_2_y = attr.ib(default=None)  # type: int
    pass_item_button_3_y = attr.ib(default=None)  # type: int
    pass_item_button_4_y = attr.ib(default=None)  # type: int

    def _use_resolution(self, resolution: str):
        keyword = f"_at_{resolution}"
        for attr in coordinator.__dict__:
            if keyword in attr:
                setattr(
                    self,
                    attr.replace(keyword, ""),
                    getattr(coordinator, attr)
                )

    def use_1920_1080_resolution(self):
        self._use_resolution("1920_1080")

    def use_1600_900_resolution(self):
        self._use_resolution("1600_900")

    def use_1176_664_resolution(self):
        self._use_resolution("1176_664")
