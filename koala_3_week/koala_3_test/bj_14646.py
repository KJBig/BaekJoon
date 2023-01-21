import sys

ssr = sys.stdin.readline


N = int(ssr())
P = list(map(int, ssr().split()))

visited = [0 for _ in range(len(P))]

count = 0
maxSti = 0

for i in range(len(P)):

    if visited[P[i]] == 0:
        visited[P[i]] += 1
        count += 1
    else:
        visited[P[i]] = 0
        count -= 1
    maxSti = max(maxSti, count)


print(maxSti)
