#!/usr/bin/env python3
import math

N = int(input().split()[0])
t_list = []

for _ in range(5):
    t = int(input().split()[0])
    t_list.append(t)

min_t = t_list[0]

if N <= min(t_list):
    ans = 5
else:
    w_time = 0
    for t in t_list:
        min_t = min([t, min_t])
        # 追加待ち時間
        w = max([math.ceil(N / min_t) - w_time, 0])
        w_time += w

    ans = w_time + 4
print(ans)
