from collections import deque


def bfs(y, x):
    q = deque()
    q.append((y, x))
    bcount = 1

    visited[y][x] = 1
    while q:
        ny, nx = q.popleft()

        for i in range(4):
            ty = ny + dy[i]
            tx = nx + dx[i]

            if -1 < ty < M and -1 < tx < N and visited[ty][tx] == 0 and board[ty][tx] == 0:
                q.append((ty, tx))
                visited[ty][tx] = 1
                bcount += 1
    return bcount


dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

M, N, K = map(int, input().split())

board = [[0] * N for _ in range(M)]
visited = [[0] * N for _ in range(M)]
arange = []


for i in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for j in range(y1, y2):
        for k in range(x1, x2):
            board[j][k] = 1

for i in range(M):
    for j in range(N):
        if visited[i][j] == 0 and board[i][j] == 0:
            arange.append(bfs(i, j))

print(len(arange))
arange.sort()
for i in arange:
    print(i, end=" ")
