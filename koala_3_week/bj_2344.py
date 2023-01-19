import sys

ssr = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
dir = [1, 0, 3, 2]


def out(x, y):
    if x == -1:
        return 2 * N + 2 * M - y
    elif y == -1:
        return x + 1
    elif x == N:
        return N + y + 1
    else:
        return 2 * N + M - x


def search(start, direct):
    x, y = start
    while 0 <= x < N and 0 <= y < M:
        if box[x][y] == 1:
            direct = dir[direct]
        x += dx[direct]
        y += dy[direct]
    return str(out(x, y))


N, M = map(int, ssr().split())
box = [list(map(int, ssr().split())) for _ in range(N)]
result = []

for i in range(N):
    direction = 1
    result.append(search([i, 0], direction))
for i in range(M):
    direction = 0
    result.append(search([N - 1, i], direction))
for i in range(N - 1, -1, -1):
    direction = 3
    result.append(search([i, M - 1], direction))
for i in range(M - 1, -1, -1):
    direction = 2
    result.append(search([0, i], direction))
print(' '.join(result))
