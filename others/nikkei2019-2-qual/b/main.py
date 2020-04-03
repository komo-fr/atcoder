#!/usr/bin/env python3
import collections

N = int(input().split()[0])
d_list = list(map(int, input().split()))
counter = collections.Counter(d_list)
max_d = max(counter.keys())
w = 0
mod = 998244353

if d_list[0] != 0 or counter[0] >= 2:
    w = 0
else:
    for d in range(1, max_d + 1):
        if d not in counter.keys():
            w = 0
            break
        if d == 1:
            w += 1
            continue
        x = counter[d - 1] ** counter[d]  # D=iとなるルートのパターン数
        w = (w % mod) * x
w = w % mod
ans = w
print(ans)
