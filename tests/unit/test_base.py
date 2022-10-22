import pytest # noqa F401
# from viewer_page.domain.page import (EntryPoint, Shop)
from src.modules.viewer_page.domain.page import (EntryPoint, Shop)


def test_add_entry_point_increament_version_number():
    # given
    shop = Shop('intymna')
    ep = EntryPoint('https://www.intymna.pl/c1381,1167,0,0,,body')

    # when
    assert shop.version_number == 0
    shop.add_entry_point(ep)

    # then
    assert shop.version_number == 1


def test_add_main_category_to_entry_point():
    # given
    shop = Shop('intymna')
    ep = EntryPoint('https://www.intymna.pl/c1381,1167,0,0,,body')

    # when
    shop.add_entry_point(ep)

    # then
    assert shop.name == 'intymna'
