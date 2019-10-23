#!/usr/bin/env python3

N = int(input().split()[0])
s = list(str(N))

if N <= int(s[0] * len(s)):
    ans = s[0] * len(s)
else:
    ans = str(int(s[0]) + 1) * len(s)

print(ans)
