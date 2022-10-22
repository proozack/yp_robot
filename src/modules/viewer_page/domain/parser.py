#  najważniejse pytanie:  czy nie powinienem się tutaj posługiwać cały czas agregat root?
from ..domain.entry_point import (
    EntryPoint,
    Url,
    HostName,
    ClassName,
    ObjectInstance
)

from src.utl_utils import UrlUtils
from importlib import import_module
# !!! object_instances == parser

#  !!! czy to powinna być instancja entry point czy parser's


class Parser():
    def __init__(self):
        pass

    #  czy tu nie powinno być settera ??

    def choose_parser(self, entry_point: EntryPoint) -> ObjectInstance:
        host_name = self._get_host_name(entry_point)
        class_name = self._change_host_to_class(host_name)
        object_instances = self._get_object_instaces(class_name)
        # dynamicly import class and run this class with params
        return object_instances

    def _get_url(self, entry_point: EntryPoint) -> Url:  # czy to ma sens gdy to będzie wszystko w  obiekcie
        u = Url(entry_point.url)
        return u.url

    def _get_host_name(self, entry_point: EntryPoint) -> HostName:
        uu = UrlUtils(self._get_url())
        hn = HostName(uu.get_domain())
        return hn.host_name  # pole host_name powinno być zmienione na value

    def _change_host_to_class(self, host_name: HostName) -> ClassName:
        uu = UrlUtils(self._get_url())  # przerobić tą biblotekę na funkcje
        cn = ClassName(uu.convert_domain_to_class_name(host_name))
        return cn.class_name  # przerobić na name

    def _get_object_instaces(self, class_name: ClassName) -> ObjectInstance:
        module_str = 'src.modules.viver_page.scraper.parasers.{}'.format(class_name)
        module = import_module(module_str)
        object_instaces = getattr(module, class_name)
        return object_instaces
