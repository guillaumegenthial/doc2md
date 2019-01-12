# `doc2md.main`

Defined in [doc2md.main.py](../doc2md/main.py)


<br/>


Entry point of doc2md

`doc2md` is a command-line tool that allows you to build
simple markdown files from any python package.

### Get Started

Make sure you are in a python environment where your package is
installed.

Then, run

```
doc2md PACKAGE_NAME -o OUTPUT_DIR
```




<br/>


#### list_submodules

---

```python
list_submodules(list_name:List, package_name)
```

Recursively explore module in package name



__Args__


- `list_name` (List): Empty list that will contain the list of module names

- `package_name` (python package): Imported module


<br/>

#### main

---

```python
main()
```

Parses the arguments and build the documentation




<br/>



<br/>

#### parse_arguments

---

```python
parse_arguments()
```

Parse arguments from command line




<br/>

#### parse_function_docstring

---

```python
parse_function_docstring(function) -> str
```

Parse function docstring and return formated markdown

An example would be

```python
def my_function(x: int) -> int:
    return 2 * x

print(parse_function_docstring(my_function))
```

__Args__


- `function` (python function): Imported function to convert

__Returns__


- `str`: Formated markdown documentation of the function


<br/>

#### parse_module_docstring

---

```python
parse_module_docstring(module, base_path:str=None) -> str
```

Parse module docstring and return formated markdown



__Args__


- `module` (python module): Imported module containing code and docstring, to parse

- `base_path` (str, optional): Base path for relative imports

__Returns__


- `str`: Formated markdown documentation of the module
