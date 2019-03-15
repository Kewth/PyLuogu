from distutils.core import setup

setup(
    name='PyLuogu',
    version='0.9',
    package_dir={'PyLuogu': 'source'},
    packages=['PyLuogu'],
    install_requires=[
        'argparse',
        'bs4',
        'colorama',
        'lxml',
    ],
    )
