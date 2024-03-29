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


# ------------------------------------------------------------------------------
# regular key with modifier
# ------------------------------------------------------------------------------
# CTRL
CTRL_TAB = CTRL_(TAB)

CTRL_F1 = CTRL_(F1)
CTRL_F2 = CTRL_(F2)
CTRL_F3 = CTRL_(F3)
CTRL_F4 = CTRL_(F4)
CTRL_F5 = CTRL_(F5)
CTRL_F6 = CTRL_(F6)
CTRL_F7 = CTRL_(F7)
CTRL_F8 = CTRL_(F8)
CTRL_F9 = CTRL_(F9)
CTRL_F10 = CTRL_(F10)
CTRL_F11 = CTRL_(F11)
CTRL_F12 = CTRL_(F12)

CTRL_OEM3_WAVE_OR_BACK_QUOTE = CTRL_(OEM3_WAVE_OR_BACK_QUOTE)
CTRL_1 = CTRL_(KEY_1)
CTRL_2 = CTRL_(KEY_2)
CTRL_3 = CTRL_(KEY_3)
CTRL_4 = CTRL_(KEY_4)
CTRL_5 = CTRL_(KEY_5)
CTRL_6 = CTRL_(KEY_6)
CTRL_7 = CTRL_(KEY_7)
CTRL_8 = CTRL_(KEY_8)
CTRL_9 = CTRL_(KEY_9)
CTRL_0 = CTRL_(KEY_0)
CTRL_11_MINUS = CTRL_(KEY_11_MINUS)
CTRL_12_PLUS = CTRL_(KEY_12_PLUS)
CTRL_BACKSPACE = CTRL_(BACKSPACE)

CTRL_NUMPAD_1 = CTRL_(NUMPAD_1)
CTRL_NUMPAD_2 = CTRL_(NUMPAD_2)
CTRL_NUMPAD_3 = CTRL_(NUMPAD_3)
CTRL_NUMPAD_4 = CTRL_(NUMPAD_4)
CTRL_NUMPAD_5 = CTRL_(NUMPAD_5)
CTRL_NUMPAD_6 = CTRL_(NUMPAD_6)
CTRL_NUMPAD_7 = CTRL_(NUMPAD_7)
CTRL_NUMPAD_8 = CTRL_(NUMPAD_8)
CTRL_NUMPAD_9 = CTRL_(NUMPAD_9)
CTRL_NUMPAD_0 = CTRL_(NUMPAD_0)
CTRL_NUMPAD_11_DIVIDE = CTRL_(NUMPAD_11_DIVIDE)
CTRL_NUMPAD_12_MULTIPLY = CTRL_(NUMPAD_12_MULTIPLY)

CTRL_A = CTRL_(A)
CTRL_B = CTRL_(B)
CTRL_C = CTRL_(C)
CTRL_D = CTRL_(D)
CTRL_E = CTRL_(E)
CTRL_F = CTRL_(F)
CTRL_G = CTRL_(G)
CTRL_H = CTRL_(H)
CTRL_I = CTRL_(I)
CTRL_J = CTRL_(J)
CTRL_K = CTRL_(K)
CTRL_L = CTRL_(L)
CTRL_M = CTRL_(M)
CTRL_N = CTRL_(N)
CTRL_O = CTRL_(O)
CTRL_P = CTRL_(P)
CTRL_Q = CTRL_(Q)
CTRL_R = CTRL_(R)
CTRL_S = CTRL_(S)
CTRL_T = CTRL_(T)
CTRL_U = CTRL_(U)
CTRL_V = CTRL_(V)
CTRL_W = CTRL_(W)
CTRL_X = CTRL_(X)
CTRL_Y = CTRL_(Y)
CTRL_Z = CTRL_(Z)

# SHIFT
SHIFT_TAB = SHIFT_(TAB)

SHIFT_F1 = SHIFT_(F1)
SHIFT_F2 = SHIFT_(F2)
SHIFT_F3 = SHIFT_(F3)
SHIFT_F4 = SHIFT_(F4)
SHIFT_F5 = SHIFT_(F5)
SHIFT_F6 = SHIFT_(F6)
SHIFT_F7 = SHIFT_(F7)
SHIFT_F8 = SHIFT_(F8)
SHIFT_F9 = SHIFT_(F9)
SHIFT_F10 = SHIFT_(F10)
SHIFT_F11 = SHIFT_(F11)
SHIFT_F12 = SHIFT_(F12)

