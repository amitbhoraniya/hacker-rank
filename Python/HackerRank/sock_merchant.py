import os


# https://www.hackerrank.com/challenges/sock-merchant/problem

# Sample Input
# 9
# 10 20 20 10 10 30 50 10 20
#
# Sample Output
# 3

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    i = 0
    count = 0
    t = []
    while i < n:
        cur = ar[i]
        if cur in t:
            count += 1
            t.remove(cur)
            pass
        else:
            t.append(cur)
        i += 1
    return count


if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = 'out.txt'
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = sockMerchant(n, ar)
    print(result)

    fptr.write(str(result) + '\n')
    fptr.close()
