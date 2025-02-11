from setuptools import setup, find_packages

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

__version__ = "2.0.1"

setup(
    name='python-redis-cache',
    version=__version__,
    description='Basic Redis caching for functions',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='http://github.com/taylorhakes/python-redis-cache',
    author='Taylor Hakes',
    license='MIT',
    python_requires='>=3.7',
    packages=find_packages(),
    setup_requires=['pytest-runner==5.3.1'],
    tests_require=['pytest==6.2.5', 'redis==3.5.3'],
)
