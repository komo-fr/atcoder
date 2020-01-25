#!/usr/bin/env python3
import numpy as np

H, W = list(map(int, input().split()))
s_table = []
total_table = []
c_table = []
for _ in range(H):
    s = list(input())
    s_num = [0 if ch == "#" else 1 for ch in s]
    s_table.append(s_num)

s_table = np.pad(s_table, 1, "constant")

l_table = np.zeros((H + 2, W + 2))
r_table = np.zeros((H + 2, W + 2))
u_table = np.zeros((H + 2, W + 2))
b_table = np.zeros((H + 2, W + 2))

for i in range(1, W):
    l_table[:, i] = (l_table[:, i - 1] + 1) * s_table[:, i]
    r_table[:, -i - 1] = (r_table[:, -i] + 1) * s_table[:, -i - 1]


for i in range(1, H):
    u_table[i] = (u_table[i - 1] + 1) * s_table[i]
    b_table[-i - 1] = (b_table[-i] + 1) * s_table[-i - 1]

total_table = l_table + r_table + u_table + b_table
ans = np.max(total_table)

if H <= 1:
    ans += 2
if W <= 1:
    ans += 2
ans = int(ans) - 3

print(ans)
