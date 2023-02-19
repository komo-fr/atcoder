#!/usr/bin/env python3
import bisect

N, X = list(map(int, input().split()))
a_list = list(map(int, input().split()))

ans = bisect.bisect_left(a_list, X) + 1
print(ans)
