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
exp_output1 = [17,248]


def test_lib_count():

    assert lib_lines(input1) == exp_output1, "The lib_lines function does not work properly"
