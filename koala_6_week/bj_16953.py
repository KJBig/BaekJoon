from collections import deque


def bfs(a):
    q = deque()
    q.append((a, 1))

    while q:
        x, y = q.popleft()
        if x > B:
            continue
        if x == B:
            print(y)
            exit()

        q.append(((x * 2), y + 1))
        q.append(((x * 10) + 1, y + 1))


A, B = map(int, input().split())

bfs(A)
print(-1)
