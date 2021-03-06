# -*- coding: utf-8 -*-

import pytest

from hotkeynet.projects.warmane.constant.talent_category_association import (
    Talent, TalentCategory, get_talent_by_category, get_category_by_talent,
)


def test_get_talent_by_category():
    assert get_talent_by_category(category=TalentCategory.healer) == [
        Talent.paladin_pve_holy,
        Talent.shaman_pve_resto,
        Talent.druid_pve_resto,
        Talent.priest_pve_disco,
        Talent.priest_pve_holy,
    ]


def test_get_category_by_talent():
    assert get_category_by_talent(talent=Talent.priest_pve_shadow) == [
        TalentCategory.pve,
        TalentCategory.dps,
        TalentCategory.ranger,
        TalentCategory.caster,
    ]


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
