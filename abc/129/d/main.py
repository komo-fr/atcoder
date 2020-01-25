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
    c_table.append([dict(l=0, r=0, u=0, b=0)] * W)

for i in range(H):
    for j in range(W):
        if j != 0:
            # 左側の数を数える
            if s_table[i][j - 1] == "." and s_table[i][j] == ".":
                c_table[i][j]["l"] = c_table[i][j - 1]["l"] + 1
                total_table[i][j] += c_table[i][j]["l"]
        if j != 0:
            if s_table[i][W - j] == "." and s_table[i][W - j - 1] == ".":
                c_table[i][W - j - 1]["r"] = c_table[i][W - j]["r"] + 1
                total_table[i][W - j - 1] += c_table[i][W - j - 1]["r"]
        if i != 0:
            # 上側の数を数える
            if s_table[i - 1][j] == "." and s_table[i][j] == ".":
                c_table[i][j]["u"] = c_table[i - 1][j]["u"] + 1
                total_table[i][j] += c_table[i][j]["u"]
        if i != 0:
            if s_table[H - i][j] == "." and s_table[H - i - 1][j] == ".":
                c_table[H - i - 1][j]["b"] = c_table[H - i][j]["b"] + 1
                total_table[H - i - 1][j] += c_table[H - i - 1][j]["b"]
ans = np.array(total_table).max() + 1

print(ans)
