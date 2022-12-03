import coop_grader
from setuptools import setup, find_packages

setup(
    name = 'coop_grader',
    version = coop_grader.__version__,
    author = 'Martin Arroyo',
    author_email = 'captmarroyo@coopcareers.org',
    packages = find_packages(),
    install_requires = ['pyyaml']
)