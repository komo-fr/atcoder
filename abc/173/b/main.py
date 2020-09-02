#!/usr/bin/env python3
import collections

N = int(input().split()[0])
s_list = []

for _ in range(N):
    s = input()
    s_list.append(s)

counter = collections.Counter(s_list)

for item in ["AC", "WA", "TLE", "RE"]:
    print(f"{item} x {counter[item]}")
