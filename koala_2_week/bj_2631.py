import sys
ssr = sys.stdin.readline

N = int(ssr())
s = []
dp = [0 for i in range(N)]

for i in range(N):
    s.append(int(ssr()))

dp[0] = 1

for i in range(1, N):
    a = []
    for j in range(i):
        if s[i] > s[j]:
            a.append(dp[j])
    if not a:
        dp[i] = 1
    else:
        dp[i] = max(a) + 1

print(N - max(dp))
