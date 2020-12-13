#!/usr/bin/env python3
import math

N, K = list(map(int, input().split()))
total_p = 0
for i in range(1, N + 1):
    n = math.log2(K / i)
    n = int(n)
    point = i * 2 ** n
    if point < K:
        n += 1
    else:
        if i * 2 ** (n - 1) >= K:
            n -= 1
    n = max([0, n])
    # サイコロの目がiの時はi回連続で表が出る必要がある
    p = (1 / N) * ((1 / 2) ** n)
    # print(f"{i=}, {n=}, {p=}")
    total_p += p

ans = total_p
print(ans)
