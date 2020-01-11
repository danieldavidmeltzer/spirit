from .Exceptions import Ambiguous


def get_single_item(a_list):
    """
    get single item from list.
    raises Ambiguous Exception if more than one item
    returns None if list is empty.
    """
    if len(a_list) == 1:
        return a_list[0]
    elif len(a_list) > 1:
        raise Ambiguous("Ambiguous representations")
    return None


def lower_list(a_list):
    return [item.lower() for item in a_list]
