import sys

ssr = sys.stdin.readline


def backT(kitsN, day):
    global count

    if len(plan) == N:
        weight = 500

        for i in plan:
            weight -= K - i
            if weight < 500:
                return
        count += 1
        return

    for i in range(N):
        if not used[i]:
            used[i] = True
            plan.append(kits[i])
            backT(kitsN + 1, day + 1)
            used[i] = False
            plan.pop()


N, K = map(int, ssr().split())
kits = list(map(int, ssr().split()))

count = 0
plan = []
used = [False] * N

backT(0, 1)

print(count)
