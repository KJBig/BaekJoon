sequence = 10000
remove_num = []
natural_num = list(range(1,sequence+1))

for n in range(1,sequence+1):
    num = n
    for i in str(n):
        num += int(i)

    if num <= sequence:
        remove_num.append(num)

for i in set(remove_num):
    natural_num.remove(i)

for i in natural_num:
    print(i)

