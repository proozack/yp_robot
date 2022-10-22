from typing import NoReturn
from dataclasses import dataclass
from .aggregate import AggregateRoot


@dataclass(unsafe_hash=True)
class Url:
    url: str


@dataclass(unsafe_hash=True)
class HostName:
    host_name: str


@dataclass(unsafe_hash=True)
class ClassName:
    class_name: str


@dataclass(unsafe_hash=True)
class ObjectInstance:
    instance: object


class EntryPoint(AggregateRoot):
    def __init__(self, url):
        super().__init__()
        self.url = url

    def __repr__(self) -> str:
        return 'EntryPoint(url=\'{}\')'.format(self.url)

    def add_entry_point(self, url) -> NoReturn:
        self.entry_points.add(url)
        self.version_number += 1
