#!/usr/bin/env python3

H, W, N = list(map(int, input().split()))

p_dict = {}
a_list = []
b_list = []

for i in range(N):
    a, b = list(map(int, input().split()))
    p_dict[i + 1] = (a, b)
    a_list.append(a)
    b_list.append(b)

a_list = sorted(list(set(a_list)))
b_list = sorted(list(set(b_list)))

new_row_dict = {}

for i, a in enumerate(a_list):
    new_row_dict[a] = i + 1

new_col_dict = {}

for i, b in enumerate(b_list):
    new_col_dict[b] = i + 1


for i in range(N):
    node = i + 1
    a, b = p_dict[node]
    a = new_row_dict[a]
    b = new_col_dict[b]
    print(a, b)
