from collections import deque


def bfs(que):
    while que:
        y, x = que.popleft()
        for i in range(4):
            ty = y + dy[i]
            tx = x + dx[i]

            if -1 < ty < N and -1 < tx < M and visited[ty][tx] == 0 and field[ty][tx] == 0:
                que.append((ty, tx))
                visited[ty][tx] = 1
                field[ty][tx] = field[y][x] + 1


dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

M, N = map(int, input().split())

field = []
visited = []
count = 0
que = deque()

for _ in range(N):
    field.append(list(map(int, input().split())))

for _ in range(N):
    visited.append([0 for _ in range(M)])

for i in range(N):
    for j in range(M):
        if field[i][j] == 1:
            que.append((i, j))

bfs(que)
day = 0

for i in range(N):
    for j in range(M):
        if field[i][j] == 0:
            print(-1)
            exit()
        day = max(day, field[i][j])

if day == 1:
    print(0)
else:
    print(day - 1)
