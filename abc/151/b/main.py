#!/usr/bin/env python3


n, k, m = list(map(int, input().split()))
a_list = list(map(int, input().split()))

total = n * m
c = total - sum(a_list)
ans = max(c, 0) if c <= k else -1

print(ans)
