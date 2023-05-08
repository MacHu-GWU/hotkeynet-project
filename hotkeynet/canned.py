# -*- coding: utf-8 -*-

"""
Similar to :mod:`hotkeynet.keyname`. However, everything in this module is
:mod:`hotkeynet.maker` factory object. Everything in this module should be called
to use.

Example:

    >>> from hotkeynet import canned
    >>> canned.KEY_1()
    >>> canned.CTRL_(canned.KEY_1)()
"""

import typing as _T
from . import keyname as _KN
from .maker import (
    KeyMaker as _KeyMaker,
    ClickMaker as _ClickMaker,
    ModifiedClickMaker as _ModifiedClickMaker,
)

ESC = _KeyMaker(_KN.ESC)
TRIGGER = _KeyMaker(_KN.TRIGGER)

# ------------------------------------------------------------------------------
# F1 - F12
# ------------------------------------------------------------------------------
F1 = _KeyMaker(_KN.F1)
F2 = _KeyMaker(_KN.F2)
F3 = _KeyMaker(_KN.F3)
F4 = _KeyMaker(_KN.F4)
F5 = _KeyMaker(_KN.F5)
F6 = _KeyMaker(_KN.F6)
F7 = _KeyMaker(_KN.F7)
F8 = _KeyMaker(_KN.F8)
F9 = _KeyMaker(_KN.F9)
F10 = _KeyMaker(_KN.F10)
F11 = _KeyMaker(_KN.F11)
F12 = _KeyMaker(_KN.F12)

# ------------------------------------------------------------------------------
# Main number keys
# ------------------------------------------------------------------------------
OEM3_WAVE_OR_BACK_QUOTE = _KeyMaker(_KN.OEM3_WAVE_OR_BACK_QUOTE)  # ~
KEY_1 = _KeyMaker(_KN.KEY_1)
KEY_2 = _KeyMaker(_KN.KEY_2)
KEY_3 = _KeyMaker(_KN.KEY_3)
KEY_4 = _KeyMaker(_KN.KEY_4)
KEY_5 = _KeyMaker(_KN.KEY_5)
KEY_6 = _KeyMaker(_KN.KEY_6)
KEY_7 = _KeyMaker(_KN.KEY_7)
KEY_8 = _KeyMaker(_KN.KEY_8)
KEY_9 = _KeyMaker(_KN.KEY_9)
KEY_0 = _KeyMaker(_KN.KEY_0)
KEY_11_MINUS = _KeyMaker(_KN.KEY_11_MINUS)
KEY_12_PLUS = _KeyMaker(_KN.KEY_12_PLUS)
BACKSPACE = _KeyMaker(_KN.BACKSPACE)

# ------------------------------------------------------------------------------
# Modifier keys
# ------------------------------------------------------------------------------
TAB = _KeyMaker(_KN.TAB)
CAPS_LOCK = _KeyMaker(_KN.CAPS_LOCK)
SHIFT = _KeyMaker(_KN.SHIFT)
CTRL = _KeyMaker(_KN.CTRL)
ALT = _KeyMaker(_KN.ALT)

LSHIFT = _KeyMaker(_KN.LSHIFT)
RSHIFT = _KeyMaker(_KN.RSHIFT)
LCTRL = _KeyMaker(_KN.LCTRL)
RCTRL = _KeyMaker(_KN.RCTRL)
LALT = _KeyMaker(_KN.LALT)
RALT = _KeyMaker(_KN.RALT)

SPACE = _KeyMaker(_KN.SPACE)

LWIN = _KeyMaker(_KN.LWIN)
RWIN = _KeyMaker(_KN.RWIN)

# ------------------------------------------------------------------------------
# Alphabet keys
# ------------------------------------------------------------------------------
A = _KeyMaker(_KN.A)
B = _KeyMaker(_KN.B)
C = _KeyMaker(_KN.C)
D = _KeyMaker(_KN.D)
E = _KeyMaker(_KN.E)
F = _KeyMaker(_KN.F)
G = _KeyMaker(_KN.G)
H = _KeyMaker(_KN.H)
I = _KeyMaker(_KN.I)
J = _KeyMaker(_KN.J)
K = _KeyMaker(_KN.K)
L = _KeyMaker(_KN.L)
M = _KeyMaker(_KN.M)
N = _KeyMaker(_KN.N)
O = _KeyMaker(_KN.O)
P = _KeyMaker(_KN.P)
Q = _KeyMaker(_KN.Q)
R = _KeyMaker(_KN.R)
S = _KeyMaker(_KN.S)
T = _KeyMaker(_KN.T)
U = _KeyMaker(_KN.U)
V = _KeyMaker(_KN.V)
W = _KeyMaker(_KN.W)
X = _KeyMaker(_KN.X)
Y = _KeyMaker(_KN.Y)
Z = _KeyMaker(_KN.Z)

