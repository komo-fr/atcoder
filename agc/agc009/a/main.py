#!/usr/bin/env python3

N = int(input().split()[0])
ab_list = []

for _ in range(N):
    a, b = list(map(int, input().split()))
    ab_list.append((a, b))

count = 0
w_list = ab_list[:]
# 後ろから確定させる
for i in range(N):
    idx = (N - 1) - i
    a, b = ab_list[idx]
    a += count

    if a % b == 0:
        continue

    if a < b:
        count += b - a
    else:
        w = b - (a % b)
        count += w

ans = count
print(ans)
