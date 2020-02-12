"""PyLAYNII setup.

Notes for development installation
==================================
To install for development, using the commandline do:
    pip install -e /path/to/PyLAYNII

Notes for PyPI:
===============
1. cd to repository folder
2. ```python setup.py sdist upload -r pypitest```
3. Check everything looks fine on the test server.
4. ```python setup.py sdist upload -r pypi```
"""

from setuptools import setup

setup(
    name='pylaynii',
    description='Layer-MRI analysis in python.',
    license='BSD-3-clause',
    version="0.0.0",
    url='https://github.com/ofgulban/PyLAYNII',
    author='Omer Faruk Gulban',
    packages=['pylaynii'],
    install_requires=['numpy', 'scipy', 'nibabel'],
    keywords=["mri", "nifti", "layer"],
    zip_safe=True,
    entry_points={
    "console_scripts": [
        "PYLN_LAYER_SMOOTH = pylaynii.PYLN_LAYER_SMOOTH:main",
        ]}
    )
