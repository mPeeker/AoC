import os
import sys
import numpy as np
import re
import pprint as pp

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
file = r"C:\Users\qmarpee\OneDrive - Ericsson\Documents\aoc22\days\8_1.txt"
size = 99
matr = read_input_int_matrix(file)
matr = np.array(matr)

xaxis = range(size)
yaxis = range(size)

scores = []

def calc_dirscore(treelist):
    dir_score = 1
    # dir = np.delete(dir, -1)
    # dir = np.flip(dir)
    if len(treelist) == 1:
        dir_score = 1
    else:
        for index in range(len(treelist)-1):
            next = treelist[index +1]
            curr = treelist[index]
            if curr <= next:
                dir_score += 1           
            else:
                break
    return dir_score

for x in xaxis:
    for y in yaxis:
        score = 1
        north = np.flip(matr[:, y][:x])
        south = matr[:, y][x+1:]
        west = np.flip(matr[x, :][:y])
        east = matr[x, :][y+1:]
        if x == 0:
            score = 0
        elif y == 0:
            score = 0
        else:
            score = calc_dirscore(north) * calc_dirscore(south) * calc_dirscore(east) * calc_dirscore(west)

        scores.append(score)
print(max(scores))
print(scores.index(max(scores)))
        

