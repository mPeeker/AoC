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
    read_input_int_matrix,
    read_input_2_lists
)
file = r"C:\Users\qmarpee\OneDrive - Ericsson\Documents\aoc22\days\4_1.txt"
(str_data1, str_data2) = read_input_2_lists(file)
# print(str_data1, str_data2)

asisgs1 = []
assigs2 = []
for elem1, elem2 in zip(str_data1, str_data2):
    ellist1 = elem1.split('-')
    ellist2 = elem2.split('-')
    list1 = list(range(int(ellist1[0]), int(ellist1[1])+1))
    list2 = list(range(int(ellist2[0]), int(ellist2[1])+1))
    asisgs1.append(list1)
    assigs2.append(list2)

print(asisgs1, assigs2)
unions = []
for list1, list2 in zip(asisgs1, assigs2):
    union = list(set(list1 + list2))
    unions.append(union)
print(unions)

score = 0
for union, list1, list2 in zip(unions, asisgs1, assigs2):
    if len(union) == max(len(list1), len(list2)):
        score +=1

print(score)

score = 0
for union, list1, list2 in zip(unions, asisgs1, assigs2):
    if len(union) < len(list1) + len(list2):
        score +=1

print(score)


