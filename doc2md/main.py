"""Entry point of doc2md

`doc2md` is a command-line tool that allows you to build
simple markdown files from any python package.

__Get Started__

Make sure you are in a python environment where your package is
installed.

Then, run

```
doc2md PACKAGE_NAME -o OUTPUT_DIR
```

"""

__author__ = "Guillaume Genthial"

import argparse
import inspect
from pathlib import Path
import pkgutil
import re
from typing import List

from numpydoc.docscrape import NumpyDocString


VSPACE = '\n\n<br/>\n\n'
DELIMITER = '\n---\n'


def parse_arguments():
    """Parse arguments from command line"""
    parser = argparse.ArgumentParser()
    parser.add_argument('package')
    parser.add_argument('-o', '--output_dir')
    parser.add_argument('-b', '--base_path', required=False)
    parser.add_argument('-n', '--nested', action='store_true')
    parser.add_argument('-i', '--include_init', action='store_true')
    arguments = parser.parse_args()
    return arguments


def list_submodules(list_name: List, package_name):
    """Recursively explore module in package name

    Parameters
    ----------
    list_name : List
        Empty list that will contain the list of module names
    package_name : python package
        Imported module
    """
    for _, module_name, is_pkg in pkgutil.walk_packages(
            package_name.__path__, package_name.__name__ + '.'):
        list_name.append(module_name)
        module_name = __import__(module_name, fromlist='dummylist')
        if is_pkg:
            list_submodules(list_name, module_name)


def module_to_path(module, base_path: str, nested: bool):
    filename = '{}.py'.format(str(module).replace('.', '/'))
    if not nested:
        return '/'.join(['.', base_path, filename])
    else:
        nlevelup = len(module.split('.')) - 2
        return '/'.join(['.'] + ['..'] * nlevelup + [base_path, filename])


def camel_to_snake(s):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', s)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


def replace_links(doc, module, nested):
    """Replace cross reference links `@@package.foo.bar`"""
    if not doc:
        return doc

    def my_sub_fn(match):
        group = match.group(1)
        if nested:
            nlevelup = len(module.split('.')) - 2
            rel_path = '/'.join([
                '/'.join(['.'] + ['..'] * nlevelup),
                '/'.join(group.split('.')[1:])])
        else:
            rel_path = './' + '.'.join(group.split('.')[1:])
        return '[{}]({}.md)'.format(group, rel_path)

    pattern = r'@@([^\s]*)'
    return re.sub(pattern, my_sub_fn, doc)


def parse_docstring(doc: str, module: str, nested: bool) -> str:
    """Parse docstring and returns formatted markdown

    Parameters
    ----------
    doc : str
        The docstring of a python object

    Returns
    -------
    str
        Formatted markdown
    """
    lines = []
    if not doc:
        return ''
    doc = replace_links(doc, module, nested)
    doc = NumpyDocString(doc)

    if doc.get('Summary'):
        lines.append('{}'.format('\n'.join(doc['Summary'])))
        lines.append('')

    if doc.get('Extended Summary'):
        lines.append('{}'.format('\n'.join(doc['Extended Summary'])))
        lines.append('')

    if doc.get('Examples'):
        lines.append('__Examples__\n\n')
        lines.extend(doc['Examples'])
        lines.append('')

    if doc.get('Attributes'):
        lines.append('__Attributes__\n\n')
        for name, dtype, description in doc['Attributes']:
            lines.append('- `{}` (`{}`): {}'.format(
                name, dtype, '\n\t'.join(description)))
            lines.append('')

    if doc.get('Parameters'):
        lines.append('__Args__\n\n')
        for name, dtype, description in doc['Parameters']:
            lines.append('- `{}` (`{}`): {}'.format(
                name, dtype, '\n\t'.join(description)))
            lines.append('')

    if doc.get('Returns'):
        lines.append('__Returns__\n\n')
        for name, dtype, description in doc['Returns']:
            lines.append('- `{}`: {}'.format(
                name, '\n'.join(description)))
            lines.append('')

    return '\n'.join(lines)


def parse_function_docstring(function, module, nested, level=0) -> str:
    """Parse function docstring and return formated markdown

    An example would be

    ```python
    def my_function(x: int) -> int:
        return 2 * x

    print(parse_function_docstring(my_function))
    ```

    Parameters
    ----------
    function : python function
        Imported function to convert

    Returns
    -------
    str
        Formated markdown documentation of the function
    """
    title = '`{}`'.format(function.__name__)
    identifier = title.lower().replace('_', '-')
    size = '#' * (3 + level)
    lines = [
        '<a id="{}"></a>'.format(identifier),
        '{} {}'.format(size, title),
        DELIMITER,
        '`{}{}`'.format(function.__name__, str(inspect.signature(function))),
        '',
        parse_docstring(inspect.getdoc(function), module, nested)]

    return [(level, title, identifier)], '\n'.join(lines)


