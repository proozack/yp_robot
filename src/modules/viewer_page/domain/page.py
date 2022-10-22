from typing import NoReturn
from dataclasses import dataclass
from .aggregate import AggregateRoot

#  !!! To wszystko jest do przeorganizowania !!!

@dataclass(unsafe_hash=True)
class HostName:
    host_name: str


@dataclass(unsafe_hash=True)
class ClassName:
    class_name: str


@dataclass(unsafe_hash=True)
class ObjectInstance:
    instance: object


@dataclass(unsafe_hash=True)
class EntryPoint:
    url: str


class Shop(AggregateRoot):  # to nie będzie shop tylko encja entry point

    def __init__(self, name):
        super().__init__()
        self.name = name
        self.base_url = None
        self.brand_shop = None
        self.entry_points: set[EntryPoint] = set()

    def __repr__(self) -> str:
        return 'Shop(name=\'{}\')'.format(self.name)

    def add_entry_point(self, entry_point: EntryPoint) -> NoReturn:
        self.entry_points.add(entry_point)
        self.version_number += 1
