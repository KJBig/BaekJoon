S = input()
alpha = [0 for i in range(0, 26)]
abc ="abcdefghijklmnopqrstuvwxyz"

for i in abc:
    if i in S:
        alpha[abc.index(i)] = S.index(i)
    else:
        alpha[abc.index(i)] = -1

for i in alpha:
    print(i, end=" ")