'''
Created on Aug 4, 2021

@author: maltaweel
'''
"""Setup for the chocobo package."""

import setuptools


with open('README.md') as f:
    README = f.read()

setuptools.setup(
    author="Mark Altaweel",
    author_email="m.altaweel@ucl.ac.uk",
    name='MaskUAV',
    license="MIT",
    description='MaskUAV is a python package used to annotate, train, and segment imagery using the Mask RCNN algorithm.',
    version='v1.0',
    long_description=README,
    url='https://github.com/maltaweel/Mask_RCNN_UAV',
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    install_requires=['requests'],
    classifiers=[
        # Trove classifiers
        # (https://pypi.python.org/pypi?%3Aaction=list_classifiers)
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
    ],
)