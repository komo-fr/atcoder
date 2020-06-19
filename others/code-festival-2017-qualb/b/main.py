#!/usr/bin/env python3
import collections

N = int(input().split()[0])
d_list = list(map(int, input().split()))
M = int(input().split()[0])
t_list = list(map(int, input().split()))

d_counter = collections.Counter(d_list)
t_counter = collections.Counter(t_list)
is_ok = True
for k, v in t_counter.items():
    if d_counter[k] < v:
        is_ok = False

ans = "YES" if is_ok else "NO"

print(ans)
