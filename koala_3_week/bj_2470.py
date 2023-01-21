import sys
ssr = sys.stdin.readline

N = int(ssr())
Liquids = list(map(int, ssr().split()))
Liquids.sort()

left = 0
right = N - 1

result = abs(Liquids[left] + Liquids[right])
final = [Liquids[left], Liquids[right]]

while left < right:
    sumM = Liquids[left] + Liquids[right]

    if abs(sumM) < result:
        result = abs(sumM)
        final = [Liquids[left], Liquids[right]]
        if result == 0:
            break
    if sumM < 0:
        left += 1
    else:
        right -= 1

print(final[0], final[1])
