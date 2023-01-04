import sys
ssr = sys.stdin.readline


def dfs(str_len, num):
    if str_len == L:
        moN = 0
        jaN = 0
        for i in pwd:
            if i in mo:
                moN += 1
            else:
                jaN += 1
        if moN >= 1 and jaN >= 2:
            print(''.join(i for i in pwd))
        return

    for i in range(num, C):
        pwd.append(als[i])
        dfs(str_len + 1, i + 1)
        pwd.pop()


L, C = map(int, ssr().split())
als = list(map(str, ssr().split()))
als.sort()
mo = ['a', 'e', 'i', 'o', 'u']
pwd = []

dfs(0, 0)
