from collections import deque


def bfs(y, x):
    q = deque()
    q.append((y, x))
    visited[y][x] = 1

    while q:
        ny, nx = q.popleft()

        for i in range(8):
            ty = ny + dy[i]
            tx = nx + dx[i]

            if -1 < ty < H and -1 < tx < W and visited[ty][tx] == 0 and board[ty][tx] == 1:
                q.append((ty, tx))
                visited[ty][tx] = 1


dy = [0, 0, 1, -1, 1, -1, 1, -1]
dx = [1, -1, 0, 0, 1, 1, -1, -1]

while 1:
    W, H = map(int, input().split())

    if W == 0 and H == 0:
        exit()

    board = []
    visited = []
    count = 0

    for _ in range(H):
        board.append(list(map(int, input().split())))
        visited.append(list(0 for _ in range(W)))

    for i in range(H):
        for j in range(W):
            if board[i][j] == 1 and visited[i][j] == 0:
                bfs(i, j)
                count += 1

    print(count)
