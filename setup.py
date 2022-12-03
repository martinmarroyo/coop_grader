import coop_grader
from setuptools import setup

setup(
    name = 'coop_grader',
    version = coop_grader.__version__,
    author = 'Martin Arroyo',
    author_email = 'captmarroyo@coopcareers.org',
    packages = ['coop_grader'],
    install_requires = ['pyyaml']
)