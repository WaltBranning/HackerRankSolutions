#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bomberMan' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING_ARRAY grid
#

def bomberMan(n, grid):
    # Write your code here
    fill = lambda: [['O' for _ in range(len(grid[0]))] for _ in range(len(grid))]
    if n < 2: return grid
    elif n%2 == 0: return [''.join(i) for i in fill()]
    
    def get_bombs(state):
        bomb_loc = []
        for row in range(len(state)):
            for i in range(len(state[row])):
                if state[row][i] == 'O': bomb_loc.append((row, i))
        return bomb_loc

    def explode(bomb_loc, grid):
        shape = [(0,-1), (-1,0), (0,0), (0,1), (1,0)]
        for x,y in bomb_loc:
            for mx, my in shape:
                try:
                    grid[max(0, x+mx)][max(0,y+my)] = '.'
                except: pass
        return grid

    state = [list(i) for i in grid]

    if (n-1)%4 == 2: 
        state = explode(get_bombs(state), fill())        
    elif (n-1)%4== 0:
        for _ in range(2):state = explode(get_bombs(state), fill())
    
    return [''.join(i) for i in state]
        
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    r = int(first_multiple_input[0])

    c = int(first_multiple_input[1])

    n = int(first_multiple_input[2])

    grid = []

    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    result = bomberMan(n, grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
