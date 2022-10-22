from abc import ABC, abstractmethod
from typing import Callable, Any # noqa F401
from bs4 import BeautifulSoup # noqa F401
from .exceptions import VPScraperError # noqa F401

import logging

log = logging.getLogger(__name__)


class CatalogParser(ABC):
    def __init__(self):
        pass

    """
    @abstractmethod
    def set_response(self, value: str):
        pass

    @abstractmethod
    def get_list_links_from_page(self) -> list:
        pass

    @abstractmethod
    def get_list_image_from_page(self) -> list:
        pass

    @abstractmethod
    def get_title(self) -> str:
        pass
    """
    @abstractmethod
    def get_entity(self) -> list:
        pass

    @abstractmethod
    def get_title(self):
        pass

    @abstractmethod
    def get_price(self):
        pass


class PageParser(ABC):
    def __init__(self):
        pass

    def get_images(self):
        pass

    def get_title(self):
        pass


class ProductParser(ABC):
    def __init__(self):
        pass
