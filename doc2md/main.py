"""Entry point of doc2md

`doc2md` is a command-line tool that allows you to build
simple markdown files from any python package.

### Get Started

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
from typing import List

from numpydoc.docscrape import NumpyDocString


VSPACE = '\n\n<br/>\n\n'
DELIMITER = '\n---\n'


class Dummy:
    """My class docstring"""

    def my_method(self):
        """My method docstring"""
        pass


def parse_arguments():
    """Parse arguments from command line"""
    parser = argparse.ArgumentParser()
    parser.add_argument('package')
    parser.add_argument('-o', '--output_dir')
    parser.add_argument('-b', '--base_path', required=False)
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


def module_to_path(import_str, base_path: str = None):
    if base_path is None:
        base_path = './'
    return '{}{}.py'.format(base_path, str(import_str).replace('.', '/'))


def parse_function_docstring(function) -> str:
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
    name = function.__name__
    signature = str(inspect.signature(function))

    raw_doc = inspect.getdoc(function)
    if raw_doc:
        doc = NumpyDocString(raw_doc)
    else:
        return ''
    # print(doc["Summary"])
    # print(doc['Extended Summary'])
    # print(doc["Parameters"])
    # print(doc["Attributes"])
    # print(doc["Methods"])

    lines = [
        '#### {}'.format(name),
        DELIMITER,
        '```python',
        '{}{}'.format(name, signature),
        '```',
        '',
        '{}'.format('\n'.join(doc['Summary'])),
        '',
        '{}'.format('\n'.join(doc['Extended Summary'])),
        '',
        ]

    if doc['Parameters']:
        lines.append('__Args__\n\n')
        for name, dtype, description in doc['Parameters']:
            lines.append('- `{}` ({}): {}\n'.format(
                name, dtype, '\n'.join(description)))
    if doc['Returns']:
        lines.append('__Returns__\n\n')
        for name, dtype, description in doc['Returns']:
            lines.append('- `{}`: {}\n'.format(
                name, '\n'.join(description)))

    return '\n'.join(lines)


def parse_module_docstring(module, base_path: str = None) -> str:
    """Parse module docstring and return formated markdown

    Parameters
    ----------
    module : python module
        Imported module containing code and docstring, to parse
    base_path : str, optional
        Base path for relative imports

    Returns
    -------
    str
        Formated markdown documentation of the module
    """
    # Import module, functions and classes
    module = __import__(module, fromlist="dummy")
    rel_path = module_to_path(module.__name__, base_path)
    functions = [m[1] for m in inspect.getmembers(module, inspect.isfunction)
                 if m[1].__module__ == module.__name__]
    classes = [m[1] for m in inspect.getmembers(module, inspect.isclass)
               if m[1].__module__ == module.__name__]

    # Parse module docstring
    doc = module.__doc__

    if doc is None:
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
    for function in functions:
        content.append(parse_function_docstring(function))

    return '\n'.join([
        '# `{}`'.format(module.__name__),
        '',
        'Defined in [{}.py]({})'.format(module.__name__, rel_path),
        VSPACE,
        header,
        intro,
        VSPACE,
        VSPACE.join(content)
        ])


def main():
    """Parses the arguments and build the documentation"""
    # Parse options, load package, create output directory
    args = parse_arguments()
    package = __import__(args.package)
    output_dir = args.output_dir
    base_path = args.base_path
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    # Get list of modules
    package_modules = []
    list_submodules(package_modules, package)

    # For each module write markdown file in output directory
    for module in package_modules:
        markdown = parse_module_docstring(module, base_path)
        with Path(output_dir, module + '.md').open('w') as file:
            file.write(markdown)
