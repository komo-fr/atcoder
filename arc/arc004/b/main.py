#!/usr/bin/env python3

N = int(input().split()[0])
d_list = []

for _ in range(N):
    d = int(input().split()[0])
    d_list.append(d)

max_d = sum(d_list)
min_d = max(max(d_list) - (max_d - max(d_list)), 0)

print(max_d)
print(min_d)
