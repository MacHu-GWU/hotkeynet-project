# -*- coding: utf-8 -*-

import attr
from .base import BaseConfig
from ..constant import game_client

@attr.s
class GameClientConfig(BaseConfig):
    """
    Number of windows.
    """
    wow_exe_path = attr.ib(default=None)
    n_windows = attr.ib(default=None)
    window_left_top_x = attr.ib(default=None)
    window_left_top_y = attr.ib(default=None)
    window_width = attr.ib(default=None)
    window_height = attr.ib(default=None)
    wrong_password_pop_up_x = attr.ib(default=None)
    wrong_password_pop_up_y = attr.ib(default=None)
    username_input_box_x = attr.ib(default=None)
    username_input_box_y = attr.ib(default=None)
    pass_item_button_x = attr.ib(default=None)
    pass_item_button_1_y= attr.ib(default=None)
    pass_item_button_2_y = attr.ib(default=None)
    pass_item_button_3_y = attr.ib(default=None)
    pass_item_button_4_y = attr.ib(default=None)

    def use_n_windows(self, n):
        self.n_windows = n

    def use_1920_1080_resolution(self):
        self.window_width = game_client.window_width_at_1920_1080
        self.window_height = game_client.window_height_at_1920_1080
        self.wrong_password_pop_up_x = game_client.wrong_password_pop_up_x_at_1920_1080
        self.wrong_password_pop_up_y = game_client.wrong_password_pop_up_y_at_1920_1080
        self.username_input_box_x = game_client.username_input_box_x_at_1920_1080
        self.username_input_box_y = game_client.username_input_box_y_at_1920_1080
        self.pass_item_button_x = game_client.pass_item_button_x_at_1920_1080
        self.pass_item_button_1_y = game_client.pass_item_button_1_y_at_1920_1080
        self.pass_item_button_2_y = game_client.pass_item_button_2_y_at_1920_1080
        self.pass_item_button_3_y = game_client.pass_item_button_3_y_at_1920_1080
        self.pass_item_button_4_y = game_client.pass_item_button_4_y_at_1920_1080

    def use_1600_900_resolution(self):
        self.window_width = game_client.window_width_at_1600_900
        self.window_height = game_client.window_height_at_1600_900
        self.wrong_password_pop_up_x = game_client.wrong_password_pop_up_x_at_1600_900
        self.wrong_password_pop_up_y = game_client.wrong_password_pop_up_y_at_1600_900
        self.username_input_box_x = game_client.username_input_box_x_at_1600_900
        self.username_input_box_y = game_client.username_input_box_y_at_1600_900
        self.pass_item_button_x = game_client.pass_item_button_x_at_1600_900
        self.pass_item_button_1_y = game_client.pass_item_button_1_y_at_1600_900
        self.pass_item_button_2_y = game_client.pass_item_button_2_y_at_1600_900
        self.pass_item_button_3_y = game_client.pass_item_button_3_y_at_1600_900
        self.pass_item_button_4_y = game_client.pass_item_button_4_y_at_1600_900

    def validate(self):
        pass