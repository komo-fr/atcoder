#!/usr/bin/env python3
from collections import Counter

N = int(input().split()[0])
a_list = list(map(int, input().split()))
counter = Counter(a_list)
x = 0
for v in counter.values():
    x += v
count = 0
key_count = len(counter.keys()) - 1
for v in counter.values():
    x -= v
    count += x * v

ans = int(count)
print(ans)
