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

            if -1 < ty < N and -1 < tx < M and visit[ty][tx] == 0 and [tx, ty] in ary:
                que.append((ty, tx))
                visit[ty][tx] = 1


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

T = int(input())
for _ in range(T):
    ary = []
    visited = []
    M, N, T = map(int, input().split())

    for i in range(N):
        temp = [0 for _ in range(M)]
        visited.append(temp)

    for _ in range(T):
        ary.append(list(map(int, input().split())))

    count = 0
    for i in ary:
        x = i[0]
        y = i[1]
        if visited[y][x] == 0:
            bfs(y, x, visited)
            count += 1

    print(count)
