import sys

ssr = sys.stdin.readline


def HMC(num):
    global count

    if num == N:
        count += 1
        return
    if num > N:
        return

    for j in range(1, 4):
        HMC(num + j)


T = int(ssr())
result = []

for i in range(T):
    count = 0

    N = int(ssr())
    HMC(0)
    result.append(count)

for i in result:
    print(i)