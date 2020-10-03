from typing import Tuple

from setuptools import setup
from setuptools import find_packages


requirements: Tuple[str, ...] = (
    'setuptools',
    'numpy',
    'scikit-image',
    'opencv-python',
    'torch',
    'torchvision',
)


setup(
    name='quadratum',
    version='0.2.1',
    license='MIT',
    author='Jamie Seol',
    author_email='theeluwin@gmail.com',
    url='https://github.com/theeluwin/pytorch-quadratum',
    description='Additional torchvision image transforms for practical usage.',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    classifiers=[]
)
