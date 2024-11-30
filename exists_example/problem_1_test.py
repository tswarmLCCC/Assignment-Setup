# DO NOT MODIFY THE CODE IN THIS FILE

# Tests for Problem 1
# Simple Pay Calculator

import os.path
import sys
from problem_1 import main
from tud_tests import *

def test_problem_1():

    try:
        exists = os.path.exists("problem_1.py")
        assert exists == True
    except:
        sys.exit()
