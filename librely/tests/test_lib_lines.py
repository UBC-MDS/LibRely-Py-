# Feb 8th, 2019
# Zixin Zhang
# This script tests the function for lib_writeme.py
#
# input: a path leads to the .py script
# output: a list that contains all the dependencies
import pytest
from librely.lib_lines import lib_lines

# input: a file path to a test script that uses a few functions and imports common packages
input1 = "test.py"
input1_pdf = "test.pdf"
input1_txt = "test.txt"
# expected output: a list of dependencies
exp_output1 = [17,173]

#Handled file not found errors with exception handling
#def test_input_path():
#    """
#    This function is to check whether the input path is correct.
#    """
#    with pytest.raises(FileNotFoundError):
#        lib_lines(input1_txt)
#    with pytest.raises(FileNotFoundError):
#        lib_lines(input1_pdf)

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

def test_lib_count():
    """
    This function checks that the output of the function is equal to the expected output
    """
    assert lib_lines(input1) == exp_output1, "The lib_count function does not work properly"
