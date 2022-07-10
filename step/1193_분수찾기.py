line = 1

X = int(input())

while X > line:
    X -= line
    line += 1

if line %2 == 0:
    num = X
    deno = line - X + 1
else:
    num = line - X + 1
    deno = X

print(str(num) + '/' + str(deno))
