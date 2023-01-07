import sys
from collections import deque

ssr = sys.stdin.readline

text = ssr().strip()
N = int(ssr())
count = 0
rings = []

for i in range(N):
    temp = deque(ssr().strip())
    rings.append(temp)

for i in rings:
    ring_str = ''.join(i)
    for _ in range(len(ring_str)):
        if text in ring_str:
            count += 1
            break
        else:
            ta = i.pop()
            i.appendleft(ta)
            ring_str = ''.join(i)

print(count)