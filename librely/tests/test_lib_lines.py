# Feb 8th, 2019
# Zixin Zhang
# This script tests the function for lib_writeme.py
#
# input: a path leads to the .py script
# output: a list that contains all the dependencies
import pytest
from librely.lib_lines import lib_lines

# input: a file path to a test script that uses a few functions and imports common packages
input1 = "./librely/tests/test.py"

# expected output: a list of dependencies
exp_output1 = [17,173]


def test_input_path():
    """
    This function is to check whether the input path is correct.
    """
    with pytest.raises(FileNotFoundError):
        lib_lines("./librely/tests/input1.txt")
    with pytest.raises(FileNotFoundError):
        lib_lines("test_file/input1.pdf")

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
