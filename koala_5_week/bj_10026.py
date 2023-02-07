from collections import deque


def bfs(y, x, visit):
    q = deque()
    q.append((y, x))
    visit[y][x] = 1

    while q:
        ny, nx = q.popleft()

        for i in range(4):
            ty = ny + dy[i]
            tx = nx + dx[i]

            if -1 < ty < N and -1 < tx < N and visit[ty][tx] == 0 and board[ty][tx] == board[ny][nx]:
                q.append((ty, tx))
                visit[ty][tx] = 1


dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

N = int(input())
board = []
visited1 = [[0 for _ in range(N)] for _ in range(N)]
visited2 = [[0 for _ in range(N)] for _ in range(N)]

count = 0
count2 = 0

for _ in range(N):
    temp = []
    for i in input():
        temp.append(i)
    board.append(temp)

for i in range(N):
    for j in range(N):
        if visited1[i][j] == 0:
            bfs(i, j, visited1)
            count += 1

for i in range(N):
    for j in range(N):
        if board[i][j] == 'G':
            board[i][j] = 'R'

for i in range(N):
    for j in range(N):
        if visited2[i][j] == 0:
            bfs(i, j, visited2)
            count2 += 1

print(count, count2)
