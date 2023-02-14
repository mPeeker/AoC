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
file = r"C:\Users\qmarpee\OneDrive - Ericsson\Documents\aoc22\days\5_1.txt"
lines = read_input_lines(file)
#print(lines)
i=0
for _ in lines:
    if '[' not in _:
        break
    else:
        i += 1

stacks_str = lines[:i]
moves_str = lines[i+2:]
print(stacks_str)

stacks = []
for stack_str in stacks_str:
    stack = [stack_str[1], stack_str[5], stack_str[9], stack_str[13], stack_str[17], stack_str[21], stack_str[25], stack_str[29], stack_str[33]]
    #stack = [stack_str[1], stack_str[5], stack_str[9],]
    stacks.append(stack)

#print(stacks)




stacks = np.array(stacks).T
stacks = stacks.tolist()
#print(stacks)
stacks_cleared = []
for stack in stacks:
    while stack[0] == ' ':
        stack.pop(0)
    stacks_cleared.append(stack)
print(stacks_cleared)


moves = []
for line in moves_str:
    no = re.search(r'move \d+', line).group()
    no = int(re.search(r'\d+', line).group())
    outof = re.search(r'from \d+', line).group()
    outof = int(re.search(r'\d+', outof).group())
    to = re.search(r'to \d+', line).group()
    to = int(re.search(r'\d+', to).group())
    move = {'no': no, 'outof': outof -1, 'to': to -1}
    moves.append(move)
    #print(move)
#print(stacks_cleared)
# for move in moves:
#     for _ in range(move['no']):
#         crate = stacks_cleared[move['outof']].pop(0)
#         stacks_cleared[move['to']].insert(0, crate)
print(stacks_cleared)
for move in moves:
    print(move)
    crates = stacks_cleared[move['outof']][:move['no']]
    for _ in range(move['no']):
        stacks_cleared[move['outof']].pop(0)
    stacks_cleared[move['to']] = crates + stacks_cleared[move['to']]
    print(stacks_cleared)

text = ''
for stack in stacks_cleared:
    text = text+stack[0]
print(text)






    
print('/n')
#print(stacks)
