import sys

ssr = sys.stdin.readline


def bridge(n):
    num = 1
    for i in range(1, n + 1):
        num *= i
    return num


T = int(ssr())
result = []

for _ in range(T):
    n, m = map(int, ssr().split())
    bNum = int(bridge(m) / (bridge(n) * bridge(m - n)))
    result.append(bNum)

for i in result:
    print(i)
