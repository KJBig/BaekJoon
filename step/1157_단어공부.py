alpha ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
count = [0 for i in range(0,26)]
where = 0
max_num = 0
same = 0

st = input()

for i in st:
    for j in range(0,26):
        if alpha[j] == i.upper():
            count[j] += 1

for i in range(0, len(count)):
    if max_num < count[i]:
        max_num = count[i]
        where = i
        same = 0
    elif max_num == count[i]:
        same = 1

if same == 1:
    print("?")
else:
    print(alpha[where])
