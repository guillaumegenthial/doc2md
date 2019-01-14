# `mydummypackage.foo.bar`

Defined in [mydummypackage.foo.bar.py](./../mydummypackage/foo/bar.py)

This is a short one line description of this module

* [*class* `MyDummyClass`](#my-dummy-class)
	* [`my_method`](#`my-method`)
	* [`my_method2`](#`my-method2`)



<br/>



__Overview__


Now, some plain markdown for the module level docstring

Here is a link to another module [mydummypackage.bar](./bar.md)

Here is an *example* of how to __use__ it

Examples
--------

```python
from mydummypackage.bar import dummy_function
dummy_function(1, 1)  # Returns 2
```

Simple isn't it?




<br/>



<a id="my-dummy-class"></a>
### *class* `MyDummyClass`

---

```python
__init__(self, x:int)
```
This is a short one line description of this class

Now, some plain markdown for more information.

Here is an *example* of how to __use__ it

```python
from mydummypackage.bar import dummy_function
dummy_function(1, 1)  # Returns 2
```

__Examples__


You can also write your examples under the `Examples` section.

This is a first example
```python
from mydummypackage.bar import dummy_function
dummy_function(1, 1)  # Returns 2
```

__Attributes__


- `x` (`int`): Some description of this attribute.
	
	Some longer description of this attribute.

<a id="`my-method`"></a>
#### `my_method`

---

`my_method(self, y:int) -> int`

This is a one line description of this method

__Args__


- `y` (`int`): Some integer that we want to increment by x.

__Returns__


- `int`: The sum of y and self.x

<a id="`my-method2`"></a>
#### `my_method2`

---

`my_method2(self, y:int) -> int`

This is a one line description of this method

__Args__


- `y` (`int`): Some integer that we want to increment by x.

__Returns__


- `int`: The sum of y and self.x
