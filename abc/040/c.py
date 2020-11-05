# https://atcoder.jp/contests/abc040/tasks/abc040_c
# C - 柱柱柱柱柱

N = int(input().split()[0])
a_list = list(map(int, input().split()))

cost_list = [float('inf')] * N
cost_list[0] = 0

for i in range(N - 1):
    w = cost_list[i] + abs(a_list[i] - a_list[i + 1])
    cost_list[i + 1] = min(cost_list[i + 1], w)

    if i + 2 <= N - 1:
        w = cost_list[i] + abs(a_list[i] - a_list[i + 2])
        cost_list[i + 2] = min(cost_list[i + 2], w)

ans = cost_list[-1]
print(ans)
