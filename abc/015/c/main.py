#!/usr/bin/env python3
import itertools

N, K = list(map(int, input().split()))
t_list_list = []

for _ in range(N):
    t_list = list(map(int, input().split()))
    t_list_list.append(t_list)

p_gen = itertools.product(*t_list_list)
is_ok = True
for pattern in p_gen:
    a = pattern[0]
    for p in pattern[1:]:
        a = a ^ p
    if a == 0:
        is_ok = False

ans = "Nothing" if is_ok else "Found"
print(ans)
