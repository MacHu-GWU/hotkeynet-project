# -*- coding: utf-8 -*-

"""
[EN]

Enumerate all mouse and keyboard keys for reference in other places, to avoid
hard coding string in the code.

Virtual key table: https://www.cnblogs.com/del/archive/2007/12/07/987364.html
Key Names table: http://www.hotkeynet.com/ref/keynames.html

[CN]
对所有的 鼠标, 键盘 按键的枚举. 以供在其他地方引用, 避免由于手动输入字符串所引发的错误.

- 虚拟按键表: https://www.cnblogs.com/del/archive/2007/12/07/987364.html
- Key Names表: http://www.hotkeynet.com/ref/keynames.html
"""


ESC = "Esc"
TRIGGER = "%Trigger%"

# ------------------------------------------------------------------------------
# F1 - F12
# ------------------------------------------------------------------------------
F1 = "F1"
F2 = "F2"
F3 = "F3"
F4 = "F4"
F5 = "F5"
F6 = "F6"
F7 = "F7"
F8 = "F8"
F9 = "F9"
F10 = "F10"
F11 = "F11"
F12 = "F12"

# ------------------------------------------------------------------------------
# Main number keys
# ------------------------------------------------------------------------------
OEM3_WAVE_OR_BACK_QUOTE = "Oem3"  # ~
KEY_1 = "1"
KEY_2 = "2"
KEY_3 = "3"
KEY_4 = "4"
KEY_5 = "5"
KEY_6 = "6"
KEY_7 = "7"
KEY_8 = "8"
KEY_9 = "9"
KEY_0 = "0"
KEY_11_MINUS = "Minus"
KEY_12_PLUS = "Plus"
BACKSPACE = "Backspace"

# ------------------------------------------------------------------------------
# Modifier keys
# ------------------------------------------------------------------------------
TAB = "Tab"
CAPS_LOCK = "CapsLock"
SHIFT = "Shift"
CTRL = "Ctrl"
ALT = "Alt"

LSHIFT = "LShift"
RSHIFT = "RShift"
LCTRL = "LCtrl"
RCTRL = "RCtrl"
LALT = "LAlt"
RALT = "RAlt"

SPACE = "Space"

LWIN = "LWin"
RWIN = "RWin"

# ------------------------------------------------------------------------------
# Alphabet keys
# ------------------------------------------------------------------------------
A = "A"
B = "B"
C = "C"
D = "D"
E = "E"
F = "F"
G = "G"
H = "H"
I = "I"
J = "J"
K = "K"
L = "L"
M = "M"
N = "N"
O = "O"
P = "P"
Q = "Q"
R = "R"
S = "S"
T = "T"
U = "U"
V = "V"
W = "W"
X = "X"
Y = "Y"
Z = "Z"

# ------------------------------------------------------------------------------
# Special characters
# ------------------------------------------------------------------------------
OEM4_SQUARE_BRACKET_LEFT = "Oem4"  # (
OEM6_SQUARE_BRACKET_RIGHT = "Oem6"  # )
OEM5_PIPE_OR_BACK_SLASH = "Oem5"  # /
OEM1_SEMICOLUMN = "Oem1"  # :
OEM7_QUOTE = "Oem7"  # "
COMMA = "Comma"  # ,
PERIOD = "Period"  # .
OEM2_QUESTION = "Oem2"  # ? Key
ENTER = "Enter"

# ------------------------------------------------------------------------------
# Arrow keys
# ------------------------------------------------------------------------------
INSERT = "Insert"
HOME = "Home"
PAGE_UP = "PgUp"
DELETE = "Delete"
END = "End"
PAGE_DOWN = "PgDn"

LEFT = "Left"
UP = "Up"
RIGHT = "Right"
DOWN = "Down"

# ------------------------------------------------------------------------------
# Numpad keys
# ------------------------------------------------------------------------------
SCROLL_LOCK = "ScrollLock"

NUMPAD_1 = "Numpad1"
NUMPAD_2 = "Numpad2"
NUMPAD_3 = "Numpad3"
NUMPAD_4 = "Numpad4"
NUMPAD_5 = "Numpad5"
NUMPAD_6 = "Numpad6"
NUMPAD_7 = "Numpad7"
NUMPAD_8 = "Numpad8"
NUMPAD_9 = "Numpad9"
NUMPAD_0 = "Numpad0"
NUMPAD_11_DIVIDE = "Divide"
NUMPAD_12_MULTIPLY = "Multiply"

NUMPAD_MINUS = "NumpadMinus"
NUMPAD_PLUS = "NumpadPlus"
NUMPAD_ENTER = "NumpadEnter"
NUMPAD_DELETE = "NumpadDelete"

NUMPAD_SHIFT_1_END = "NumpadEnd"
NUMPAD_SHIFT_2_DOWN = "NumpadDown"
NUMPAD_SHIFT_3_PAGE_DOWN = "NumpadPgDn"
NUMPAD_SHIFT_4_LEFT = "NumpadLeft"
NUMPAD_SHIFT_5_CLEAR = "Clear"
NUMPAD_SHIFT_6_RIGHT = "NumpadRight"
NUMPAD_SHIFT_7_HOME = "NumpadHome"
NUMPAD_SHIFT_8_UP = "NumpadUp"
NUMPAD_SHIFT_9_PAGE_UP = "NumpadPgUp"

UNKNOWN = "Unknown"

# ------------------------------------------------------------------------------
# Mouse buttons
# ------------------------------------------------------------------------------
MOUSE_LButton = "LButton"
MOUSE_RButton = "RButton"
MOUSE_MButton = "MButton"
MOUSE_Button4 = "Button4"
MOUSE_Button5 = "Button5"

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
def CTRL_(*keys: str) -> str:
    return "{} {}".format(CTRL, ", ".join(keys))


def SHIFT_(*keys: str) -> str:
    return "{} {}".format(SHIFT, ", ".join(keys))


def ALT_(*keys: str) -> str:
    return "{} {}".format(ALT, ", ".join(keys))


# ------------------------------------------------------------------------------
# Two modifier compound keys
# ------------------------------------------------------------------------------
def CTRL_ALT_(*keys: str) -> str:
    return "{} {} {}".format(CTRL, ALT, ", ".join(keys))


def CTRL_SHIFT_(*keys: str) -> str:
    return "{} {} {}".format(CTRL, SHIFT, ", ".join(keys))


def ALT_SHIFT_(*keys: str) -> str:
    return "{} {} {}".format(ALT, SHIFT, ", ".join(keys))


# ------------------------------------------------------------------------------
# Three modifier compound keys
# ------------------------------------------------------------------------------
def CTRL_SHIFT_ALT(*keys: str) -> str:
    return "{} {} {} {}".format(CTRL, SHIFT, ALT, ", ".join(keys))


# ------------------------------------------------------------------------------
# Special modifier compound keys
# ------------------------------------------------------------------------------
def SCROLOCK_ON(key: str) -> str:
    return "{}On {}".format(SCROLL_LOCK, key)


def CAPSLOCK_ON(key: str) -> str:
    return "{}On {}".format(CAPS_LOCK, key)


def LWIN_(*keys: str) -> str:
    """
    Left windows + any key
    """
    return "{} {}".format(LWIN, ", ".join(keys))


def RWIN_(*keys: str) -> str:
    """
    Right windows + any key
    """
    return "{} {}".format(RWIN, ", ".join(keys))
