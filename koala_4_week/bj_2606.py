from collections import deque


def bfs(que):
    count = 0

    while que:
        x = que.popleft()
        visited[x] = 1
        for i in computers[x]:
            if visited[i] == 0:
                visited[i] = 1
                count += 1
                que.append(i)

    return count


N = int(input())
M = int(input())

computers = [[] for i in range(N + 1)]
visited = [0 for _ in range(N + 1)]

for _ in range(M):
    q, w = map(int, input().split())
    computers[q].append(w)
    computers[w].append(q)

que = deque()
que.append(1)
print(bfs(que))
