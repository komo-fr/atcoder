#!/usr/bin/env python3
import itertools

N = int(input().split()[0])
N = str(N)
p_gen = itertools.product([True, False],repeat=len(N))

min_k = float("inf")
for pattern in p_gen:
    after = ""
    for p, x in zip(pattern, N):
        if p:
            after += x
    if after and int(after) % 3 == 0:
        k = len(N) - len(after)
        if k < min_k:
            min_k = k

ans = min_k if min_k < float("inf") else -1
print(ans)
