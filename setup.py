import ez_setup
ez_setup.use_setuptools()
from setuptools import setup, find_packages
import sys

setup(
    name = "request_logging",
    version = '0.1.0',
    description = 'Log requests in the database for the diagrostic purposes',
    packages = find_packages(),
    author = 'Evgeny.Fadeev',
    author_email = 'evgeny.fadeev@gmail.com',
    url = 'http://askbot.com',
    include_package_data = True,
)
