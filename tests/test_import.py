# -*- coding: utf-8 -*-

import pytest


def test():
    import hotkeynet

    _ = hotkeynet.KN
    _ = hotkeynet.CN
    _ = hotkeynet.ActFactory


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
