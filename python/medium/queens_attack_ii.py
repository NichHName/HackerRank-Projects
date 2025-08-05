#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'queensAttack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER r_q
#  4. INTEGER c_q
#  5. 2D_INTEGER_ARRAY obstacles
#

def queensAttack(n, k, r_q, c_q, obstacles):
    
    # Straight line distances
    left = c_q - 1
    right = n - c_q
    up = n - r_q
    down = r_q - 1

    straight_squares = left + right + up + down

    # Diagonal distances
    top_right = min(up, right)
    top_left = min(up, left)
    bottom_right = min(down, right)
    bottom_left = min(down, left)

    diag_squares = top_right + top_left + bottom_right + bottom_left

    num_possible_squares = straight_squares + diag_squares
    if k == 0:
        return num_possible_squares
    elif k != 0:
        # Process each obstacle and update limits if it's closer than current blocker
        for k in obstacles:
            r_o, c_o = k

            # Diagonal obstacles
            if abs(r_o - r_q) == abs(c_o - c_q):
                dist = abs(r_o - r_q) - 1  # Squares between queen and obstacle
                if r_o < r_q and c_o < c_q:  # Bottom-Left
                    if dist < bottom_left:
                        bottom_left = dist
                elif r_o < r_q and c_o > c_q:  # Bottom-Right
                    if dist < bottom_right:
                        bottom_right = dist
                elif r_o > r_q and c_o < c_q:  # Top-Left
                    if dist < top_left:
                        top_left = dist
                elif r_o > r_q and c_o > c_q:  # Top-Right
                    if dist < top_right:
                        top_right = dist

            # Horizontal obstacles (same row)
            elif r_o == r_q:
                dist = abs(c_o - c_q) - 1
                if c_o > c_q:  # Right
                    if dist < right:
                        right = dist
                elif c_o < c_q:  # Left
                    if dist < left:
                        left = dist

            # Vertical obstacles (same column)
            elif c_o == c_q:
                dist = abs(r_o - r_q) - 1
                if r_o > r_q:  # Up
                    if dist < up:
                        up = dist
                elif r_o < r_q:  # Down
                    if dist < down:
                        down = dist

            # Total reachable squares
            num_possible_squares = up + down + left + right + top_left + top_right + bottom_left + bottom_right

        return num_possible_squares
            
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    r_q = int(second_multiple_input[0])

    c_q = int(second_multiple_input[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
