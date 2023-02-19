#!/usr/bin/env python3

D = int(input().split()[0])
N = int(input().split()[0])
lr_list = []

for _ in range(N):
    l, r = list(map(int, input().split()))
    lr_list.append((l, r))

diff_list = [0] * D
for lr in lr_list:
    l, r = lr
    diff_list[l-1] += 1
    if r != D:
        diff_list[r] -= 1

cumsum_list = []
for i, d in enumerate(diff_list):
    if i == 0:
        cumsum_list.append(d)
        continue
    cumsum_list.append(cumsum_list[i-1] + d)

[print(x) for x in cumsum_list]