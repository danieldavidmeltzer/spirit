import inspect

from purl import URL

from .list_utils import get_single_item


def get_all(module, evaluator):
    sub_modules = inspect.getmembers(module, inspect.ismodule)
    items = []
    for item in sub_modules:
        # getting items from inspect result
        concrete_item = item[1]
        items_contained = inspect.getmembers(concrete_item, evaluator)
        formatted_items = [contained_item[1]
                           for contained_item in items_contained]
        items.extend(formatted_items)
    return items


def get_all_classes(module):
    return get_all(module, inspect.isclass)


def get_all_funcs(module):
    return get_all(module, inspect.isfunction)


def find_driver(url,
                drivers,
                filter_scheme_field="scheme",
                special_filter=lambda x: True
                ,**kwargs):
    """
    find driver given url
    Args:
        drivers: drivers to check in
        filter_scheme_field: the field that has the relevant scheme
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
        if hasattr(cls_driver, filter_scheme_field):
            if getattr(cls_driver, filter_scheme_field) == url_scheme:
                return True
        return False

    all_drivers = get_all_classes(drivers)
    url_drivers = list(filter(driver_filter, all_drivers))
    url_drivers = list(filter(special_filter, url_drivers))
    driver_cls = get_single_item(url_drivers)
    return driver_cls(url, **kwargs)
