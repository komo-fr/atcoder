#!/usr/bin/env python3

N, K = list(map(int, input().split()))
r_list = list(map(int, input().split()))
r_list = sorted(r_list, reverse=True)
r_list = sorted(r_list[:K])
c = 0

for r in sorted(r_list):
    c = (c + r) / 2

print(c)
