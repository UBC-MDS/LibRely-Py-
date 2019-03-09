# Feb 8th, 2019
# Zixin Zhang
# This script is the function in Python to find the dependencies used in a .py script


import pandas as pd
import numpy as np

def lib_search(filepath):

    """
    This function takes in a Python script (.py) and returns a dataframe
    containing the libraries within the script

    Parameters
    ----------
    filepath(string): The path to the input .py script

    Return
    ----------
    dependency(list): A list that stores all the dependencies
    """

    dependency=[] #### Set an empty list containing dependencies

    try:
        in_file=open(filepath,"r") ### Open File
        lines = in_file.readlines() ### Read Lines of File

        for line in lines: ### For Loop for Each Line
            thisline=line.split(" ") ### Split Every Word in the Line

            if thisline[0] == 'import': ### If the line starts with 'import'
                edits = thisline[1].replace('\n', '') #### Grab the word after it
                dependency.append(edits) #### Append the word into dependency list
            elif thisline[0] == 'from':
                edits = thisline[1] ##### To Deal with packages where someone imports using 'from'
                dependency.append(edits) ### append the word after 'from' to dependency list

        return dependency

    except FileNotFoundError:
        print("This file was not found")
