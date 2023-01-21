import sys
from collections import deque

ssr = sys.stdin.readline

N, K = map(int, ssr().split())
L = list(map(int, ssr().split()))

one = deque()

minL = 1e9

left = -1
right = 0

for i in range(N):
    if L[right] == 2:
        right += 1
        continue

    if L[right] == 1:
        one.append(right)

        if left == -1:
            left = right
            right += 1
            continue

        if len(one) == K:
            minL = min(minL, right - left + 1)
            left = one[1]
            one.popleft()
            right += 1
        else:
            right += 1

if minL == 1e9:
    print(-1)
else:
    print(minL)
