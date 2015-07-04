from setuptools import setup

import os


def Readme():
    return open(os.path.join(os.path.dirname(__file__), 'README.md'), "r").read()

setup(
    name='stackexchange',
    packages=['stackexchange', 'stackexchange/api', 'stackexchange/rest'],
    version='0.0.2',
    description='Stackexchange API for Python',
    long_description= Readme(),
    author='plasmashadow',
    author_email='plasmashadowx@gmail.com',
    url='https://github.com/plasmashadow/stackexchange.git',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Intended Audience :: Developers'
    ],
    install_requires = ['requests', 'six'],
    license='MIT License',
)