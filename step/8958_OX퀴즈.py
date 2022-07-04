check = []

n = int(input())

for j in range(0, n):
    now = 0
    score = 0
    check.clear()
    x = input()

    for i in x:
        check.append(i)

    for i in check:
        if i == 'O':
            now += 1
            score += now
        elif i == 'X':
            now = 0
    print(score)

