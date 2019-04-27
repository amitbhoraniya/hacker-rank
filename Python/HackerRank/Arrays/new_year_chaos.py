# !/bin/python3

# https://www.hackerrank.com/challenges/new-year-chaos/problem
# Sample Input
# 2
# 5
# 2 1 5 3 4
# 5
# 2 5 1 3 4
# Sample Output
# 3
# Too chaotic


# Complete the minimumBribes function below.
def minimumBribes(q):
    count = 0
    for i in range(0, len(q)):
        if q[i] - 3 > i:
            print('Too chaotic')
            return
        for j in range(max(0, q[i] - 2), i):
            if q[j] > q[i]:
                count += 1
    print(count)


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
