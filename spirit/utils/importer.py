import importlib
import pkgutil


def import_all_submodules(package):
    """
    recursively import submodules of package
    package: name of package to import
    """
    package = importlib.import_module(package)
    modules = {}
    for _, name, is_package in pkgutil.walk_packages(package.__path__):
        package_name = f"{package.__name__}.{name}"
        modules[package_name] = importlib.import_module(package_name)
        if is_package:
            modules.update(import_all_submodules(package_name))
    return modules
