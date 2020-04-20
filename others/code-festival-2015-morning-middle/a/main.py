#!/usr/bin/env python3
import math

N, K, M, R = list(map(int, input().split()))
s_list = []

for _ in range(N - 1):
    s = int(input().split()[0])
    s_list.append(s)

s_list = sorted(s_list, reverse=True)
w_1 = sum(s_list[:K])
w_2 = sum(s_list[: K - 1])

if w_1 / K >= R:
    ans = 0
elif (w_2 + M) / K < R:
    ans = -1
else:
    ans = int(math.ceil(R * K - w_2))

print(ans)
