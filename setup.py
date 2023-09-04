from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '1.0'
DESCRIPTION = 'Streaming video data via networks'
LONG_DESCRIPTION = 'A package that allows to build simple streams of video, audio and camera data.'

setup(
    name="stride-license",
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[
        "cryptography"
    ]
)