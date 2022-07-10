n = int(input())
score = []
class_avg = []

for i in range(0,n):
    count = 0
    avg = 0

    nums = input().split()
    x = int(nums[0])

    for k in range(1, len(nums)):
        score.append(nums[k])

    for k in score:
        avg += int(k)
    avg /= x

    for k in score:
        if int(k) > avg:
            count += 1
    class_avg.append((count/x)*100)
    score.clear()

for i in class_avg:
    print("{:.3f}%".format(i))




