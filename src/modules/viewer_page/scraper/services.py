# from ..domain.catalog import Catalog
from ..domain.entry_point import EntryPoint
from ..domain.parser import Parser
from ..service_layer import messagebus


#  To nic innego jak services_layer
class ScraperServices():
    def __init__(self):
        pass

    # entry point powinien dziedziczy po obiekcie bazowym ze zmienionym url strony docelowej

    def process_entry_point(self, entry_point):
        # catalog = Catalog()
        parser = self._specify_parser(entry_point)
        # result = catalog.process.delay(entry_point, parser)  # czym będzie result?
        # result = catalog.process(entry_point, parser)  # czym będzie result?
        command = 'viewer_page:catalog_process'  # assync jest bez sensu, ponieważ wszystko jest assync
        messagebus.process(command, (entry_point, parser))

        # command = 'save:process_entry_point'
        # messagebus.process(command, result)

        # to będzie task celery
        # zlecam przetworzenie pierwszej strony
        # coś w stylu catalog.process.delay(entry_point)
        #
        # /wewnątrz tego obirktu zostana wyemitowane eventy zapisu produktów/
        # /wewnątrz tego obiektu zostanie wyemtowany event przetworzenie nastepnej strony/
        # zwroócony zostanie status przetorzzenia strony
        #
        #
        # url do przetworzenia
        #
        # z któego zostanie zorbiony koleny task z nowym adresem url i nowymi parametrami
        #
        # next_page powinno być obiektem z parametrami url oraz danymi dziedziczoącymi po pierwszym zleceniu
        #
        # next_page = peocess_catalog_page(url)
        #
        return True

    def _specify_parser(self, entry_point: EntryPoint) -> Parser:
        # nie wiem czy to jest właściwe podejście do zagadnienia bo wszystko emituje evenetu,
        # a to działą synchronicznie, druga spraw to, to że do celery chyba nie można przekazać obiektu
        p = Parser()  # ToDo  czy to nie powinno być dwóch klas jedna dla instancji parsera a fróga ogóna ?
        parser = p.choose_parser(entry_point)
        return parser
