#!/bin/python3
import os


# https://www.hackerrank.com/challenges/counting-valleys/problem

# Sample Input
# 8
# UDDDUDUU

# Expected Output
# 1
def countingValleys(n, s):
    result = 0
    cvalue = 0
    for c in s:
        if c == 'D':
            cvalue -= 1
        elif c == 'U':
            if cvalue == -1:
                result += 1
            cvalue += 1
    return result


if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = 'out.txt'
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    s = input()
    result = countingValleys(n, s)
    print(result)
    fptr.write(str(result) + '\n')
    fptr.close()
