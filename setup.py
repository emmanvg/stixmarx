# Copyright (c) 2017, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from os.path import abspath, dirname, join
from setuptools import setup, find_packages

CUR_DIR = dirname(abspath(__file__))
INIT_FILE = join(CUR_DIR, 'stixmarx', '__init__.py')
VERSION_FILE = join(CUR_DIR, 'stixmarx', 'version.py')


def get_version():
    with open(VERSION_FILE) as f:
        for line in f:
            if not line.startswith("__version__"):
                continue

            version = line.split()[-1].strip('"')
            return version

        raise AttributeError("Package does not have a __version__")


with open('README.rst') as f:
    readme = f.read()


requirements = [
    'lxml',
    'mixbox>=1.0.2',
    'stix>=1.1.1.8,<1.2.1.0'
]


setup(
    name="stixmarx",
    version=get_version(),
    author="The MITRE Corporation",
    author_email="stix@mitre.org",
    description="A data marking API for STIX 1 content.",
    long_description=readme,
    url="http://stixproject.github.io/",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ]
)
