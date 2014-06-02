import ez_setup
ez_setup.use_setuptools()
from setuptools import setup, find_packages
import sys
import windriver

setup(
    name = "askbot_log",
    version = askbot_log.__version__,#remember to manually set this correctly
    description = 'Log post activity of watched users',
    packages = find_packages(),
    author = 'Evgeny.Fadeev',
    author_email = 'evgeny.fadeev@gmail.com',
    url = 'http://askbot.com',
    include_package_data = True,
)
