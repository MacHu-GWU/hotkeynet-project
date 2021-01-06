# -*- coding: utf-8 -*-

ESC = "Esc"

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

OEM3_WAVE = "Oem3"
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

TAB = "Tab"
CAPSLOCK = "CapsLock"
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

OEM4_SQUARE_BRACKET_LEFT = "Oem4"
OEM6_SQUARE_BRACKET_RIGHT = "Oem6"
OEM5_PIPE = "Oem5"
OEM1_SEMICOLUMN = "Oem1"
OEM7_QUOTE = "Oem7"
COMMA = "Comma"
PERIOD = "Period"
OEM2_QUESTION = "Oem2"
ENTER = "Enter"

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

NUMPAD_0 = "Numpad0"
NUMPAD_1 = "Numpad1"
NUMPAD_2 = "Numpad2"
NUMPAD_3 = "Numpad3"
NUMPAD_4 = "Numpad4"
NUMPAD_5 = "Numpad5"
NUMPAD_6 = "Numpad6"
NUMPAD_7 = "Numpad7"
NUMPAD_8 = "Numpad8"
NUMPAD_9 = "Numpad9"
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

MOUSE_LButton = "LButton"
MOUSE_RButton = "RButton"
MOUSE_MButton = "MButton"
MOUSE_Button4 = "Button4"
MOUSE_Button5 = "Button5"


def CTRL_(*keys):
    return "{} {}".format(CTRL, ", ".join(keys))


def SHIFT_(*keys):
    return "{} {}".format(SHIFT, ", ".join(keys))


def ALT_(*keys):
    return "{} {}".format(ALT, ", ".join(keys))


def CTRL_ALT_(*keys):
    return "{} {} {}".format(CTRL, ALT, ", ".join(keys))


def CTRL_SHIFT_(*keys):
    return "{} {} {}".format(CTRL, SHIFT, ", ".join(keys))


def ALT_SHIFT_(*keys):
    return "{} {} {}".format(ALT, SHIFT, ", ".join(keys))


def CTRL_SHIFT_ALT(*keys):
    return "{} {} {} {}".format(CTRL, SHIFT, ALT, ", ".join(keys))


def SCROLOCK_ON(key):
    return "ScrollLockOn {}".format(key)


def CAPSLOCK_ON(key):
    return "CapsLockOn {}".format(key)


