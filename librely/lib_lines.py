# Feb 8th, 2019
# Zixin Zhang


import pandas as pd
import numpy as np

def lib_lines(input_path):

    """
    This function takes an input Python script and returns the number of lines and characters.

    Parameters
    ---------
    input_path(string): the path to the input .py script

    """
    in_file=open(input_path,"r") ### Open File
    lines = in_file.readlines() ### Read Lines of File
    total_lines = len(lines) ### Number of lines
    
    total_char = 0
    for line in lines: ### For Loop for Each Line
        total_char += sum(c.isalpha() for c in line)
    
    return [total_lines, total_char]
