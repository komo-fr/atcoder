#!/usr/bin/env python3
import numpy as np
from collections import defaultdict

N, K = list(map(int, input().split()))
p_table = []

for _ in range(N):
    p_list = list(map(int, input().split()))
    p_table.append(p_list)

sum_list = np.array(p_table).sum(axis=1)
sum_list = [(s, i) for i, s in enumerate(sum_list)]
sum_list = sorted(sum_list, reverse=True)

r_dict = defaultdict(lambda: False)
k_point = None
for i, s in enumerate(sum_list):
    k = i + 1
    if k < K:
        r_dict[s[1]] = True
    elif k == K:
        r_dict[s[1]] = True
        k_point = s[0]
    else:
        if s[0] + 300 >= k_point:
            r_dict[s[1]] = True
        else:
            break

for i in range(N):
    ans = "Yes" if r_dict[i] else "No"
    print(ans)
