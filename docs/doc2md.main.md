# `doc2md.main`

Defined in [doc2md.main.py](../doc2md/main.py)

Entry point of doc2md

* [camel_to_snake](#camel-to-snake)
* [format_toc](#format-toc)
* [list_submodules](#list-submodules)
* [main](#main)
* [module_to_path](#module-to-path)
* [parse_arguments](#parse-arguments)
* [parse_class_docstring](#parse-class-docstring)
* [parse_docstring](#parse-docstring)
* [parse_function_docstring](#parse-function-docstring)
* [parse_module_docstring](#parse-module-docstring)
* [replace_links](#replace-links)



<br/>



__Overview__


`doc2md` is a command-line tool that allows you to build
simple markdown files from any python package.

__Get Started__

Make sure you are in a python environment where your package is
installed.

Then, run

```
doc2md PACKAGE_NAME -o OUTPUT_DIR
```





<br/>



<a id="camel-to-snake"></a>
### `camel_to_snake`

---

`camel_to_snake(s)`



<br/>

<a id="format-toc"></a>
### `format_toc`

---

`format_toc(toc) -> str`

Format toc to markdown

__Args__


- `toc` (`List[Tuple[str]]`): Each tuple is name / id of a markdown object


<br/>

<a id="list-submodules"></a>
### `list_submodules`

---

`list_submodules(list_name:List, package_name)`

Recursively explore module in package name

__Args__


- `list_name` (`List`): Empty list that will contain the list of module names

- `package_name` (`python package`): Imported module


<br/>

<a id="main"></a>
### `main`

---

`main()`

Parses the arguments and build the documentation


<br/>

<a id="module-to-path"></a>
### `module_to_path`

---

`module_to_path(import_str, base_path:str)`



<br/>

<a id="parse-arguments"></a>
### `parse_arguments`

---

`parse_arguments()`

Parse arguments from command line


<br/>

<a id="parse-class-docstring"></a>
### `parse_class_docstring`

---

`parse_class_docstring(cls, level=0) -> str`

Parse class docstring and return formated markdown

__Args__


- `cls` (`python class`): Imported class to convert

__Returns__


- `str`: Formated markdown documentation of the class


<br/>

<a id="parse-docstring"></a>
### `parse_docstring`

---

`parse_docstring(doc:str) -> str`

Parse docstring and returns formatted markdown

__Args__


- `doc` (`str`): The docstring of a python object

__Returns__


- `str`: Formatted markdown


<br/>

<a id="parse-function-docstring"></a>
### `parse_function_docstring`

---

`parse_function_docstring(function, level=0) -> str`

Parse function docstring and return formated markdown

An example would be

```python
def my_function(x: int) -> int:
    return 2 * x

print(parse_function_docstring(my_function))
```

__Args__


- `function` (`python function`): Imported function to convert

__Returns__


- `str`: Formated markdown documentation of the function


<br/>

<a id="parse-module-docstring"></a>
### `parse_module_docstring`

---

`parse_module_docstring(module, base_path:str) -> str`

Parse module docstring and return formated markdown

__Args__


- `module` (`python module`): Imported module containing code and docstring, to parse

- `base_path` (`str`): Base path for relative imports

__Returns__


- `str`: Formated markdown documentation of the module


<br/>

<a id="replace-links"></a>
### `replace_links`

---

`replace_links(doc)`

