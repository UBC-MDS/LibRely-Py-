# LibRely (Python)

### Collaborators
| Name | GitHub Handle |
| ---- | ------ |
| Alex Hope | [@ehhope ]( https://github.com/ehhope) |
| Zixin Zhang     | [@zxzzhangg](https://github.com/zxzzhangg) |
| Aaron Quinton     | [@aaronquinton](https://github.com/aaronquinton ) |


### Install LibRely
To install ```LibRely``` on your own device using ```pip```, type this in your terminal:

```pip install git+https://github.com/UBC-MDS/LibRely-Py-.git```


### Releases

[Milestone 1 Release](https://github.com/UBC-MDS/LibRely-Py-/releases/tag/V1.0)
[Milestone 2 Release](https://github.com/UBC-MDS/LibRely-Py-/tree/2.0)


### Overview
The `LibRely` package is designed to provide a meta analysis of Python scripts to aid with data science workflows and software development projects. The functionalities in this package interpret scripts to compile library/module dependencies, document specific functions imported in the script and measure the length of the script by the number of lines and characters.

The user can use `LibRely` to better understand the packages used in a script authored by someone else. Alternatively, a user can take advantage of the functionalities when preparing the ReadMe documentation in their project. The following functions are included in the `LibRely` package.

`lib_search()`

- Input parameter(string): a file path to the script
- Output parameter(list): a list of dependencies
- Function purpose: It finds and lists the libraries/modules used in the script passed as an argument

`lib_count()`

- Input parameter(string): a file path to the script
- Output parameter(tuple): A tuple of two lists, 1) dependencies 2) functions
- Function purpose: It counts the functions used in the script and detail the libraries/packages contained

`lib_lines()`

 - Input parameter(string): a file path to the script
 - Output parameter(print statements): a list of two numbers, one for the number of lines and one for the number of characters
 - Function purpose: It counts the number of lines and characters of the script

### Usage

- To use the ```LibRely``` package in python, you can integrate the entire package by writing into your editor/notebook:

``` import librely```

- If you are interested in only using a specific function within the ```LibRely``` package such as ```lib_count``` (to return the dependencies and functions in a script) you can call it specifically by writing in your editor/notebook:

``` from librely.lib_count import lib_count```

### Branch Coverage Test
You can go to `librely/tests` and run the following command lines in terminal
```
coverage run -m --branch pytest -q test_lib_search.py test_lib_count.py test_lib_lines.py
coverage report -m
```
The results are shown below.
![](./doc/coverage_result.png)

### Test result
To test all the tests function, we run `pytest` in terminal.  
The results are shown below.
![](./doc/test_result.png)

### Python Ecosystem

- **Python**: We were not able to find any Python software packages that address the same functionality as we intend to with ```LibRely```, however, a package called [meta_func](https://pypi.org/project/meta_func/) does keep track of metadata about function use in a given script you examine.

#### Package Fit
Due to the lack of python packages available for analyzing script qualities, we feel LibRely has something unique to offer the Python ecosystem. It grants quick access to relevant information about the contents of scripts and offers insight into the actions being performed. If anyone wants to get a sense of a longer pipeline, they can simply import LibRely and use it's distinct functions on different scripts that may be linked together in a pipeline. For these reasons, we feel LibRely is an interesting and useful package for the user and a meaningful addition to the Python ecosystem.
