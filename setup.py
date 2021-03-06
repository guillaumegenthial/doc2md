"""Setup Script"""

from distutils.core import setup
import re
from setuptools import find_packages


with open("README.md", "r") as fh:
    long_description = fh.read()


versionfile = open("doc2md/version.py").read()
metadata = dict(re.findall(r"__([a-z]+)__\s*=\s*'([^']+)'", versionfile))

setup(
    name="doc2md",
    version=metadata['version'],
    author=metadata['author'],
    description="Generator of Markdown from docstrings",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=["tests"]),
    classifiers=(
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3 :: Only",
    ),
    python_requires='>=3.5.2',
    install_requires=[
        "numpydoc"
    ],
    entry_points={
        'console_scripts': ['doc2md = doc2md.main:main']
    },
)
