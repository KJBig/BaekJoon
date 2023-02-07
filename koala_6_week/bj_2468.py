from collections import deque

def bfs(y, x, s):
    q = deque()
    q.append((y, x))
    visited[y][x] = 1

    while q:
        ny, nx = q.popleft()

        for i in range(4):
            ty = ny + dy[i]
            tx = nx + dx[i]

            if -1 < ty < N and -1 < tx < N and visited[ty][tx] == 0 and board[ty][tx] > s:
                visited[ty][tx] = 1
                q.append((ty, tx))


dy = [0, 0, 1, -1]
dx = [-1, 1, 0, 0]

N = int(input())
board = []
minNum = 1e9
maxNum = -1e9
maxCount = []

for _ in range(N):
    board.append(list(map(int, input().split())))

for i in range(N):
    for j in board[i]:
        maxNum = max(maxNum, j)

for k in range(maxNum + 1):
    visited = [[0] * N for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0 and board[i][j] > k:
                bfs(i, j, k)
                count += 1
    maxCount.append(count)
    if count == 0:
        break


print(max(maxCount))
