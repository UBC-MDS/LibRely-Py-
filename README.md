# scriptme

### Collaborators
| Name | GitHub handle |
| ---- | ------ |
| Alex Hope | [@ehhope ]( https://github.com/ehhope) |
| Zixin Zhang     | [@zxzzhangg](https://github.com/zxzzhangg) |
| Aaron Quinton     | [@aaronquinton](https://github.com/aaronquinton ) |


## Overview
The `scriptme` package is designed to provide a meta analysis on R or Python scripts to aid in the workflow for a data science or software development project. The functionalities in this package interpret scripts to compile library/module dependancies and prepare summary documentation.

The user can use `scriptme` to better understand the packages used in a script authored by someone else. Alternatively a user can take advantage of the functionalities when preparing the ReadMe documentation in their project. The following functions are included in the `scriptme` package.
- `findme()`: Find and list the libraries/modules used in the script passed as an argument
- `countme()`: Count the functions used and detail their corresponding libraries/packages
- `writeme()`: Prepare a markdown file describing the script dependacies and their popularity. This output is designed to be included in a user's supporting ReadMe file.


### Python/R ecosystems

- **Python**: We were not able to find any Python software packages that address the same functionality as we intend to with ```scriptme```, however, a package called [meta_func](https://pypi.org/project/meta_func/) does keep track of metadata about function use in a given script you examine.

- **R**: We haven't found any R software packages that offer the same functionality either. In R, the [tidyverse/stringr](https://stringr.tidyverse.org/index.html) package has a similar use case for text scraping, but this is not deployed in a broader sense to convey the details of a script.
