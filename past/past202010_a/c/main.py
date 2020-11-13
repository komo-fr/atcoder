#!/usr/bin/env python3
from collections import Counter

N, M = list(map(int, input().split()))
a_table = []

for _ in range(N):
    a_list = input()
    a_table.append(a_list)

for i, a_list in enumerate(a_table):
    c_text = ""
    for j, a in enumerate(a_list):
        count = 0
        adj_list = []
        if i != 0:  # 上
            adj_list.append(a_table[i - 1][j])
            if j != 0:
                # 左
                adj_list.append(a_table[i - 1][j - 1])
            if j < M - 1:
                # 右
                adj_list.append(a_table[i - 1][j + 1])

        if i < N - 1:  # 下
            adj_list.append(a_table[i + 1][j])
            if j != 0:
                adj_list.append(a_table[i + 1][j - 1])
            if j < M - 1:
                adj_list.append(a_table[i + 1][j + 1])

        if j != 0:
            adj_list.append(a_table[i][j - 1])
        if j < M - 1:
            adj_list.append(a_table[i][j + 1])
        adj_list.append(a_table[i][j])

        # print(f"{i=}, {j=}, {adj_list}")
        c_text += str(Counter(adj_list)["#"])
    print(c_text)
