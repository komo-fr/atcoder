#!/usr/bin/env python3

N, M, T = list(map(int, input().split()))
ab_list = []

for _ in range(M):
    a, b = list(map(int, input().split()))
    ab_list.append((a, b))

pre_b = 0
n = N
is_ok = True
for i, ab in enumerate(ab_list):
    a, b = ab
    # バッテリーが減る
    n -= a - pre_b
    # print(f"{n=}")
    if n <= 0:
        is_ok = False
        break
    # バッテリーが増える
    n = min(n + (b - a), N)
    # print(f"{n=}")
    pre_b = b
else:
    n -= T - pre_b
    if n <= 0:
        is_ok = False

ans = "Yes" if is_ok else "No"
print(ans)
