#!/usr/bin/env python3
from collections import Counter

S = input()
count = 0
left_b_count = 0
for char in S:
    if char == "B":
        left_b_count += 1
    else:
        count += left_b_count

ans = count
print(ans)
