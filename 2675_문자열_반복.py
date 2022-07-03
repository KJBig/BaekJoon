QR_code = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./:"

n = int(input())

for i in range(0,n):
    S = input()
    R = 0
    P = []
    for q in range(0,len(S)):
        if q == 0:
            R = int(S[q])
        else:
            P.append(S[q])

    for j in P:
        if j in QR_code:
            for k in range(0, R):
                print(j, end = "")
    print()