import sys

ssr = sys.stdin.readline


def backT(num, idx):
    if len(num) == M:
        print(' '.join(num))
        return

    for i in range(idx, N+1):
        num.append(str(i))
        backT(num, i)
        num.pop()


N, M = map(int, ssr().split())

backT([], 1)

