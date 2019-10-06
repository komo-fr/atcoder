# https://atcoder.jp/contests/abc087/tasks/arc090_a
# C - Candies

import itertools

n = int(input().split()[0])

a_matrix = []
a_matrix.append(list(map(int, input().split())))
a_matrix.append(list(map(int, input().split())))

max_cost = -float('inf')

for i in range(n):
    cost_list = []
    cost_list.append(a_matrix[0][:i+1])
    cost_list.append(a_matrix[1][i:])
    cost_list = list(itertools.chain.from_iterable(cost_list))
    if sum(cost_list) > max_cost:
        max_cost = sum(cost_list)

print(max_cost)
