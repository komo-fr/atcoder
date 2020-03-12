#!/usr/bin/env python3
import math

n, a, b = list(map(int, input().split()))

mod = 10 ** 9 + 7
# m = math.factorial(n) * N
m = 1
for i in range(1, n + 1):
    m *= i

c_1, c_2 = 1, m
t = 0
for i in range(1, n + 1):
    c_1 *= i
    c_2 /= n + 1 - i
    if i in [a, b]:
        continue
    t += m / (c_1 * c_2)

ans = int(t % mod)

print(ans)
