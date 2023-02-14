import os
import sys
import numpy as np
import re

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from aoc_cookiecutter.template.utils.decorators import time_it
from aoc_cookiecutter.template.utils.helper_functions import (
    read_input,
    read_input_lines,
    read_input_int,
    read_input_int_individuals,
    read_input_int_matrix,
    read_input_2_lists
)
file = r"C:\Users\qmarpee\OneDrive - Ericsson\Documents\aoc22\days\6_1.txt"
line = read_input(file)

chars = []
for char in line:
    chars.append(char)
#print(chars)

four_chars = []
for _ in range(14):
    char = chars.pop(0)
    four_chars.append(char)
ind = 14
while len(chars) > 0:
    uniques = len(set(four_chars))
    if uniques < 14:
        char = chars.pop(0)
        four_chars.pop(0)
        four_chars.append(char)
        ind += 1
    else:
        break

print(ind)

