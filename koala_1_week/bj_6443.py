import sys
ssr = sys.stdin.readline


def backT(word, idx):
    if len(word) == len(words[idx]):
        print(''.join(word))
        return

    for k in wordD[idx]:
        if wordD[idx][k]:
            word.append(k)
            wordD[idx][k] -= 1

            backT(word, idx)

            word.pop()
            wordD[idx][k] += 1


N = int(ssr())
wordD = []
words = []

for i in range(N):
    inWord = sorted(ssr().strip())
    words.append(inWord)
    visited = {}

    for j in inWord:
        if j in visited:
            visited[j] += 1
        else:
            visited[j] = 1

    wordD.append(visited)


for i in range(N):
    backT([], i)