# ------------------------------------------------------------------------------
# Special characters
# ------------------------------------------------------------------------------
OEM4_SQUARE_BRACKET_LEFT = _KeyMaker(_KN.OEM4_SQUARE_BRACKET_LEFT)  # (
OEM6_SQUARE_BRACKET_RIGHT = _KeyMaker(_KN.OEM6_SQUARE_BRACKET_RIGHT)  # )
OEM5_PIPE_OR_BACK_SLASH = _KeyMaker(_KN.OEM5_PIPE_OR_BACK_SLASH)  # /
OEM1_SEMICOLUMN = _KeyMaker(_KN.OEM1_SEMICOLUMN)  # :
OEM7_QUOTE = _KeyMaker(_KN.OEM7_QUOTE)  # "
COMMA = _KeyMaker(_KN.COMMA)  # ,
PERIOD = _KeyMaker(_KN.PERIOD)  # .
OEM2_QUESTION = _KeyMaker(_KN.OEM2_QUESTION)  # ? Key
ENTER = _KeyMaker(_KN.ENTER)

# ------------------------------------------------------------------------------
# Arrow keys
# ------------------------------------------------------------------------------
INSERT = _KeyMaker(_KN.INSERT)
HOME = _KeyMaker(_KN.HOME)
PAGE_UP = _KeyMaker(_KN.PAGE_UP)
DELETE = _KeyMaker(_KN.DELETE)
END = _KeyMaker(_KN.END)
PAGE_DOWN = _KeyMaker(_KN.PAGE_DOWN)
LEFT = _KeyMaker(_KN.LEFT)
UP = _KeyMaker(_KN.UP)
RIGHT = _KeyMaker(_KN.RIGHT)
DOWN = _KeyMaker(_KN.DOWN)

# ------------------------------------------------------------------------------
# Numpad keys
# ------------------------------------------------------------------------------
SCROLL_LOCK = _KeyMaker(_KN.SCROLL_LOCK)

NUMPAD_1 = _KeyMaker(_KN.NUMPAD_1)
NUMPAD_2 = _KeyMaker(_KN.NUMPAD_2)
NUMPAD_3 = _KeyMaker(_KN.NUMPAD_3)
NUMPAD_4 = _KeyMaker(_KN.NUMPAD_4)
NUMPAD_5 = _KeyMaker(_KN.NUMPAD_5)
NUMPAD_6 = _KeyMaker(_KN.NUMPAD_6)
NUMPAD_7 = _KeyMaker(_KN.NUMPAD_7)
NUMPAD_8 = _KeyMaker(_KN.NUMPAD_8)
NUMPAD_9 = _KeyMaker(_KN.NUMPAD_9)
NUMPAD_0 = _KeyMaker(_KN.NUMPAD_0)
NUMPAD_11_DIVIDE = _KeyMaker(_KN.NUMPAD_11_DIVIDE)
NUMPAD_12_MULTIPLY = _KeyMaker(_KN.NUMPAD_12_MULTIPLY)

NUMPAD_MINUS = _KeyMaker(_KN.NUMPAD_MINUS)
NUMPAD_PLUS = _KeyMaker(_KN.NUMPAD_PLUS)
NUMPAD_ENTER = _KeyMaker(_KN.NUMPAD_ENTER)
NUMPAD_DELETE = _KeyMaker(_KN.NUMPAD_DELETE)

NUMPAD_SHIFT_1_END = _KeyMaker(_KN.NUMPAD_SHIFT_1_END)
NUMPAD_SHIFT_2_DOWN = _KeyMaker(_KN.NUMPAD_SHIFT_2_DOWN)
NUMPAD_SHIFT_3_PAGE_DOWN = _KeyMaker(_KN.NUMPAD_SHIFT_3_PAGE_DOWN)
NUMPAD_SHIFT_4_LEFT = _KeyMaker(_KN.NUMPAD_SHIFT_4_LEFT)
NUMPAD_SHIFT_5_CLEAR = _KeyMaker(_KN.NUMPAD_SHIFT_5_CLEAR)
NUMPAD_SHIFT_6_RIGHT = _KeyMaker(_KN.NUMPAD_SHIFT_6_RIGHT)
NUMPAD_SHIFT_7_HOME = _KeyMaker(_KN.NUMPAD_SHIFT_7_HOME)
NUMPAD_SHIFT_8_UP = _KeyMaker(_KN.NUMPAD_SHIFT_8_UP)
NUMPAD_SHIFT_9_PAGE_UP = _KeyMaker(_KN.NUMPAD_SHIFT_9_PAGE_UP)

UNKNOWN = _KeyMaker(_KN.UNKNOWN)

# ------------------------------------------------------------------------------
# Mouse buttons
# ------------------------------------------------------------------------------
MOUSE_LButton = _ClickMaker(_KN.MOUSE_LButton)
MOUSE_RButton = _ClickMaker(_KN.MOUSE_RButton)
MOUSE_MButton = _ClickMaker(_KN.MOUSE_MButton)
MOUSE_Button4 = _ClickMaker(_KN.MOUSE_Button4)
MOUSE_Button5 = _ClickMaker(_KN.MOUSE_Button5)

