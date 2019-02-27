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

# expected output: a list of dependencies
exp_output1 = ['numpy', 'sklearn.model_selection', 'matplotlib', 'pandas', 'sklearn', 'sklearn.tree']


def test_lib_search():

    assert lib_search(input1) == exp_output1, "The lib_search function does not work properly"
