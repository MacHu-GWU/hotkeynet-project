# -*- coding: utf-8 -*-

import pytest

from hotkeynet.game.wow.wlk.talent_category import TalentCategory


class TestTalentCategory:
    def test_name_is_string_value_is_int(self):
        assert TalentCategory.warrior_tank.name == "warrior_tank"
        assert isinstance(TalentCategory.warrior_tank.value, int)

    def test_sortable(self):
        talent_category_list = [
            TalentCategory.tank,
            TalentCategory.dps,
            TalentCategory.healer
        ]
        talent_category_list.sort()

        talent_category_code_list = [t.value for t in talent_category_list]
        talent_category_code_list.sort()
        assert (
            talent_category_code_list[1] > talent_category_code_list[0]
            and talent_category_code_list[2] > talent_category_code_list[1]
        )


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
