# setup file for nimLib
import setuptools
from nimporter import get_nim_extensions, WINDOWS, MACOS, LINUX

setuptools.setup(
    name='nimmedPy',
    version="0.1.0",
    author='ESUme-beep',
    url="https://github.com/ESUme-beep/nimmedPy",
    description="Small personal nim library to speed up python projects",
    install_requires=['nimporter'],
    py_modules=['nimmedPy.py'],
    ext_modules=get_nim_extensions(platforms=[WINDOWS, LINUX, MACOS])
)