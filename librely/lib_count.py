import pandas as pd
import numpy as np

# Feb 9th, 2019
# Zixin Zhang, Alex Hope, Aaron Quinton
# This script tests the function for lib_count.py
#
# input: a path leads to the .py script
# output: a list that contains all the dependencies

library(pandas)
library(numpy)

def lib_count(input_path):

    """
    This function takes in a Python script (.py) and returns a dataframe
    containing the libraries and functions within the script as well as a
    use-count of the functions

    Parameters
    ----------
    input_path(string): The path to the input .py script

    Return
    ----------
    depen(DataFrame): A DataFrame that stores all the dependencies, functions
    and function counts
    """

    return depen_func_dataframe
