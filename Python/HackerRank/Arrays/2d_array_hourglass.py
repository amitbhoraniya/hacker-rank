#!/bin/python3

import sys


# https://www.hackerrank.com/challenges/2d-array/problem
# Sample Input
# 1 1 1 0 0 0
# 0 1 0 0 0 0
# 1 1 1 0 0 0
# 0 0 2 4 4 0
# 0 0 0 2 0 0
# 0 0 1 2 4 0
#
# Sample Output
# 19

# Complete the hourglassSum function below.
def hourglassSum(arr):
    cr = 0
    mx = -sys.maxsize - 1
    while cr < len(arr) - 2:
        cc = 0
        while cc < len(arr[0]) - 2:
            hs = arr[cr][cc] + arr[cr][cc + 1] + arr[cr][cc + 2] + arr[cr + 1][cc + 1] + arr[cr + 2][cc] + +arr[cr + 2][
                cc + 1] + +arr[cr + 2][cc + 2]
            if mx < hs:
                mx = hs
            cc += 1
        cr += 1
    return mx


if __name__ == '__main__':
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    result = hourglassSum(arr)
    print(result)
