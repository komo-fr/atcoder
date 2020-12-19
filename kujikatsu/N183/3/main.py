#!/usr/bin/env python3
from collections import namedtuple, defaultdict

N, W = list(map(int, input().split()))

w_list = [0 for _ in range(2 * 10 ** 5 + 10)]  # 十分な大きさ
for _ in range(N):
    s, t, p = list(map(int, input().split()))
    w_list[s] += p
    w_list[t] -= p

for i in range(1, len(w_list)):
    w_list[i] += w_list[i - 1]
ans = "Yes" if max(w_list) <= W else "No"
print(ans)
