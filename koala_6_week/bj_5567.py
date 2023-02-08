from collections import deque


def bfs(x):
    q = deque()
    q.append(x)
    visited[x] = 1

    while q:
        t = q.popleft()
        for i in node[t]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = visited[t] + 1



N = int(input())
M = int(input())

node = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    node[a].append(b)
    node[b].append(a)


bfs(1)

result = 0
for i in visited:
    if 1 < i <= 3 and i != 0:
        result += 1
print(result)
