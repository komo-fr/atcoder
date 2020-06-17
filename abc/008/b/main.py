#!/usr/bin/env python3
import collections

N = int(input().split()[0])
s_list = []

for _ in range(N):
    s_list.append(input())
counter = collections.Counter(s_list)
ans = counter.most_common()[0][0]

print(ans)
