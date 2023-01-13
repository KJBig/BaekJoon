import sys
ssr = sys.stdin.readline

N, K = map(int, ssr().split())
prod = [[0, 0]]
dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

for _ in range(N):
    prod.append(list(map(int, ssr().split())))

for i in range(1, N + 1):
    W = prod[i][0]
    V = prod[i][1]

    for j in range(1, K + 1):
        if j < W:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(V + dp[i - 1][j - W], dp[i - 1][j])

print(dp[N][K])
