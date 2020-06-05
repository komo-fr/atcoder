#!/usr/bin/env python3
import itertools

N = int(input().split()[0])
a_dict = {}
total = 0
for i in range(N - 1):
    a_list = list(map(int, input().split()))
    pre_index = i + 2
    for j, a in enumerate(a_list):
        a_dict[(i + 1, pre_index + j)] = a
    total += sum(a_list)

# 1つの場合
h_list = [total]
# 2つまたは3つに分ける場合
p_list = list(itertools.product([0, 1], repeat=N)) + list(
    itertools.product([0, 1, 2], repeat=N)
)

for p in p_list:
    group_0 = []
    group_1 = []
    group_2 = []
    h = 0
    for i, v in enumerate(p):
        if v == 0:
            for member in group_0:
                h += a_dict[(member, i + 1)]
            group_0.append(i + 1)
        elif v == 1:
            for member in group_1:
                h += a_dict[(member, i + 1)]
            group_1.append(i + 1)
        else:
            for member in group_2:
                h += a_dict[(member, i + 1)]
            group_2.append(i + 1)

    h_list.append(h)
ans = max(h_list)

print(ans)
