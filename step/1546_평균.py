score = []
avg = 0

n = int(input())

x = input().split()

for i in x:
    score.append(int(i))

score.sort()
max = score[n-1]

for i in range(0, n):
    score[i] = score[i]/max*100

for i in score:
    avg += i

avg /= n

print(avg)
