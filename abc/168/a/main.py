#!/usr/bin/env python3

N = input()
n = int(N[-1])

if n in [2, 4, 5, 7, 9]:
    ans = "hon"
elif n in [0, 1, 6, 8]:
    ans = "pon"
elif n == 3:
    ans = "bon"

print(ans)
