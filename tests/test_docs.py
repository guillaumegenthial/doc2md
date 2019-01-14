"""Tests that output is the same as expected"""

__author__ = "Guillaume Genthial"

from pathlib import Path


EXPECTED = 'tests/mydummypackage/docs'
GOT = 'tests/mydummypackage/test-docs'
FILES = [
    'bar.md',
    'foo.bar.md',
]

EXPECTED_NESTED = 'tests/mydummypackage/docs-nested'
GOT_NESTED = 'tests/mydummypackage/test-docs-nested'
FILES_NESTED = [
    'bar.md',
    'foo/bar.md',
]


def test_docs():
    for file in FILES:
        with Path(EXPECTED, file).open() as expected, \
             Path(GOT, file).open() as got:
            assert expected.read() == got.read()


def test_docs_nested():
    for file in FILES_NESTED:
        with Path(EXPECTED_NESTED, file).open() as expected, \
             Path(GOT_NESTED, file).open() as got:
            assert expected.read() == got.read()
