import sys
ssr = sys.stdin.readline

N = int(ssr())
M = 1e9

Liquids = list(map(int, ssr().split()))
left = 0
right = N-1

while left < right:
    temp = Liquids[left] + Liquids[right]
    if abs(M) > abs(temp):
        M = temp
    if temp < 0:
        left += 1
    else:
        right -= 1

print(M)


