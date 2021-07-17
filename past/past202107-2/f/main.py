#!/usr/bin/env python3
from collections import defaultdict

N = int(input().split()[0])
dst_list = []

for _ in range(N):
    d, s, t = list(map(int, input().split()))
    dst_list.append((d, s, t))

dst_list = sorted(dst_list)

time_table = defaultdict(lambda: [0] * 24)
is_ok = True
for schedule in dst_list:
    d, s, t = schedule
    for i in range(24):
        if s <= i < t:
            if time_table[d][i] >= 1:
                is_ok = False
                break
            else:
                time_table[d][i] += 1

ans = "No" if is_ok else "Yes"
print(ans)
