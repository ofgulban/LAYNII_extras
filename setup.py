"""PyLAYNII setup.

Notes for development installation
==================================
To install for development, using the commandline do:
    pip install -e /path/to/PyLAYNII

Notes for PyPI:
===============
1. Prepare for pypi:
```python setup.py sdist```
2. Upload to pypi test server to check:
```twine upload --repository-url https://test.pypi.org/legacy/ dist/*```
3. Use testpypi with pip:
```pip install --index-url https://test.pypi.org/simple/ pylaynii```
4. Upload to pypi:
```twine upload dist/*```
"""

from setuptools import setup

setup(
    name='pylaynii',
    description='Layer-MRI analysis in python.',
    license='BSD-3-clause',
    version="0.1.0",
    url='https://github.com/ofgulban/PyLAYNII',
    author='Omer Faruk Gulban',
    author_email='faruk.gulban@maastrichtuniversity.nl',
    packages=['pylaynii'],
    install_requires=['numpy', 'scipy', 'nibabel'],
    keywords=["mri", "nifti", "layer"],
    zip_safe=True,
    entry_points={
    "console_scripts": [
        "PYLN_LAYER_SMOOTH = pylaynii.PYLN_LAYER_SMOOTH:main",
        ]},
    )
