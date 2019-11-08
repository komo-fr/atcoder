#!/usr/bin/env python3
import collections
import math


def C(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


N = int(input().split()[0])
a_list = list(map(int, input().split()))
cumsum_list = [0]
for i, a in enumerate(a_list):
    idx = i + 1
    c = cumsum_list[idx - 1] + a
    cumsum_list.append(c)

counter = collections.Counter(cumsum_list)
total = 0
for k, v in counter.items():
    if v > 1:
        total += C(v, 2)

ans = total
print(ans)
