# -*- coding: utf-8 -*-

import sys

from setuptools import find_packages, setup


requirements = [
    'setuptools',
    'numpy',
    'scikit-image',
    'torch',
    'torchvision',
]

setup(
    name='quadratum',
    version='0.1.2',
    license='MIT',
    author='Jamie Seol',
    author_email='theeluwin@gmail.com',
    url='https://github.com/theeluwin/pytorch-quadratum',
    description='Additional torchvision image transforms for practical usage.',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    classifiers=[],
)
