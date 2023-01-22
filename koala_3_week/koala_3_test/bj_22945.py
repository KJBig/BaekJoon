import sys

ssr = sys.stdin.readline

N = int(ssr())
L = list(map(int, ssr().split()))

maxTeam = 0
left = 0
right = N - 1

while left != right:
    maxTeam = max(maxTeam, (right - left - 1) * min(L[left], L[right]))
    if L[left] > L[right]:
        right -= 1
    else:
        left += 1

print(maxTeam)
