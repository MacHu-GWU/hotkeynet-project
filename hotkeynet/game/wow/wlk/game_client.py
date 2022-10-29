# -*- coding: utf-8 -*-

"""
该模块定义了对游戏客户端的抽象.
"""

import typing as T
import attr
from attrs_mate import AttrsClass

from hotkeynet.game.wow.wlk import coordinator


class LocaleEnum:
    enUS = "enUS"
    zhCN = "zhCN"
    zhTW = "zhTW"


@attr.s
class GameClient(AttrsClass):
    """
    定义了你所使用的游戏客户端的详细信息.

    :param wow_exe_path: 你的游戏客户端路径
    :param locale: 游戏客户端的语言

    下面四个坐标是从整个桌面的视角看的绝对坐标, 以下坐标的单位都为 pixel, 像素:

    :param window_left_top_x: 游戏窗口左上角的 x 坐标
    :param window_left_top_y: 游戏窗口左上角的 y 坐标
    :param window_width: 游戏窗口的宽度
    :param window_height: 游戏窗口的高度

    下面的坐标都是从游戏客户端内看的相对坐标:

    :param wrong_password_pop_up_x: 输入错误的账号密码后的对话框的确认按钮的 x 坐标
    :param wrong_password_pop_up_y: 输入错误的账号密码后的对话框的确认按钮的 y 坐标
    :param username_input_box_x: 输入账号的文本框的 x 坐标
    :param username_input_box_y: 输入账号的文本框的 y 坐标
    :param log_out_button_x: 游戏内按 ESC 打开系统菜单后, 登出按钮 的 x 坐标
    :param log_out_button_y: 游戏内按 ESC 打开系统菜单后, 登出按钮 的 y 坐标
    :param exit_game_button_x: 游戏内按 ESC 打开系统菜单后, 退出游戏 的 x 坐标
    :param exit_game_button_y: 游戏内按 ESC 打开系统菜单后, 退出游戏 的 y 坐标
    :param return_to_game_button_x: 游戏内按 ESC 打开系统菜单后, 返回游戏 的 x 坐标
    :param return_to_game_button_y: 游戏内按 ESC 打开系统菜单后, 返回游戏 的 x 坐标
    :param pass_item_button_x: 游戏内按 roll 装备的弹出框的取消按钮的 x 坐标
    :param pass_item_button_1_y: 游戏内按 roll 装备的 1 号弹出框的取消按钮的 y 坐标
    :param pass_item_button_2_y: 游戏内按 roll 装备的 2 号弹出框的取消按钮的 y 坐标
    :param pass_item_button_3_y: 游戏内按 roll 装备的 3 号弹出框的取消按钮的 y 坐标
    :param pass_item_button_4_y: 游戏内按 roll 装备的 4 号弹出框的取消按钮的 y 坐标
    :param rdf_confirm_role_accept_button_x: RDF 排本时选择自己的角色的确认按钮的 x 坐标
    :param rdf_confirm_role_accept_button_y: RDF 排本时选择自己的角色的确认按钮的 y 坐标
    :param rdf_enter_dungeon_button_x: RDF 确认进入副本按钮的 x 坐标
    :param rdf_enter_dungeon_button_y: RDF 确认进入副本按钮的 y 坐标
    :param choose_char_N_x: 在人物选择界面选中第 N 个人物的 x 坐标
    :param choose_char_N_y: 在人物选择界面选中第 N 个人物的 y 坐标
    """
    wow_exe_path: str = attr.ib(default=None)
    locale: str = attr.ib(default=None)

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
    exit_game_button_x: int = attr.ib(default=None)
    exit_game_button_y: int = attr.ib(default=None)
    return_to_game_button_x: int = attr.ib(default=None)
    return_to_game_button_y: int = attr.ib(default=None)
    pass_item_button_x: int = attr.ib(default=None)
    pass_item_button_1_y: int = attr.ib(default=None)
    pass_item_button_2_y: int = attr.ib(default=None)
    pass_item_button_3_y: int = attr.ib(default=None)
    pass_item_button_4_y: int = attr.ib(default=None)
    rdf_confirm_role_accept_button_x: int = attr.ib(default=None)
    rdf_confirm_role_accept_button_y: int = attr.ib(default=None)
    rdf_enter_dungeon_button_x: int = attr.ib(default=None)
    rdf_enter_dungeon_button_y: int = attr.ib(default=None)

    choose_char_1_x = attr.ib(default=None)
    choose_char_1_y = attr.ib(default=None)
    choose_char_2_x = attr.ib(default=None)
    choose_char_2_y = attr.ib(default=None)
    choose_char_3_x = attr.ib(default=None)
    choose_char_3_y = attr.ib(default=None)
    choose_char_4_x = attr.ib(default=None)
    choose_char_4_y = attr.ib(default=None)
    choose_char_5_x = attr.ib(default=None)
    choose_char_5_y = attr.ib(default=None)
    choose_char_6_x = attr.ib(default=None)
    choose_char_6_y = attr.ib(default=None)
    choose_char_7_x = attr.ib(default=None)
    choose_char_7_y = attr.ib(default=None)
    choose_char_8_x = attr.ib(default=None)
    choose_char_8_y = attr.ib(default=None)
    choose_char_9_x = attr.ib(default=None)
    choose_char_9_y = attr.ib(default=None)

    def get_choose_char_x_y(self, nth: int) -> T.Tuple:
        return (
            getattr(self, f"choose_char_{nth}_x"),
            getattr(self, f"choose_char_{nth}_y"),
        )