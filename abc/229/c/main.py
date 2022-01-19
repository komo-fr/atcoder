#!/usr/bin/env python3

N, W = list(map(int, input().split()))
ab_list = []

for _ in range(N):
    a, b = list(map(int, input().split()))
    ab_list.append((a, b))

ab_list = sorted(ab_list, reverse=True)
w = W
total = 0
for a, b in ab_list:
    if w >= b:
        w -= b
        total += a * b
    else:
        total += a * w
        w = 0
    if w == 0:
        break
ans = total
print(ans)
