from spirit.utils.fetcher import get_all_funcs
from spirit.utils.list_utils import get_single_item
from . import drivers
from purl import URL


def find_publisher_driver(url):
    url_parts = URL(url)
    optional_publishers = get_all_funcs(drivers)

    def publisher_filter(publisher):
        filter_scheme_field = "scheme"
        if hasattr(publisher, filter_scheme_field):
            if getattr(publisher, filter_scheme_field) == url_parts.scheme():
                return True
        return False

    optional_publishers = list(filter(publisher_filter, optional_publishers))
    create_publisher = get_single_item(optional_publishers)
    return create_publisher(url)