SHIFT_OEM3_WAVE_OR_BACK_QUOTE = SHIFT_(OEM3_WAVE_OR_BACK_QUOTE)
SHIFT_1 = SHIFT_(KEY_1)
SHIFT_2 = SHIFT_(KEY_2)
SHIFT_3 = SHIFT_(KEY_3)
SHIFT_4 = SHIFT_(KEY_4)
SHIFT_5 = SHIFT_(KEY_5)
SHIFT_6 = SHIFT_(KEY_6)
SHIFT_7 = SHIFT_(KEY_7)
SHIFT_8 = SHIFT_(KEY_8)
SHIFT_9 = SHIFT_(KEY_9)
SHIFT_0 = SHIFT_(KEY_0)
SHIFT_11_MINUS = SHIFT_(KEY_11_MINUS)
SHIFT_12_PLUS = SHIFT_(KEY_12_PLUS)
SHIFT_BACKSPACE = SHIFT_(BACKSPACE)

SHIFT_NUMPAD_1 = SHIFT_(NUMPAD_1)
SHIFT_NUMPAD_2 = SHIFT_(NUMPAD_2)
SHIFT_NUMPAD_3 = SHIFT_(NUMPAD_3)
SHIFT_NUMPAD_4 = SHIFT_(NUMPAD_4)
SHIFT_NUMPAD_5 = SHIFT_(NUMPAD_5)
SHIFT_NUMPAD_6 = SHIFT_(NUMPAD_6)
SHIFT_NUMPAD_7 = SHIFT_(NUMPAD_7)
SHIFT_NUMPAD_8 = SHIFT_(NUMPAD_8)
SHIFT_NUMPAD_9 = SHIFT_(NUMPAD_9)
SHIFT_NUMPAD_0 = SHIFT_(NUMPAD_0)
SHIFT_NUMPAD_11_DIVIDE = SHIFT_(NUMPAD_11_DIVIDE)
SHIFT_NUMPAD_12_MULTIPLY = SHIFT_(NUMPAD_12_MULTIPLY)

SHIFT_A = SHIFT_(A)
SHIFT_B = SHIFT_(B)
SHIFT_C = SHIFT_(C)
SHIFT_D = SHIFT_(D)
SHIFT_E = SHIFT_(E)
SHIFT_F = SHIFT_(F)
SHIFT_G = SHIFT_(G)
SHIFT_H = SHIFT_(H)
SHIFT_I = SHIFT_(I)
SHIFT_J = SHIFT_(J)
SHIFT_K = SHIFT_(K)
SHIFT_L = SHIFT_(L)
SHIFT_M = SHIFT_(M)
SHIFT_N = SHIFT_(N)
SHIFT_O = SHIFT_(O)
SHIFT_P = SHIFT_(P)
SHIFT_Q = SHIFT_(Q)
SHIFT_R = SHIFT_(R)
SHIFT_S = SHIFT_(S)
SHIFT_T = SHIFT_(T)
SHIFT_U = SHIFT_(U)
SHIFT_V = SHIFT_(V)
SHIFT_W = SHIFT_(W)
SHIFT_X = SHIFT_(X)
SHIFT_Y = SHIFT_(Y)
SHIFT_Z = SHIFT_(Z)

# ALT
ALT_TAB = ALT_(TAB)

ALT_F1 = ALT_(F1)
ALT_F2 = ALT_(F2)
ALT_F3 = ALT_(F3)
ALT_F4 = ALT_(F4)
ALT_F5 = ALT_(F5)
ALT_F6 = ALT_(F6)
ALT_F7 = ALT_(F7)
ALT_F8 = ALT_(F8)
ALT_F9 = ALT_(F9)
ALT_F10 = ALT_(F10)
ALT_F11 = ALT_(F11)
ALT_F12 = ALT_(F12)

