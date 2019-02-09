# Feb 9th, 2019
# Zixin Zhang, Alex Hope, Aaron Quinton
# This script tests the function for lib_count.py
#
# input: a path leads to the .py script
# output: a list that contains all the dependencies


import numpy as np
import pandas as pd
import pytest

# input: a script
exp_input1 = "test_file/input1.py"
exp_input2 = "test_file/input2.py"

# expected output: a list of dependencies
exp_output1 = lib_count(exp_input1) #[pandas, numpy]
exp_output2 = []


def test_lib_count():
    """
    This function checks general performance of function
    """
    lib_count(exp_input1)
    output = pd.DataFrame([(pandas,concatenate,1),(numpy,array,3)])
    test_output = lib_count(exp_input1)
    assert np.array_equal(output, test_output), "The lib_count function does not work properly"

def test_input_path():
    """
    This function is to check whether the input path is correct.
    """
    with pytest.raises(FileNotFoundError):
        lib_count("test_file/input1.txt")
    with pytest.raises(FileNotFoundError):
        lib_count("test_file/input1.pdf")
    with pytest.raises(FileNotFoundError):
        lib_count("123/input1.py")

def test_input_arg():
    """
    This function is to check if user specifies an additional argument.
    """
    with pytest.raises(AttributeError):
        lib_count(lib_count("test_file/input1.py", "script"))

def test_input_string():
    """
    This function is to check whether the input is a string.
    """
    with pytest.raises(AttributeError):
        lib_count(lib_count(123))
    with pytest.raises(AttributeError):
        lib_count([1,2,3])
    with pytest.raises(AttributeError):
        lib_count((2,3))
    with pytest.raises(AttributeError):
        lib_count(notastring)


def test_output_empty():
    """
    This function check the whether the output is correct.
    """
    assert np.array_equal(lib_count("test_file/input2.py"), []), "There are no dependencies."
