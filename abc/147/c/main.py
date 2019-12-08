#!/usr/bin/env python3
import itertools

N = int(input().split()[0])
# a_list = list(map(int, input().split()))
a_list = []
xy_list_list = []

for _ in range(N):
    a = int(input().split()[0])
    a_list.append(a)
    xy_list = []
    for _ in range(a):
        x, y = list(map(int, input().split()))
        xy_list.append((x, y))
    xy_list_list.append(xy_list)

# 2 ** 3 パターン
p_list = list(itertools.product([0, 1], repeat=N))
max_c = 0

for pattern in p_list:  # 2 ** 15
    is_ok = True
    for i in range(N):  # 15
        if pattern[i] == 0:
            # 真偽不明
            continue
        for xy in xy_list_list[i]:  # 15
            x, y = xy
            x = x - 1
            if pattern[x] != y:
                # 矛盾
                is_ok = False
                break
        if not is_ok:
            # 矛盾
            break
    if is_ok:
        max_c = max(max_c, sum(pattern))

ans = max_c
print(ans)
