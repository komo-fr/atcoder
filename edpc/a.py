# https://atcoder.jp/contests/dp/tasks/dp_a
# A - Frog 1

n = int(input().split()[0])
h_list = list(map(int, input().split()))

min_com_cost = [0]

for i in range(1, len(h_list)):
    # 1個前からくるパターン
    cost_1step = min_com_cost[i-1] + abs(h_list[i] - h_list[i-1])

    # 2個前からくるパターン
    if i > 1:
        cost_2step = min_com_cost[i-2] + abs(h_list[i] - h_list[i-2])
    else:
        cost_2step = float('inf')

    cost = min(cost_1step, cost_2step)
    min_com_cost.append(cost)

print(min_com_cost[-1])
