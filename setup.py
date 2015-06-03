from setuptools import setup

import os


def Readme():
    return open(os.path.join(os.path.dirname(__file__), 'README.rst'), "r").read()

setup(
    name='stackexchange',
    packages=['stackexchange'],
    version='0.0.1',
    description='Stackexchange API for Python',
    author='plasmashadow',
    author_email='plasmashadowx@gmail.com',
    url='https://github.com/plasmashadow/stackexchange.git',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Intended Audience :: Developers'
    ],
    install_requires = ['requests'],
    include_package_data=True,
    license='MIT License',
)