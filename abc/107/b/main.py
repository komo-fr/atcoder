#!/usr/bin/env python3

H, W = list(map(int, input().split()))
a_table = []

for _ in range(H):
    a_list = input()
    if set(a_list) == {"."}:
        continue
    a_table.append(a_list)

a_table = list(zip(*a_table))
b_table = []
for a_list in a_table:
    if set(a_list) == {"."}:
        continue
    b_table.append(a_list)

b_table = list(zip(*b_table))
for b in b_table:
    print("".join(b))
