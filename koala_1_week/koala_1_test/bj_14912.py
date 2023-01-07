import sys

ssr = sys.stdin.readline

target, N = map(int, ssr().split())
count = 0

for i in range(1, target+1):
    for j in str(i):
        if N == int(j):
            count += 1


print(count)
