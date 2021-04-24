#!/usr/bin/env python3

N, M = list(map(int, input().split()))
a_table = []

for _ in range(N):
    ka_list = list(map(int, input().split()))
    a_list = ka_list[1:]
    a_table.append(a_list)
P, Q = list(map(int, input().split()))
b_list = list(map(int, input().split()))
b_set = set(b_list)
count = 0

for a_list in a_table:
    # print(a_list)
    a_set = set(a_list)
    if len(a_set & b_set) >= Q:
        count += 1
ans =count
print(ans)
