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
file = r"C:\Users\qmarpee\OneDrive - Ericsson\Documents\aoc22\days\3_1.txt"
str_data = read_input_lines(file, True)

alfa = "abcdefghijklmnopqrstuvwxyz"
ALFA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
points = {}
for char in alfa:
    points[char] = ord(char)-96

for char in ALFA:
    points[char] = ord(char)-64+26

print(points)

str1 = []
str2 = []

for line in str_data:
    ind = int(len(line)/2)
    str2.append(line[ind:])
    str1.append(line[:ind])




scores = []

for s1, s2 in zip(str1, str2):
    score = 0
    for char in s1:
        if char in s2:
            score =points[char]
            break
    scores.append(score)

#print(scores)
total = np.sum(scores)
print(total)
scores2 = []
while len(str_data) > 0:
    curr3 = []
    for _ in range(3):
        curr3.append(str_data.pop())
    print(curr3)
    score = 0
    for char in curr3.pop():
        if char in curr3[0] and char in curr3[1]:
            score = points[char]
            break
    scores2.append(score)

print(scores2)
total = np.sum(scores2)
print(total)
    
