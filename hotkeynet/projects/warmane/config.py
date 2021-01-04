# Use Monkey Patch to replace this value

import json
from pathlib_mate import PathCls as Path

credentials_file = Path(__file__).parent.parent.parent.change(new_basename="credentials.json")
credentials = json.loads(credentials_file.read_text(encoding="utf-8"))

class Config:
    WOW_EXE_PATH = r"D:\HSH\Games\WOW Private\Client\World of Warcraft 3.3.5 enUS (Warman wod models)\Wow.exe"

    WRONG_PASSWORD_POP_UP_X_AT_1920_1080 = 890
    WRONG_PASSWORD_POP_UP_Y_AT_1920_1080 = 565
    USERNAME_INPUT_BOX_X_AT_1920_1080 = 900
    USERNAME_INPUT_BOX_Y_AT_1920_1080 = 505

    WRONG_PASSWORD_POP_UP_X_AT_1600_900 = 792
    WRONG_PASSWORD_POP_UP_Y_AT_1600_900 = 502
    USERNAME_INPUT_BOX_X_AT_1600_900 = 788
    USERNAME_INPUT_BOX_Y_AT_1600_900 = 451

    WRONG_PASSWORD_POP_UP_X = None
    WRONG_PASSWORD_POP_UP_Y = None
    USERNAME_INPUT_BOX_X = None
    USERNAME_INPUT_BOX_Y = None

    fatmulti1_username = "fatmulti1"
    fatmulti1_password = credentials["fatmulti1"]

    fatmulti2_username = "fatmulti2"
    fatmulti2_password = credentials["fatmulti2"]

    fatmulti3_username = "fatmulti3"
    fatmulti3_password = credentials["fatmulti3"]

    fatmulti4_username = "fatmulti4"
    fatmulti4_password = credentials["fatmulti4"]

    fatmulti5_username = "fatmulti5"
    fatmulti5_password = credentials["fatmulti5"]

    fitsheep_username = "fitsheep"
    fitsheep_password = credentials["fitsheep"]

    fatmulti6_username = "fatmulti6"
    fatmulti6_password = credentials["fatmulti6"]

    fatmulti8_username = "fatmulti8"
    fatmulti8_password = credentials["fatmulti8"]

    fatmulti9_username = "fatmulti9"
    fatmulti9_password = credentials["fatmulti9"]

    fatmulti10_username = "fatmulti10"
    fatmulti10_password = credentials["fatmulti10"]

    fatmulti11_username = "fatmulti11"
    fatmulti11_password = credentials["fatmulti11"]

    fatmulti12_username = "fatmulti12"
    fatmulti12_password = credentials["fatmulti12"]

    fatmulti13_username = "fatmulti13"
    fatmulti13_password = credentials["fatmulti13"]

    fatmulti14_username = "fatmulti14"
    fatmulti14_password = credentials["fatmulti14"]

    fatmulti15_username = "fatmulti15"
    fatmulti15_password = credentials["fatmulti15"]

    fatmulti16_username = "fatmulti16"
    fatmulti16_password = credentials["fatmulti16"]

    fatmulti17_username = "fatmulti17"
    fatmulti17_password = credentials["fatmulti17"]

    fatmulti18_username = "fatmulti18"
    fatmulti18_password = credentials["fatmulti18"]

    credentials = [
        dict(username=fatmulti1_username, password=fatmulti1_password),
        dict(username=fatmulti2_username, password=fatmulti2_password),
        dict(username=fatmulti3_username, password=fatmulti3_password),
        dict(username=fatmulti4_username, password=fatmulti4_password),
        dict(username=fatmulti5_username, password=fatmulti5_password),
        dict(username=fitsheep_username, password=fitsheep_password),
        dict(username=fatmulti6_username, password=fatmulti6_password),
        dict(username=fatmulti8_username, password=fatmulti8_password),
        dict(username=fatmulti9_username, password=fatmulti9_password),
        dict(username=fatmulti10_username, password=fatmulti10_password),
        dict(username=fatmulti11_username, password=fatmulti11_password),
        dict(username=fatmulti12_username, password=fatmulti12_password),
        dict(username=fatmulti13_username, password=fatmulti13_password),
        dict(username=fatmulti14_username, password=fatmulti14_password),
        dict(username=fatmulti15_username, password=fatmulti15_password),
        dict(username=fatmulti16_username, password=fatmulti16_password),
        dict(username=fatmulti17_username, password=fatmulti17_password),
        dict(username=fatmulti18_username, password=fatmulti18_password),
    ]

    class SendLabelTo:
        all = []