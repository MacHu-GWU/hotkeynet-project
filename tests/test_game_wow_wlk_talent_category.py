# -*- coding: utf-8 -*-

import pytest

from hotkeynet.projects.warmane.constant.talent import Talent


class TestTalent:
    def test_value_is_string(self):
        assert Talent.dk_pve_blood_tank.name == "dk_pve_blood_tank"
        assert isinstance(Talent.dk_pve_blood_tank.value, int)

    def test_sortable(self):
        l = [
            Talent.druid_pve_balance,
            Talent.dk_pve_blood_tank,
            Talent.priest_pve_disco
        ]
        l.sort()



if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
