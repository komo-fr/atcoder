#!/usr/bin/env python3
import math

N, H = list(map(int, input().split()))
a_list = []
b_list = []

for _ in range(N):
    a, b = list(map(int, input().split()))
    a_list.append(a)
    b_list.append(b)

max_a = max(a_list)
b_list = sorted(b_list, reverse=True)
b_list = [b for b in b_list if b > max_a]
count = 0

while H > 0:
    if b_list:
        H -= b_list.pop(0)
        count += 1
    else:
        count += math.ceil(H / max_a)
        break

ans = count
print(ans)
