# -*- coding: utf-8 -*-

import os
import enum
from hotkeynet.enumerate import EnumHelper


class NameEnum(enum.Enum):
    alice = "Alice"
    bob = "Bob"


class NameHelper(EnumHelper[NameEnum, str]):
    enum_class = NameEnum


class InvalidEnum(enum.Enum):
    foo = "foo"


class TestEnumGetter:
    def test(self):
        assert NameHelper.get_name("alice") == "alice"
        assert NameHelper.get_name(NameEnum.alice) == "alice"

        assert NameHelper.get_enum("alice") is NameEnum.alice
        assert NameHelper.get_enum(NameEnum.alice) is NameEnum.alice

        assert NameHelper.get_value("alice") == "Alice"
        assert NameHelper.get_value(NameEnum.alice) == "Alice"

        assert NameHelper.iter_names()[0] == "alice"
        assert NameHelper.iter_enums()[0] is NameEnum.alice
        assert NameHelper.iter_values()[0] == "Alice"

        assert NameHelper.iter_items()[0][0] == "alice"
        assert NameHelper.iter_items()[0][1] is NameEnum.alice
        assert NameHelper.iter_items()[0][2] == "Alice"

        assert NameHelper.has_name("alice") is True
        assert NameHelper.has_name("invalid") is False

        assert NameHelper.has_enum(NameEnum.alice) is True
        assert NameHelper.has_enum(InvalidEnum.foo) is False

        assert NameHelper.has_value("Alice") is True
        assert NameHelper.has_value("Foo") is False


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
