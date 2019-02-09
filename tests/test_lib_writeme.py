# Feb 8th, 2019
# Zixin Zhang
# This script tests the function for lib_writeme.py
#
# input: a path leads to the .py script
# output: a list that contains all the dependencies

import numpy as np
import pytest

# input: a script
exp_input1_arg1 = "test_file/input1.py"
exp_input1_arg2 = "test_file/result/dependency.md"

# expected output: a list of dependencies
exp_output1 = "test_file/exp_dependency.md"


def test_lib_writeme():
    lib_writeme("test_file/input1.py", "test_file/result/dependency.md")
    output = "test_file/exp_dependency.md"
    test_output = lib_writeme("test_file/input1.py", "test_file/result/dependency.md")
    assert np.array_equal(output, test_output), "The lib_search function does not work properly"

def test_output_empty():
    """
    This function check the whether the output is correct.
    """
    output = "test_file/exp_dependency.md"
    test_output = lib_writeme("test_file/input1.py", "test_file/result/dependency.md")
    assert np.array_equal(lib_writeme("test_file/input2.py"), []), "There are no dependencies."

def test_input_path():
    """
    This function is to check whether the input path is correct.
    """
    with pytest.raises(FileNotFoundError):
        lib_writeme("test_file/input1.txt", "test_file/result/dependency.md")
    with pytest.raises(FileNotFoundError):
        lib_writeme("test_file/input1.pdf","test_file/result/dependency.md")
    with pytest.raises(FileNotFoundError):
        llib_writeme("123/input1.py", "test_file/result/dependency.md")

def test_input_arg():
    """
    This function is to check if user specifies an additional argument.
    """
    with pytest.raises(AttributeError):
        lib_writeme("test_file/input1.py", "test_file/result/dependency.md","script")

def test_input_string():
    """
    This function is to check whether the input is a string.
    """
    with pytest.raises(AttributeError):
        lib_writme(123,"test_file/result/dependency.md")
    with pytest.raises(AttributeError):
        lib_writeme([1,2,3],"test_file/result/dependency.md")
    with pytest.raises(AttributeError):
        lib_writeme((2,3),"test_file/result/dependency.md")
    with pytest.raises(AttributeError):
        lib_writeme("test_file/input1.py", test_file/result/dependency.md)
