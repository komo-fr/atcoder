#!/usr/bin/env python3

N = int(input().split()[0])
s = input()
c = 0

for i, ch in enumerate(s):
    if i + 3 > len(s):
        break

    sub = s[i : i + 3]
    if sub == "ABC":
        c += 1
ans = c
print(ans)
