#!/usr/bin/env python
import os
from setuptools import setup


PKG_NAME = "vim-profiler"
AUTHOR_NAME = "<YOUR-NAME>"
AUTHOR_EMAIL = "<YOUR-EMAIL>"
URL = 'https://github.com/bchretien/vim-profiler'


# Utility function to read the README file.
# Used for the long_description.
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name=PKG_NAME,
      version='0.1',
      description='Utility script to profile (n)vim (e.g. startup times of plugins) ',
      long_description=read('README.md'),
      author=AUTHOR_NAME,
      author_email=AUTHOR_EMAIL,
      maintainer=AUTHOR_NAME,
      maintainer_email=AUTHOR_EMAIL,
      license='GPL-3.0',
      install_requires=("argparse", "matplotlib"),
      python_requires='>2.0',
      url=URL,
      dependency_links=[],
      download_url=URL,
      scripts=['vim-profiler.py', ],
      platforms="Linux",
      data_files=[],
      packages=[])

