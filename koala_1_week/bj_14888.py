import sys
ssr = sys.stdin.readline

N = int(ssr())
nums = list(map(int, ssr().split()))
ops = list(map(int, ssr().split()))

max_num = -1e9
min_num = 1e9


def dfs(num, idx, add, sub, mul, div):
    global max_num, min_num

    if idx == N:
        max_num = max(max_num, num)
        min_num = min(min_num, num)
        return

    if add > 0:
        dfs(num + nums[idx], idx + 1, add - 1, sub, mul, div)
    if sub > 0:
        dfs(num - nums[idx], idx + 1, add, sub - 1, mul, div)
    if mul > 0:
        dfs(num * nums[idx], idx + 1, add, sub, mul - 1, div)
    if div > 0:
        dfs(int(num / nums[idx]), idx + 1, add, sub, mul, div - 1)


dfs(nums[0], 1, ops[0], ops[1], ops[2], ops[3])
print(max_num)
print(min_num)