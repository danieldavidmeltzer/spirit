from setuptools import setup, find_packages

setup(
    name='spirit',
    version='0.1.0',
    author='Daniel Meltzer',
    description='An example package.',
    packages=find_packages(),
    install_requires=['Pillow==7.0.0', 'numpy==1.22.0', 'alabaster==0.7.12',
                      'attrs==19.2.0', 'Babel==2.7.0', 'certifi==2019.9.11',
                      'chardet==3.0.4', 'Click==7.0', 'codecov==2.0.15',
                      'coverage==4.5.4', 'docutils==0.15.2', 'Flask==1.1.1',
                      'idna==2.8', 'imagesize==1.1.0', 'itsdangerous==1.1.0',
                      'Jinja2==2.10.3', 'MarkupSafe==1.1.1',
                      'more-itertools==7.2.0', 'packaging==19.2',
                      'pluggy==0.13.0', 'py==1.8.0', 'Pygments==2.4.2',
                      'pyparsing==2.4.2', 'pytest==5.3.0', 'pytest-cov==2.8.1',
                      'pytz==2019.3', 'requests==2.22.0', 'six==1.13.0',
                      'snowballstemmer==2.0.0', 'Sphinx==2.2.1',
                      'sphinxcontrib-applehelp==1.0.1',
                      'sphinxcontrib-devhelp==1.0.1',
                      'sphinxcontrib-htmlhelp==1.0.2',
                      'sphinxcontrib-jsmath==1.0.1',
                      'sphinxcontrib-qthelp==1.0.2',
                      'sphinxcontrib-serializinghtml==1.1.3',
                      'urllib3==1.25.7', 'wcwidth==0.1.7', 'Werkzeug==0.16.0',
                      'protobuf==3.11.2', 'matplotlib==3.1.2', 'purl==1.5',
                      'pika==1.1.0', 'minio==5.0.7', 'pymongo==3.10.1'],
    tests_require=['Pillow==7.0.0', 'numpy==1.22.0', 'alabaster==0.7.12',
                   'attrs==19.2.0', 'Babel==2.7.0', 'certifi==2019.9.11',
                   'chardet==3.0.4', 'Click==7.0', 'codecov==2.0.15',
                   'coverage==4.5.4', 'docutils==0.15.2', 'Flask==1.1.1',
                   'idna==2.8', 'imagesize==1.1.0', 'itsdangerous==1.1.0',
                   'Jinja2==2.10.3', 'MarkupSafe==1.1.1',
                   'more-itertools==7.2.0', 'packaging==19.2',
                   'pluggy==0.13.0', 'py==1.8.0', 'Pygments==2.4.2',
                   'pyparsing==2.4.2', 'pytest==5.3.0', 'pytest-cov==2.8.1',
                   'pytz==2019.3', 'requests==2.22.0', 'six==1.13.0',
                   'snowballstemmer==2.0.0', 'Sphinx==2.2.1',
                   'sphinxcontrib-applehelp==1.0.1',
                   'sphinxcontrib-devhelp==1.0.1',
                   'sphinxcontrib-htmlhelp==1.0.2',
                   'sphinxcontrib-jsmath==1.0.1',
                   'sphinxcontrib-qthelp==1.0.2',
                   'sphinxcontrib-serializinghtml==1.1.3', 'urllib3==1.25.7',
                   'wcwidth==0.1.7', 'Werkzeug==0.16.0', 'protobuf==3.11.2',
                   'matplotlib==3.1.2', 'purl==1.5', 'pika==1.1.0',
                   'minio==5.0.7', 'pymongo==3.10.1'],
)
