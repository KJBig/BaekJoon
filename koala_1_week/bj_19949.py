import sys

ssr = sys.stdin.readline


def backT(zero_len, pn, ppn):
    global count

    if zero_len == 10:
        score = 0
        for i in range(0, 10):
            if zero[i] == A[i]:
                score += 1
        if score >= 5:
            count += 1
        return

    for i in range(1, 6):
        if pn == i and ppn == i:
            continue
        else:
            zero.append(i)
            backT(zero_len+1, i, pn)
            zero.pop()


A = list(map(int, ssr().split()))
zero = []
count = 0
backT(0, 0, 0)

print(count)
