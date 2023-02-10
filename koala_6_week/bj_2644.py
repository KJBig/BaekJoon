from collections import deque


def bfs(x):
    famN[x] = 0
    visited[x] = 1

    q = deque()
    q.append(x)

    while q:
        target = q.popleft()

        for i in fam[target]:
            if visited[i] == 0:
                famN[i] = famN[target] + 1
                q.append(i)
                visited[i] = 1


N = int(input())
fam = [[] for _ in range(N + 1)]
famN = [-1 for _ in range(N + 1)]
visited = [0 for _ in range(N + 1)]

x1, x2 = map(int, input().split())

M = int(input())

for _ in range(M):
    t, p = map(int, input().split())
    fam[t].append(p)
    fam[p].append(t)

bfs(x1)

print(famN[x2])
