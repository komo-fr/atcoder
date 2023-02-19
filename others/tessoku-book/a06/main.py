#!/usr/bin/env python3
# A06 - How Many Guests?
# 一次元の累積和（1）
# https://atcoder.jp/contests/tessoku-book/tasks/math_and_algorithm_ai

N, Q = list(map(int, input().split()))
a_list = list(map(int, input().split()))
lr_list = []
for _ in range(Q):
    l, r = list(map(int, input().split()))
    lr_list.append((l, r))

cumsum_list = []

for i in range(N):
    if i == 0:
        cumsum_list.append(a_list[0])
        continue
    x = cumsum_list[i - 1] + a_list[i]
    cumsum_list.append(x)

for lr in lr_list:
    if lr[0] == 1:
        x = cumsum_list[lr[1] - 1]
    else:
        x = cumsum_list[lr[1] - 1] - cumsum_list[lr[0] - 2]
    print(x)
