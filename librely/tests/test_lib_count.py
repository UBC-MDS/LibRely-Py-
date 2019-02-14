# Feb 9th, 2019
# Zixin Zhang, Alex Hope, Aaron Quinton
# This script tests the function for lib_count.py
#
# input: a path leads to the .py script
# output: a list that contains all the dependencies
import pytest
from librely.lib_count import lib_count

# input: a file path to a test script that uses a few functions and imports common packages
input1 = "./librely/tests/test.py"

# expected output: a list of dependencies
exp_output1 = ['numpy', 'sklearn.model_selection', 'matplotlib', 'pandas', 'sklearn', 'sklearn.tree']


def test_lib_count():

    assert lib_count(input1) == exp_output1, "The lib_count function does not work properly"
