# doc2md

[![Build Status](https://travis-ci.org/guillaumegenthial/doc2md.svg?branch=master)](https://travis-ci.org/guillaumegenthial/doc2md)

`doc2md` is a __simple__ tool that allow you to automatically build `.md` files to document a python package.

Nothing more, nothing less.

See the [example package](./tests/mydummypackage/) and its [documentation produced by `doc2md`](./tests/mydummypackage/docs/)

<!-- MarkdownTOC -->

* [Install](#install)
    - [With pip](#with-pip)
    - [Editable mode](#editable-mode)
* [Getting Started](#getting-started)
    - [Usage](#usage)
    - [Example](#example)
    - [Docstring examples](#docstring-examples)
* [Relevant links](#relevant-links)

<!-- /MarkdownTOC -->


It supports __plain markdown docstrings__ as well as __NumPy__-style docstring.

For each module in your package, it creates a markdown file with

- module level docstring
- classes and public methods docstrings
- function docstrings

It automatically adds links back to the code and allows cross-references between modules markdown files (see below).

<a id="install"></a>
## Install

You need `python>=3.5.2`.


<a id="with-pip"></a>
### With pip

```
pip install git+https://github.com/guillaumegenthial/doc2md.git
```

<a id="editable-mode"></a>
### Editable mode

```
git clone git@github.com:guillaumegenthial/doc2md.git
cd doc2md
make install
```

<a id="getting-started"></a>
## Getting Started

<a id="usage"></a>
### Usage

```
doc2md PACKAGE_NAME -o OUTPUT_DIR
```

Typically, if your repo looks like

```
setup.py
requirements.txt
mypackage/
    __init__.py
    foo.py
    bar.py
docs/
```

Simply do

```
doc2md mypackage -o docs -b ../
```

> The `-b` option lets you specify the relative path from the documentation to the code. The default is `../` (one level up from the `docs` folder).

your repo will look like

```
setup.py
requirements.txt
mypackage/
    __init__.py
    foo.py
    bar.py
docs/
    mypackage.foo.md
    mypackage.bar.md
```


<a id="example"></a>
### Example

To test locally,

1. Clone the repo and install `doc2md`
    ```
    git clone git@github.com:guillaumegenthial/doc2md.git
    cd doc2md
    make install
    ```
2. Place yourself in `tests/` and install the provided `mydummypackage` with
    ```
    cd tests/mydummypackage
    pip install -e .
    ```
3. Produce the documentation
    ```
    doc2md mydummypackage -o my-docs -b ../
    ```

<a id="docstring-examples"></a>
### Docstring examples

Support plain Markdown and NumPy-style docstring.

You can add references to other module's documentation with `@@path.to.module`.

#### Module

```python
    """This is a short one line description of this module

    Now, some plain markdown for the module level docstring

    Here is a link to another module @@mydummypackage.bar

    Here is an *example* of how to __use__ it

    Examples
    --------

    ```python
    from mydummypackage.bar import dummy_function
    dummy_function(1, 1)  # Returns 2
    ```

    Simple isn't it?
    """


    def some_function_of_my_module():
        pass
```

<a id="function"></a>
#### Function

```python
    def dummy_function(x: int, y: int) -> int:
        """A short one line description of this function

        Now, you can add some plain markdown that explains the usage of
        this function in more details.

        Here is an *example* of how to __use__ it

        Examples
        --------
        Here is a code snippet

        ```python
        x = 1
        y = 1
        assert dummy_function(x, y) == x + y
        ```

        Parameters
        ----------
        x : int
            A short one line description of this argument.

            You can provide more details here.
        y : int
            A short one line description of this argument.

        Returns
        -------
        int
            The sum of the 2 inputs
        """
        return x + y
```

<a id="class"></a>
#### Class


```python

    class MyDummyClass:
        """This is a short one line description of this class

        Now, some plain markdown for more information.

        Here is an *example* of how to __use__ it

        ```python
        from mydummypackage.bar import dummy_function
        dummy_function(1, 1)  # Returns 2
        ```

        Examples
        --------
        You can also write your examples under the `Examples` section.

        This is a first example
        ```python
        from mydummypackage.bar import dummy_function
        dummy_function(1, 1)  # Returns 2
        ```

        Attributes
        ----------
        x : int
            Some description of this attribute.

            Some longer description of this attribute.
        """

        def __init__(self, x: int):
            self.x = x

        def my_method(self, y: int) -> int:
            """This is a one line description of this method

            Parameters
            ----------
            y : int
                Some integer that we want to increment by x.

            Returns
            -------
            int
                The sum of y and self.x
            """
            return self.x + y

        def _my_private_method(self, y: int) -> int:
            """Private methods won't be added to the doc.

            Parameters
            ----------
            y : int
                Some integer that we want to increment by x.

            Returns
            -------
            int
                The sum of y and self.x
            """
            return self.x + y

        @property
        def my_property(self):
            """Some property of my class, won't be added to the doc.

            Not supported yet.

            Returns
            -------
            int
                The value of the attribute x
            """
            return self.x
```



<a id="relevant-links"></a>
## Relevant links

- [pydoc-markdown](https://github.com/NiklasRosenstein/pydoc-markdown/): built on top of pydoc.
- [keras `autogen.py` script](https://github.com/keras-team/keras/blob/master/docs/autogen.py): an inspiration for this project.

