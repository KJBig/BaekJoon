from collections import deque


def bfs(x):
    q = deque()
    q.append(x)

    while q:
        x = q.popleft()
        if x == K:
            print(visited[x])
            exit()

        for i in (x - 1, x + 1, x * 2):
            if 0 <= i <= MAX and not visited[i]:
                visited[i] = visited[x] + 1
                q.append(i)


MAX = 10 ** 5
N, K = map(int, input().split())
visited = [0 for _ in range(MAX+1)]

bfs(N)