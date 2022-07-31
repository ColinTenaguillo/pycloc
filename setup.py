from distutils.core import setup

setup(
    name='pycloc',
    version='1.0',
    description='Python implementation of the cloc command.',
    author='Colin Tenaguillo',
    author_email='tenaguillo.c@gmail.com',
    packages=['distutils', 'distutils.command'],
)