#!/usr/bin/env python3
# 二分探索で求める方法
import bisect

N, K = list(map(int, input().split()))
a_list = list(map(int, input().split()))

total = 0
for i, a in enumerate(a_list):
    target = a + K
    r = bisect.bisect_right(a_list, target) - 1
    total += r - i

ans = total
print(ans)
