from collections import deque


def bfs(ary):
    q = deque()
    q.append(1)

    while q:
        x = q.popleft()

        for i in ary[x]:
            if pAry[i] == 0 and visited[i] == 0:
                pAry[i] = x
                q.append(i)
                visited[i] = 1


N = int(input())
nodes = [[] for _ in range(N + 1)]
pAry = [0] * (N + 1)
visited = [0] * (N + 1)

for i in range(N - 1):
    p, c = map(int, input().split())
    nodes[p].append(c)
    nodes[c].append(p)

bfs(nodes)

for i in range(2, N+1):
    print(pAry[i])
