# Feb 9th, 2019
# Zixin Zhang, Alex Hope, Aaron Quinton
# This script tests the function for lib_count.py
#
# input: a path leads to the .py script
# output: a list that contains all the dependencies
import pytest
from librely.lib_count import lib_count

# input: a file path to a test script that uses a few functions and imports common packages
input1 = "test.py"
input1_pdf = "test.pdf"
input1_txt = "test.txt"

# expected output: a list of dependencies
exp_output1 = (['numpy', 'sklearn.model_selection', 'matplotlib', 'pandas', 'sklearn', 'sklearn.tree'],
                ['train_test_split', 'DecisionTreeClassifier'])

def test_input_path():
    """
    This function is to check whether the input path is correct.
    """
    with pytest.raises(FileNotFoundError):
        lib_count(input1_txt)
    with pytest.raises(FileNotFoundError):
        lib_count(input1_pdf)


def test_input_string():
    """
    This function is to check whether the input is a string.
    """
    with pytest.raises(OSError):
        lib_count(123)
    with pytest.raises(TypeError):
        lib_count([1,2,3])
    with pytest.raises(TypeError):
        lib_count((2,3))

def test_lib_count():
    """
    This function checks that the output of the function is equal to the expected output
    """
    assert lib_count(input1) == exp_output1, "The lib_count function does not work properly"
