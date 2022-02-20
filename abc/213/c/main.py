#!/usr/bin/env python3
from collections import defaultdict

H, W, N = list(map(int, input().split()))

ab_table = []

row_dict = defaultdict(lambda: [])
col_dict = defaultdict(lambda: [])
p_dict = {}

for i in range(N):
    a, b = list(map(int, input().split()))
    row_dict[a].append(i + 1)
    col_dict[b].append(i + 1)
    p_dict[i + 1] = (a, b)

new_row_dict = {}
new_col_dict = {}
minus_row = 0
minus_col = 0

for h in range(1, H + 1):
    print(h)
    if not row_dict[h]:
        # 1つも数字がない
        minus_row += 1
    else:
        # 数字がある
        new_row_dict[h] = h - minus_row

for w in range(1, W + 1):
    if not col_dict[w]:
        # 1つも数字がない
        minus_col += 1
    else:
        # 数字がある
        new_row_dict[w] = w - minus_col

for i in range(N):
    node = i + 1
    a, b = p_dict[node]
    a = new_row_dict[a]
    b = new_row_dict[b]
    print(a, b)
