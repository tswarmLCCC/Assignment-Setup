# DO NOT MODIFY THE CODE IN THIS FILE

# Tests for Problem 1
# Simple Pay Calculator

import os.path
import sys
from problemIO import main
from tud_tests import *

#def test_problem_1():


set_keyboard_input([5])
main()
output = get_display_output()

assert output == [
        "You entered: 5"
]