def dfs(now, count):
    global G, U, D
    visited[now] = 1

    if now == G:
        print(count)
        exit()

    if G > now:
        move = U
    else:
        move = -D

    if visited[now + move]:
        print("user the stairs")
        exit()

    dfs(now + move, count + 1)


F, S, G, U, D = map(int, input().split())

visited = [0 for _ in range(F+1)]
dfs(S, 0)
