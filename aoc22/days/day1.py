import os
import sys
import numpy as np

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from aoc_cookiecutter.template.utils.decorators import time_it
from aoc_cookiecutter.template.utils.helper_functions import (
    read_input,
    read_input_lines,
    read_input_int,
    read_input_int_individuals,
    read_input_int_matrix
)
file = r"C:\Users\qmarpee\OneDrive - Ericsson\Documents\aoc22\days\1_1.txt"
str_data = read_input_lines(file)
str_data.append("\n")
spliced_arr = []
curr_arr = []
print(str_data)

while len(str_data) > 0:
    elem = str_data.pop()
    if elem == "\n":
        spliced_arr.append(curr_arr)
        curr_arr = []
    else:
        curr_arr.append(int(elem))

print(spliced_arr)

sum_array = []
for arr in spliced_arr:
    sum = 0
    for elem in arr:
        sum += elem
    sum_array.append(sum)

print(sum_array)
sum_array = np.sort(sum_array)
print(sum_array)
max_array = sum_array[-3:]
print(max_array)

max = np.sum(max_array)
print(max)