#!/usr/bin/env python3
import bisect


N = int(input().split()[0])
l_list = list(map(int, input().split()))
l_list = sorted(l_list)
p_list = []
total = 0
for a_i, a in enumerate(l_list):
    for b_i, b in enumerate(l_list):
        if a_i == b_i:
            continue
        c_end_i = bisect.bisect_left(l_list, a + b)
        c_start_i = bisect.bisect_right(l_list, abs(a - b))
        total += c_end_i - c_start_i


# p_list = ["{}_{}_{}".format(p[0], p[1], p[2]) for p in p_list]
ans = total

print(ans)
