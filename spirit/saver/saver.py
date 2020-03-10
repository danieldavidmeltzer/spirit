from purl import URL

from spirit.representation_construction.protobuf_construction.protobuf_parsers \
    import saver_protobuf_parser
from spirit.saver_protobuf.saver_proto_pb2 import ParsingResult
from spirit.utils import fetcher
from spirit.utils.list_utils import get_single_item
from . import drivers


class Saver:
    def __init__(self, database_url):
        self.driver = find_driver(database_url)

    def save(self, packet):
        result = ParsingResult()
        result.ParseFromString(packet)
        represented_result = saver_protobuf_parser.parse_saver_protobuf(result)
        self.driver.save_parsing_result(represented_result)


# TODO: move to fetcher's driver
def find_driver(url, special_filter=lambda x: True):
    """
    find driver given url
    Args:
        url: url to find driver, scheme is relevant part
        special_filter: special filter is optional, should be used
        when more than one filter for scheme

    Returns:
        driver to use
    Raises:
        "Ambiguous" Exception if there is more than one supporting driver

    """

    def driver_filter(cls_driver):
        """
        filter driver using the url given to find_driver
        Args:
            cls_driver:
                the class of the driver
        Returns:
            True if the driver supports matching scheme for url,
            False otherwise
        """
        url_scheme = URL(url).scheme()
        filter_scheme_field = "scheme"
        if hasattr(cls_driver, filter_scheme_field):
            if getattr(cls_driver, filter_scheme_field) == url_scheme:
                return True
        return False

    all_drivers = fetcher.get_all_classes(drivers)
    url_drivers = list(filter(driver_filter, all_drivers))
    url_drivers = list(filter(special_filter, url_drivers))
    driver_cls = get_single_item(url_drivers)
    return driver_cls(url)
