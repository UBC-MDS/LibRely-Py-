# LibRely (Python)

### Collaborators
| Name | GitHub Handle |
| ---- | ------ |
| Alex Hope | [@ehhope ]( https://github.com/ehhope) |
| Zixin Zhang     | [@zxzzhangg](https://github.com/zxzzhangg) |
| Aaron Quinton     | [@aaronquinton](https://github.com/aaronquinton ) |


### Releases

Milestone 1 Release: https://github.com/UBC-MDS/LibRely-Py-/releases/tag/V1.0



## Overview
The `LibRely` package is designed to provide a meta analysis of Python scripts to aid in the workflow for a data science or software development project. The functionalities in this package interpret scripts to compile library/module dependancies, document specific functions imported in the script and measure the length of the script by number of lines and characters.

The user can use `LibRely` to better understand the packages used in a script authored by someone else. Alternatively a user can take advantage of the functionalities when preparing the ReadMe documentation in their project. The following functions are included in the `LibRely` package.
- `lib_search()`: Find and list the libraries/modules used in the script passed as an argument.
- `lib_count()`: Count the modules and functions that are specifically imported into a script.
- `lib_lines()`: Count the number of lines and characters in the script.


### Python Ecosystems

- **Python**: We were not able to find any Python software packages that address the same functionality as we intend to with ```LibRely```, however, a package called [meta_func](https://pypi.org/project/meta_func/) does keep track of metadata about function use in a given script you examine.
