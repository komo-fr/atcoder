#!/usr/bin/env python3
import itertools
ab_list = list(map(int, input().split()))
cd_list = list(map(int, input().split()))
max_v = -float("inf")
for x, y in itertools.product(ab_list, cd_list):
    max_v = max([max_v, x-y])
ans = max_v
print(ans)
