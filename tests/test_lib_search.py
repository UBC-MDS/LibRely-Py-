# Feb 8th, 2019
# Zixin Zhang
# This script tests the function for findme.py
#
# input: a path leads to the .py script
# output: a list that contains all the dependencies

import numpy as np
import pytest

# input: a script
exp_input1 = "test_file/input1.R"
exp_input2 = "test_file/input2.R"

# expected output: a list of dependencies
exp_output1 = lib_search(exp_input1) #[ggplot, tidyverse]
exp_output2 = []


def test_lib_search():
    lib_search(exp_input1)
    output = [ggplot, tidyverse]
    test_output = lib_search(exp_input1)
    assert np.array_equal(output, test_output), "The lib_search function does not work properly"

def test_input_path():
    """
    This function is to check whether the input path is correct.
    """
    with pytest.raises(FileNotFoundError):
        lib_search("test_file/input1.txt")
    with pytest.raises(FileNotFoundError):
        lib_search("test_file/input1.pdf")
    with pytest.raises(FileNotFoundError):
        lib_search("123/input1.py")

def test_input_arg():
    """
    This function is to check if user specifies an additional argument.
    """
    with pytest.raises(AttributeError):
        lib_search(lib_search("test_file/input1.py", "script"))

def test_input_string():
    """
    This function is to check whether the input is a string.
    """
    with pytest.raises(AttributeError):
        lib_search(lib_search(123))
    with pytest.raises(AttributeError):
        lib_search([1,2,3])
    with pytest.raises(AttributeError):
        lib_search((2,3))


def test_output_empty():
    """
    This function check the whether the output is correct.
    """
    assert np.array_equal(lib_search("test_file/input2.py"), []), "There are no dependencies."
