#!/usr/bin/env python3
import math

tx_a, ty_a, tx_b, ty_b, T, V = list(map(int, input().split()))
n = int(input().split()[0])
xy_list = []

for _ in range(n):
    x, y = list(map(int, input().split()))
    xy_list.append((x, y))

d = T * V
yes_flag = False

for xy in xy_list:
    x, y = xy
    a = math.sqrt((tx_a - x) ** 2 + abs(ty_a - y) ** 2)
    b = math.sqrt((tx_b - x) ** 2 + abs(ty_b - y) ** 2)
    if d >= a + b:
        yes_flag = True
        break

ans = "YES" if yes_flag else "NO"
print(ans)
