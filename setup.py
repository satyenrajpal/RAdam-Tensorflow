import os
import re
import codecs
from setuptools import setup, find_packages

current_path = os.path.abspath(os.path.dirname(__file__))


def read_file(*parts):
    with codecs.open(os.path.join(current_path, *parts), 'r', 'utf8') as reader:
        return reader.read()


def get_requirements(*parts):
    with codecs.open(os.path.join(current_path, *parts), 'r', 'utf8') as reader:
        return list(map(lambda x: x.strip(), reader.readlines()))


setup(
    name='tf-1.x-rectified-adam',
    version=0.1,
    packages=find_packages(),
    url='https://github.com/satyenrajpal/RAdam-Tensorflow',
    license='MIT',
    author='Satyen Rajpal',
    author_email='satyen.2.rajpal@gmail.com',
    description='RAdam implemented in Tensorflow 1.x',
    long_description=read_file('README.md'),
    long_description_content_type='text/markdown',
    install_requires=get_requirements('requirements.txt'),
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)