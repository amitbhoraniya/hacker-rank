#!/bin/python3

import os


# https://www.hackerrank.com/challenges/repeated-string/problem
# Sample Input 0
# aba
# 10
#
# Sample Output 0
# 7
#
# Sample Input 1
# a
# 1000000000000
# Sample Output 1
#
# 1000000000000

# Complete the repeatedString function below.
def repeatedString(s, n):
    mp = int(n / len(s))
    lt = n % len(s)

    a_per_string = 0
    for c in s:
        if c == 'a':
            a_per_string += 1

    count = mp * a_per_string
    for c in s[0:lt]:
        if c == 'a':
            count += 1
    return count


if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = 'out.txt'
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    print(result)

    fptr.write(str(result) + '\n')

    fptr.close()
