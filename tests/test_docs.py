"""Tests that output is the same as expected"""

__author__ = "Guillaume Genthial"

from pathlib import Path


EXPECTED = 'tests/mydummypackage/docs'
GOT = 'tests/mydummypackage/test-docs'
FILES = [
    'mydummypackage.bar.md',
    'mydummypackage.foo.bar.md',
    'mydummypackage.foo.md'
]


def test_docs():
    for file in FILES:
        with Path(EXPECTED, file).open() as expected, \
             Path(GOT, file).open() as got:
            assert expected.read() == got.read()
