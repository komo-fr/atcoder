#!/usr/bin/env python3
import copy
import itertools

R, C, K = list(map(int, input().split()))
s_table = []

for _ in range(R):
    s = list(input())
    s_table.append(s)

x_min, x_max = K, R - K + 1
y_min, y_max = K, C - K + 1

count = 0
w_table = [[0, 0] * C for _ in range(R)]

# 満点解法
# 縦方向に何個連続するか数える

cumsum_table = [[[0, 0] for _ in range(C)] for _ in range(R)]

for j in range(C):
    cumsum_up = 0
    cumsum_down = 0
    for i in range(R):
        s_1 = s_table[i][j]
        s_2 = s_table[-(i + 1)][j]
        if s_1 == "o":
            # 上にあるやつ
            cumsum_up += 1
        else:
            cumsum_up = 0
        cumsum_table[i][j][0] = cumsum_up

        if s_2 == "o":
            # 下にあるやつ
            cumsum_down += 1
        else:
            cumsum_down = 0
        cumsum_table[-(i + 1)][j][1] = cumsum_down

expected_list = [i + 1 for i in range(K - 1)]
expected_list = expected_list + [K] + list(reversed(expected_list))
count = 0

for x in range(x_min, x_max + 1):  # OK
    for y in range(y_min, y_max + 1):  # OK
        # x, yを固定
        i = 0
        is_ok = True
        for j in range(y - K + 1, y + K):  # OK
            c = cumsum_table[x - 1][j - 1]  # OK

            if c[0] < expected_list[i] or c[1] < expected_list[i]:
                is_ok = False
                break
            i += 1
        if is_ok:
            count += 1

ans = count
print(ans)
