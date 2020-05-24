#!/usr/bin/env python3
import collections
import math

N, M = list(map(int, input().split()))
name = input()
kit = input()

name_counter = collections.Counter(name)
kit_counter = collections.Counter(kit)
count = 0
for k, v in name_counter.items():
    if kit_counter[k] == 0:
        count = -1
        break
    count = max(count, math.ceil(v / kit_counter[k]))
ans = count
print(ans)
