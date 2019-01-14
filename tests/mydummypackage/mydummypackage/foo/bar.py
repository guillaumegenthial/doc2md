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

__author__ = "Guillaume Genthial"


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

    def my_method2(self, y: int) -> int:
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
        """Private methods won't be displayed

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
        """Some property of my class

        Returns
        -------
        int
            The value of the attribute x
        """
        return self.x
