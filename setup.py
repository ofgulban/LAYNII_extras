"""PyLAYNII setup.

To install, using the command line do:
    pip install -e /path/to/PyLAYNII

Notes for PyPI:
python setup.py sdist upload -r pypitest
python setup.py sdist upload -r pypi

"""

from setuptools import setup

setup(
    name='pylaynii',
    description='Layer-MRI analysis in python.',
    version="0.0.0",
    url='https://github.com/ofgulban/PyLAYNII',
    author='Omer Faruk Gulban',
    license='BSD-3-clause',
    packages=['pylaynii'],
    install_requires=['numpy', 'scipy', 'nibabel'],
    zip_safe=True,
    entry_points={
    "console_scripts": [
        "PYLN_LAYER_SMOOTH = pylaynii.PYLN_LAYER_SMOOTH:main",
        ]}
    )
