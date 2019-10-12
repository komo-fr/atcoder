#!/usr/bin/env python3

S = input()
n_list = list(S)
min_diff = float("inf")

for i in range(len(n_list)):
    n = int("".join(n_list[i : i + 3]))
    min_diff = min(min_diff, abs(753 - n))

ans = min_diff
print(ans)
