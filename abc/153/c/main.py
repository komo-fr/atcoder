#!/usr/bin/env python3

N, K = list(map(int, input().split()))
h_list = list(map(int, input().split()))
h_list = sorted(h_list, reverse=True)

if K >= N:
    ans = 0
else:
    ans = sum(h_list[K:])

print(ans)