ALT_OEM3_WAVE_OR_BACK_QUOTE = ALT_(OEM3_WAVE_OR_BACK_QUOTE)
ALT_1 = ALT_(KEY_1)
ALT_2 = ALT_(KEY_2)
ALT_3 = ALT_(KEY_3)
ALT_4 = ALT_(KEY_4)
ALT_5 = ALT_(KEY_5)
ALT_6 = ALT_(KEY_6)
ALT_7 = ALT_(KEY_7)
ALT_8 = ALT_(KEY_8)
ALT_9 = ALT_(KEY_9)
ALT_0 = ALT_(KEY_0)
ALT_11_MINUS = ALT_(KEY_11_MINUS)
ALT_12_PLUS = ALT_(KEY_12_PLUS)
ALT_BACKSPACE = ALT_(BACKSPACE)

ALT_NUMPAD_1 = ALT_(NUMPAD_1)
ALT_NUMPAD_2 = ALT_(NUMPAD_2)
ALT_NUMPAD_3 = ALT_(NUMPAD_3)
ALT_NUMPAD_4 = ALT_(NUMPAD_4)
ALT_NUMPAD_5 = ALT_(NUMPAD_5)
ALT_NUMPAD_6 = ALT_(NUMPAD_6)
ALT_NUMPAD_7 = ALT_(NUMPAD_7)
ALT_NUMPAD_8 = ALT_(NUMPAD_8)
ALT_NUMPAD_9 = ALT_(NUMPAD_9)
ALT_NUMPAD_0 = ALT_(NUMPAD_0)
ALT_NUMPAD_11_DIVIDE = ALT_(NUMPAD_11_DIVIDE)
ALT_NUMPAD_12_MULTIPLY = ALT_(NUMPAD_12_MULTIPLY)

ALT_A = ALT_(A)
ALT_B = ALT_(B)
ALT_C = ALT_(C)
ALT_D = ALT_(D)
ALT_E = ALT_(E)
ALT_F = ALT_(F)
ALT_G = ALT_(G)
ALT_H = ALT_(H)
ALT_I = ALT_(I)
ALT_J = ALT_(J)
ALT_K = ALT_(K)
ALT_L = ALT_(L)
ALT_M = ALT_(M)
ALT_N = ALT_(N)
ALT_O = ALT_(O)
ALT_P = ALT_(P)
ALT_Q = ALT_(Q)
ALT_R = ALT_(R)
ALT_S = ALT_(S)
ALT_T = ALT_(T)
ALT_U = ALT_(U)
ALT_V = ALT_(V)
ALT_W = ALT_(W)
ALT_X = ALT_(X)
ALT_Y = ALT_(Y)
ALT_Z = ALT_(Z)

# CTRL ALT
CTRL_ALT_F1 = CTRL_ALT_(F1)
CTRL_ALT_F2 = CTRL_ALT_(F2)
CTRL_ALT_F3 = CTRL_ALT_(F3)
CTRL_ALT_F4 = CTRL_ALT_(F4)
CTRL_ALT_F5 = CTRL_ALT_(F5)
CTRL_ALT_F6 = CTRL_ALT_(F6)
CTRL_ALT_F7 = CTRL_ALT_(F7)
CTRL_ALT_F8 = CTRL_ALT_(F8)
CTRL_ALT_F9 = CTRL_ALT_(F9)
CTRL_ALT_F10 = CTRL_ALT_(F10)
CTRL_ALT_F11 = CTRL_ALT_(F11)
CTRL_ALT_F12 = CTRL_ALT_(F12)

CTRL_ALT_OEM3_WAVE_OR_BACK_QUOTE = CTRL_ALT_(OEM3_WAVE_OR_BACK_QUOTE)
CTRL_ALT_1 = CTRL_ALT_(KEY_1)
CTRL_ALT_2 = CTRL_ALT_(KEY_2)
CTRL_ALT_3 = CTRL_ALT_(KEY_3)
CTRL_ALT_4 = CTRL_ALT_(KEY_4)
CTRL_ALT_5 = CTRL_ALT_(KEY_5)
CTRL_ALT_6 = CTRL_ALT_(KEY_6)
CTRL_ALT_7 = CTRL_ALT_(KEY_7)
CTRL_ALT_8 = CTRL_ALT_(KEY_8)
CTRL_ALT_9 = CTRL_ALT_(KEY_9)
CTRL_ALT_0 = CTRL_ALT_(KEY_0)
CTRL_ALT_11_MINUS = CTRL_ALT_(KEY_11_MINUS)
CTRL_ALT_12_PLUS = CTRL_ALT_(KEY_12_PLUS)
CTRL_ALT_BACKSPACE = CTRL_ALT_(BACKSPACE)

