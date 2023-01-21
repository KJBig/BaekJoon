import sys

ssr = sys.stdin.readline

N, K = map(int, ssr().split())

po = [int(ssr()) for _ in range(N)]
result = [-1 for _ in range(N)]

now = po[0]
result[0] = 0
count = 0

for i in range(N):
    count += 1
    if result[now] == -1:
        result[now] = count
    now = po[now]

print(result[K])
