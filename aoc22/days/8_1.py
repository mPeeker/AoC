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
matr = read_input_int_matrix(file)
npmatr = np.array(matr)

print(len(matr))

for line in matr:
    line.insert(0, -1)
    line.append(-1)

# pp.pprint(matr)

begin_end_list = [-1]*len(matr[0])
matr.insert(0, begin_end_list)
matr.append(begin_end_list)

# pp.pprint(matr)
matr = np.array(matr)
# pp.pprint(matr)
trees = []
for x in range(len(matr[:, 0]) - 2):
    x_ind = x+1
    for y in range(len(matr[0, :]) - 2):
        y_ind = y+1
        # print(matr[x+1,y+1])
        tree = {}
        name = str(x_ind) + str(y_ind)
        tree['name'] = name
        tree['height'] = matr[x_ind, y_ind]
        north = np.flip(matr[:, y_ind][:x_ind])
        south = matr[:, y_ind][x_ind+1:]
        west = np.flip(matr[x_ind, :][:y_ind])
        east = matr[x_ind, :][y_ind+1:]
        tree['north'] = max(north)
        tree['south'] = max(south)
        tree['west'] = max(west)
        tree['east'] = max(east)

        dirs = [north, south, west, east]
        # pp.pprint(dirs)
        dir_scores = []
        for dir in dirs:
            dir_score = 0
            # dir = np.delete(dir, -1)
            # dir = np.flip(dir)
            if len(dir) == 1:
                dir_score = 0
            else:
                for index in range(len(dir)):
                    next = dir[index +1]
                    curr = dir[index]
                    if next == -1:
                        dir_score += 1
                        break
                    elif curr <= next:
                        dir_score += 1
                    
                    else:
                        break

            dir_scores.append(dir_score)
        # pp.pprint(dir_scores)    
        score = 1
        for _ in dir_scores:
            score = score * _
        tree['score'] = score
      
        # tree = {name: [north, south, east, west]}
        trees.append(tree)
# pp.pprint(west)
# pp.pprint(east)
# pp.pprint(north)
# pp.pprint(south)
# pp.pprint(trees)
count = 0
treemax = 0
ind = 0
maxind = 0
maxtree = {}
for tree in trees:
    # print(tree['score'])

    # pp.pprint(tree)
    h = tree['height']
    n = tree['north']
    s = tree['south']
    e = tree['east']
    w = tree['west']
    if h <= n and h <= s and h <= e and h <= w:
        tree['vis'] = False
    else:
        tree['vis'] = True
    if tree['vis']:
        count += 1
    if tree['score'] > treemax:
        treemax = tree['score']
        maxind = ind
        maxtree = tree
    # treemax = max(treemax, tree['score'])
    ind +=1
    # pp.pprint(tree)
print(dir_scores)
print(count)
print(treemax)
print(maxind)
print(maxtree)
print(len(trees))



    