from typing import NoReturn
from dataclasses import dataclass
from .aggregate import AggregateRoot
# from src.utils.url_utils import UrlUtils
from urllib.parse import urlparse

# jakie jest różnica pomiędzy obiektem tworzomnym a odczytywanym ?
# Odp. nie powinno być różnicy, stanobiektu powinnien być taki sam
#
#
#
# bo tworzony powinien wyznaczać te wszystkie obiekty
# a odczytywany mógł by je mieć zapisane i nie musiał by niczego robić


@dataclass(unsafe_hash=True)
class Url:
    url: str

    def __post_init__(self):
        self._init__var()
        self._set_fields()

    def _init__var(self):
        self._login = None
        self._password = None
        self._host = None
        self._host = None

    def _set_fields(self):
        self._url_parse = urlparse(self.url)
        netl = self._url_parse.netloc.split('@')
        if len(netl) == 1:
            self._host = netl[0]
        else:
            auth_date = netl[0].split(':')
            self._login = auth_date[0]
            if len(auth_date) != 1:
                self._password = auth_date[1]
            server = netl[1].split(':')
            self._host = server[0]

    @property
    def protocol(self) -> str:  # lub enum [http, https]
        return self._url_parse.scheme

    @property
    def username(self) -> str:
        return self._url_parse.username

    @property
    def password(self) -> str:
        return self._password

    @property
    def host(self) -> str:
        return self._host

    @property
    def port(self) -> int:
        _default_ports = {
            'http': 80,
            'https': 443,
        }
        if self._url_parse.port is None:
            return _default_ports.get('https')
        return self._url_parse.port

    @property
    def params(self) -> str:
        return None if self._url_parse.params == '' else self._url_parse.params

    @property
    def path(self) -> str:
        return self._url_parse.path

    @property
    def query(self) -> str:
        kv_dct = {}
        for kv in self._url_parse.query.split('&'):
            if kv:
                temp_tab = kv.split('=')
                kv_dct[temp_tab[0]] = temp_tab[1]
        self._query = kv_dct
        return self._query

    @property
    def fragment(self) -> str:
        return None if self._url_parse.fragment == '' else self._url_parse.fragment


@dataclass(unsafe_hash=True)
class ClassName:
    class_name: str


@dataclass(unsafe_hash=True)
class ObjectInstance:
    instance: object


class EntryPoint(AggregateRoot):
    def __init__(self, url):
        super().__init__()
        self.url = Url(url)

    def __repr__(self) -> str:
        return 'EntryPoint(url=\'{}\')'.format(self.url)

    def add_entry_point(self, url) -> NoReturn:
        self.entry_points.add(
            Url(url)
        )
        self.version_number += 1
