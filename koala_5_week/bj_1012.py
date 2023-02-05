from collections import deque


def bfs(y, x):
    count = 1
    que = deque()
    que.append((y, x))
    visited[y][x] = 1
    while que:
        ny, nx = que.popleft()
        for i in range(4):
            ty = ny + dy[i]
            tx = nx + dx[i]
            if -1 < ty < N and -1 < tx < N and visited[ty][tx] == 0 and ary[ty][tx] == 1:
                que.append((ty, tx))
                visited[ty][tx] = 1
                count += 1
    return count


N = int(input())
ary = []
visited = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(N):
    temp = [0 for _ in range(N)]
    visited.append(temp)

for _ in range(N):
    ary.append(list(map(int, input())))

totalH = []

for i in range(N):
    for j in range(N):
        if ary[i][j] == 1:
            if visited[i][j] == 0:
                k = bfs(i, j)
                totalH.append(k)

totalH.sort()
print(len(totalH))
for i in totalH:
    print(i)
