import sys

ssr = sys.stdin.readline

N = int(ssr())
nums = list(map(int, ssr().split()))
M = int(ssr())
result = [[0] * N for _ in range(N)]

for i in range(N):
    for head in range(N):
        tail = head + i
        if tail >= N:
            break

        if i == 0:
            result[head][tail] = 1
            continue

        if i == 1:
            if nums[head] == nums[tail]:
                result[head][tail] = 1
                continue

        if nums[head] == nums[tail] and result[head + 1][tail - 1]:
            result[head][tail] = 1


for i in range(M):
    S, E = map(int, ssr().split())
    print(result[S - 1][E - 1])