def parse_class_docstring(cls, module, nested, level=0) -> str:
    """Parse class docstring and return formated markdown

    Parameters
    ----------
    cls : python class
        Imported class to convert

    Returns
    -------
    str
        Formated markdown documentation of the class
    """
    title = '*class* `{}`'.format(cls.__name__)
    signature = str(inspect.signature(cls.__init__))
    identifier = camel_to_snake(cls.__name__).replace('_', '-')
    size = '#' * (3 + level)

    lines = [
        '<a id="{}"></a>'.format(identifier),
        '{} {}'.format(size, title),
        DELIMITER,
        '```python',
        '__init__{}'.format(signature),
        '```',
        parse_docstring(inspect.getdoc(cls), module, nested)
    ]

    tocs = [(level, title, identifier)]
    for attr_name, attr in cls.__dict__.items():
        if attr_name.startswith('_') and attr_name not in {'__call__'}:
            continue
        if inspect.isfunction(attr):
            fn_tocs, fn_doc = parse_function_docstring(
                attr, module, nested, level=1)
            lines.append(fn_doc)
            tocs.extend(fn_tocs)

    return tocs, '\n'.join(lines)


def format_toc(toc) -> str:
    """Format toc to markdown

    Parameters
    ----------
    toc : List[Tuple[str]]
        Each tuple is name / id of a markdown object
    """
    lines = []
    for level, name, identifier in toc:
        lines.append('{}* [{}](#{})'.format('\t' * level, name, identifier))
    return '\n'.join(lines)


def parse_module_docstring(module: str, base_path: str, nested: bool) -> str:
    """Parse module docstring and return formated markdown

    Parameters
    ----------
    module : str
        Module name to parse
    base_path : str
        Base path for relative imports
    nested : bool
        If true, docs dir structures follows package's

    Returns
    -------
    str
        Formated markdown documentation of the module
    """
    # Import module, functions and classes
    imported_module = __import__(module, fromlist="dummy")
    rel_path = module_to_path(module, base_path, nested)
    functions = [m[1] for m in inspect.getmembers(imported_module,
                                                  inspect.isfunction)
                 if m[1].__module__ == module]
    classes = [m[1] for m in inspect.getmembers(imported_module,
                                                inspect.isclass)
               if m[1].__module__ == module]
    doc = replace_links(imported_module.__doc__, module, nested)

    # Parse module docstring
    if not doc:
        header = ''
        intro = ''
    else:
        general = doc.split('\n')
        if len(general) >= 2:
            header = general[0]
            intro = '\n'.join(general[1:])
        else:
            header = doc
            intro = ''

    # Parse function docstrings
    content = []
    tocs = []
    for cls in classes:
        if cls.__name__.startswith('_'):
            # Private
            continue
        cls_tocs, cls_doc = parse_class_docstring(cls, module, nested)
        tocs.extend(cls_tocs)
        content.append(cls_doc)

    for function in sorted(functions, key=lambda fn: fn.__name__):
        if function.__name__.startswith('_'):
            # Private
            continue
        fn_tocs, fn_doc = parse_function_docstring(function, module, nested)
        tocs.extend(fn_tocs)
        content.append(fn_doc)

    lines = [
        '# `{}`'.format(module),
        'Defined in [{}.py]({})'.format(module, rel_path)
    ]

    if header:
        lines.append(header)
    if tocs:
        lines.extend([
            format_toc(tocs),
            VSPACE
        ])
    if intro:
        lines.extend([
            '__Overview__',
            intro,
            VSPACE
        ])
    if content:
        lines.append(VSPACE.join(content))

    return '\n\n'.join(lines)


def is_init_module(module):
    init = '__init__.py'
    return Path(__import__(module, fromlist="dummy").__file__).name == init


def main():
    """Parses the arguments and build the documentation"""
    # Parse options, load package, create output directory
    args = parse_arguments()
    package = __import__(args.package)
    output_dir = args.output_dir
    base_path = '..' if not args.base_path else args.base_path
    nested = args.nested
    include_init = args.include_init
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    # Get list of modules
    package_modules = []
    list_submodules(package_modules, package)

    # For each module write markdown file in output directory
    for module in package_modules:
        if not include_init and is_init_module(module):
            continue
        markdown = parse_module_docstring(module, base_path, nested)
        separator = '/' if nested else '.'
        name = separator.join(module.split('.')[1:])
        Path(output_dir, name + '.md').parent.mkdir(
            exist_ok=True, parents=True)
        with Path(output_dir, name + '.md').open('w') as file:
            file.write(markdown)
