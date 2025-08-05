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

def timeConversion(s): # Converts 12hour AM/PM time to 24-hour time
    s.strip("")
    split = s.split(":")
    if s.endswith("PM"):
        s = s.strip("PM")
        split = s.split(":")
        split[0] = int(split[0])
        if split[0] == 12:
            split[0] = 0
        
        result = f"{split[0] + 12}:{split[1]}:{split[2]}"
    
    if s.endswith("AM"):
        s = s.strip("AM")
        split = s.split(":")
        if split[0] == "12":
            split[0] = "00"
        result = f"{split[0]}:{split[1]}:{split[2]}"
    
    return result
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
