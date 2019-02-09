# LibRely (Python)

### Collaborators
| Name | GitHub handle |
| ---- | ------ |
| Alex Hope | [@ehhope ]( https://github.com/ehhope) |
| Zixin Zhang     | [@zxzzhangg](https://github.com/zxzzhangg) |
| Aaron Quinton     | [@aaronquinton](https://github.com/aaronquinton ) |


## Overview
The `scriptme` package is designed to provide a meta analysis on Python scripts to aid in the workflow for a data science or software development project. The functionalities in this package interpret scripts to compile library/module dependancies and prepare summary documentation.

The user can use `scriptme` to better understand the packages used in a script authored by someone else. Alternatively a user can take advantage of the functionalities when preparing the ReadMe documentation in their project. The following functions are included in the `scriptme` package.
- `findme()`: Find and list the libraries/modules used in the script passed as an argument
- `countme()`: Count the functions used and detail their corresponding libraries/packages
- `writeme()`: Prepare a markdown file describing the script dependacies and their popularity. This output is designed to be included in a user's supporting ReadMe file.


### Python/R ecosystems

- **Python**: We haven't found any Python software package that have the same functionality.

- **R**: We haven't found any R software package that have the same functionality. In R, the [tidyverse/stringr](https://stringr.tidyverse.org/index.html) has similar functionality on our purpose of text-scrapping.
