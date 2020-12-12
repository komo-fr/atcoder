#!/usr/bin/env python3
from collections import Counter

N = int(input().split()[0])
d_list = list(map(int, input().split()))
M = int(input().split()[0])
t_list = list(map(int, input().split()))

d_counter = Counter(d_list)
t_counter = Counter(t_list)
is_ok = True
for k, v in t_counter.items():
    if v > d_counter[k]:
        is_ok = False
ans = "YES" if is_ok else "NO"
print(ans)
