# -*- coding: utf-8 -*-

import attr
from attrs_mate import AttrsClass

from hotkeynet.game.wow.wlk import coordinator


@attr.s
class GameClient(AttrsClass):
    """
    定义了你所使用的游戏客户端的详细信息.
    """
    wow_exe_path: str = attr.ib(default=None)

    window_left_top_x: int = attr.ib(default=None)
    window_left_top_y: int = attr.ib(default=None)
    window_width: int = attr.ib(default=None)
    window_height: int = attr.ib(default=None)
    wrong_password_pop_up_x: int = attr.ib(default=None)
    wrong_password_pop_up_y: int = attr.ib(default=None)
    username_input_box_x: int = attr.ib(default=None)
    username_input_box_y: int = attr.ib(default=None)
    log_out_button_x: int = attr.ib(default=None)
    log_out_button_y: int = attr.ib(default=None)
    return_to_game_button_x: int = attr.ib(default=None)
    return_to_game_button_y: int = attr.ib(default=None)
    pass_item_button_x: int = attr.ib(default=None)
    pass_item_button_1_y: int = attr.ib(default=None)
    pass_item_button_2_y: int = attr.ib(default=None)
    pass_item_button_3_y: int = attr.ib(default=None)
    pass_item_button_4_y: int = attr.ib(default=None)

    def _use_resolution(self, resolution: str) -> 'GameClient':
        keyword = f"_at_{resolution}"
        for attr in coordinator.__dict__:
            if keyword in attr:
                setattr(
                    self,
                    attr.replace(keyword, ""),
                    getattr(coordinator, attr)
                )
        return self

    def use_1920_1080_resolution(self):
        return self._use_resolution("1920_1080")

    def use_1600_900_resolution(self):
        return self._use_resolution("1600_900")

    def use_1176_664_resolution(self):
        return self._use_resolution("1176_664")
