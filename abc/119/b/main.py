#!/usr/bin/env python3

N = int(input().split()[0])
xu_list = []

for _ in range(N):
    x, u = list(input().split())
    xu_list.append((float(x), u))

total = 0

for xu in xu_list:
    x, u = xu
    total += x * 38 * 10 ** 4 if u == "BTC" else x

ans = total
print(ans)