CTRL_ALT_NUMPAD_1 = CTRL_ALT_(NUMPAD_1)
CTRL_ALT_NUMPAD_2 = CTRL_ALT_(NUMPAD_2)
CTRL_ALT_NUMPAD_3 = CTRL_ALT_(NUMPAD_3)
CTRL_ALT_NUMPAD_4 = CTRL_ALT_(NUMPAD_4)
CTRL_ALT_NUMPAD_5 = CTRL_ALT_(NUMPAD_5)
CTRL_ALT_NUMPAD_6 = CTRL_ALT_(NUMPAD_6)
CTRL_ALT_NUMPAD_7 = CTRL_ALT_(NUMPAD_7)
CTRL_ALT_NUMPAD_8 = CTRL_ALT_(NUMPAD_8)
CTRL_ALT_NUMPAD_9 = CTRL_ALT_(NUMPAD_9)
CTRL_ALT_NUMPAD_0 = CTRL_ALT_(NUMPAD_0)
CTRL_ALT_NUMPAD_11_DIVIDE = CTRL_ALT_(NUMPAD_11_DIVIDE)
CTRL_ALT_NUMPAD_12_MULTIPLY = CTRL_ALT_(NUMPAD_12_MULTIPLY)

CTRL_ALT_A = CTRL_ALT_(A)
CTRL_ALT_B = CTRL_ALT_(B)
CTRL_ALT_C = CTRL_ALT_(C)
CTRL_ALT_D = CTRL_ALT_(D)
CTRL_ALT_E = CTRL_ALT_(E)
CTRL_ALT_F = CTRL_ALT_(F)
CTRL_ALT_G = CTRL_ALT_(G)
CTRL_ALT_H = CTRL_ALT_(H)
CTRL_ALT_I = CTRL_ALT_(I)
CTRL_ALT_J = CTRL_ALT_(J)
CTRL_ALT_K = CTRL_ALT_(K)
CTRL_ALT_L = CTRL_ALT_(L)
CTRL_ALT_M = CTRL_ALT_(M)
CTRL_ALT_N = CTRL_ALT_(N)
CTRL_ALT_O = CTRL_ALT_(O)
CTRL_ALT_P = CTRL_ALT_(P)
CTRL_ALT_Q = CTRL_ALT_(Q)
CTRL_ALT_R = CTRL_ALT_(R)
CTRL_ALT_S = CTRL_ALT_(S)
CTRL_ALT_T = CTRL_ALT_(T)
CTRL_ALT_U = CTRL_ALT_(U)
CTRL_ALT_V = CTRL_ALT_(V)
CTRL_ALT_W = CTRL_ALT_(W)
CTRL_ALT_X = CTRL_ALT_(X)
CTRL_ALT_Y = CTRL_ALT_(Y)
CTRL_ALT_Z = CTRL_ALT_(Z)

# CTRL SHIFT
CTRL_SHIFT_F1 = CTRL_SHIFT_(F1)
CTRL_SHIFT_F2 = CTRL_SHIFT_(F2)
CTRL_SHIFT_F3 = CTRL_SHIFT_(F3)
CTRL_SHIFT_F4 = CTRL_SHIFT_(F4)
CTRL_SHIFT_F5 = CTRL_SHIFT_(F5)
CTRL_SHIFT_F6 = CTRL_SHIFT_(F6)
CTRL_SHIFT_F7 = CTRL_SHIFT_(F7)
CTRL_SHIFT_F8 = CTRL_SHIFT_(F8)
CTRL_SHIFT_F9 = CTRL_SHIFT_(F9)
CTRL_SHIFT_F10 = CTRL_SHIFT_(F10)
CTRL_SHIFT_F11 = CTRL_SHIFT_(F11)
CTRL_SHIFT_F12 = CTRL_SHIFT_(F12)

