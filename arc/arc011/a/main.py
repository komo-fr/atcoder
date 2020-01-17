#!/usr/bin/env python3

m, n, N = list(map(int, input().split()))
now_short_m = N
total = N
c = 0
while now_short_m >= m:
    c += 1
    new_n = (now_short_m // m) * n
    now_short_m = now_short_m % m + new_n
    total += new_n
ans = total
print(ans)
