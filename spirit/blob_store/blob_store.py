from purl import URL
from spirit.utils import fetcher
from spirit.utils.list_utils import get_single_item
from . import drivers


class BlobStore:
    """
    class that helps mange saving and reading binaries through
    different services using different drivers
    """
    def __init__(self, url, keys=None):
        """
        initialise a blob store using a url, correct blob store and it's
        driver are identified through the url's scheme
        Args:
            url: the url of the blob store
            keys: optional keys for the blob center
        """
        self.driver = find_driver(url, keys)

    def save_binary(self, binary):
        """
        save a binary to the blob store
        Args:
            binary:
                binary to save
        Returns:
            unique id for fetching the binary later
        """
        return self.driver.save_binary(binary)

    def get_binary(self, binary_id):
        """
        get binary using id given when saving
        Args:
            binary_id: the id given to the file upon saving

        Returns:
            bytes typed obj
        """
        return self.driver.get_binary(binary_id)


def find_driver(url, keys=None, special_filter=lambda x: True):
    """
    find driver given url
    Args:
        url: url to find driver, scheme is relevant part
        keys: the keys to use for some drivers, None if
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
    if keys:
        return driver_cls(url, keys)
    else:
        return driver_cls(url)
