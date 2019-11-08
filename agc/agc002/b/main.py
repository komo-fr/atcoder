#!/usr/bin/env python3

N, M = list(map(int, input().split()))
xy_table = []

for _ in range(M):
    x, y = list(map(int, input().split()))
    xy_table.append((x, y))

red_box_dict = {i: False for i in range(1, N + 1)}
red_box_dict[1] = True
# 添字0はダミー
# 添字 = 箱の番号として扱う
n_box_list = [0] + [1] * N

for xy in xy_table:
    x, y = xy
    n_box_list[x] -= 1
    n_box_list[y] += 1
    if red_box_dict[x]:
        red_box_dict[y] = True

        if n_box_list[x] == 0:
            red_box_dict[x] = False

ans = len([v for v in red_box_dict.values() if v])

print(ans)
