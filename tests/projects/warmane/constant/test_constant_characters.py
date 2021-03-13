# -*- coding: utf-8 -*-

import pytest

from hotkeynet.projects.warmane.constant.characters import CharacterFactory


class TestCharacterFactory:
    def test(self):
        CharacterFactory.make_char_fatmulti1_batlefury_pve_protect_pala().evolve(window_index=1)


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
