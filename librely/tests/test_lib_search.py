# Feb 8th, 2019
# Zixin Zhang
# This script tests the function for lib_search.py
#
# input: a path leads to the .py script
# output: a list that contains all the dependencies
import pytest
from librely.lib_search import lib_search

# input: a file path to a test script that uses a few functions and imports common packages
input1 = "test.py"
input2 = "test2.py"
input3 = "test3_empty.py"
input4_txt = "test3.txt"
input5_no_file = None

# expected output: a couple lists of dependencies
exp_output1 = ['numpy', 'sklearn.model_selection', 'matplotlib', 'pandas', 'sklearn', 'sklearn.tree']
exp_output2 = []

def test_input_provided():
    """
    This function is to ensure a filepath is provided.
    """
    with pytest.raises(FileNotFoundError):
        lib_lines(input5_no_file)

def test_input_arg():
    """
    This function is to check if user specifies an additional argument.
    """
    with pytest.raises(TypeError):
        lib_lines(input1, "script")

def test_input_string():
    """
    This function is to check whether the input is a string.
    """
    with pytest.raises(OSError):
        lib_lines(123)
    with pytest.raises(TypeError):
        lib_lines([1,2,3])
    with pytest.raises(TypeError):
        lib_lines((2,3))

def test_output_path():
    """
    Compare the expected outut of lib_search to the pre-selected expected exp_output1
    """

    assert lib_search(input1) == exp_output1, "The lib_search function does not work properly"

def test_output_path2():
    """
    Compare the expected empty output of lib_search with test2 to the expected empty exp_output2
    """
    assert lib_search(input2) == exp_output2, "The lib_search function does not work properly"
