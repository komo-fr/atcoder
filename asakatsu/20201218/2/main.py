#!/usr/bin/env python3

N = int(input().split()[0])

s_table = []
for _ in range(N):
    s_list = list(input())
    s_table.append(s_list)

x_table = list(zip(*s_table))

for x_list in x_table:
    print("".join(x_list[::-1]))