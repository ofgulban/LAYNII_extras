"""Compoda setup.

To install, using the command line do:
    pip install -e /path/to/PyLAYNII

Notes for PyPI:
python setup.py sdist upload -r pypitest
python setup.py sdist upload -r pypi

"""

from setuptools import setup

VERSION = '0.0.0'

setup(name='pylaynii',
      version=VERSION,
      description='LAYNII in python.',
      url='https://github.com/ofgulban/compoda',
      download_url=('https://github.com/ofgulban/pylaynii/archive/'
                    + VERSION + '.tar.gz'),
      author='Omer Faruk Gulban',
      author_email='faruk.gulban@maastrichtuniversity.nl',
      license='BSD-3-clause',
      packages=['compoda'],
      install_requires=['numpy', 'scipy', 'nibabel'],
      zip_safe=False)
