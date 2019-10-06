# https://atcoder.jp/contests/abc092/tasks/arc093_a
# C - Traveling Plan

N = int(input().split()[0])
a_list = list(map(int, input().split()))
a_list = [0] + a_list + [0]
total_cost = 0
for x, y in zip(a_list[:-1], a_list[1:]):
    total_cost += abs(x - y)

diff_list = []

for i in range(1, N + 1): # 10 ** 5
    before = abs(a_list[i-1] - a_list[i]) + abs(a_list[i] - a_list[i+1])
    after = abs(a_list[i-1] - a_list[i+1])
    diff_list.append(before - after)

ans = '\n'.join([str(total_cost - d) for d in diff_list])
print(ans)
