#!/usr/bin/env python3

N, M = list(map(int, input().split()))
a_list = list(map(int, input().split()))
x_list = []

total = 0
tmp_list = []
max_sum = -float("inf")

for i, a in enumerate(a_list):
    if a < 0:
        s = sum(tmp_list)
        max_sum = s if s > max_sum else max_sum
        tmp_list = []
        continue
    tmp_list.append(a * (i + 1))

ans = max_sum
print(ans)