SHIFT_LEFT_CLICK = _ModifiedClickMaker(_KN.MOUSE_LButton, _KN.SHIFT)
SHIFT_RIGHT_CLICK = _ModifiedClickMaker(_KN.MOUSE_RButton, _KN.SHIFT)
SHIFT_MIDDLE_CLICK = _ModifiedClickMaker(_KN.MOUSE_MButton, _KN.SHIFT)
ALT_LEFT_CLICK = _ModifiedClickMaker(_KN.MOUSE_LButton, _KN.ALT)
ALT_RIGHT_CLICK = _ModifiedClickMaker(_KN.MOUSE_RButton, _KN.ALT)
ALT_MIDDLE_CLICK = _ModifiedClickMaker(_KN.MOUSE_MButton, _KN.ALT)
CTRL_LEFT_CLICK = _ModifiedClickMaker(_KN.MOUSE_LButton, _KN.CTRL)
CTRL_RIGHT_CLICK = _ModifiedClickMaker(_KN.MOUSE_RButton, _KN.CTRL)
CTRL_MIDDLE_CLICK = _ModifiedClickMaker(_KN.MOUSE_MButton, _KN.CTRL)

# ------------------------------------------------------------------------------
# Key collections
# ------------------------------------------------------------------------------
F1_to_F12 = [
    F1,
    F2,
    F3,
    F4,
    F5,
    F6,
    F7,
    F8,
    F9,
    F10,
    F11,
    F12,
]

INSERT_TO_PGDN = [
    INSERT,
    HOME,
    PAGE_UP,
    DELETE,
    END,
    PAGE_DOWN,
]

KEY_1_to_12 = [
    KEY_1,
    KEY_2,
    KEY_3,
    KEY_4,
    KEY_5,
    KEY_6,
    KEY_7,
    KEY_8,
    KEY_9,
    KEY_0,
    KEY_11_MINUS,
    KEY_12_PLUS,
]

NUMPAD_1_to_12 = [
    NUMPAD_1,
    NUMPAD_2,
    NUMPAD_3,
    NUMPAD_4,
    NUMPAD_5,
    NUMPAD_6,
    NUMPAD_7,
    NUMPAD_8,
    NUMPAD_9,
    NUMPAD_0,
    NUMPAD_11_DIVIDE,
    NUMPAD_12_MULTIPLY,
]


# ------------------------------------------------------------------------------
# One modifier compound keys
# ------------------------------------------------------------------------------
def _resolve_key_liked_arg(key: _T.Union[str, _KeyMaker]) -> str:
    if isinstance(key, _KeyMaker):
        return key.key
    elif isinstance(key, str):
        return key
    else:  # pragma: no cover
        raise TypeError("key must be a str or a KeyMaker instance")


def _key_with_modifier(mod: str, *keys: _T.Union[str, _KeyMaker]) -> _KeyMaker:
    return _KeyMaker(
        "{} {}".format(mod, ", ".join([_resolve_key_liked_arg(k) for k in keys]))
    )


def CTRL_(*keys: _T.Union[str, _KeyMaker]) -> _KeyMaker:
    return _key_with_modifier(_KN.CTRL, *keys)


def SHIFT_(*keys: _T.Union[str, _KeyMaker]) -> _KeyMaker:  # pragma: no cover
    return _key_with_modifier(_KN.SHIFT, *keys)


def ALT_(*keys: _T.Union[str, _KeyMaker]) -> _KeyMaker:  # pragma: no cover
    return _key_with_modifier(_KN.ALT, *keys)


# ------------------------------------------------------------------------------
# Two modifier compound keys
# ------------------------------------------------------------------------------
def CTRL_ALT_(*keys: _T.Union[str, _KeyMaker]) -> _KeyMaker:
    return _key_with_modifier(f"{_KN.CTRL} {_KN.ALT}", *keys)


def CTRL_SHIFT_(*keys: _T.Union[str, _KeyMaker]) -> _KeyMaker:  # pragma: no cover
    return _key_with_modifier(f"{_KN.CTRL} {_KN.SHIFT}", *keys)


def ALT_SHIFT_(*keys: _T.Union[str, _KeyMaker]) -> _KeyMaker:  # pragma: no cover
    return _key_with_modifier(f"{_KN.ALT} {_KN.SHIFT}", *keys)


# ------------------------------------------------------------------------------
# Three modifier compound keys
# ------------------------------------------------------------------------------
def CTRL_SHIFT_ALT(*keys: _T.Union[str, _KeyMaker]) -> _KeyMaker:
    return _key_with_modifier(f"{_KN.CTRL} {_KN.SHIFT} {_KN.ALT}", *keys)


# ------------------------------------------------------------------------------
# Special modifier compound keys
# ------------------------------------------------------------------------------
def LWIN_(*keys: _T.Union[str, _KeyMaker]) -> _KeyMaker:
    """
    Left windows + any key
    """
    return _key_with_modifier(_KN.LWIN, *keys)


def RWIN_(*keys: _T.Union[str, _KeyMaker]) -> _KeyMaker:
    """
    Right windows + any key
    """
    return _key_with_modifier(_KN.RWIN, *keys)
