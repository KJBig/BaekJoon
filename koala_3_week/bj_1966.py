import sys
from collections import deque

ssr = sys.stdin.readline


def printing(pList, target, num):
    count = 0
    while count != num:
        if pList[0] == max(pList):
            pList.popleft()
            count += 1
            target -= 1
            if -1 == target:
                return count

        else:
            back = pList.popleft()
            pList.append(back)
            target -= 1
            if target == -1:
                target = num - count - 1



L = int(ssr())
result = []
for _ in range(L):
    N, M = map(int, ssr().split())
    printerList = deque(map(int, ssr().split()))

    result.append(printing(printerList, M, N))

for i in result:
    print(i)
