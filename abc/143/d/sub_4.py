#!/usr/bin/env python3
import bisect
import collections


N = int(input().split()[0])
l_list = list(map(int, input().split()))
l_list = sorted(l_list)

counter = collections.Counter(l_list)
p_list = []

for a in range(1, 10 ** 3 + 1):
    for b in range(1, 10 ** 3 + 1):
        for c in range(1, 10 ** 3 + 1):
            if abs(b - c) < a < b + c:
                p_list += [sorted([a, b, c])]

p_list = ["{}_{}_{}".format(p[0], p[1], p[2]) for p in p_list]
p_list = list(set(p_list))
total = 0
for p in p_list:
    p_counter = collections.Counter(p)
    is_ok = True

    for k, v in p_counter.items():
        if k not in counter or counter[k] < v:
            is_ok = False
            break
    if is_ok:
        total += 1

ans = len(set(p_list))

print(ans)
