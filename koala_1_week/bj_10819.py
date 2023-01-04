import sys
ssr = sys.stdin.readline


def backT(tryA_len):
    global maxN

    if tryA_len == N:
        result = 0
        for i in range(0, N - 1):
            result += abs(tryA[i] - tryA[i + 1])
        maxN = max(maxN, result)
        return

    for i in range(0, N):
        if visited[i]:
            continue
        else:
            visited[i] = True
            tryA.append(nums[i])
            backT(tryA_len + 1)
            visited[i] = False
            tryA.pop()


N = int(ssr())
nums = list(map(int, ssr().split()))
tryA = []
visited = [False]*N
maxN = -1e9

backT(0)

print(maxN)
