#!/bin/python3

import math
import os
import random
import re
import sys

#a single line of n space-separated integers in an array, a, denoting the final state of the array after performing d left rotations

def rotLeft(a, d):
    a = a[d:] + a[:d]
    return a

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

