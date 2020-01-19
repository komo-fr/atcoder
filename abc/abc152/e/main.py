#!/usr/bin/env python3
import fractions

N = int(input())
a_list = list(map(int, input().split()))
x = a_list[0]
for i in range(1, N):
    x = x * a_list[i] // fractions.gcd(x, a_list[i])
mod = 10 ** 9 + 7
t = 0
for a in a_list:
    b = x // a
    t += b % mod

ans = t % mod
print(ans)
