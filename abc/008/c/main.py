#!/usr/bin/env python3
import itertools

N = int(input().split()[0])
c_list = []

for _ in range(N):
    c = int(input().split()[0])
    c_list.append(c)

# 約数の数
s_list = []

for i, c in enumerate(c_list):
    s = 0
    for j, o in enumerate(c_list):
        if c % o == 0:
            s += 1
    # 自分自身も含んでいるので、1引く
    s -= 1
    s_list.append(s)

w = 0

for s in s_list:
    if s % 2 == 0:
        w += s / (2 * s + 2)
    else:
        w += 0.5
ans = N - w
print(ans)
