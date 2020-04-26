#!/usr/bin/env python3
import collections

N = int(input().split()[0])
s_dict = collections.defaultdict(int)

for _ in range(N):
    s = input()
    s_dict[s] += 1

ans = len(s_dict)
print(ans)
