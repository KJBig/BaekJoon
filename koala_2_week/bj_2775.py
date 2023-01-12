import sys

ssr = sys.stdin.readline


def HMP(_k, _n):
    if _k == 0:
        return _n
    else:
        if _n == 1:
            return HMP(_k - 1, _n)
        else:
            result = 0
            for i in range(1, _n + 1):
                result += HMP(_k - 1, i)
            return result


T = int(ssr())

for i in range(T):
    k, n = int(ssr()), int(ssr())
    print(HMP(k, n))