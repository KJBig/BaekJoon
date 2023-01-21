import sys

ssr = sys.stdin.readline

N = int(ssr())
P = list(map(int, ssr().split()))
S = list(map(int, ssr().split()))

# N = N
target = []
for i in range(int(N / 3)):
    for j in range(3):
        target.append(j)

temp = P.copy()
minus = P.copy()
count = 0

while 1:
    if target == P:
        break

    for i in range(N):
        P[S[i]] = temp[i]

    temp = P.copy()

    if count > 0 and P == minus:
        count = -1
        break

    count += 1

print(count)
