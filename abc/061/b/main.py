#!/usr/bin/env python3
import collections

N, M = list(map(int, input().split()))
ab_list = []

for _ in range(M):
    a, b = list(map(int, input().split()))
    ab_list.append(a)
    ab_list.append(b)

counter = collections.Counter(ab_list)
for i in range(N):
    print(counter[i + 1])
