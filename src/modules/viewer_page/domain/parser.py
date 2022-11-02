#  najważniejse pytanie:  czy nie powinienem się tutaj posługiwać cały czas agregat root?
from ..domain.entry_point import (
    EntryPoint,
    # Url,  # tylko na potrzeby typing  # to powinien zwrać agergateroot i wszystkie pozostałe powinnien też
    # HostName,
    ClassName,
    ObjectInstance  # ale część tych importów musi funkjconować żeby zachować adnotacje
)

# from src.utils.url_utils import UrlUtils
from importlib import import_module
# !!! object_instances == parser

#  !!! czy to powinna być instancja entry point czy parser's


class Parser():
    def __init__(self):
        pass

    #  czy tu nie powinno być settera ??

    def choose_parser(self, entry_point: EntryPoint) -> ObjectInstance:
        self.entry_point = entry_point
        # host_name = entry_point.url.host  # self._get_host_name(entry_point)
        class_name = self._convert_domain_to_class_name(entry_point.url.host)
        object_instances = self._get_object_instaces(class_name)
        # dynamicly import class and run this class with params
        return object_instances

    def _convert_domain_to_class_name(self, host: str) -> str:
        tab = host.split('.')
        tmp_tab = []
        for ent in tab:
            if ent != 'www':
                tmp_tab.append(ent.capitalize())
        return ''.join(tmp_tab)

    """
    def _get_url(self, entry_point: EntryPoint) -> Url:  # czy to ma sens gdy to będzie wszystko w  obiekcie
        u = Url(entry_point.url)
        return u.url
    """

    """
    def _get_host_name(self, entry_point: EntryPoint) -> HostName:
        # uu = UrlUtils(self._get_url(entry_point))
        # hn = HostName(uu.get_domain())
        return entry_point.url.host  # hn.host_name  # pole host_name powinno być zmienione na value
    """
    """
    def _change_host_to_class(self, host_name: str) -> ClassName:
        # uu = self.entry_point.url  # UrlUtils(self._get_url())  # przerobić tą biblotekę na funkcje
        cn = ClassName(
            self._convert_domain_to_class_name(
                self.entry_point.url.host
            )
        )
        return cn.class_name  # przerobić na name
    """

    def _get_object_instaces(self, class_name: ClassName) -> ObjectInstance:
        module_str = 'src.modules.viewer_page.scraper.parsers.{}'.format(class_name)
        module = import_module(module_str)
        object_instaces = getattr(module, class_name)
        return object_instaces