CTRL_SHIFT_OEM3_WAVE_OR_BACK_QUOTE = CTRL_SHIFT_(OEM3_WAVE_OR_BACK_QUOTE)
CTRL_SHIFT_1 = CTRL_SHIFT_(KEY_1)
CTRL_SHIFT_2 = CTRL_SHIFT_(KEY_2)
CTRL_SHIFT_3 = CTRL_SHIFT_(KEY_3)
CTRL_SHIFT_4 = CTRL_SHIFT_(KEY_4)
CTRL_SHIFT_5 = CTRL_SHIFT_(KEY_5)
CTRL_SHIFT_6 = CTRL_SHIFT_(KEY_6)
CTRL_SHIFT_7 = CTRL_SHIFT_(KEY_7)
CTRL_SHIFT_8 = CTRL_SHIFT_(KEY_8)
CTRL_SHIFT_9 = CTRL_SHIFT_(KEY_9)
CTRL_SHIFT_0 = CTRL_SHIFT_(KEY_0)
CTRL_SHIFT_11_MINUS = CTRL_SHIFT_(KEY_11_MINUS)
CTRL_SHIFT_12_PLUS = CTRL_SHIFT_(KEY_12_PLUS)
CTRL_SHIFT_BACKSPACE = CTRL_SHIFT_(BACKSPACE)

CTRL_SHIFT_NUMPAD_1 = CTRL_SHIFT_(NUMPAD_1)
CTRL_SHIFT_NUMPAD_2 = CTRL_SHIFT_(NUMPAD_2)
CTRL_SHIFT_NUMPAD_3 = CTRL_SHIFT_(NUMPAD_3)
CTRL_SHIFT_NUMPAD_4 = CTRL_SHIFT_(NUMPAD_4)
CTRL_SHIFT_NUMPAD_5 = CTRL_SHIFT_(NUMPAD_5)
CTRL_SHIFT_NUMPAD_6 = CTRL_SHIFT_(NUMPAD_6)
CTRL_SHIFT_NUMPAD_7 = CTRL_SHIFT_(NUMPAD_7)
CTRL_SHIFT_NUMPAD_8 = CTRL_SHIFT_(NUMPAD_8)
CTRL_SHIFT_NUMPAD_9 = CTRL_SHIFT_(NUMPAD_9)
CTRL_SHIFT_NUMPAD_0 = CTRL_SHIFT_(NUMPAD_0)
CTRL_SHIFT_NUMPAD_11_DIVIDE = CTRL_SHIFT_(NUMPAD_11_DIVIDE)
CTRL_SHIFT_NUMPAD_12_MULTIPLY = CTRL_SHIFT_(NUMPAD_12_MULTIPLY)

CTRL_SHIFT_A = CTRL_SHIFT_(A)
CTRL_SHIFT_B = CTRL_SHIFT_(B)
CTRL_SHIFT_C = CTRL_SHIFT_(C)
CTRL_SHIFT_D = CTRL_SHIFT_(D)
CTRL_SHIFT_E = CTRL_SHIFT_(E)
CTRL_SHIFT_F = CTRL_SHIFT_(F)
CTRL_SHIFT_G = CTRL_SHIFT_(G)
CTRL_SHIFT_H = CTRL_SHIFT_(H)
CTRL_SHIFT_I = CTRL_SHIFT_(I)
CTRL_SHIFT_J = CTRL_SHIFT_(J)
CTRL_SHIFT_K = CTRL_SHIFT_(K)
CTRL_SHIFT_L = CTRL_SHIFT_(L)
CTRL_SHIFT_M = CTRL_SHIFT_(M)
CTRL_SHIFT_N = CTRL_SHIFT_(N)
CTRL_SHIFT_O = CTRL_SHIFT_(O)
CTRL_SHIFT_P = CTRL_SHIFT_(P)
CTRL_SHIFT_Q = CTRL_SHIFT_(Q)
CTRL_SHIFT_R = CTRL_SHIFT_(R)
CTRL_SHIFT_S = CTRL_SHIFT_(S)
CTRL_SHIFT_T = CTRL_SHIFT_(T)
CTRL_SHIFT_U = CTRL_SHIFT_(U)
CTRL_SHIFT_V = CTRL_SHIFT_(V)
CTRL_SHIFT_W = CTRL_SHIFT_(W)
CTRL_SHIFT_X = CTRL_SHIFT_(X)
CTRL_SHIFT_Y = CTRL_SHIFT_(Y)
CTRL_SHIFT_Z = CTRL_SHIFT_(Z)

