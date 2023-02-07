from collections import deque


def bfs(y, x, visit):
    que = deque()
    que.append((y, x))
    visit[y][x] = 1

    while que:
        ny, nx = que.popleft()

        for i in range(4):
            ty = ny + dy[i]
            tx = nx + dx[i]
            if -1 < ty < N and -1 < tx < M and visited[ty][tx] == 0 and maze[ty][tx] == 1:
                que.append((ty, tx))
                visited[ty][tx] = 1
                maze[ty][tx] = maze[ny][nx] + 1


N, M = map(int, input().split())
maze = []
visited = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(N):
    visited.append([0 for _ in range(M)])

for _ in range(N):
    maze.append(list(map(int, input())))

for i in range(N):
    for j in range(M):
        if maze[i][j] == 1:
            if visited[i][j] == 0:
                bfs(i, j, visited)

print(maze[N - 1][M - 1])
