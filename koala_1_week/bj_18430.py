import sys
ssr = sys.stdin.readline


def RU(y, x):
    return (board[y][x] * 2) + board[y + 1][x] + board[y][x - 1]


def RD(y, x):
    return (board[y][x] * 2) + board[y - 1][x] + board[y][x - 1]


def LD(y, x):
    return (board[y][x] * 2) + board[y - 1][x] + board[y][x + 1]


def LU(y, x):
    return (board[y][x] * 2) + board[y + 1][x] + board[y][x + 1]


def backT(y, x):
    global maxS

    if y == H-1 and x == W:
        maxS = max(maxS, sum(boomerangs))
        return

    if x == W:
        x = 0
        y += 1

    if 0 < x and y < H - 1 and not visited[y][x] and not visited[y + 1][x] and not visited[y][x - 1]:
        visited[y][x] = True
        visited[y + 1][x] = True
        visited[y][x - 1] = True

        boomerangs.append(RU(y, x))
        backT(y, x + 1)
        boomerangs.pop()

        visited[y][x] = False
        visited[y + 1][x] = False
        visited[y][x - 1] = False

    if 0 < x and 0 < y and not visited[y][x] and not visited[y - 1][x] and not visited[y][x - 1]:
        visited[y][x] = True
        visited[y - 1][x] = True
        visited[y][x - 1] = True

        boomerangs.append(RD(y, x))
        backT(y, x + 1)
        boomerangs.pop()

        visited[y][x] = False
        visited[y - 1][x] = False
        visited[y][x - 1] = False

    if x < W - 1 and 0 < y and not visited[y][x] and not visited[y - 1][x] and not visited[y][x + 1]:

        visited[y][x] = True
        visited[y - 1][x] = True
        visited[y][x + 1] = True

        boomerangs.append(LD(y, x))
        backT(y, x + 1)
        boomerangs.pop()

        visited[y][x] = False
        visited[y - 1][x] = False
        visited[y][x + 1] = False

    if x < W - 1 and y < H - 1 and not visited[y][x] and not visited[y + 1][x] and not visited[y][x + 1]:

        visited[y][x] = True
        visited[y + 1][x] = True
        visited[y][x + 1] = True

        boomerangs.append(LU(y, x))
        backT(y, x + 1)
        boomerangs.pop()

        visited[y][x] = False
        visited[y + 1][x] = False
        visited[y][x + 1] = False

    backT(y, x + 1)


H, W = map(int, ssr().split())
board = []
boomerangs = []
visited = []

maxS = 0

for i in range(H):
    board.append(list(map(int, ssr().split())))

    temp = [False] * W
    visited.append(temp)

backT(0, 0)

print(maxS)
