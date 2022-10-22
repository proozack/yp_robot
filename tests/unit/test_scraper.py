import pytest # noqa F401
from src.modules.viewer_page.scraper.services import ScraperServices


def test_entry_point():
    url = 'https://pakuten.pl/27-sukienki'
    # given
    ss = ScraperServices()
    catalog = ss.process_entry_point(url)
    # when
    assert catalog is None
    # then
    pass
