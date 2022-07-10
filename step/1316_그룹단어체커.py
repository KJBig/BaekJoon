count = 0
n = int(input())

for i in range(0, n):
    ary = ['0']
    now = 0
    x = input()
    for j in x:
        if ary[now] != j:
            '''
            print("now = ", now)
            print("ary = ", ary)
            '''
            if j not in ary:
                ary.append(j)
                now += 1
            else:
                count -= 1
                break
    count += 1

print(count)
