#!/usr/bin/env python3
from collections import defaultdict

N, M = list(map(int, input().split()))
s_list = list(input().split())
t_list = list(input().split())

stop_dict = defaultdict(lambda: False)
for t in t_list:
    stop_dict[t] = True

p_list = []
for s in s_list:
    stop = stop_dict[s]
    p_list.append("Yes" if stop else "No")


ans = "\n".join(p_list)
print(ans)
