#!/bin/python3
import os


# https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem/

# Sample Input
# 7
# 0 0 1 0 0 1 0

# Expected Output
# 4


# Sample Input - 2
# 6
# 0 0 0 0 1 0

# Expected Output
# 3

def jumpingOnClouds(c):
    i = 0
    jump = 0
    while i < len(c) - 2:
        n1 = c[i + 2]
        if n1 == 0:
            i += 2
        elif n1 == 1:
            i += 1
        jump += 1
    if i < len(c) - 1:
        jump += 1
    return jump


if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = 'out.txt'

    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    print(result)

    fptr.write(str(result) + '\n')

    fptr.close()