# ALT SHIFT
ALT_SHIFT_F1 = ALT_SHIFT_(F1)
ALT_SHIFT_F2 = ALT_SHIFT_(F2)
ALT_SHIFT_F3 = ALT_SHIFT_(F3)
ALT_SHIFT_F4 = ALT_SHIFT_(F4)
ALT_SHIFT_F5 = ALT_SHIFT_(F5)
ALT_SHIFT_F6 = ALT_SHIFT_(F6)
ALT_SHIFT_F7 = ALT_SHIFT_(F7)
ALT_SHIFT_F8 = ALT_SHIFT_(F8)
ALT_SHIFT_F9 = ALT_SHIFT_(F9)
ALT_SHIFT_F10 = ALT_SHIFT_(F10)
ALT_SHIFT_F11 = ALT_SHIFT_(F11)
ALT_SHIFT_F12 = ALT_SHIFT_(F12)

ALT_SHIFT_OEM3_WAVE_OR_BACK_QUOTE = ALT_SHIFT_(OEM3_WAVE_OR_BACK_QUOTE)
ALT_SHIFT_1 = ALT_SHIFT_(KEY_1)
ALT_SHIFT_2 = ALT_SHIFT_(KEY_2)
ALT_SHIFT_3 = ALT_SHIFT_(KEY_3)
ALT_SHIFT_4 = ALT_SHIFT_(KEY_4)
ALT_SHIFT_5 = ALT_SHIFT_(KEY_5)
ALT_SHIFT_6 = ALT_SHIFT_(KEY_6)
ALT_SHIFT_7 = ALT_SHIFT_(KEY_7)
ALT_SHIFT_8 = ALT_SHIFT_(KEY_8)
ALT_SHIFT_9 = ALT_SHIFT_(KEY_9)
ALT_SHIFT_0 = ALT_SHIFT_(KEY_0)
ALT_SHIFT_11_MINUS = ALT_SHIFT_(KEY_11_MINUS)
ALT_SHIFT_12_PLUS = ALT_SHIFT_(KEY_12_PLUS)
ALT_SHIFT_BACKSPACE = ALT_SHIFT_(BACKSPACE)

ALT_SHIFT_NUMPAD_1 = ALT_SHIFT_(NUMPAD_1)
ALT_SHIFT_NUMPAD_2 = ALT_SHIFT_(NUMPAD_2)
ALT_SHIFT_NUMPAD_3 = ALT_SHIFT_(NUMPAD_3)
ALT_SHIFT_NUMPAD_4 = ALT_SHIFT_(NUMPAD_4)
ALT_SHIFT_NUMPAD_5 = ALT_SHIFT_(NUMPAD_5)
ALT_SHIFT_NUMPAD_6 = ALT_SHIFT_(NUMPAD_6)
ALT_SHIFT_NUMPAD_7 = ALT_SHIFT_(NUMPAD_7)
ALT_SHIFT_NUMPAD_8 = ALT_SHIFT_(NUMPAD_8)
ALT_SHIFT_NUMPAD_9 = ALT_SHIFT_(NUMPAD_9)
ALT_SHIFT_NUMPAD_0 = ALT_SHIFT_(NUMPAD_0)
ALT_SHIFT_NUMPAD_11_DIVIDE = ALT_SHIFT_(NUMPAD_11_DIVIDE)
ALT_SHIFT_NUMPAD_12_MULTIPLY = ALT_SHIFT_(NUMPAD_12_MULTIPLY)

