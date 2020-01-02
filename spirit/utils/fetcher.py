import inspect


def get_all(module, evaluator):
    sub_modules = inspect.getmembers(module, inspect.ismodule)
    items = []
    for item in sub_modules:
        concrete_item = item[1]
        items_contained = inspect.getmembers(concrete_item, evaluator)
        formatted_items = [contained_item[1] for contained_item in items_contained]
        items.extend(formatted_items)
    return items


def get_all_classes(module):
    return get_all(module, inspect.isclass)


def get_all_funcs(module):
    return get_all(module, inspect.isfunction)
