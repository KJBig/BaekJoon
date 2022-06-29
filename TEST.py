i = list(range(0,100))
j = list(range(0,100,2))

for k in j:
    i.remove(k)

print(i)