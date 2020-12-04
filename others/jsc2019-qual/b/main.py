#!/usr/bin/env python3
from collections import defaultdict

N, K = list(map(int, input().split()))
a_list = list(map(int, input().split()))
counter = defaultdict(lambda: dict(left=0, right=0))
total_right = 0
total_left = 0
for i, a in enumerate(a_list):
    for j, b in enumerate(a_list):
        if i == j:
            continue
        if i < j and a > b:
            counter[i]["right"] += 1
        if i > j and a > b:
            counter[i]["left"] += 1
    total_right += (counter[i]["right"] * K * (K + 1)) // 2
    total_left += (counter[i]["left"] * (K - 1) * K) // 2

mod = 10 ** 9 + 7
ans = (total_left + total_right) % mod
print(ans)
