#!/usr/bin/env python3

N, M = list(map(int, input().split()))
xy_table = []

for _ in range(M):
    x, y = list(map(int, input().split()))
    xy_table.append((x, y))

red_box_list = [1]
# 添字0はダミー
# 添字 = 箱の番号として扱う
n_box_list = [0] + [1] * N

for xy in xy_table:
    x, y = xy
    n_box_list[x] -= 1
    n_box_list[y] += 1
    if x in red_box_list:
        if y not in red_box_list:
            red_box_list.append(y)

        if n_box_list[x] == 0:
            red_box_list.remove(x)

ans = len(red_box_list)

print(ans)
