#!/usr/bin/env python3
from collections import namedtuple

N, M, T = list(map(int, input().split()))
ab_list = []
# namedtuple("AB")

for _ in range(M):
    a, b = list(map(int, input().split()))
    ab_list.append((a, b))
n = N
pre_b = 0
is_ok = True
for ab in ab_list:
    a, b = ab
    n -= a - pre_b
    if n <= 0:
        is_ok = False
        break

    n = min(N, n + b - a)
    pre_b = b
else:
    n -= T - pre_b
    if n <= 0:
        is_ok = False

ans = "Yes" if is_ok else "No"
print(ans)
