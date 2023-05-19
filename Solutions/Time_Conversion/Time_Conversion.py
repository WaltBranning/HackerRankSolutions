#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    a_p = s[-2:]
    h, m, sec = s.split(':')
    if h == '12' and a_p == 'AM':
        h = '00'
    elif a_p == 'PM' and h != '12':
        h = str(int(h) + 12)
    
    return ':'.join([h,m,sec[:2]])
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
