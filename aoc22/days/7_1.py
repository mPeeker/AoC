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
file = r"C:\Users\qmarpee\OneDrive - Ericsson\Documents\aoc22\days\7_1.txt"
lines = read_input_lines(file)

sub_folders = {}
folder_sizes = {}
curr_folder_tree = ['\\']

lines.pop(0)

def parse_cd_line(line):
    return line.split()[2]

def parse_file_size(line):
    return int(line.split()[0])

def containsNumber(value):
    for character in value:
        if character.isdigit():
            return True
    return False

index = 0
for line in lines:
    index += 1
    if 'cd ..' in line:
        curr_folder_tree.pop()
    elif 'cd ' in line:
        folder = curr_folder_tree[-1]
        new_folder = parse_cd_line(line)
        if folder in sub_folders:
            sub_folders[folder].append(folder+new_folder)
        else:
            sub_folders[folder] =[folder+new_folder]
        curr_folder_tree.append(folder+new_folder)
    elif containsNumber(line):
        size = parse_file_size(line)
        folder = curr_folder_tree[-1]
        for folder in curr_folder_tree:
            if folder in folder_sizes:
                folder_sizes[folder] += size
            else:
                folder_sizes[folder] = size
    else: pass

print(sub_folders)
print(folder_sizes)

sum = 0
for key in folder_sizes:
    size = folder_sizes[key]
    if size <= 100000:
        sum += size

print(sum)

available_space = 70000000
needed_space = 30000000

needed_delete = needed_space - (available_space - folder_sizes['\\'])
print(needed_delete)

smallest = folder_sizes['\\']
for key in folder_sizes:
    if folder_sizes[key] > needed_delete and folder_sizes[key] < smallest:
        smallest = folder_sizes[key]

print(smallest)






    
