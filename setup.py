from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))

this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md')) as f:
    long_description = f.read()

about = {}
with open(os.path.join(here, 'adapy', '__version__.py'), 'r') as f:
    exec(f.read(), about)

setup(
    name='adapy',
    version=os.getenv('BUILD_VERSION', about['__version__']),
    description='Python library for the ada REST API',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='khanhct',
    author_email='trongkhanh.chu@gmail.com',
    url='https://github.com/KhanhCT/adapy',
    packages=find_packages(),
    test_suite='nose.collector',
    install_requires=[
        'requests',
        'base58>=1.0.3',
        'ecdsa',
        'colander',
        'pytz',
        'six',
        'pyyaml',
    ],
    entry_points={
    })