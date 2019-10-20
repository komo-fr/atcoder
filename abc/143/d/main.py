#!/usr/bin/env python3
import bisect


N = int(input().split()[0])
l_list = list(map(int, input().split()))
l_list = sorted(l_list)
total = 0

for a_i, a in enumerate(l_list):
    # 一番長い辺を固定
    for b_i, b in enumerate(l_list[:a_i]):
        # 2番目に長い辺を固定
        c_i = bisect.bisect_right(l_list, abs(a - b))
        total += max(b_i - c_i, 0)

ans = total
print(ans)
