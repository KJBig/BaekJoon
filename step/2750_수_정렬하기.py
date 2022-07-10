n = int(input())
ary = []
for i in range(0,n):
    ary.append(int(input()))

for i in range(0, len(ary)):
    for j in range(0, len(ary)):
        if ary[i] < ary[j]:
            ary[i], ary[j] = ary[j], ary[i]


for i in ary:
    print(i)
