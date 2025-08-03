#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr): # Find the smallest and largest sum of four integers from a five integer set
    # Write your code here
    arr.sort()
    min_val = arr[0] + arr[1] + arr[2] + arr[3]
    max_val = arr[4] + arr[1] + arr[2] + arr[3]
    
    print(f"{min_val} {max_val}")

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
