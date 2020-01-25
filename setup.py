from setuptools import setup, find_packages


setup(
    name = 'spirit',
    version = '0.1.0',
    author = 'Daniel Meltzer',
    description = 'An example package.',
    packages = find_packages(),
    install_requires = ['click', 'flask'],
    tests_require = ['pytest', 'pytest-cov'],
)
