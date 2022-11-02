import pytest # noqa F401
from src.modules.viewer_page.scraper.services import ScraperServices  # noqa F401
from src.modules.viewer_page.domain.entry_point import EntryPoint, Url  # noqa F401
from src.modules.viewer_page.domain.parser import Parser


@pytest.mark.parametrize("test_case,expected", [
    (
        'https://pakuten.pl/27-sukienki',
        {
            'protocol': 'https',
            'username': None,
            'password': None,
            'host': 'pakuten.pl',
            'port': 443,
            'path': '/27-sukienki',
            'query': {},
            'fragment': None
        },
    ),
    (
        'https://test_login:test_haslo@pakuten.pl/27-sukienki?kolor=czerwony&typ=mini#zdjecia',
        {
            'protocol': 'https',
            'username': 'test_login',
            'password': 'test_haslo',
            'host': 'pakuten.pl',
            'port': 443,
            'path': '/27-sukienki',
            'query': {'kolor': 'czerwony', 'typ': 'mini'},
            'fragment': 'zdjecia'
        },
    ),
    (
        'http://test_login@pakuten.pl:8080/27-sukienki?kolor=czerwony&typ=mini#zdjecia',
        {
            'protocol': 'http',
            'username': 'test_login',
            'password': None,
            'host': 'pakuten.pl',
            'port': 8080,
            'path': '/27-sukienki',
            'query': {'kolor': 'czerwony', 'typ': 'mini'},
            'fragment': 'zdjecia'
        },
    ),
    (
        'https://www.intymna.pl/p1,1,0,67034,,sari-biustonosz-soft',
        {
            'protocol': 'https',
            'username': None,
            'password': None,
            'host': 'www.intymna.pl',
            'port': 443,
            'path': '/p1,1,0,67034,,sari-biustonosz-soft',
            'query': {},
            'fragment': None
        },
    ),
])
def test_url(test_case, expected):
    # given
    url = Url(test_case)

    # when
    assert url.protocol == expected.get('protocol')
    assert url.username == expected.get('username')
    assert url.password == expected.get('password')
    assert url.host == expected.get('host')
    assert url.port == expected.get('port')
    assert url.path == expected.get('path')
    assert url.query == expected.get('query')
    assert url.fragment == expected.get('fragment')
    assert url.params == expected.get('params')

    # then
    pass


@pytest.mark.parametrize("test_case,expected", [
    ('pakuten.pl', 'PakutenPl'),
    ('www.pakuten.pl', 'PakutenPl'),
    ]
)
def test_parser(test_case, expected):
    # given
    p = Parser()
    result = p._convert_domain_to_class_name(test_case)
    # when
    assert result == expected
    # then
    pass


def test_entry_point():
    url = 'https://intymna.pl/27-sukienki'
    # given
    ep = EntryPoint(url)
    # ep.url = url
    ss = ScraperServices()
    catalog = ss.process_entry_point(ep)
    # when
    assert catalog is None
    # then
    pass
