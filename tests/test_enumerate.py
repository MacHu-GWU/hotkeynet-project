# -*- coding: utf-8 -*-

import os
import enum
from hotkeynet.enumerate import EnumGetter


class NameEnum(enum.Enum):
    alice = "Alice"
    bob = "Bob"


class NameGetter(EnumGetter[NameEnum, str]):
    enum_class = NameEnum


class TestEnumGetter:
    def test(self):
        assert NameGetter.get_name("alice") == "alice"
        assert NameGetter.get_name(NameEnum.alice) == "alice"

        assert NameGetter.get_enum("alice") is NameEnum.alice
        assert NameGetter.get_enum(NameEnum.alice) is NameEnum.alice

        assert NameGetter.get_value("alice") == "Alice"
        assert NameGetter.get_value(NameEnum.alice) == "Alice"

        assert NameGetter.iter_keys()[0] == "alice"
        assert NameGetter.iter_enum()[0] is NameEnum.alice
        assert NameGetter.iter_values()[0] == "Alice"

        assert NameGetter.iter_items()[0][0] == "alice"
        assert NameGetter.iter_items()[0][1] is NameEnum.alice
        assert NameGetter.iter_items()[0][2] == "Alice"


if __name__ == "__main__":
    import sys
    import subprocess

    abspath = os.path.abspath(__file__)
    dir_project_root = os.path.dirname(abspath)
    for _ in range(10):
        if os.path.exists(os.path.join(dir_project_root, ".git")):
            break
        else:
            dir_project_root = os.path.dirname(dir_project_root)
    else:
        raise FileNotFoundError("cannot find project root dir!")
    dir_htmlcov = os.path.join(dir_project_root, "htmlcov")
    bin_pytest = os.path.join(os.path.dirname(sys.executable), "pytest")

    args = [
        bin_pytest,
        "-s", "--tb=native",
        f"--rootdir={dir_project_root}",
        "--cov=hotkeynet.enumerate",
        "--cov-report", "term-missing",
        "--cov-report", f"html:{dir_htmlcov}",
        abspath,
    ]
    subprocess.run(args)
