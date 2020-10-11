#!/usr/bin/env python3

N = int(input().split()[0])
mod = 10 ** 9 + 7

p = 9 ** N + 9 ** N - 8 ** N
ans = (10 ** N - p) % mod

print(ans)
