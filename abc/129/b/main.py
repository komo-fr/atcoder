#!/usr/bin/env python3

N = int(input().split()[0])
w_list = list(map(int, input().split()))
min_diff = float("inf")
for n in range(1, N + 1):
    a = sum(w_list[: n + 1])
    b = sum(w_list[n + 1 :])
    min_diff = min(min_diff, abs(a - b))

ans = min_diff
print(ans)
