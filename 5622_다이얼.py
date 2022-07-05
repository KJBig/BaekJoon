ar =[0,'ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']

X = input()
count = 0
for i in range(1,len(ar)):
    for k in X:
        if k in ar[i]:
            count += 2
            for j in range(0,i):
                count += 1

print(count)