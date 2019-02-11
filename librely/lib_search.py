# Feb 8th, 2019
# Zixin Zhang
# This script is the function in Python to find the dependencies used in a .py script


import pandas as pd
import numpy as np


def lib_search(input_path):

    """
    This function takes in a Python script (.py) and returns a dataframe
    containing the libraries and functions within the script as well as a
    use-count of the functions

    Parameters
    ----------
    input_path(string): The path to the input .py script

    Return
    ----------
    depen_func_dataframe(DataFrame): A DataFrame that stores all the dependencies, functions
    and function counts
    """

    dependency=[] #### Set an empty list containing dependencies
    in_file=open(filepath,"r") ### Open File

    lines = in_file.readlines() ### Read Lines of File

    for line in lines: ### For Loop for Each Line
        thisline=line.split(" ") ### Split Every Word in the Line

        if thisline[0] == 'import': ### If the line starts with 'import'
            edits = thisline[1].replace('\n', '') #### Grab the word after it
            dependency.append(edits) #### Append the word into dependency list

    return dependency
