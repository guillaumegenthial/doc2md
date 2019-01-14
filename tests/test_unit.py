# pylint: disable=missing-docstring
"""Some unit tests"""
# TODO: would be nice to add more, even if good integration tests

__author__ = "Guillaume Genthial"

from pathlib import Path

from doc2md.main import replace_links, parse_docstring


def test_replace_links():
    s = 'One @@foo.bar two'
    got = replace_links(s)
    expected = 'One [foo.bar](./foo.bar.md) two'
    assert got == expected


def test_parse_docstring():
    docstring_file = Path(__file__).parent / 'docstring.txt'
    expected_file = Path(__file__).parent / 'expected.txt'
    with Path(expected_file).open() as expected, \
            Path(docstring_file).open() as docstring:
        assert parse_docstring(docstring.read()) == expected.read()
