import sys

ssr = sys.stdin.readline

N = int(ssr().strip())
schedule = {}

for i in range(N):
    T, P = map(int, ssr().split())
    schedule[i + 1] = [T, P]

result = [0 for i in range(N + 1)]

for i in range(N-1, -1, -1):
    if i + schedule[i+1][0] > N:
        result[i] = result[i+1]
    else:
        result[i] = max(result[i+1], schedule[i+1][1] + result[i + schedule[i+1][0]])

print(result[0])
