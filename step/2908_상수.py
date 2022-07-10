n = input().split()

x = n[0]
y = n[1]

tran_x = ""
tran_y = ""

for i in x:
    tran_x = i + tran_x

for i in y:
    tran_y = i + tran_y

if int(tran_x) > int(tran_y):
    print(int(tran_x))
else:
    print(int(tran_y))
