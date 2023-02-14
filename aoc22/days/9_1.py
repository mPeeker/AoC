import os
import sys
import numpy as np
import re
import pprint as pp
import math
import matplotlib.pyplot as plt
import time

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
file = r"C:\Users\qmarpee\OneDrive - Ericsson\Documents\GitHub\AoC\aoc22\days\9_1.txt"
moves = read_input_lines(file, True)

def distance (H, T):
    x_dist = abs(H['x'] - T['x'])
    y_dist = abs(H['y'] - T['y'])
    dist = math.sqrt(x_dist*x_dist + y_dist*y_dist)
    return dist

def move_tail(H, T):
    moved_x = False
    moved_y = False
    if H['x'] > T['x']:
        new_x = T['x'] + 1
        moved_x = True
    if H['x'] < T['x']:
        new_x = T['x'] - 1
        moved_x = True
    if H['y'] > T['y']:
        new_y = T['y'] + 1
        moved_y = True
    if H['y'] < T['y']:
        new_y = T['y'] - 1
        moved_y = True
    new_T = T
    if moved_x:
        new_T['x'] = new_x
    if moved_y:
        new_T['y'] = new_y
    moved = moved_x or moved_y

    return new_T, moved

def move_head(H, move):
    move = move.split()
    dist = int(move[1])
    if move[0] == 'U':
        H['y'] += dist
    if move[0] == 'D':
        H['y'] -= dist
    if move[0] == 'R':
        H['x'] += dist
    if move[0] == 'L':
        H['x'] -= dist
    return H

visited = {}
visited['0-0'] = 1
H = {}
H['x'] = 0
H['y'] = 0
T = {}
T['x'] = 0
T['y'] = 0

knots = [T.copy()]*10
inds = range(9)

# Create a figure and axis
x = [d['x'] for d in knots]
y = [d['y'] for d in knots]

fig, ax = plt.subplots()
scatter = ax.scatter(x, y)
ax.grid()

# Define the update function
def update(frame):
    global data
    x = [d['x'] for d in data]
    y = [d['y'] for d in data]
    scatter.set_offsets(np.c_[x, y])
    fig.canvas.draw_idle()
    # ax.relim()
    # ax.autoscale_view()
    xmin=min(x); xmax=max(x)
    ymin=min(y); ymax=max(y)
    ax.set_xlim(xmin-0.1*(xmax-xmin),xmax+0.1*(xmax-xmin))
    # ax.set_xlim(-100,100)
    ax.set_ylim(ymin-0.1*(ymax-ymin),ymax+0.1*(ymax-ymin))
    # ax.set_ylim(-100,100)
    


for move in moves:
    knots[0] = move_head(knots[0].copy(), move)

    for ind in inds:
        h = knots[ind].copy()
        t = knots[ind + 1].copy()
        while(distance(h, t) > 1.5):
            d= distance(h, t)
            (t, moved) = move_tail(h, t)
            knots[ind + 1] = t
            data = knots
            update(ind)

            plt.pause(0.00000000001)
            if moved:
                if ind == 8:
                    name = str(knots[ind + 1]['x']) + '-' + str(knots[ind + 1]['y'])
                    if name in visited.keys():
                        visited[name] += 1
                    else:
                        visited[name] = 1
                    # print(len(visited.keys()))

print(visited)
print(len(visited.keys()))