ALT_SHIFT_A = ALT_SHIFT_(A)
ALT_SHIFT_B = ALT_SHIFT_(B)
ALT_SHIFT_C = ALT_SHIFT_(C)
ALT_SHIFT_D = ALT_SHIFT_(D)
ALT_SHIFT_E = ALT_SHIFT_(E)
ALT_SHIFT_F = ALT_SHIFT_(F)
ALT_SHIFT_G = ALT_SHIFT_(G)
ALT_SHIFT_H = ALT_SHIFT_(H)
ALT_SHIFT_I = ALT_SHIFT_(I)
ALT_SHIFT_J = ALT_SHIFT_(J)
ALT_SHIFT_K = ALT_SHIFT_(K)
ALT_SHIFT_L = ALT_SHIFT_(L)
ALT_SHIFT_M = ALT_SHIFT_(M)
ALT_SHIFT_N = ALT_SHIFT_(N)
ALT_SHIFT_O = ALT_SHIFT_(O)
ALT_SHIFT_P = ALT_SHIFT_(P)
ALT_SHIFT_Q = ALT_SHIFT_(Q)
ALT_SHIFT_R = ALT_SHIFT_(R)
ALT_SHIFT_S = ALT_SHIFT_(S)
ALT_SHIFT_T = ALT_SHIFT_(T)
ALT_SHIFT_U = ALT_SHIFT_(U)
ALT_SHIFT_V = ALT_SHIFT_(V)
ALT_SHIFT_W = ALT_SHIFT_(W)
ALT_SHIFT_X = ALT_SHIFT_(X)
ALT_SHIFT_Y = ALT_SHIFT_(Y)
ALT_SHIFT_Z = ALT_SHIFT_(Z)

# CTRL SHIFT ALT
CTRL_SHIFT_ALT_F1 = CTRL_SHIFT_ALT(F1)
CTRL_SHIFT_ALT_F2 = CTRL_SHIFT_ALT(F2)
CTRL_SHIFT_ALT_F3 = CTRL_SHIFT_ALT(F3)
CTRL_SHIFT_ALT_F4 = CTRL_SHIFT_ALT(F4)
CTRL_SHIFT_ALT_F5 = CTRL_SHIFT_ALT(F5)
CTRL_SHIFT_ALT_F6 = CTRL_SHIFT_ALT(F6)
CTRL_SHIFT_ALT_F7 = CTRL_SHIFT_ALT(F7)
CTRL_SHIFT_ALT_F8 = CTRL_SHIFT_ALT(F8)
CTRL_SHIFT_ALT_F9 = CTRL_SHIFT_ALT(F9)
CTRL_SHIFT_ALT_F10 = CTRL_SHIFT_ALT(F10)
CTRL_SHIFT_ALT_F11 = CTRL_SHIFT_ALT(F11)
CTRL_SHIFT_ALT_F12 = CTRL_SHIFT_ALT(F12)

CTRL_SHIFT_ALT_OEM3_WAVE_OR_BACK_QUOTE = CTRL_SHIFT_ALT(OEM3_WAVE_OR_BACK_QUOTE)
CTRL_SHIFT_ALT_1 = CTRL_SHIFT_ALT(KEY_1)
CTRL_SHIFT_ALT_2 = CTRL_SHIFT_ALT(KEY_2)
CTRL_SHIFT_ALT_3 = CTRL_SHIFT_ALT(KEY_3)
CTRL_SHIFT_ALT_4 = CTRL_SHIFT_ALT(KEY_4)
CTRL_SHIFT_ALT_5 = CTRL_SHIFT_ALT(KEY_5)
CTRL_SHIFT_ALT_6 = CTRL_SHIFT_ALT(KEY_6)
CTRL_SHIFT_ALT_7 = CTRL_SHIFT_ALT(KEY_7)
CTRL_SHIFT_ALT_8 = CTRL_SHIFT_ALT(KEY_8)
CTRL_SHIFT_ALT_9 = CTRL_SHIFT_ALT(KEY_9)
CTRL_SHIFT_ALT_0 = CTRL_SHIFT_ALT(KEY_0)
CTRL_SHIFT_ALT_11_MINUS = CTRL_SHIFT_ALT(KEY_11_MINUS)
CTRL_SHIFT_ALT_12_PLUS = CTRL_SHIFT_ALT(KEY_12_PLUS)
CTRL_SHIFT_ALT_BACKSPACE = CTRL_SHIFT_ALT(BACKSPACE)

