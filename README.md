# LibRely (Python)

### Collaborators
| Name | GitHub Handle |
| ---- | ------ |
| Alex Hope | [@ehhope ]( https://github.com/ehhope) |
| Zixin Zhang     | [@zxzzhangg](https://github.com/zxzzhangg) |
| Aaron Quinton     | [@aaronquinton](https://github.com/aaronquinton ) |


### Releases

[Milestone 1 Release](https://github.com/UBC-MDS/LibRely-Py-/releases/tag/V1.0)

### Overview
The `LibRely` package is designed to provide a meta analysis of Python scripts to aid with data science workflows and software development projects. The functionalities in this package interpret scripts to compile library/module dependencies, document specific functions imported in the script and measure the length of the script by the number of lines and characters.

The user can use `LibRely` to better understand the packages used in a script authored by someone else. Alternatively, a user can take advantage of the functionalities when preparing the ReadMe documentation in their project. The following functions are included in the `LibRely` package.

`lib_search()`

- Input parameter(string): a file path to the script
- Output parameter(list): a list of dependencies
- Function purpose: It finds and lists the libraries/modules used in the script passed as an argument

`lib_count()`

- Input parameter(string): a file path to the script
- Output parameter(dataframe): A tuple of two lists, 1) dependencies 2) functions
- Function purpose: It counts the functions used in the script and detail the libraries/packages contained

 `lib_lines()`

 - Input parameter(string): a file path to the script
 - Output parameter(print statements): a list of two numbers, one for # of lines and one for # of characters
 - Function purpose: It counts the number of lines and characters of the script


### Python Ecosystem

- **Python**: We were not able to find any Python software packages that address the same functionality as we intend to with ```LibRely```, however, a package called [meta_func](https://pypi.org/project/meta_func/) does keep track of metadata about function use in a given script you examine. 

Due to the lack of available libraries we feel LibRely has something unique to offer the Python ecosystem in addition to the user. It allows for quick access to potentially interesting information about scripts. If someone wants to quickly understand a pipeline, they can simply import LibRely and use it's distinct functions to learn about what functions may be contained in the script and what dependencies were called. In analysis pipelines with multiple scripts, this is valuable information. For these reasons, we feel LibRely is an interesting and useful package in the Python environment.

