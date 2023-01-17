import sys
ssr = sys.stdin.readline

N, S = map(int, ssr().split())
cow = []
count = 0
for _ in range(N):
    cow.append(int(ssr()))

for i in range(N - 1):
    for j in range(i+1, N):
        if cow[i] + cow[j] <= S:
            count += 1

print(count)


