from distutils.core import setup
from pycloc import __version__

setup(
    name='pycloc',
    version=__version__,
    description='Python implementation of the cloc command.',
    author='Colin Tenaguillo',
    author_email='tenaguillo.c@gmail.com',
    py_modules=['pycloc'],
    entry_points={
        'console_scripts': ['pycloc=pycloc.__main__:main'],
    },
    requires=["tabulate==0.8.10"]
)