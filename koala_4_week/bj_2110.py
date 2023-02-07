n, c = map(int, input().split())

house = []
for i in range(n):
    house.append(int(input()))

house.sort()


def binary_search(left, right):
    while left <= right:
        mid = (left + right) // 2
        current = house[0]
        count = 1

        for i in range(1, len(house)):
            if house[i] >= current + mid:
                count += 1
                current = house[i]

        if count >= c:
            global result
            left = mid + 1
            result = mid
        else:
            right = mid - 1


start = 1
end = house[-1] - house[0]
result = 0

binary_search(start, end)
print(result)
