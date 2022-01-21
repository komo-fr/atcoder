#!/usr/bin/env python3
from collections import defaultdict
N = int(input().split()[0])
s_dict = defaultdict(lambda: {0:False, 1:False})

for _ in range(N):
    s = input()
    target = 1 if s.startswith("!") else 0
    t = s.lstrip("!")
    s_dict[t][target] = True

t = "satisfiable"
is_fuman = False
for k, v in s_dict.items():
    if v[0] and v[1]:
        is_fuman = True
        t = k
        break

ans = t
print(ans)
