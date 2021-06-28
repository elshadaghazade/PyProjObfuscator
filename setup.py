from os import EX_SOFTWARE
from sys import version
from setuptools import setup, find_packages, Extension
# from Cython.Build import cythonize

setup(
    name='PyProjObfuscator',
    version="1.0.0-rc-1",
    description="Python Code Obfuscator",
    ext_modules = [Extension('obfuscator', ['src/obfuscator.c'])],
    packages=find_packages(exclude=('.py3', 'dist', 'build', 'test', 'hello_world', 'src')),
    author='Elshad Aghazade',
    author_email='info@elshadaghazade.com',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    license='MIT',
    entry_points = {
        'console_scripts': ['obfuscate=obfuscate_command.obfuscate:main'],
    }
)