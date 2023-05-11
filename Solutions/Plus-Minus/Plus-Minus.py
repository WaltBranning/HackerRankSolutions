# Raw solution from HackerRank

import math
import os
import random
import re
import sys
from itertools import groupby
#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    base_len = len(arr)
    arr.sort()
    def sorter(x):
        if x > 0: return 'pos'
        elif x < 0: return 'neg'
        else: return 'zero'
    lx = {key: list(val)  for key, val in groupby(arr, key=sorter)}
    div_lx = lambda x: len(lx[x]) / base_len
    for i in ['pos', 'neg', 'zero']: 
        print(div_lx(i)) if i in lx.keys() else print(0.000000)
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
