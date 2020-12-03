#!/usr/bin/env python3
import itertools

S = input()

patterns = itertools.product(["A", ""], repeat=4)
target_list = []
for p in patterns:
    target_list.append(f"{p[0]}KIH{p[1]}B{p[2]}R{p[3]}")

ans = "YES" if S in target_list else "NO"
print(ans)
