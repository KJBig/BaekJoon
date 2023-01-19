import sys

ssr = sys.stdin.readline

N = int(ssr())

score = [100, 100]

for _ in range(N):
    C, S = map(int, ssr().split())
    if C > S:
        score[1] -= C
    elif C < S:
        score[0] -= S

for i in score:
    print(i)
