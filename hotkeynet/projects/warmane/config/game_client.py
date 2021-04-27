# -*- coding: utf-8 -*-

import attr
import typing
from .base import BaseConfig
from ..constant import game_client
from ..constant import credentials

@attr.s
class GameClientConfig(BaseConfig):
    """
    Number of windows.
    """
    wow_exe_path = attr.ib(default=None) # type: str
    n_windows = attr.ib(default=None) # type: int
    window_left_top_x = attr.ib(default=None) # type: int
    window_left_top_y = attr.ib(default=None) # type: int
    window_width = attr.ib(default=None) # type: int
    window_height = attr.ib(default=None) # type: int
    wrong_password_pop_up_x = attr.ib(default=None) # type: int
    wrong_password_pop_up_y = attr.ib(default=None) # type: int
    username_input_box_x = attr.ib(default=None) # type: int
    username_input_box_y = attr.ib(default=None) # type: int
    log_out_button_x = attr.ib(default=None) # type: int
    log_out_button_y = attr.ib(default=None) # type: int
    return_to_game_button_x = attr.ib(default=None) # type: int
    return_to_game_button_y = attr.ib(default=None) # type: int
    pass_item_button_x = attr.ib(default=None) # type: int
    pass_item_button_1_y= attr.ib(default=None) # type: int
    pass_item_button_2_y = attr.ib(default=None) # type: int
    pass_item_button_3_y = attr.ib(default=None) # type: int
    pass_item_button_4_y = attr.ib(default=None) # type: int
    credential_list = attr.ib(default=lambda: list())  # type: typing.List[credentials.Credentials.Credential]

    def use_n_windows(self, n):
        self.n_windows = n

    def use_1920_1080_resolution(self):
        self.window_left_top_x = game_client.window_left_top_x
        self.window_left_top_y = game_client.window_left_top_y
        self.window_width = game_client.window_width_at_1920_1080
        self.window_height = game_client.window_height_at_1920_1080
        self.wrong_password_pop_up_x = game_client.wrong_password_pop_up_x_at_1920_1080
        self.wrong_password_pop_up_y = game_client.wrong_password_pop_up_y_at_1920_1080
        self.username_input_box_x = game_client.username_input_box_x_at_1920_1080
        self.username_input_box_y = game_client.username_input_box_y_at_1920_1080
        self.log_out_button_x = game_client.log_out_button_x_at_1920_1080
        self.log_out_button_y = game_client.log_out_button_y_at_1920_1080
        self.return_to_game_button_x = game_client.return_to_game_button_x_at_1920_1080
        self.return_to_game_button_y = game_client.return_to_game_button_y_at_1920_1080
        self.pass_item_button_x = game_client.pass_item_button_x_at_1920_1080
        self.pass_item_button_1_y = game_client.pass_item_button_1_y_at_1920_1080
        self.pass_item_button_2_y = game_client.pass_item_button_2_y_at_1920_1080
        self.pass_item_button_3_y = game_client.pass_item_button_3_y_at_1920_1080
        self.pass_item_button_4_y = game_client.pass_item_button_4_y_at_1920_1080

    def use_1600_900_resolution(self):
        self.window_left_top_x = game_client.window_left_top_x
        self.window_left_top_y = game_client.window_left_top_y
        self.window_width = game_client.window_width_at_1600_900
        self.window_height = game_client.window_height_at_1600_900
        self.wrong_password_pop_up_x = game_client.wrong_password_pop_up_x_at_1600_900
        self.wrong_password_pop_up_y = game_client.wrong_password_pop_up_y_at_1600_900
        self.username_input_box_x = game_client.username_input_box_x_at_1600_900
        self.username_input_box_y = game_client.username_input_box_y_at_1600_900
        self.log_out_button_x = game_client.log_out_button_x_at_1600_900
        self.log_out_button_y = game_client.log_out_button_y_at_1600_900
        self.return_to_game_button_x = game_client.return_to_game_button_x_at_1600_900
        self.return_to_game_button_y = game_client.return_to_game_button_y_at_1600_900
        self.pass_item_button_x = game_client.pass_item_button_x_at_1600_900
        self.pass_item_button_1_y = game_client.pass_item_button_1_y_at_1600_900
        self.pass_item_button_2_y = game_client.pass_item_button_2_y_at_1600_900
        self.pass_item_button_3_y = game_client.pass_item_button_3_y_at_1600_900
        self.pass_item_button_4_y = game_client.pass_item_button_4_y_at_1600_900

    def use_1176_664_resolution(self):
        self.window_left_top_x = game_client.window_left_top_x
        self.window_left_top_y = game_client.window_left_top_y
        self.window_width = game_client.window_width_at_1176_664
        self.window_height = game_client.window_height_at_1176_664
        self.wrong_password_pop_up_x = game_client.wrong_password_pop_up_x_at_1176_664
        self.wrong_password_pop_up_y = game_client.wrong_password_pop_up_y_at_1176_664
        self.username_input_box_x = game_client.username_input_box_x_at_1176_664
        self.username_input_box_y = game_client.username_input_box_y_at_1176_664
        self.log_out_button_x = game_client.log_out_button_x_at_1176_664
        self.log_out_button_y = game_client.log_out_button_y_at_1176_664
        self.return_to_game_button_x = game_client.return_to_game_button_x_at_1176_664
        self.return_to_game_button_y = game_client.return_to_game_button_y_at_1176_664
        self.pass_item_button_x = game_client.pass_item_button_x_at_1176_664
        self.pass_item_button_1_y = game_client.pass_item_button_1_y_at_1176_664
        self.pass_item_button_2_y = game_client.pass_item_button_2_y_at_1176_664
        self.pass_item_button_3_y = game_client.pass_item_button_3_y_at_1176_664
        self.pass_item_button_4_y = game_client.pass_item_button_4_y_at_1176_664

    def use_credential_list_default(self):
        self.credential_list = [
            # 1-5
            credentials.Credentials.cred_fatmulti1.value,
            credentials.Credentials.cred_fatmulti2.value,
            credentials.Credentials.cred_fatmulti3.value,
            credentials.Credentials.cred_fatmulti4.value,
            credentials.Credentials.cred_fatmulti5.value,

            # 6-10
            credentials.Credentials.cred_fitsheep.value,
            credentials.Credentials.cred_fatmulti6.value,
            credentials.Credentials.cred_fatmulti8.value,
            credentials.Credentials.cred_fatmulti9.value,

            # credentials.Credentials.cred_fatmulti10.value,
            credentials.Credentials.cred_makun7551.value,
            # credentials.Credentials.cred_monkey130.value,
            # credentials.Credentials.cred_freiliheng.value,

            # 11-14
            credentials.Credentials.cred_fatmulti11.value,
            credentials.Credentials.cred_fatmulti12.value,
            credentials.Credentials.cred_fatmulti13.value,
            credentials.Credentials.cred_fatmulti14.value,

            # credentials.Credentials.cred_fatmulti15.value,
            # credentials.Credentials.cred_fatmulti16.value,
            # credentials.Credentials.cred_fatmulti17.value,
            # credentials.Credentials.cred_fatmulti18.value,

            # 15-18
            credentials.Credentials.cred_fatmulti19.value,
            credentials.Credentials.cred_fatmulti20.value,
            credentials.Credentials.cred_fatmulti21.value,
            credentials.Credentials.cred_fatmulti22.value,

            # 19-22
            credentials.Credentials.cred_fatmulti23.value,
            credentials.Credentials.cred_fatmulti24.value,
            credentials.Credentials.cred_fatmulti25.value,
            credentials.Credentials.cred_fatmulti26.value,

            # 23,24,25
            credentials.Credentials.cred_fatmulti27.value,
            credentials.Credentials.cred_fatmulti28.value,
            credentials.Credentials.cred_fatmulti29.value,
        ]

    def use_credential_list_luxiaofeng(self):
        self.use_credential_list_default()
        self.credential_list[9] = credentials.Credentials.cred_fatmulti10.value

    def use_credential_list_flydps(self):
        self.use_credential_list_default()
        self.credential_list[9] = credentials.Credentials.cred_monkey130.value

    def use_credential_list_stophealing(self):
        self.use_credential_list_default()
        self.credential_list[9] = credentials.Credentials.cred_freiliheng.value

    def use_credential_list_litgugu_efgh(self):
        self.use_credential_list_default()
        self.credential_list[10] = credentials.Credentials.cred_fatmulti15.value
        self.credential_list[11] = credentials.Credentials.cred_fatmulti16.value
        self.credential_list[12] = credentials.Credentials.cred_fatmulti17.value
        self.credential_list[13] = credentials.Credentials.cred_fatmulti18.value

    def use_credential_list_luxiaofeng_litgugu_efgh(self):
        self.use_credential_list_default()
        self.credential_list[9] = credentials.Credentials.cred_fatmulti10.value
        self.credential_list[10] = credentials.Credentials.cred_fatmulti15.value
        self.credential_list[11] = credentials.Credentials.cred_fatmulti16.value
        self.credential_list[12] = credentials.Credentials.cred_fatmulti17.value
        self.credential_list[13] = credentials.Credentials.cred_fatmulti18.value

    def use_credential_list_flydps_litgugu_efgh(self):
        self.use_credential_list_default()
        self.credential_list[9] = credentials.Credentials.cred_monkey130.value
        self.credential_list[10] = credentials.Credentials.cred_fatmulti15.value
        self.credential_list[11] = credentials.Credentials.cred_fatmulti16.value
        self.credential_list[12] = credentials.Credentials.cred_fatmulti17.value
        self.credential_list[13] = credentials.Credentials.cred_fatmulti18.value

    _credential_index = None # type:

    @property
    def credential_index(self) -> typing.Dict[int, credentials.Credential]:
        """
        为账号密码创建一个数字引用, 例如 1 就对应 fatmulti1.
        这样开发者就可以很容易地使用形如 credential_index[1].username 这样的 API 来访问数据.
        而无需使用 credentials.Credentials.cred_fatmulti1.username 这样的 API.
        """
        if self._credential_index is None:
            self._credential_index = {
                ind + 1: cred
                for ind, cred in enumerate(self.credential_list)
            }
        return self._credential_index

    def validate(self):
        pass
