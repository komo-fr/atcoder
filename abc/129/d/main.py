#!/usr/bin/env python3
import numpy as np

H, W = list(map(int, input().split()))
s_table = []
total_table = []
c_table = []
for _ in range(H):
    s = list(input())
    s_table.append(s)
    total_table.append([0] * W)
    c_table.append([[0] * 4 for _ in range(W)])

for i in range(H):
    for j in range(W):
        if j != 0:
            # 左側の数を数える
            if s_table[i][j - 1] == "." and s_table[i][j] == ".":
                c_table[i][j][0] = c_table[i][j - 1][0] + 1
                total_table[i][j] += c_table[i][j][0]
        if j != 0:
            # 右側の数を数える
            if s_table[i][W - j] == "." and s_table[i][W - j - 1] == ".":
                c_table[i][W - j - 1][1] = c_table[i][W - j][1] + 1
                total_table[i][W - j - 1] += c_table[i][W - j - 1][1]
        if i != 0:
            # 上側の数を数える
            if s_table[i - 1][j] == "." and s_table[i][j] == ".":
                c_table[i][j][2] = c_table[i - 1][j][2] + 1
                total_table[i][j] += c_table[i][j][2]
        if i != 0:
            # 下側の数を数える
            if s_table[H - i][j] == "." and s_table[H - i - 1][j] == ".":
                c_table[H - i - 1][j][3] = c_table[H - i][j][3] + 1
                total_table[H - i - 1][j] += c_table[H - i - 1][j][3]
ans = np.array(total_table).max() + 1

print(ans)
