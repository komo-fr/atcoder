#!/usr/bin/env python3
from collections import defaultdict

N, K = list(map(int, input().split()))
c_list = list(map(int, input().split()))
p_list = list(map(int, input().split()))

min_dict = defaultdict(lambda: float("inf"))
for c, p in zip(c_list, p_list):
    if p < min_dict[c]:
        min_dict[c] = p

if len(min_dict) < K:
    ans = -1
else:
    ans = sum(sorted(min_dict.values())[:K])

print(ans)