CTRL_SHIFT_ALT_NUMPAD_1 = CTRL_SHIFT_ALT(NUMPAD_1)
CTRL_SHIFT_ALT_NUMPAD_2 = CTRL_SHIFT_ALT(NUMPAD_2)
CTRL_SHIFT_ALT_NUMPAD_3 = CTRL_SHIFT_ALT(NUMPAD_3)
CTRL_SHIFT_ALT_NUMPAD_4 = CTRL_SHIFT_ALT(NUMPAD_4)
CTRL_SHIFT_ALT_NUMPAD_5 = CTRL_SHIFT_ALT(NUMPAD_5)
CTRL_SHIFT_ALT_NUMPAD_6 = CTRL_SHIFT_ALT(NUMPAD_6)
CTRL_SHIFT_ALT_NUMPAD_7 = CTRL_SHIFT_ALT(NUMPAD_7)
CTRL_SHIFT_ALT_NUMPAD_8 = CTRL_SHIFT_ALT(NUMPAD_8)
CTRL_SHIFT_ALT_NUMPAD_9 = CTRL_SHIFT_ALT(NUMPAD_9)
CTRL_SHIFT_ALT_NUMPAD_0 = CTRL_SHIFT_ALT(NUMPAD_0)
CTRL_SHIFT_ALT_NUMPAD_11_DIVIDE = CTRL_SHIFT_ALT(NUMPAD_11_DIVIDE)
CTRL_SHIFT_ALT_NUMPAD_12_MULTIPLY = CTRL_SHIFT_ALT(NUMPAD_12_MULTIPLY)

CTRL_SHIFT_ALT_A = CTRL_SHIFT_ALT(A)
CTRL_SHIFT_ALT_B = CTRL_SHIFT_ALT(B)
CTRL_SHIFT_ALT_C = CTRL_SHIFT_ALT(C)
CTRL_SHIFT_ALT_D = CTRL_SHIFT_ALT(D)
CTRL_SHIFT_ALT_E = CTRL_SHIFT_ALT(E)
CTRL_SHIFT_ALT_F = CTRL_SHIFT_ALT(F)
CTRL_SHIFT_ALT_G = CTRL_SHIFT_ALT(G)
CTRL_SHIFT_ALT_H = CTRL_SHIFT_ALT(H)
CTRL_SHIFT_ALT_I = CTRL_SHIFT_ALT(I)
CTRL_SHIFT_ALT_J = CTRL_SHIFT_ALT(J)
CTRL_SHIFT_ALT_K = CTRL_SHIFT_ALT(K)
CTRL_SHIFT_ALT_L = CTRL_SHIFT_ALT(L)
CTRL_SHIFT_ALT_M = CTRL_SHIFT_ALT(M)
CTRL_SHIFT_ALT_N = CTRL_SHIFT_ALT(N)
CTRL_SHIFT_ALT_O = CTRL_SHIFT_ALT(O)
CTRL_SHIFT_ALT_P = CTRL_SHIFT_ALT(P)
CTRL_SHIFT_ALT_Q = CTRL_SHIFT_ALT(Q)
CTRL_SHIFT_ALT_R = CTRL_SHIFT_ALT(R)
CTRL_SHIFT_ALT_S = CTRL_SHIFT_ALT(S)
CTRL_SHIFT_ALT_T = CTRL_SHIFT_ALT(T)
CTRL_SHIFT_ALT_U = CTRL_SHIFT_ALT(U)
CTRL_SHIFT_ALT_V = CTRL_SHIFT_ALT(V)
CTRL_SHIFT_ALT_W = CTRL_SHIFT_ALT(W)
CTRL_SHIFT_ALT_X = CTRL_SHIFT_ALT(X)
CTRL_SHIFT_ALT_Y = CTRL_SHIFT_ALT(Y)
CTRL_SHIFT_ALT_Z = CTRL_SHIFT_ALT(Z)
