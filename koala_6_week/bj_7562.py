from collections import deque


def bfs(y, x):
    q = deque()
    q.append((y, x))
    visited[y][x] = 1
    board[y][x] = 0

    while q:
        y, x = q.popleft()

        for i in range(8):
            ty = y + dy[i]
            tx = x + dx[i]
            if -1 < ty < N and -1 < tx < N and visited[ty][tx] == 0:
                visited[ty][tx] = 1
                board[ty][tx] = board[y][x] + 1
                q.append((ty, tx))


dy = [2, 1, -1, -2, -2, -1, 1, 2]
dx = [1, 2, 2, 1, -1, -2, -2, -1]
cAry = []
T = int(input())

for i in range(T):
    N = int(input())
    visited = [[0] * N for _ in range(N)]
    board = [[0] * N for _ in range(N)]
    X, Y = map(int, input().split())
    TX, TY = map(int, input().split())

    bfs(Y, X)

    cAry.append(board[TY][TX])

for i in cAry:
    print(i)
