#!/usr/bin/env python3

s = input()
s = list(s)
s_r = list(reversed(s))
n = len(s)
c = 0
for i in range(n // 2):
    if s[i] != s_r[i]:
        c += 1
ans = c
print(ans)
