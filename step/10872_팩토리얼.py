def fun(x):
    if x == 0:
        return 1
    return x * fun(x-1)


x = int(input())
print(fun(x))
