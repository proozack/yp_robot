from ..domain.entry_point import EntryPoint
from ..domain.product import Product
from ..domain.parser import Parser
from ..service_layer import messagebus
from src.modules.viewer_page.exceptions import VPScraperCatalogError
# import celery -> nie używamy tutaj celry tylko emitujemy do messagebus
# a heandlar powinnien mieć specianylny miejsce na przechytywanie tych eventów
# i dopiero on poiwnnien clecać taski celery jeśli będzie to celery

log = None  # ToDo Create logger


class Catalogs():  # czy na pewno catalogs czy raczej powinno być catalog
    catalogs: [Product] = set()  # ?? czy prawidłowa nazwa obiektu ??

    # @celery.task
    def process(self, entry_point: EntryPoint, parser: Parser) -> bool:
        # uruchamia paraser dla strony typu catalog
        # emituje event zapisz produkty dla obiektu Catalog

        # Tutaj powinno być uruchomienie paraserów
        try:
            lst_product = self._parse_catalog(entry_point)
            for product in lst_product:
                self.catalogs.add(product)
            command = 'save:products'
            messagebus.save(command, self.catalogs)
            result = True  # czy to napewno powinno być true,
            # bo w sumie to o niczym nie mówi poza tym że zakończyło bez błędów
        except VPScraperCatalogError as e:
            log.warnning('Can\'t parse catalog {} '.format(entry_point.url))
            result = e.message
        return result

    def _parse_catalog(self, entry_point: EntryPoint, parser: Parser) -> [Product]:
        lst_products = set()
        # prser = None  # ToDo stworzyc metodę generowania parserów i emitowania następnej strony
        for product in parser(entry_point):
            lst_products.add(product)
        return product
