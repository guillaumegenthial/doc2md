"""This is a short one line description of this module

Now, some plain markdown for the module level docstring

Here is a link to another module @@mydummypackage.foo.bar

Here is an *example* of how to __use__ it

Examples
--------
Here is some code

```python
from mydummypackage.bar import dummy_function
dummy_function(1, 1)  # Returns 2
```

Simple isn't it?
"""

__author__ = "Guillaume Genthial"


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


def dummy_function2(x: int, y: int) -> int:
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
