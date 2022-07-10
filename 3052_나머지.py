divide_num = 42
rest = []
count_arry = [0 for i in range(0,divide_num)]
count = 0

for i in range(0, 10):
    n = int(input())
    rest.append(n%divide_num)

for i in rest:
    count_arry[i] += 1

for i in count_arry:
    if i != 0:
        count += 1

print(count)