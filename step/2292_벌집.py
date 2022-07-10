N = int(input())
count = 1
bound = 1

while N > bound:
    bound = bound + (6 * count)
    count += 1

print(count)
