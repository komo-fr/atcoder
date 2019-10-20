#!/usr/bin/env python3
import bisect


N = int(input().split()[0])
l_list = list(map(int, input().split()))
l_list = sorted(l_list)
p_list = []
total = 0

for a_i, a in enumerate(l_list[::-1]):
    # 1番目に長い辺を固定
    for b_i, b in enumerate(l_list[-(a_i + 2) :: -1]):
        # 2番目に長い辺を固定
        w_list = l_list[: -(a_i + 2)]
        c_i = bisect.bisect_right(w_list, abs(a - b))
        total += len(w_list) - c_i

ans = total
print(ans)
