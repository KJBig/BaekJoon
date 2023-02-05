# from collections import deque
#
#
# def bfs(u):
#     que = deque()
#     que.append(u)
#
#     while que:
#         nu = que.popleft()
#         for i in ary[nu]:
#             if visited[i] == 0:
#                 visited[i] = 1
#                 que.append(i)
#
#
# N, M = map(int, input().split())
#
# ary = [[] for _ in range(N+1)]
# visited = [0 for _ in range(N + 1)]
# count = 0
#
# for _ in range(M):
#     u, v = map(int, input().split())
#     ary[u].append(v)
#     ary[v].append(u)
#
# for i in range(1, N+1):
#     if visited[i] == 0:
#         if ary[i]:
#             bfs(i)
#         visited[i] = 1
#         count += 1
#
# print(count)


from collections import deque


def bfs(start):
    queue = deque([start])
    visited[start] = True
    while queue:
        node = queue.popleft()
        for i in graph[node]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)


N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


visited = [False] * (1 + N)
count = 0


for i in range(1, N + 1):
    if not visited[i]:
        if not graph[i]:
            count += 1
            visited[i] = True
        else:
            bfs(i)
            count += 1

print(count)