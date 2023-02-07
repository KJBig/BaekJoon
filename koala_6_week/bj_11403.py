from collections import deque


def bfs(i, visit):
    q = deque()
    q.append(i)

    while q:
        ni = q.popleft()

        for j in range(N):
            if visit[j] == 0 and board[ni][j] == 1:
                visit[j] = 1
                q.append(j)
                result[i][j] = 1


N = int(input())

board = []
result = [[0] * N for _ in range(N)]

for _ in range(N):
    board.append(list(map(int, input().split())))

for i in range(N):
    visited = [0] * N
    bfs(i, visited)

for i in result:
    for j in i:
        print(j, end=" ")
    print()
