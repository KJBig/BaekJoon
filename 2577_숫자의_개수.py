A = int(input())
B = int(input())
C = int(input())

num = A*B*C

n = [0 for i in range(10)]

for i in str(num):
    n[int(i)] += 1

for i in n:
    print(i)